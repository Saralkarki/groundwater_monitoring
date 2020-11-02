# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Marker(Component):
    """A Marker component.
Marker is a wrapper of Marker in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- position (list of numbers; required): A geographical point (lat, lon)
- icon (dict; optional): Options passed to Icon constructor.
- draggable (boolean; optional): Whether the marker is draggable with mouse/touch or not.
- opacity (number; optional): The opacity of the marker.
- zIndexOffset (number; optional): By default, marker images zIndex is set automatically based
on its latitude. Use this option if you want to put the
marker on top of all others (or below), specifying a high
value like 1000 (or high negative value, respectively).
- keyboard (boolean; optional): Whether the marker can be tabbed to with a keyboard and clicked by
pressing enter.
- title (string; optional): Text for the browser tooltip that appear on marker hover (no tooltip
by default).
- alt (string; optional): Text for the alt attribute of the icon image (useful for accessibility).
- riseOnHover (boolean; optional): If true, the marker will get on top of others when you hover the mouse
over it.
- riseOffset (number; optional): The z-index offset used for the riseOnHover feature.
- bubblingMouseEvents (boolean; optional): When true, a mouse event on this marker will trigger the same event
on the map (unless L.DomEvent.stopPropagation is used).
- autoPan (boolean; optional): Whether to pan the map when dragging this marker near its edge or not.
- autoPanPadding (dict; optional): Distance (in pixels to the left/right and to the top/bottom) of the map
edge to start panning the map.
- autoPanSpeed (number; optional): Number of pixels the map should pan by.
- interactive (boolean; optional): If false, the layer will not emit mouse events and will act as a part of
the underlying map.
- id (string; optional): The ID used to identify this component in Dash callbacks
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component
- n_clicks (number; default 0): Dash callback property. Number of times the marker has been clicked"""
    @_explicitize_args
    def __init__(self, children=None, position=Component.REQUIRED, icon=Component.UNDEFINED, draggable=Component.UNDEFINED, opacity=Component.UNDEFINED, zIndexOffset=Component.UNDEFINED, keyboard=Component.UNDEFINED, title=Component.UNDEFINED, alt=Component.UNDEFINED, riseOnHover=Component.UNDEFINED, riseOffset=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, autoPan=Component.UNDEFINED, autoPanPadding=Component.UNDEFINED, autoPanSpeed=Component.UNDEFINED, interactive=Component.UNDEFINED, id=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'position', 'icon', 'draggable', 'opacity', 'zIndexOffset', 'keyboard', 'title', 'alt', 'riseOnHover', 'riseOffset', 'bubblingMouseEvents', 'autoPan', 'autoPanPadding', 'autoPanSpeed', 'interactive', 'id', 'pane', 'attribution', 'n_clicks']
        self._type = 'Marker'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'position', 'icon', 'draggable', 'opacity', 'zIndexOffset', 'keyboard', 'title', 'alt', 'riseOnHover', 'riseOffset', 'bubblingMouseEvents', 'autoPan', 'autoPanPadding', 'autoPanSpeed', 'interactive', 'id', 'pane', 'attribution', 'n_clicks']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['position']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Marker, self).__init__(children=children, **args)
