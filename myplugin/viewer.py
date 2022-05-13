from glue_jupyter.view import IPyWidgetView

from .state import MyPluginViewerState
from .layer_artist import MyPluginLayerArtist
from .widgets import MyPluginViewerStateWidget, MyPluginLayerStateWidget

class MyPluginView(IPyWidgetView):
    
    _state_cls = MyPluginViewerState
    _data_artist_cls = MyPluginLayerArtist
    _subset_artist_cls = MyPluginLayerArtist
    _options_cls = MyPluginViewerStateWidget
    _layer_style_widget_cls = MyPluginLayerStateWidget

    tools = []
    
    def __init__(self, session, state=None):
        super(MyPluginView, self).__init__(session, state=state)
