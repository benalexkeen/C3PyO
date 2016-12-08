import datetime

from c3pyo import C3Chart
from c3pyo.utils import DATE_FORMAT, DATETIME_FORMAT, valid_types


class LineChart(C3Chart):
    def __init__(self, **kwargs):
        super(LineChart, self).__init__(**kwargs)
        self._data = []
        self._x_is_dates = False
        self._x_is_datetimes = False
        self.x_s = {}
        self.y_number = 1

    def plot(self, x, y, color=None, marker='o', label=None, type=None):
        x = list(x)
        y = list(y)
        if not len(x) == len(y):
            raise ValueError("The length of the two passed arrays for x and y are different")
        if not label:
            y_series_label = "y{}".format(self.y_number)
            self.y_number += 1
        else:
            y_series_label = label
        x_series_label = "x_{}".format(y_series_label)
        x_data = [x_series_label]
        x_data.extend(list(x))
        y_data = [y_series_label]
        y_data.extend(list(y))
        if color:
            self.add_color(color, y_series_label)
        self._data.append(x_data)
        self._data.append(y_data)
        self.x_s[y_series_label] = x_series_label
        if marker == 'o' or marker is True:
            self._show_points = True
        elif marker is None or marker is False:
            self._show_points = False
        else:
            raise ValueError("Currently only 'o' and None supported for marker")
        if (type is not None) and (type in valid_types):
            self._types[y_series_label] = type
        elif type is None:
            pass
        else:
            raise ValueError('type {} not recognised, use type from {}'.format(type, valid_types))

    def get_type(self):
        if self._show_area:
            self._chart_type = 'area'
        else:
            self._chart_type = 'line'

    def get_all_data_for_plot(self):
        for x_key in self.x_s.values():
            for idx, item in enumerate(self._data):
                if item[0] == x_key:
                    x_is_dates = [isinstance(x, datetime.date) for x in item[1:]]
                    x_is_datetimes = [isinstance(x, datetime.datetime) for x in item[1:]]
                    if all(x_is_dates) and not all(x_is_datetimes):
                        self._x_is_dates = True
                        self._data[idx] = [x.strftime(DATE_FORMAT) if isinstance(x, datetime.date) else x for x in item]
                    elif all(x_is_datetimes):
                        self._x_is_datetimes = True
                        self._data[idx] = [x.strftime(DATETIME_FORMAT) if isinstance(x, datetime.date) else x for x in item]
        all_data = self._data
        return all_data

    def get_data_for_json(self):
        self.get_type()
        self.check_chart_type()
        data = {
            'columns': self.get_all_data_for_plot(),
            'type': self._chart_type,
            'colors': self._colors,
            'xs': self.x_s
        }
        if self._x_is_datetimes:
            data['xFormat'] = DATETIME_FORMAT
        elif self._x_is_dates:
            data['xFormat'] = DATE_FORMAT
        return data

    def get_axis_for_json(self):
        if self._x_is_datetimes:
            axis = {
                'x': {
                    'type': 'timeseries',
                    'tick': {
                        'format': DATETIME_FORMAT
                    },
                },
                'y': {}
            }
        elif self._x_is_dates:
            axis = {
                'x': {
                    'type': 'timeseries',
                    'tick': {
                        'format': DATE_FORMAT
                    },
                },
                'y': {}
            }
        else:
            axis = {
                'x': {},
                'y': {}
            }
        if self._label_for_x:
            axis['x']['label'] = self._label_for_x
        if self._label_for_y:
            axis['y']['label'] = self._label_for_y
        if self._y_max:
            axis['y']['max'] = self._y_max
        if self._y_min:
            axis['y']['min'] = self._y_min
        return axis

    def check_chart_type(self):
        assert self._chart_type in valid_types, self._chart_type


class SplineChart(LineChart):
    def __init__(self, **kwargs):
        super(SplineChart, self).__init__(**kwargs)

    def get_type(self):
        if self._show_area:
            self._chart_type = 'area-spline'
        else:
            self._chart_type = 'spline'


class StepChart(LineChart):
    def __init__(self, **kwargs):
        super(StepChart, self).__init__(**kwargs)

    def get_type(self):
        if self._show_area:
            self._chart_type = 'area-step'
        else:
            self._chart_type = 'step'


class ScatterChart(LineChart):
    def __init__(self, **kwargs):
        super(ScatterChart, self).__init__(**kwargs)

    def get_type(self):
        self._chart_type = 'scatter'
