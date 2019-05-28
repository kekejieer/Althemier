# -*- coding: utf-8 -*-
from keras.applications.vgg16 import VGG16
from keras.optimizers import SGD
import numpy as np
from keras.models import Model
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Input
from keras.layers import Activation
from keras.layers import Add
from keras.utils import plot_model
input_shape = (182,182,3)

path1 = 'F:\\weights\\vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
class  FineturnModel():

      def  fineturn_vgg16(lr=0.005, decay=1e-6, momentum=0.9, RGB=True,
                   is_plot_model=False):

            base_model = VGG16(weights=None, include_top=False,pooling=None, input_shape=input_shape)
            base_model.load_weights(path1, by_name=True)
            aa = base_model.output

            # 冻结base_model所有层，这样就可以正确获得bottleneck特征
            for i,layer in enumerate(base_model.layers):
                if i<=13:
                      layer.trainable= False

            x = base_model.output
            # 添加自己的全链接分类层
            x= MaxPooling2D(data_format="channels_first")(x)
            x = Dense(1024, activation='relu')(x)
            x= Dense(units=128)(x)
            flat10 = Flatten()(x)
            out = Dense(units=1, activation="sigmoid")(flat10)
            model = Model(inputs=base_model.input, outputs=out)
            print(model.summary())
            sgd = SGD(lr=lr, decay=decay, momentum=momentum, nesterov=True)
            model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
            # 绘制模型
            if is_plot_model:
                plot_model(model, to_file='resnet50_model.png', show_shapes=True)
            return model










