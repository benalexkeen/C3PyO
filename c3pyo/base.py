# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import webbrowser
import os
import json
import numbers
import re
import tempfile
import shutil

from jinja2 import Environment, PackageLoader

from c3pyo.utils import single_letter_color_mapping, color_mapping

__here__ = os.path.dirname(os.path.abspath(__file__))

CHART_BASE_FILENAME = './chart.html'

pl = PackageLoader('c3pyo', 'templates')
jinja2_env = Environment(loader=pl)


class C3Chart(object):
    """
    C3Chart Base Class
    """

    def __init__(self, **kwargs):
        self._chart_type = None
        self._data = None
        self._name = kwargs.get('name', 'C3 Chart')
        self._show_points = kwargs.get('show_points', True)
        self._show_legend = kwargs.get('show_legend', True)
        self._show_legend_position = kwargs.get('legend_position', 'bottom')
        self._label_for_x = kwargs.get('xlabel', None)
        self._label_for_y = kwargs.get('ylabel', None)
        self._x_grid_lines = kwargs.get('gridlines', False)
        self._y_grid_lines = kwargs.get('gridlines', False)
        self._show_area = kwargs.get('area', False)
        self._zoom_on_off = kwargs.get('zoom', False)
        self._show_subchart = kwargs.get('subchart', False)
        self._height_value = kwargs.get('height', 0)
        self._width_value = kwargs.get('width', 0)
        self._y_max = kwargs.get('y_max', None)
        self._y_min = kwargs.get('y_min', None)
        self._show_tooltip = kwargs.get('tooltip', True)
        self._chart_div = '#{}'.format(kwargs.get('chart_div', 'chart_div'))
        self._colors = {}
        self._types = {}
        self._save_output = False

    def xlabel(self, label):
        self._label_for_x = label

    def ylabel(self, label):
        self._label_for_y = label

    def area(self, show_area):
        if not isinstance(show_area, bool):
            raise TypeError("arg for area must be boolean, received {}".format(type(show_area)))
        self._show_area = show_area

    def legend(self, show_legend):
        if not isinstance(show_legend, bool):
            raise TypeError("arg for legend must be boolean, received {}".format(type(show_legend)))
        self._show_legend = show_legend

    def zoom(self, zoom_on_off):
        if not isinstance(zoom_on_off, bool):
            raise TypeError("arg for zoom must be boolean, received {}".format(type(zoom_on_off)))
        self._zoom_on_off = zoom_on_off

    def subchart(self, show_subchart):
        if not isinstance(show_subchart, bool):
            raise TypeError("arg for subchart must be boolean, received {}".format(type(show_subchart)))
        self._show_subchart = show_subchart

    def height(self, height_value):
        msg = 'height must be a number, received {} of type {}'.format(height_value, type(height_value))
        if isinstance(height_value, bool):
            raise TypeError(msg)
        if not isinstance(height_value, numbers.Number):
            raise TypeError(msg)
        self._height_value = height_value

    def width(self, width_value):
        msg = 'width must be a number, received {} of type {}'.format(width_value, type(width_value))
        if isinstance(width_value, bool):
            raise TypeError(msg)
        if not isinstance(width_value, numbers.Number):
            raise TypeError(msg)
        self._width_value = width_value

    def y_range(self, y_min=None, y_max=None):
        if (not isinstance(y_min, numbers.Number) or isinstance(y_min, bool)) and y_min is not None:
            raise TypeError('y_min must be a number, received {} of type {}'.format(y_min, type(y_min)))
        if (not isinstance(y_max, numbers.Number) or isinstance(y_max, bool)) and y_max is not None:
            raise TypeError('y_max must be a number, received {} of type {}'.format(y_max, type(y_max)))
        if y_min is not None:
            self._y_min = y_min
        if y_max is not None:
            self._y_max = y_max

    def gridlines(self, x=None, y=None):
        msg = "arg for {} gridlines must be boolean, received {}"
        if x is not None:
            if not isinstance(x, bool):
                raise(TypeError(msg.format('x', type(x))))
            else:
                self._x_grid_lines = x
        if y is not None:
            if not isinstance(y, bool):
                raise(TypeError(msg.format('y', type(y))))
            self._y_grid_lines = y

    def legend_position(self, position):
        if position not in ('bottom', 'right', 'inset'):
            raise ValueError('Currently only bottom, right and inset supported for legend_position')
        self._show_legend_position = position

    def tooltip(self, show_tooltip):
        if not isinstance(show_tooltip, bool):
            raise TypeError("arg for show_tooltip must be boolean, received {}".format(type(show_tooltip)))
        self._show_tooltip = show_tooltip

    def bind_to(self, div_name):
        try:
            basestring
        except:
            basestring = str
        if not isinstance(div_name, basestring):
            msg = "parameter for bind_to must be string, received {} of type {}"
            raise TypeError(msg.format(div_name, type(div_name)))
        if div_name.startswith('#'):
            self._chart_div = div_name
        else:
            self._chart_div = '#{}'.format(div_name)

    def add_color(self, color, y_label):
        three_hex = re.compile("^(#)?[A-Fa-f0-9]{3}$")
        six_hex = re.compile("^(#)?[A-Fa-f0-9]{6}$")
        if color.lower() in single_letter_color_mapping:
            self._colors[y_label] = single_letter_color_mapping[color.lower()]
        elif color.lower() in color_mapping:
            self._colors[y_label] = color_mapping[color.lower()]
        elif three_hex.match(color) or six_hex.match(color):
            if color.startswith('#'):
                self._colors[y_label] = color
            else:
                self._colors[y_label] = '#{}'.format(color)
        else:
            msg = "color {} not recognised for {}, please use a recognised color or hex code"
            raise ValueError(msg.format(color, y_label))



    def get_legend_for_json(self):
        return {
            'show': self._show_legend,
            'position': self._show_legend_position
        }

    def get_grid_for_json(self):
        grid = {
            'x': {
                'show': self._x_grid_lines
            },
            'y': {
                'show': self._y_grid_lines
            }
        }
        if self._chart_type == 'bar':
            grid['y']['lines'] = [{'value': 0}]
        return grid

    def get_zoom_for_json(self):
        zoom = {
            'enabled': self._zoom_on_off
        }
        return zoom

    def get_subchart_for_json(self):
        subchart = {
            'enabled': self._show_subchart
        }
        return subchart

    def get_size_for_json(self):
        size = {}
        if self._height_value:
            size['height'] = self._height_value
        if self._width_value:
            size['width'] = self._width_value
        return size

    def get_points_for_json(self):
        return {
            'show': self._show_points
        }

    def get_tooltip_for_json(self):
        return{
            'show': self._show_tooltip
        }

    def get_donut_for_json(self):
        return {}

    def get_bar_for_json(self):
        return {}

    def plot_graph(self, chart_json):
        directory_name = tempfile.mkdtemp()
        template = jinja2_env.get_template(CHART_BASE_FILENAME)
        temp_path = os.path.join(directory_name, 'chart.html')
        with open(temp_path, 'w') as f:
            f.write(
                template.render(
                    title=self._name,
                    chart_json=chart_json,
                )
            )
        shutil.copytree(os.path.join(__here__, 'static'), os.path.join(directory_name, 'static'))
        url = 'file:///' + temp_path
        webbrowser.open(url)

    def json(self):
        res = self.get_chart_json()
        return res

    def get_chart_json(self):
        chart_json = {
            'bindto': self._chart_div,
            'data': self.get_data_for_json(),
            'legend': self.get_legend_for_json(),
            'grid': self.get_grid_for_json(),
            'axis': self.get_axis_for_json(),
            'zoom': self.get_zoom_for_json(),
            'subchart': self.get_subchart_for_json(),
            'size': self.get_size_for_json(),
            'points': self.get_points_for_json(),
            'donut': self.get_donut_for_json(),
            'tooltip': self.get_tooltip_for_json(),
            'bar': self.get_bar_for_json(),
        }
        chart_json = json.dumps(chart_json)
        return chart_json

    def show(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)

    def get_data_for_json(self):
        raise NotImplementedError

    def get_axis_for_json(self):
        raise NotImplementedError
