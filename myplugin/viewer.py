from glue_jupyter.view import IPyWidgetView

from .state import MyPluginViewerState
from .layer_artist import MyPluginLayerArtist
from .widgets import MyPluginViewerStateWidget, MyPluginLayerStateWidget

import ipywidgets as widgets

class MyPluginView(IPyWidgetView):
    
    _state_cls = MyPluginViewerState
    _data_artist_cls = MyPluginLayerArtist
    _subset_artist_cls = MyPluginLayerArtist
    _options_cls = MyPluginViewerStateWidget
    _layer_style_widget_cls = MyPluginLayerStateWidget

    tools = []
    
    def __init__(self, session, state=None):
        super(MyPluginView, self).__init__(session, state=state)
        self.widget = widgets.Button(description='Simple ipywidget')
        self.widget.layout.height = "300px" # To allow us to see the options
        self.create_layout()  # This requires an actual Widget
        
    def get_layer_artist(self, cls, layer=None, layer_state=None):
        return cls(self.widget, self.state, layer=layer, layer_state=layer_state)

    @property
    def figure_widget(self):
        return self.widget
