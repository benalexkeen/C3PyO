import datetime
import numbers

from c3pyo import C3Chart
from c3pyo.utils import is_iterable, DATE_FORMAT, DATETIME_FORMAT

try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False


class LineChart(C3Chart):
    def __init__(self, **kwargs):
        super(LineChart, self).__init__(**kwargs)
        self.set_area(kwargs)
        self.data = []
        self.y_labels = []
        self.x_is_dates = False
        self.x_is_datetimes = False
        self.x_s = {}

    def set_area(self, kwargs):
        self.area = kwargs.get('area', False)
        msg = 'area must be a boolean' 
        assert isinstance(self.area, bool), msg

    def set_data(self, data):
        if isinstance(data, dict):
            if 'x' in data:
                x_data = ['x']
                x_data.extend(data['x'])
                self.data.append(x_data)
                y_data = ['y']
                y_data.extend(data['y'])
                self.data.append(y_data)
                self.x_s['y'] = 'x'
            else:
                for key in sorted(list(data.keys())):
                    msg = "missing '{} in data for key {}"
                    assert 'x' in data[key], msg.format('x', key)
                    assert 'y' in data[key], msg.format('y', key)
                    x_label = 'x_{}'.format(key)
                    self.x_s[key] = x_label
                    key_data_x = [x_label]
                    key_data_x.extend(data[key]['x'])
                    key_data_y = [key]
                    key_data_y.extend(data[key]['y'])
                    self.y_labels.append(key)
                    self.data.append(key_data_x)
                    self.data.append(key_data_y)
        elif is_iterable(data):
            if all([isinstance(x, numbers.Number) for x in data]):
                x_data = ['x']
                y_data = ['y']
                for idx, value in enumerate(data):
                    x_data.append(idx)
                    y_data.append(value)
                self.data.append(x_data)
                self.data.append(y_data)
                self.x_s['y'] = 'x'
            else:
                msg = "lineChart data must have an even number of collections, received {}"
                assert len(data) % 2 == 0, msg.format(data)
                msg = "Data must be an collection of collections, received {} of type {}"
                for idx, iterable in enumerate(data):
                    name_idx = idx // 2
                    x_name = "x{}".format(name_idx)
                    y_name = "y{}".format(name_idx)
                    if idx % 2 == 0:
                        self.x_s[y_name] = x_name
                        data_item = [x_name]
                    else:
                        data_item = [y_name]
                    data_item.extend(iterable)
                    self.data.append(data_item)
        elif PANDAS:
            if isinstance(data, pd.DataFrame):
                if data.index.name:
                    x_label = data.index.name
                else:
                    x_label = 'x'
                x_data = [x_label]
                x_data.extend(list(data.index))
                self.data.append(x_data)
                for column in data:
                    self.x_s[column] = x_label
                    col_data = [column]
                    col_data.extend(list(data[column]))
                    self.data.append(col_data)
            elif isinstance(data, pd.Series):
                if data.name:
                    y_label = data.name
                else:
                    y_label = 'y'
                self.x_s[y_label] = 'x'
                x_data = ['x']
                x_data.extend(list(data.index))
                self.data.append(x_data)
                y_data = [y_label]
                y_data.extend(list(data))
                self.data.append(y_data)
        else:
            raise TypeError("y_data must be a dict or an iterable")

    def get_type(self):
        if self.area:
            self.chart_type = 'area'
        else:
            self.chart_type = 'line'

    def get_all_data_for_plot(self):
        x_is_dates = False
        x_is_datetimes = False
        for x_key in self.x_s:
            for item in self.data:
                if item[0] == x_key:
                    x_is_dates = [isinstance(x, datetime.date) for x in item[1:]]
                    x_is_datetimes = [isinstance(x, datetime.datetime) for x in item[1:]]

        if all(x_is_dates) and not all(x_is_datetimes):
            self.x_is_dates = True
            self.x_data = [x.strftime(DATE_FORMAT) for x in self.x_data]
        if all(x_is_datetimes):
            self.x_is_datetimes = True
            self.x_data = [x.strftime(DATETIME_FORMAT) for x in self.x_data]

        all_data = self.data
        return all_data

    def get_data_for_json(self):
        self.get_type()
        self.check_chart_type()
        data = {
            'columns': self.get_all_data_for_plot(),
            'type': self.chart_type,
            'xs': self.x_s
        }
        if self.x_is_datetimes:
            data['xFormat'] = DATETIME_FORMAT
        elif self.x_is_dates:
            data['xFormat'] = DATE_FORMAT
        return data

    def get_axis_for_json(self):
        if self.x_is_datetimes:
            return {
                'x': {
                    'type': 'timeseries',
                    'tick': {
                        'format': DATETIME_FORMAT
                    }
                }
            }
        elif self.x_is_dates:
            return {
                'x': {
                    'type': 'timeseries',
                    'tick': {
                        'format': DATE_FORMAT
                    }
                }
            }
        else:
            return {}

    def check_chart_type(self):
        valid_types = ('line', 'spline', 'step', 'area', 'area-spline', 'area-step')
        assert self.chart_type in valid_types, self.chart_type

    def plot(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)


class SplineChart(LineChart):
    def __init__(self, **kwargs):
        super(SplineChart, self).__init__(**kwargs)

    def get_type(self):
        if self.area:
            self.chart_type = 'area-spline'
        else:
            self.chart_type = 'spline'


class StepChart(LineChart):
    def __init__(self, **kwargs):
        super(StepChart, self).__init__(**kwargs)

    def get_type(self):
        if self.area:
            self.chart_type = 'area-step'
        else:
            self.chart_type = 'step'