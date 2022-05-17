from ipywidgets import VBox
import ipywidgets
from glue_jupyter.vuetify_helpers import link_glue_choices
from glue_jupyter.widgets import LinkedDropdown, Color
from glue.utils import color2hex
from glue_jupyter.link import on_change, link, dlink


class MyPluginViewerStateWidget(VBox):
    
    def __init__(self, viewer_state):
        self.state = viewer_state
        
        self.widget_x = LinkedDropdown(self.state, "x_att", label="x:")
        
        super().__init__([self.widget_x])

class MyPluginLayerStateWidget(VBox):
        
    def __init__(self, layer_state):
    
        self.state = layer_state
                
        super().__init__()
