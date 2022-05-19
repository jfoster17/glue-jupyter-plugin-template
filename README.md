# Plugin Template
A template for creating a glue-jupyter plugin from an ipywidget.

This viewer does not really *do* anything, it just uses the button ipywidget as a sample
to show how you can structure a new viewer. It does adjust the color of the button
to match the color of the layer being displayed as an example of how to keep glue
state in sync with ipywidget state.

## How to run

```python
import numpy as np
import glue_jupyter as gj
from glue.core import Data
app = gj.jglue()

dataset1 = Data(x=np.random.rand(100),y=np.random.rand(100),label='test')
app.add_data(dataset1 = dataset1)

myviewer = app.new_data_viewer('myplugin',data=dataset1)
```
