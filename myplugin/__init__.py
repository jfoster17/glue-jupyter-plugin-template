def setup():
    from .viewer import MyPluginView
    from glue_jupyter.registries import viewer_registry
    viewer_registry.add("myplugin", MyPluginView)