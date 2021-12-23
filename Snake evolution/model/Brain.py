

class Brain():
    """
    Brain is a keras Sequential object 
    you can pass a 
    """
    def __init__(self, network_layout):
        input_layer = tf.keras.layers.Dense()
        hidden_layers = []
        output_layer = tf.keras.layers.Dense()
        sequential_layers = []
        self.NN = tf.keras.models.Sequential(sequential_layers)