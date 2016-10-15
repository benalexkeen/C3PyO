# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import webbrowser
import os
import json

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
        self.name = kwargs.get('name', 'chart')
        self.set_show_points(kwargs)
        self.set_grid_lines(kwargs)
        self.set_legend(kwargs)
        self.x_data = []
        self.y_data = []
        self.x_label = kwargs.get('x_label', 'x')
        self.y_labels = []
        self.save_output = False

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
        self.show_legend = kwargs.get('show_legend', False)
        self.legend_position = kwargs.get('legend_position')
        if not self.legend_position:
            self.legend_position = 'bottom'
        if self.legend_position:
            self.show_legend = True
        msg = 'Currently only bottom, right and inset supported for legend_position'
        assert self.legend_position in ('bottom', 'right', 'inset'), msg
        msg = 'show_legend must be a boolean'
        assert isinstance(self.show_legend, bool), msg

    def set_show_points(self, kwargs):
        self.show_points = kwargs.get('show_points', True)
        msg = 'show_points must be a boolean'
        assert isinstance(self.show_points, bool), msg

    def set_x_data(self, data):
        if is_iterable(data):
            self.x_data = data
        if isinstance(data, dict):
            x_data = data.values()[0]
            if not is_iterable(x_data):
                raise TypeError("x_data must be iterable")
            self.x_data = x_data
            self.x_label = data.keys()[0]
        else:
            raise TypeError("x_data must be iterable or of type dict")

    def set_y_data(self, data):
        if isinstance(data, dict):
            for key in data:
                self.y_labels.append(key)
                self.y_data.append(data[key])
        elif is_iterable(data):
            is_iterable_of_iterables = [is_iterable(x) for x in data]
            if all([is_iterable(x) for x in data]):
                self.y_data.append(data)
            elif not any(is_iterable_of_iterables):
                self.y_data.append(data)
            else:
                raise TypeError("y_data cannot be composed of iterables and non-iterables")
        else:
            raise TypeError("y_data must be a dict or an iterable")

    def reset_data(self):
        self.x_data = []
        self.y_data = []

    def add_missing_data(self):
        if not self.y_data:
            raise ValueError("No y values, set values using set_y_data")
        if not self.x_data:
            self.x_data = range(len(self.y_data))
        if len(self.y_labels) < len(self.y_data):
            for i in range(len(self.y_labels), len(self.y_data)):
                self.y_labels.append("y{}".format(i+1))

    def get_all_data_for_plot(self):
        x_data = [str(self.x_label)]
        x_data.extend(self.x_data)
        y_data = []
        for i in range(len(self.y_data)):
            y_series = [str(self.y_labels[i])]
            y_series.extend(self.y_data[i])
            y_data.append(y_series)
        all_data = [x_data]
        all_data.extend(y_data)
        all_data = json.dumps(all_data)
        return all_data

    def plot(self):
        self.add_missing_data()
        all_data = self.get_all_data_for_plot()
        print all_data
        with open(temp_path, 'w') as f:
            f.write(template.render(
                title=self.name, 
                body='Hello, World',
                data=all_data,
                x_label=self.x_label,
                x_grid_lines=json.dumps(self.x_grid_lines),
                y_grid_lines=json.dumps(self.y_grid_lines),
                show_legend=json.dumps(self.show_legend),
                legend_position=json.dumps(self.legend_position),
                show_points=json.dumps(self.show_points)
                ))
        webbrowser.open(url)

class lineChart(C3Chart):
    def __init__(self, **kwargs):
        super(lineChart, self).__init__(**kwargs)



