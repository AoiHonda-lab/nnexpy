class NetworkGenerator(object):
    def build_model(self, *args, **kwargs):
        import tensorflow as tf
        depth = kwargs.get('depth', 1)
        input_shape = kwargs.get('input_shape', (2,))
        width = kwargs.get('width', depth)
        firstLayerWidth = kwargs.get('firstLayerWidth', depth)
        activation = kwargs.get('activation', 'relu')

        model = tf.keras.Sequential()
        init = tf.keras.initializers.RandomNormal(
            mean=0.0, stddev=1/firstLayerWidth)

        model.add(tf.keras.layers.Dense(firstLayerWidth,
                                        input_dim=input_shape[0], activation=activation, kernel_initializer=init))
        for _ in range(depth-1):
            model.add(tf.keras.layers.Dense(
                width, activation=activation, kernel_initializer=init))
        model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
        return model

    def train_and_save(self, *args, **kwargs):
        import tensorflow as tf
        import math
        tf.compat.v1.disable_eager_execution()

        model = kwargs.get('model', None)
        epoch_number = kwargs.get('epoch_number', 100)
        data = kwargs.get('data', None)
        label = kwargs.get('label', None)
        save_path = kwargs.get('save_path', './model.h5')
        callbacks = kwargs.get('callbacks', None)
        initial_batch_size = kwargs.get('batch_size', 32)
        batch_size_compute = kwargs.get(
            'batch_size_compute', (lambda x, i: x + math.floor(i * 0.1)))
        loss = kwargs.get('loss', 'binary_crossentropy')
        targetAcc = kwargs.get('targetAcc', 0.97)
        adam = tf.keras.optimizers.Adam(learning_rate=0.01)

        model.summary()
        model.compile(optimizer=adam,
                      loss=loss, metrics=['accuracy'])
        accTracker = 0
        epochNumber = 0
        while epochNumber < epoch_number and accTracker < targetAcc:
            temp = model.fit(data, label, validation_split=0.2, batch_size=batch_size_compute(
                initial_batch_size, epochNumber), epochs=1, shuffle=True, verbose=0, callbacks=callbacks)
            accTracker = temp.history.get('acc')[-1]
            epochNumber += 1
        model.save(save_path)
        import gc
        del model
        gc.collect()
        tf.keras.backend.clear_session()
        tf.compat.v1.reset_default_graph()

    def full_net_combined(self, depth, width, firstLayerWidth, input_shape, mypath, epoch_number, data, label):
        import tensorflow as tf
        tf.compat.v1.disable_eager_execution()
        model = self.build_model(
            depth=depth, input_shape=input_shape, width=width, firstLayerWidth=firstLayerWidth, activation='relu')
        earlyStop = tf.keras.callbacks.EarlyStopping(
            monitor='loss', patience=3)
        self.train_and_save(model=model, epoch_number=epoch_number, data=data, label=label, save_path=mypath + str(
            depth) + '_' + str(firstLayerWidth) + '_' + 'layer.h5', batch_size=32, loss="binary_crossentropy", callbacks=[earlyStop])
        import gc
        del model
        gc.collect()
        tf.keras.backend.clear_session()
        tf.compat.v1.reset_default_graph()
