
def test_Brain___init__(brain_class):
    net_shape = [2,3,2]
    bren = brain_class(network_shape = net_shape)
    assert len(bren.weights) == len(net_shape)-1, "Incorrect weights matrix"
    assert len(bren.biases) == len(net_shape)-1, "Incorrect biases matrix"

def test_Brain_predict(brain_class):
    output_layer_shape = 3
    net_shape = [6,12,output_layer_shape]
    bren = brain_class(network_shape = net_shape)
    food_coord = (1,0,0)
    lethal_coord = (0,0,1)
    outcome = bren.decision(food_coord, lethal_coord)
    assert len(outcome) == output_layer_shape, "Output matrix incorrect"