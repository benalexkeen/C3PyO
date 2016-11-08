from c3pyo import C3Chart
from c3pyo.utils import is_iterable

try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False


class BarChart(C3Chart):
    def __init__(self, **kwargs):
        super(BarChart, self).__init__(**kwargs)
        self.bar_ratio = kwargs.get('bar_ratio', 0.8)
        self.data = []
        self.chart_type = 'bar'
        self.y_number = 1
        self.stacked_bar = kwargs.get('stacked', False)
        self.x_labels = kwargs.get('x_ticklabels', [])

    def set_xticklabels(self, ticklabels):
        self.x_labels.extend(ticklabels)

    def stacked(self, stacked_bar):
        if not isinstance(stacked_bar, bool):
            raise TypeError("arg for stacked must be boolean, received {}".format(type(stacked_bar)))
        self.stacked_bar = stacked_bar

    def plot(self, y, color=None, label=None):
        if not label:
            y_series_label = "y{}".format(self.y_number)
        else:
            y_series_label = label
        y_data = [y_series_label]
        y_data.extend(list(y))
        self.data.append(y_data)

    def get_data_for_json(self):
        data = {
            'columns': self.data,
            'type': self.chart_type
        }
        if self.stacked_bar:
            data['groups'] = [[series[0] for series in self.data]]
        return data

    def get_axis_for_json(self):
        return {
            'x': {
                'type': 'category',
                'categories': self.x_labels,
                'label': self.label_for_x
            },
            'y': {
                'label': self.label_for_y
            }
        }

    def show(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)
