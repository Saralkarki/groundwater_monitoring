# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Colorbar(Component):
    """A Colorbar component.
Colorbar is just a wrapper of LeafletColorbar.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component
- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional): Position of the colorbar.
- colorscale (string | list of strings; optional): Chroma-js colorscale. Either a colorscale name, e.g. "Viridis", or a list of colors,
e.g. ["black", "#fdd49e", "rgba(255,0,0,0.35)"].
The predefined colorscales are listed here:
https://github.com/gka/chroma.js/blob/master/src/colors/colorbrewer.js
- width (number; optional): Width of the colorbar. If width > height then the colorbar will be in horizontal mode.
- height (number; optional): Height of the colorbar. If height > width then the colorbar will be in vertical mode.
- min (number; optional): Domain minimum of the colorbar. Translates to the first color of the colorscale.
- max (number; optional): Domain maximum of the colorbar. Translates to the last color of the colorscale.
- classes (number | list of numbers; optional): The number or positions of discrete classes in the colorbar. If not set the 
colorbar will be continuous, which is the default.
- unit (string; optional): Optional text to append to the colorbar ticks.
- nTicks (number; optional): Number of ticks on the colorbar.
- tickDecimals (number; optional): If set, fixes the tick decimal points to the given number.
- tickValues (list of numbers; optional): If set, these values are used for ticks (rather than the ones genrated based on nTicks).
- tickText (list of strings; optional): If set, this text will be used instead of the data values.
- tooltip (boolean; optional): If true, the value will be shown as tooltip on hover.
- opacity (number; optional): Opacity of the colorbar. Use it to match the perceived colors from an overlay 
with opacity.
- style (dict; optional): HTML style object to add to the colorbar entity, e.g. to set font color.
- id (string; optional): The ID used to identify this component in Dash callbacks
- className (string; optional): The class of the component"""
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, colorscale=Component.UNDEFINED, width=Component.UNDEFINED, height=Component.UNDEFINED, min=Component.UNDEFINED, max=Component.UNDEFINED, classes=Component.UNDEFINED, unit=Component.UNDEFINED, nTicks=Component.UNDEFINED, tickDecimals=Component.UNDEFINED, tickValues=Component.UNDEFINED, tickText=Component.UNDEFINED, tooltip=Component.UNDEFINED, opacity=Component.UNDEFINED, style=Component.UNDEFINED, id=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'position', 'colorscale', 'width', 'height', 'min', 'max', 'classes', 'unit', 'nTicks', 'tickDecimals', 'tickValues', 'tickText', 'tooltip', 'opacity', 'style', 'id', 'className']
        self._type = 'Colorbar'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'position', 'colorscale', 'width', 'height', 'min', 'max', 'classes', 'unit', 'nTicks', 'tickDecimals', 'tickValues', 'tickText', 'tooltip', 'opacity', 'style', 'id', 'className']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Colorbar, self).__init__(children=children, **args)
