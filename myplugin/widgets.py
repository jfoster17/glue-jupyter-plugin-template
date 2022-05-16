from ipywidgets import VBox
from glue_jupyter.vuetify_helpers import link_glue_choices

class MyPluginLayerStateWidget(VBox):

    def __init__(self, layer_state):
        super().__init__()

        self.state = layer_state


class MyPluginViewerStateWidget(VBox):
    
    def __init__(self, viewer_state):
        super().__init__()
        self.glue_state = viewer_state
        
