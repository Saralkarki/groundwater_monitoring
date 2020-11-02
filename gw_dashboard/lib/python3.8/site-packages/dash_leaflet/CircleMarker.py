# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CircleMarker(Component):
    """A CircleMarker component.
CircleMarker is a wrapper of CircleMarker in react-leaflet.
It takes similar properties to its react-leaflet counterpart.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- center (list of numbers; required): The center of the circle marker (lat, lon)
- radius (number; optional): Radius of the circle marker, in pixels
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
- interactive (boolean; optional): If true, the image overlay will emit mouse events when clicked or hovered.
- id (string; optional): The ID used to identify this component in Dash callbacks
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component
- n_clicks (number; default 0): Dash callback property. Number of times the object has been clicked"""
    @_explicitize_args
    def __init__(self, children=None, center=Component.REQUIRED, radius=Component.UNDEFINED, stroke=Component.UNDEFINED, color=Component.UNDEFINED, weight=Component.UNDEFINED, opacity=Component.UNDEFINED, lineCap=Component.UNDEFINED, lineJoin=Component.UNDEFINED, dashArray=Component.UNDEFINED, dashOffset=Component.UNDEFINED, fill=Component.UNDEFINED, fillColor=Component.UNDEFINED, fillOpacity=Component.UNDEFINED, fillRule=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, renderer=Component.UNDEFINED, className=Component.UNDEFINED, interactive=Component.UNDEFINED, id=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'center', 'radius', 'stroke', 'color', 'weight', 'opacity', 'lineCap', 'lineJoin', 'dashArray', 'dashOffset', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'bubblingMouseEvents', 'renderer', 'className', 'interactive', 'id', 'pane', 'attribution', 'n_clicks']
        self._type = 'CircleMarker'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'center', 'radius', 'stroke', 'color', 'weight', 'opacity', 'lineCap', 'lineJoin', 'dashArray', 'dashOffset', 'fill', 'fillColor', 'fillOpacity', 'fillRule', 'bubblingMouseEvents', 'renderer', 'className', 'interactive', 'id', 'pane', 'attribution', 'n_clicks']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['center']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CircleMarker, self).__init__(children=children, **args)
