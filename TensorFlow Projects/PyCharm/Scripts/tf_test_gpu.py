import tensorflow as tf

gpu_available = tf.config.experimental.list_physical_devices('GPU')

if not gpu_available:
    print("!pip install tensorflow-gpu==1.15.4")
else:
    print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
    for gpu in gpu_available:
        print('GPU Device Names: {}'.format(gpu.name))