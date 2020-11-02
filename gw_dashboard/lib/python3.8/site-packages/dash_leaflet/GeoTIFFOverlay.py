# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class GeoTIFFOverlay(Component):
    """A GeoTIFFOverlay component.
GeoTIFFOverlay is just wrapper of LeafletGeoTIFFOverlay.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- url (string; optional): The URL of the GeoTIFF file. Only EPSG:4326 / WGS84 coordinates are supported at
this time, ie. the file will be mapped without reprojection.
- band (number; optional): The band inside the GeoTIFF file. Defaults to 0.
- image (number; optional): The image inside the GeoTIFF file. Defaults to 0.
- colorscale (string | list of strings; optional): Chroma-js colorscale. Either a colorscale name, e.g. "Viridis", or a list of colors,
e.g. ["black", "#fdd49e", "rgba(255,0,0,0.35)"]
The predefined colorscales are listed here:
https://github.com/gka/chroma.js/blob/master/src/colors/colorbrewer.js
- domainMin (number; optional): Domain minimum of the colorscale. Translates to the first color of the colorscale.
- domainMax (number; optional): Domain maximum of the colorscale. Translates to the last color of the colorscale.
- clampHigh (boolean; optional): Clamp values higher than domainMax to domainMax. Defaults to false, which precludes
those values from being drawn.
- clampLow (boolean; optional): Clamp values lower than domainMin to domainMin. Defaults to false, which precludes
those values from being drawn.
- classes (number | list of numbers; optional): The number or positions of discrete classes in the colorbar. If not set the
colorbar will be continuous, which is the default.
- clip (list of list of list of numbersss; optional): List of clipping polygons. Each polygon is a list of [lat, lon] coordinates that surrounds the area to be
shown on the map.
- style (dict; optional): HTML style object to add to the overlay entity, e.g. to set interpolation mode
with {'image-rendering': 'pixelated'}
- tileSize (number; optional): Width and height of tiles in the grid. Use a number if width and
height are equal, or L.point(width, height) otherwise.
- opacity (number; optional): Opacity of the tiles. Can be used in the createTile() function.
- updateWhenIdle (boolean; optional): Load new tiles only when panning ends. true by default on mobile
browsers, in order to avoid too many requests and keep smooth
navigation. false otherwise in order to display new tiles during
panning, since it is easy to pan outside the keepBuffer option
in desktop browsers.
- updateWhenZooming (boolean; optional): By default, a smooth zoom animation (during a touch zoom or a
flyTo()) will update grid layers every integer zoom level.
Setting this option to false will update the grid layer only
when the smooth animation ends.
- updateInterval (number; optional): Tiles will not update more than once every updateInterval
milliseconds when panning.
- zIndex (number; optional): The explicit zIndex of the tile layer.
- bounds (list of numbers; optional): If set, tiles will only be loaded inside the set LatLngBounds.
- minZoom (number; optional): The minimum zoom level down to which this layer will be
displayed (inclusive).
- maxZoom (number; optional): The maximum zoom level up to which this layer will be
displayed (inclusive).
- minNativeZoom (number; optional): Minimum zoom number the tile source has available. If it
is specified, the tiles on all zoom levels lower than
minNativeZoom will be loaded from minNativeZoom level
and auto-scaled.
- maxNativeZoom (number; optional): Maximum zoom number the tile source has available. If it
is specified, the tiles on all zoom levels higher than
maxNativeZoom will be loaded from maxNativeZoom level
and auto-scaled.
- noWrap (boolean; optional): Whether the layer is wrapped around the antimeridian. If
true, the GridLayer will only be displayed once at low zoom
levels. Has no effect when the map CRS doesn't wrap around.
Can be used in combination with bounds to prevent requesting
tiles outside the CRS limits.
- className (string; optional): A custom class name to assign to the tile layer. Empty by default.
- keepBuffer (number; optional): When panning the map, keep this many rows and columns of tiles
before unloading them.
- interactive (boolean; optional): If true, the image overlay will emit mouse events when clicked or hovered.
- bubblingMouseEvents (boolean; optional): When true, a mouse event on this path will trigger the same
event on the map (unless L.DomEvent.stopPropagation is used).
- id (string; optional): The ID used to identify this component in Dash callbacks
- pane (string; optional): The leaflet pane of the component
- attribution (string; optional): The attribution string for the component
- click_lat_lng_val (list of numbers; optional): Dash callback property. Receives [lat, lng, val] upon click. Requires interactive=True.
- click_lat_lng_idx (list of numbers; optional): Dash callback property. Receives [lat, lng, idx] upon click. Requires interactive=True.
- dbl_click_lat_lng_val (list of numbers; optional): Dash callback property. Receives [lat, lng, val] upon double click. Requires interactive=True.
- dbl_click_lat_lng_idx (list of numbers; optional): Dash callback property. Receives [lat, lng, idx] upon double click. Requires interactive=True."""
    @_explicitize_args
    def __init__(self, children=None, url=Component.UNDEFINED, band=Component.UNDEFINED, image=Component.UNDEFINED, colorscale=Component.UNDEFINED, domainMin=Component.UNDEFINED, domainMax=Component.UNDEFINED, clampHigh=Component.UNDEFINED, clampLow=Component.UNDEFINED, classes=Component.UNDEFINED, clip=Component.UNDEFINED, style=Component.UNDEFINED, tileSize=Component.UNDEFINED, opacity=Component.UNDEFINED, updateWhenIdle=Component.UNDEFINED, updateWhenZooming=Component.UNDEFINED, updateInterval=Component.UNDEFINED, zIndex=Component.UNDEFINED, bounds=Component.UNDEFINED, minZoom=Component.UNDEFINED, maxZoom=Component.UNDEFINED, minNativeZoom=Component.UNDEFINED, maxNativeZoom=Component.UNDEFINED, noWrap=Component.UNDEFINED, className=Component.UNDEFINED, keepBuffer=Component.UNDEFINED, interactive=Component.UNDEFINED, bubblingMouseEvents=Component.UNDEFINED, id=Component.UNDEFINED, pane=Component.UNDEFINED, attribution=Component.UNDEFINED, click_lat_lng_val=Component.UNDEFINED, click_lat_lng_idx=Component.UNDEFINED, dbl_click_lat_lng_val=Component.UNDEFINED, dbl_click_lat_lng_idx=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'url', 'band', 'image', 'colorscale', 'domainMin', 'domainMax', 'clampHigh', 'clampLow', 'classes', 'clip', 'style', 'tileSize', 'opacity', 'updateWhenIdle', 'updateWhenZooming', 'updateInterval', 'zIndex', 'bounds', 'minZoom', 'maxZoom', 'minNativeZoom', 'maxNativeZoom', 'noWrap', 'className', 'keepBuffer', 'interactive', 'bubblingMouseEvents', 'id', 'pane', 'attribution', 'click_lat_lng_val', 'click_lat_lng_idx', 'dbl_click_lat_lng_val', 'dbl_click_lat_lng_idx']
        self._type = 'GeoTIFFOverlay'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'url', 'band', 'image', 'colorscale', 'domainMin', 'domainMax', 'clampHigh', 'clampLow', 'classes', 'clip', 'style', 'tileSize', 'opacity', 'updateWhenIdle', 'updateWhenZooming', 'updateInterval', 'zIndex', 'bounds', 'minZoom', 'maxZoom', 'minNativeZoom', 'maxNativeZoom', 'noWrap', 'className', 'keepBuffer', 'interactive', 'bubblingMouseEvents', 'id', 'pane', 'attribution', 'click_lat_lng_val', 'click_lat_lng_idx', 'dbl_click_lat_lng_val', 'dbl_click_lat_lng_idx']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(GeoTIFFOverlay, self).__init__(children=children, **args)
