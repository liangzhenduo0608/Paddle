#  Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserve.
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
from paddle.trainer_config_helpers import *

settings(batch_size=1000, learning_rate=1e-5)

din = data_layer(name='data', size=100)

enc = din
for i in range(32):
    enc = addto_layer([enc, enc])

pred = fc_layer(
    input=fc_layer(
        input=enc, size=32, act=ReluActivation()),
    size=10,
    act=SoftmaxActivation())
outputs(pred)
