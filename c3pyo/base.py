# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import webbrowser
import os
import json
import numbers
import re

from jinja2 import Environment, PackageLoader

from c3pyo.utils import single_letter_color_mapping, color_mapping

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
        self.show_points = kwargs.get('show_points', True)
        self.show_legend = kwargs.get('show_legend', True)
        self.show_legend_position = kwargs.get('legend_position', 'bottom')
        self.label_for_x = kwargs.get('xlabel', None)
        self.label_for_y = kwargs.get('ylabel', None)
        self.x_grid_lines = kwargs.get('gridlines', False)
        self.y_grid_lines = kwargs.get('gridlines', False)
        self.show_area = kwargs.get('area', False)
        self.zoom = kwargs.get('zoom', False)
        self.show_subchart = kwargs.get('subchart', False)
        self.height_value = kwargs.get('height', 0)
        self.width_value = kwargs.get('width', 0)
        self.y_max = kwargs.get('y_max', None)
        self.y_min = kwargs.get('y_min', None)
        self.show_tooltip = kwargs.get('tooltip', True)
        self.chart_div = '#{}'.format(kwargs.get('chart_div', 'chart_div'))
        self.colors = {}
        self.types = {}
        self.save_output = False

    def xlabel(self, label):
        self.label_for_x = label

    def ylabel(self, label):
        self.label_for_y = label

    def area(self, show_area):
        if not isinstance(show_area, bool):
            raise TypeError("arg for area must be boolean, received {}".format(type(show_area)))
        self.show_area = show_area

    def legend(self, show_legend):
        if not isinstance(show_legend, bool):
            raise TypeError("arg for legend must be boolean, received {}".format(type(show_legend)))
        self.show_legend = show_legend

    def zoom(self, zoom_on_off):
        if not isinstance(zoom_on_off, bool):
            raise TypeError("arg for zoom must be boolean, received {}".format(type(zoom_on_off)))
        self.zoom = zoom_on_off

    def subchart(self, show_subchart):
        if not isinstance(show_subchart, bool):
            raise TypeError("arg for subchart must be boolean, received {}".format(type(show_subchart)))
        self.show_subchart = show_subchart

    def height(self, height_value):
        if not isinstance(height_value, numbers.Number):
            raise TypeError('height must be a number, received {} of type {}'.format(height_value, type(height_value)))
        self.height_value = height_value

    def width(self, width_value):
        if not isinstance(width_value, numbers.Number):
            raise TypeError('width must be a number, received {} of type {}'.format(width_value, type(width_value)))
        self.width_value = width_value

    def y_range(self, y_min=None, y_max=None):
        if not isinstance(y_min, numbers.Number):
            raise TypeError('y_min must be a number, received {} of type {}'.format(y_min, type(y_min)))
        if not isinstance(y_max, numbers.Number):
            raise TypeError('y_max must be a number, received {} of type {}'.format(y_max, type(y_max)))
        self.y_min = y_min
        self.y_max = y_max

    def gridlines(self, x=None, y=None):
        msg = "arg for {} gridlines must be boolean, received {}"
        if x is not None and not isinstance(x, bool):
            raise(TypeError(msg.format('x', type(x))))
        if y is not None and not isinstance(y, bool):
            raise(TypeError(msg.format('y', type(y))))
        if x is not None:
            self.x_grid_lines = x
        if y is not None:
            self.y_grid_lines = y

    def legend_position(self, position):
        if not position in ('bottom', 'right', 'inset'):
            raise ValueError('Currently only bottom, right and inset supported for legend_position')
        self.show_legend_position = position

    def tooltip(self, show_tooltip):
        if not isinstance(show_tooltip, bool):
            raise TypeError("arg for show_tooltip must be boolean, received {}".format(type(show_tooltip)))
        self.show_tooltip = show_tooltip

    def add_color(self, color, y_label):
        three_hex = re.compile("^(#)?[A-Fa-f0-9]{3}$")
        six_hex = re.compile("^(#)?[A-Fa-f0-9]{6}$")
        if color.lower() in single_letter_color_mapping:
            self.colors[y_label] = single_letter_color_mapping[color]
        elif color.lower() in color_mapping:
            self.colors[y_label] = color_mapping[color]
        elif three_hex.match(color) or six_hex.match(color):
            self.colors[y_label] = color
        else:
            msg = "color {} not recognised for {}, please use a recognised color or hex code"
            raise ValueError(msg.format(color, y_label))

    def get_legend_for_json(self):
        return {
            'show': self.show_legend,
            'position': self.show_legend_position
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
            'enabled': self.show_subchart
        }
        return subchart

    def get_size_for_json(self):
        size = {}
        if self.height_value:
            size['height'] = self.height_value
        if self.width_value:
            size['width'] = self.width_value
        return size

    def get_points_for_json(self):
        return {
            'show': self.show_points
        }

    def get_tooltip_for_json(self):
        return{
            'show': self.show_tooltip
        }

    def get_donut_for_json(self):
        return {}

    def reset_data(self):
        self.x_data = []
        self.y_data = []
        self.data = []

    def plot_graph(self, chart_json):
        with open(temp_path, 'w') as f:
            f.write(template.render(
                title=self.name,
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
            'size': self.get_size_for_json(),
            'points': self.get_points_for_json(),
            'donut': self.get_donut_for_json(),
            'tooltip': self.get_tooltip_for_json()
        }
        chart_json = json.dumps(chart_json)
        return chart_json

    def get_data_for_json(self):
        raise NotImplementedError

    def get_axis_for_json(self):
        raise NotImplementedError
