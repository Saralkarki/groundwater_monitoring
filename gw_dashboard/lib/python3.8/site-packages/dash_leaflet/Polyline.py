# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Polyline(Component):
    """A Polyline component.
Polyline is a wrapper of Polyline in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- positions (list of list of numberss; required): An array of geographical points (lat, lon)
- smoothFactor (number; optional): How much to simplify the polyline on each zoom level. More means better 
performance and smoother look, and less means more accurate representation.
- noClip (boolean; optional): Disable polyline clipping.
- stroke (boolean; optional): Whether to draw stroke along the path. Set it to false to disable borders 
on polygons or circles.
- color (string; optional): Stroke color
- weight (number; optional): Stroke width in pixels
- opacity (number; optional): Stroke opacity
- lineCap (string; optional): A string that defines shape to be used at the end of the stroke.
- lineJoin (string; optional): A string that defines shape to be used at the corners of the stroke.
- dashArray (string; optional): A string that defines the stroke dash pattern. Doesn't work on Canvas-powered 
layers in some old browsers.
- dashOffset (string; optional): A string that defines the distance into the dash pattern to start the dash. 
Doesn't work on Canvas-powered layers in some old browsers.
- fill (boolean; optional): Whether to fill the path with color. Set it to false to disable filling on 
polygons or circles.
- fillColor (string; optional): Fill color. Defaults to the value of the color option
- fillOpacity (number; optional): Fill opacity
- fillRule (string; optional): A string that defines how the inside of a shape is determined.
- bubblingMouseEvents (boolean; optional): When true, a mouse event on this path will trigger the same 
event on the map (unless L.DomEvent.stopPropagation is used).
- renderer (dict; optional): Use this specific instance of Renderer for this path. Takes 
precedence over the map's default renderer.
- className (string; optional): Custom class name set on an element. Only for SVG renderer.
- interactive (boolean; optional): If false, the layer will not emit mouse events and will act
as a part of the underlying map.
- id (string; optional): The ID used to identify this component in Dash callbacks
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component
- click_lat_lng (list of numbers; optional): Dash callback property. Receives [lat, lng] upon click.
- dbl_click_lat_lng (list of numbers; optional): Dash callback property. Receives [lat, lng] upon double click."""
    @_explicitize_args
    def __init__(self, children=None, positions=Component.REQUIRED, smoothFactor=Component.UNDEFINED, noClip=Component.UNDEFINED, stroke=Component.UNDEFINED, color=Component.UNDEFINED, weight=Component.UNDEFINED, opacity=Component.UNDEFINED, lineCap=Component.UNDEFINED, lineJoin=Component.UNDEFINED, dashArray=Component.UNDEFINED, dashOffset=Component.UNDEFINED, fill=Component.UNDEFINED, fillColor=Component.UNDEFINED, fillOpacity=Component.UNDEFINED, fillRule=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, renderer=Component.UNDEFINED, className=Component.UNDEFINED, interactive=Component.UNDEFINED, id=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, click_lat_lng=Component.UNDEFINED, dbl_click_lat_lng=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'positions', 'smoothFactor', 'noClip', 'stroke', 'color', 'weight', 'opacity', 'lineCap', 'lineJoin', 'dashArray', 'dashOffset', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'bubblingMouseEvents', 'renderer', 'className', 'interactive', 'id', 'pane', 'attribution', 'click_lat_lng', 'dbl_click_lat_lng']
        self._type = 'Polyline'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'positions', 'smoothFactor', 'noClip', 'stroke', 'color', 'weight', 'opacity', 'lineCap', 'lineJoin', 'dashArray', 'dashOffset', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'bubblingMouseEvents', 'renderer', 'className', 'interactive', 'id', 'pane', 'attribution', 'click_lat_lng', 'dbl_click_lat_lng']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['positions']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Polyline, self).__init__(children=children, **args)
