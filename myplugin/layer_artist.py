import numpy as np

from glue.viewers.common.layer_artist import LayerArtist
from glue.utils import color2hex

from .state import MyPluginLayerState
from glue_jupyter.link import dlink, link, on_change

class MyPluginLayerArtist(LayerArtist):
    
    _layer_state_cls = MyPluginLayerState
    
    def __init__(self, viewer, viewer_state, layer=None, layer_state=None):
        super(MyPluginLayerArtist, self).__init__(viewer_state,
                                                  layer_state=layer_state,
                                                  layer=layer)
        self.widget = viewer
        # OPTION 1: This is the easiest way to keep glue state and widgets in sync
        link((self.state, 'color'), (self.widget.style, 'button_color'), color2hex)
        # OPTION 2: If you need more control, or to have something else happen
        # when a glue state changes, you can do the following
        #self.state.add_callback('color',self._on_color_change)
        #self._on_color_change()
        
        self._viewer_state.add_callback('x_att',self._on_attribute_change)

    #def _on_color_change(self, value=None):
    #    if self.state.color is not None:
    #        self.widget.style.button_color = color2hex(self.state.color)

    def _on_attribute_change(self, value=None):
        self.update()

    def clear(self):
        """Req: Remove the layer from viewer but allow it to be added back"""
        pass

    def remove(self):
        """Req: Permanently remove the layer from the viewer."""
        pass

    def update(self):
        """Req: Update appearance of the layer before redrawing.
        Called when a subset is changed."""
        
        x_att_data = self.layer.data[self._viewer_state.x_att]
        self.widget.description = np.array2string(x_att_data, precision=2, separator=',',
                                                 suppress_small=True)

    def redraw(self):
        """Req: Re-render the plot."""
        pass

