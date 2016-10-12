# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import webbrowser
import os

from jinja2 import Environment, PackageLoader

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
        self.legend = kwargs.get('legend', 'right') # left, right, top, bottom, false
        self.hide_points = kwargs.get('hide_points', False)
        self.grid_lines = kwargs.get('grid_lines', False)
        self.x_data = []
        self.y_data = []
        self.y2_data = []
        self.x_label = kwargs.get('x_label', 'x')
        self.y_label = kwargs.get('y_label', 'y')
        self.y2_label = kwargs.get('y2_label', 'y2')
        self.save_output = False

    def set_x_data(self, iterable):
        if isinstance(iterable, list) or isinstance(iterable, set) or isinstance(iterable, tuple):
            self.x_data = iterable

    def reset_data(self):
        self.x_data = []
        self.y_data = []
        self.y2_data = []

    def plot(self):
        if not self.x_data:
            self.x_data = range(len(self.y_data))
        x_data = [self.x_label]
        x_data.extend(self.x_data)
        y_data = [self.y_label]
        y_data.extend(self.y_data)
        data = [x_data, y_data]
        with open(temp_path, 'w') as f:
            f.write(template.render(
                title=self.name, 
                body='Hello, World',
                data=data,
                x_label=str(self.x_label)
                ))
        webbrowser.open(url)

class lineChart(C3Chart):
    def __init__(self, **kwargs):
        super(lineChart, self).__init__(**kwargs)



