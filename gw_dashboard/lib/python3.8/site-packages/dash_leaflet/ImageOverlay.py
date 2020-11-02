# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ImageOverlay(Component):
    """An ImageOverlay component.
ImageOverlay is a wrapper of ImageOverlay in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- url (string; required): The URL of the image
- bounds (list of list of numberss; required): The geographical bounds the image is tied to.
- opacity (number; optional): The opacity of the image overlay.
- zIndex (number; optional): The explicit zIndex of the overlay layer.
- alt (string; optional): Text for the alt attribute of the image (useful for accessibility).
- interactive (boolean; optional): If true, the image overlay will emit mouse events when clicked or hovered.
- bubblingMouseEvents (boolean; optional): When true, a mouse event on this path will trigger the same 
event on the map (unless L.DomEvent.stopPropagation is used).
- crossOrigin (boolean; optional): Whether the crossOrigin attribute will be added to the image. If 
a String is provided, the image will have its crossOrigin attribute 
set to the String provided. This is needed if you want to access image 
pixel data. Refer to CORS Settings for valid String values.
- errorOverlayUrl (string; optional): URL to the overlay image to show in place of the overlay that failed to load.
- className (string; optional): A custom class name to assign to the image. Empty by default.
- id (string; optional): The ID used to identify this component in Dash callbacks
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component (dynamic)
- click_lat_lng (list of numbers; optional): Dash callback property. Receives [lat, lng] upon click. Requires interactive=True.
- dbl_click_lat_lng (list of numbers; optional): Dash callback property. Receives [lat, lng] upon double click. Requires interactive=True."""
    @_explicitize_args
    def __init__(self, children=None, url=Component.REQUIRED, bounds=Component.REQUIRED, opacity=Component.UNDEFINED, zIndex=Component.UNDEFINED, alt=Component.UNDEFINED, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, crossOrigin=Component.UNDEFINED, errorOverlayUrl=Component.UNDEFINED, className=Component.UNDEFINED, id=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, click_lat_lng=Component.UNDEFINED, dbl_click_lat_lng=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'url', 'bounds', 'opacity', 'zIndex', 'alt', 'interactive', 'bubblingMouseEvents', 'crossOrigin', 'errorOverlayUrl', 'className', 'id', 'pane', 'attribution', 'click_lat_lng', 'dbl_click_lat_lng']
        self._type = 'ImageOverlay'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'url', 'bounds', 'opacity', 'zIndex', 'alt', 'interactive', 'bubblingMouseEvents', 'crossOrigin', 'errorOverlayUrl', 'className', 'id', 'pane', 'attribution', 'click_lat_lng', 'dbl_click_lat_lng']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['url', 'bounds']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ImageOverlay, self).__init__(children=children, **args)
