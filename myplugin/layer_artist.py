from glue.viewers.common.layer_artist import LayerArtist

from .state import MyPluginLayerState

class MyPluginLayerArtist(LayerArtist):
    
    _layer_state_cls = MyPluginLayerState
    
    def __init__(self, viewer, viewer_state, layer=None, layer_state=None):
        super(MyPluginLayerArtist, self).__init__(viewer_state,
                                                  layer_state=layer_state,
                                                  layer=layer
                                                  )
                                                  
    def clear(self):
        """Req: Remove the layer from viewer but allow it to be added back"""
        pass
    
    def remove(self):
        """Req: Permanently remove the layer from the viewer."""
        pass
    
    def update(self):
        """Req: Update appearance of the layer before redrawing.
        Called when a subset is changed."""
        pass
                
    def redraw(self):
        """Req: Re-render the plot."""
        pass
    
