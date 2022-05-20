from glue.viewers.common.state import ViewerState, LayerState
from echo import SelectionCallbackProperty, CallbackProperty, keep_in_sync
from glue.core.data_combo_helper import ComponentIDComboHelper


class MyPluginViewerState(ViewerState):
    
    x_att = SelectionCallbackProperty(docstring='Attribute to display')

    def __init__(self, **kwargs):
        super(MyPluginViewerState, self).__init__()
        
        self.x_att_helper = ComponentIDComboHelper(self, 'x_att')

        self.add_callback('layers', self._layers_changed)
        self.update_from_dict(kwargs)

    def _layers_changed(self, *args):
        self.x_att_helper.set_multiple_data(self.layers_data)


class MyPluginLayerState(LayerState):
    """
    Layer state defines: layer, zorder, visible
    
    We need to set `self.layer = layer`
    1) Use `super(MyPluginLayerState, self).__init__(layer=layer)`
    2) Do `self.layer = layer`
    """
    
    color = CallbackProperty()
    
    def __init__(self, layer=None, viewer_state=None, **kwargs):
        super(MyPluginLayerState, self).__init__()#viewer_state=viewer_state, layer=layer)
        self.layer=layer
        if layer is not None:
            self.color = self.layer.style.color
        self._sync_color = keep_in_sync(self, 'color', self.layer.style, 'color')

