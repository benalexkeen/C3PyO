# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import webbrowser
import os
import json
import datetime
import numbers

from jinja2 import Environment, PackageLoader

from c3pyo.utils import is_iterable

__here__ = os.path.dirname(os.path.abspath(__file__))
temp_path = os.path.join(__here__, 'temp.html')

CHART_BASE_FILENAME = './chart.html'

pl = PackageLoader('c3pyo', 'templates')
jinja2_env = Environment(loader=pl)

template = jinja2_env.get_template(CHART_BASE_FILENAME)

url = 'file:///' + temp_path


class C3Chart(object):
    """
    C3Chart Base Class
    """

    def __init__(self, **kwargs):
        self.chart_type = None
        self.name = kwargs.get('name', 'C3 Chart')
        self.set_grid_lines(kwargs)
        self.set_legend(kwargs)
        self.set_zoom(kwargs)
        self.set_subchart(kwargs)
        self.set_size(kwargs)
        self.x_label = kwargs.get('x_label', 'x')
        self.y_label = kwargs.get('y_label', 'y')
        self.chart_div = '#{}'.format(kwargs.get('chart_div', 'chart_div'))
        self.save_output = False

    def set_subchart(self, kwargs):
        self.subchart = kwargs.get('subchart', False)
        if not isinstance(self.subchart, bool):
            msg = 'zoom must be a boolean, received {} of type {}'
            raise TypeError(msg.format(self.subchart, type(self.subchart)))

    def set_zoom(self, kwargs):
        self.zoom = kwargs.get('zoom', False)
        if not isinstance(self.zoom, bool):
            msg = 'zoom must be a boolean, received {} of type {}'
            raise TypeError(msg.format(self.zoom, type(self.zoom)))

    def set_size(self, kwargs):
        self.height = kwargs.get('height', 0)
        self.width = kwargs.get('width', 0)
        if not isinstance(self.width, numbers.Number):
            msg = 'width must be a number, received {} of type {}'
            raise TypeError(msg.format(self.width, type(self.width)))
        if not isinstance(self.height, numbers.Number):
            msg = 'height must be a number, received {} of type {}'
            raise TypeError(msg.format(self.height, type(self.height)))

    def set_grid_lines(self, kwargs):
        self.grid_lines = kwargs.get('grid_lines', False)
        if self.grid_lines:
            self.x_grid_lines = True
            self.y_grid_lines = True
        else:
            self.x_grid_lines = kwargs.get('x_grid_lines', False)
            self.y_grid_lines = kwargs.get('y_grid_lines', False)
        msg = '{}_grid_lines must be a boolean'
        assert isinstance(self.x_grid_lines, bool), msg.format('x')
        assert isinstance(self.y_grid_lines, bool), msg.format('y')

    def set_legend(self, kwargs):
        self.show_legend = kwargs.get('show_legend', True)
        self.legend_position = kwargs.get('legend_position')
        if not self.legend_position:
            self.legend_position = 'bottom'
        if self.legend_position:
            self.show_legend = True
        if self.legend_position not in ('bottom', 'right', 'inset'):
            msg = 'Currently only bottom, right and inset supported for legend_position'
            raise ValueError(msg)
        if not isinstance(self.show_legend, bool):
            msg = 'show_legend must be a boolean'
            raise TypeError('show_legend must be a boolean')

    def get_legend_for_json(self):
        return {
            'show': self.show_legend,
            'position': self.legend_position
        }

    def get_grid_for_json(self):
        grid = {
            'x': {
                'show': self.x_grid_lines
            },
            'y': {
                'show': self.y_grid_lines
            }
        }
        if self.chart_type == 'bar':
            grid['y']['lines'] = [{'value': 0}]
        return grid

    def get_zoom_for_json(self):
        zoom = {
            'enabled': self.zoom
        }
        return zoom

    def get_subchart_for_json(self):
        subchart = {
            'enabled': self.subchart
        }
        return subchart

    def get_size_for_json(self):
        size = {}
        if self.height:
            size['height'] = self.height
        if self.width:
            size['width'] = self.width
        return size

    def reset_data(self):
        self.x_data = []
        self.y_data = []
        self.data = []

    def plot_graph(self, chart_json):
        with open(temp_path, 'w') as f:
            f.write(template.render(
                title=self.name, 
                body='Hello, World',
                chart_json=chart_json,
                ))
        webbrowser.open(url)

    def json(self):
        res = self.get_chart_json()
        return res

    def get_chart_json(self):
        chart_json = {
            'bindto': self.chart_div,
            'data': self.get_data_for_json(),
            'legend': self.get_legend_for_json(),
            'grid': self.get_grid_for_json(),
            'axis': self.get_axis_for_json(),
            'zoom': self.get_zoom_for_json(),
            'subchart': self.get_subchart_for_json(),
            'size': self.get_size_for_json()
        }
        chart_json = json.dumps(chart_json)
        return chart_json

    def get_data_for_json(self):
        raise NotImplementedError

    def get_axis_for_json(self):
        raise NotImplementedError
