from ipywidgets import VBox

class MyPluginLayerStateWidget(VBox):

    def __init__(self, layer_state):
        super(MyPluginLayerStateWidget).__init__()

class MyPluginViewerStateWidget(VBox):
    
    def __init__(self, viewer_state):
        super(MyPluginLayerStateWidget).__init__()
