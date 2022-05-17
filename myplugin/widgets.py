from ipywidgets import VBox
from glue_jupyter.vuetify_helpers import link_glue_choices
from glue_jupyter.widgets import LinkedDropdown, Color, Size


class MyPluginLayerStateWidget(VBox):

    def __init__(self, layer_state):

        self.state = layer_state
        super().__init__()


class MyPluginViewerStateWidget(VBox):
    
    def __init__(self, viewer_state):
        self.state = viewer_state
        
        self.widget_x = LinkedDropdown(self.state, "x_att", label="x:")
        
        super().__init__([self.widget_x])

