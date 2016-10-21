import json
import datetime

from .base import C3Chart
from c3pyo.utils import is_iterable, DATE_FORMAT, DATETIME_FORMAT


class LineChart(C3Chart):
    def __init__(self, **kwargs):
        super(LineChart, self).__init__(**kwargs)
        self.set_area(kwargs)
        self.set_show_points(kwargs)
        self.x_data = []
        self.y_data = []
        self.y_labels = []
        self.x_is_dates = False
        self.x_is_datetimes = False

    def set_show_points(self, kwargs):
        self.show_points = kwargs.get('show_points', True)
        msg = 'show_points must be a boolean'
        assert isinstance(self.show_points, bool), msg

    def set_area(self, kwargs):
        self.area = kwargs.get('area', False)
        msg = 'area must be a boolean' 
        assert isinstance(self.area, bool), msg

    def set_x_data(self, data):
        if is_iterable(data):
            self.x_data = data
        elif isinstance(data, dict):
            x_data = data.values()
            for item in x_data:
                if not is_iterable(x_data):
                    raise TypeError("x_data must be iterable")
            self.x_data = x_data
            self.x_label = list(data.keys())[0]
        else:
            raise TypeError("x_data must be iterable or of type dict")

        x_is_dates = [isinstance(x, datetime.date) for x in self.x_data]
        x_is_datetimes = [isinstance(x, datetime.datetime) for x in self.x_data]

        if all(x_is_dates) and not all(x_is_datetimes):
            self.x_is_dates = True
            self.x_data = [x.strftime(DATE_FORMAT) for x in self.x_data]
        if all(x_is_datetimes):
            self.x_is_datetimes = True
            self.x_data = [x.strftime(DATETIME_FORMAT) for x in self.x_data]

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

    def get_type(self):
        if self.area:
            self.chart_type = 'area'
        else:
            self.chart_type = 'line'

    def add_missing_data(self):
        if not self.y_data:
            raise ValueError("No y values, set values using set_y_data")
        if not self.x_data:
            self.x_data = [(x + 1) for x in range(len(self.y_data[0]))]
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
        return all_data

    def get_data_for_json(self):
        data = {
            'x': self.x_label,
            'columns': self.get_all_data_for_plot(),
            'type': self.chart_type
        }
        if self.x_is_datetimes:
            data['xFormat'] = DATETIME_FORMAT
        elif self.x_is_dates:
            data['xFormat'] = DATE_FORMAT
        return data

    def get_points_for_json(self):
        return {
            'show': self.show_points
        }

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

    def get_chart_json(self):
        self.add_missing_data()
        self.get_type()
        self.check_chart_type()
        chart_json = {
            'bindto': self.chart_div,
            'data': self.get_data_for_json(),
            'legend': self.get_legend_for_json(),
            'points': self.get_points_for_json(),
            'grid': self.get_grid_for_json(),
            'axis': self.get_axis_for_json(),
        }

        chart_json = json.dumps(chart_json)
        return chart_json

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