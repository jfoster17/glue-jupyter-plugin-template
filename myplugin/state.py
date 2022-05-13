from glue.viewers.common.state import ViewerState, LayerState


class MyPluginViewerState(ViewerState):
    def __init__(self):
        super(MyPluginViewerState, self).__init__()

class MyPluginLayerState(LayerState):
    def __init__(self, layer=None, viewer_state=None):
        super(MyPluginLayerState, self).__init__()

