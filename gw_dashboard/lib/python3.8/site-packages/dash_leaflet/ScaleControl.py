# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ScaleControl(Component):
    """A ScaleControl component.
ScaleControl is a wrapper of ScaleControl in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component (dynamic).
- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional): Position.
- imperial (boolean; optional): Imperial scale or not.
- metric (boolean; optional): Metric scale or not.
- updateWhenIdle (boolean; optional): Update when idle or not.
- maxWidth (number; optional): Control maxWidth.
- className (string; optional): A custom class name to assign to the image. Empty by default.
- id (string; optional): The ID used to identify this component in Dash callbacks."""
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, imperial=Component.UNDEFINED, metric=Component.UNDEFINED, updateWhenIdle=Component.UNDEFINED, maxWidth=Component.UNDEFINED, className=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'position', 'imperial', 'metric', 'updateWhenIdle', 'maxWidth', 'className', 'id']
        self._type = 'ScaleControl'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'position', 'imperial', 'metric', 'updateWhenIdle', 'maxWidth', 'className', 'id']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ScaleControl, self).__init__(children=children, **args)
