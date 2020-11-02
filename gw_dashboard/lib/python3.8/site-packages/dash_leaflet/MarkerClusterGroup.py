# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class MarkerClusterGroup(Component):
    """A MarkerClusterGroup component.
MarkerClusterGroup is a wrapper of MarkerClusterGroup in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component (dynamic)
- className (string; optional): A custom class name to assign to the image. Empty by default.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- options (dict; optional): Marker cluster group options (a dict). See list of options here
https://github.com/Leaflet/Leaflet.markercluster#all-options"""
    @_explicitize_args
    def __init__(self, children=None, className=Component.UNDEFINED, id=Component.UNDEFINED, options=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'className', 'id', 'options']
        self._type = 'MarkerClusterGroup'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'className', 'id', 'options']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(MarkerClusterGroup, self).__init__(children=children, **args)
