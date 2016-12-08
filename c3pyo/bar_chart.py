import numbers

from c3pyo import C3Chart
from c3pyo.utils import valid_types


class BarChart(C3Chart):
    def __init__(self, **kwargs):
        super(BarChart, self).__init__(**kwargs)
        self._bar_ratio = kwargs.get('bar_ratio', 0.8)
        self._data = []
        self._chart_type = 'bar'
        self.y_number = 1
        self._stacked_bar = kwargs.get('stacked', False)
        self._x_labels = kwargs.get('x_ticklabels', [])

    def set_xticklabels(self, ticklabels):
        self._x_labels.extend(ticklabels)

    def stacked(self, stacked_bar):
        if not isinstance(stacked_bar, bool):
            raise TypeError("arg for stacked must be boolean, received {}".format(type(stacked_bar)))
        self._stacked_bar = stacked_bar

    def bar_width(self, bar_width):
        if not isinstance(bar_width, numbers.Number):
            msg = "arg for bar_width must be boolean, received {} of type {}"
            raise TypeError(msg.format(bar_width, type(bar_width)))
        elif bar_width <= 0 or bar_width > 1:
            msg = "bar_width must be between 0 and 1.0, received {}"
            raise ValueError(msg.format(bar_width))
        else:
            self._bar_ratio = bar_width

    def plot(self, y, color=None, label=None, type=None):
        y = list(y)
        if not label:
            y_series_label = "y{}".format(self.y_number)
            self.y_number += 1
        else:
            y_series_label = label
        y_data = [y_series_label]
        y_data.extend(list(y))
        if color:
            self.add_color(color, y_series_label)
        if (type is not None) and (type in valid_types):
            self._types[y_series_label] = type
        elif type is not None:
            raise ValueError('type {} not recognised, use type from {}'.format(type, valid_types))
        self._data.append(y_data)

    def get_data_for_json(self):
        data = {
            'columns': self._data,
            'type': self._chart_type,
            'colors': self._colors,
        }
        if self._stacked_bar:
            data['groups'] = [[series[0] for series in self._data]]
            data['order'] = None
        return data

    def get_bar_for_json(self):
        return {'width': {'ratio': self._bar_ratio}}

    def get_axis_for_json(self):
        return {
            'x': {
                'type': 'category',
                'categories': self._x_labels,
                'label': self._label_for_x
            },
            'y': {
                'label': self._label_for_y
            }
        }

