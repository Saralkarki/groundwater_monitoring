# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LocateControl(Component):
    """A LocateControl component.
LocateControl is a wrapper of LocateControl in react-leaflet. The component requires linking font-awesome, i.e.
app = dash.Dash(external_stylesheets=['https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'])

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component (dynamic).
- className (string; optional): A custom class name to assign to the image. Empty by default.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- startDirectly (boolean; optional): If true, the location control is activated on map load.
- options (dict; optional): Location control options (a dict). See list of options in the code,
https://github.com/domoritz/leaflet-locatecontrol/blob/gh-pages/src/L.Control.Locate.js#L146"""
    @_explicitize_args
    def __init__(self, children=None, className=Component.UNDEFINED, id=Component.UNDEFINED, startDirectly=Component.UNDEFINED, options=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'className', 'id', 'startDirectly', 'options']
        self._type = 'LocateControl'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'className', 'id', 'startDirectly', 'options']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(LocateControl, self).__init__(children=children, **args)
