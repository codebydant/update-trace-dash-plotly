# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class EditableGraph(Component):
    """An EditableGraph component.
It takes a for-loop to delete multiples traces, and
then append the new ones.

Keyword arguments:
- id (string; required): The ID used to identify this component in Dash callbacks.
- aim (string; required): The ID used in the dcc.Graph to modify.
- data (list; default {disable:'yes'}): A list of dic with the data to update
- style (dict; optional): A object with the data style"""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, aim=Component.REQUIRED, data=Component.UNDEFINED, style=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'aim', 'data', 'style']
        self._type = 'EditableGraph'
        self._namespace = 'dash_update_data_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'aim', 'data', 'style']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id', 'aim']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(EditableGraph, self).__init__(**args)
