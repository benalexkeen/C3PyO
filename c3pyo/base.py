# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import webbrowser
import os
import json
import datetime

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
        self.x_label = kwargs.get('x_label', 'x')
        self.y_label = kwargs.get('y_label', 'y')
        self.chart_div = '#{}'.format(kwargs.get('chart_div', 'chart_div'))
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

    def get_legend_for_json(self):
        return {
            'show': self.show_legend,
            'position': self.legend_position
        }

    def get_grid_for_json(self):
        return {
            'x': {
                'show': self.x_grid_lines
            },
            'y': {
                'show': self.y_grid_lines
            }
        }

    def reset_data(self):
        self.x_data = []
        self.y_data = []

    def plot_graph(self, chart_json):
        with open(temp_path, 'w') as f:
            f.write(template.render(
                title=self.name, 
                body='Hello, World',
                chart_json=chart_json,
                ))
        webbrowser.open(url)
