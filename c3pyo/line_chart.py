import datetime

from c3pyo import C3Chart
from c3pyo.utils import DATE_FORMAT, DATETIME_FORMAT, valid_types


class LineChart(C3Chart):
    def __init__(self, **kwargs):
        super(LineChart, self).__init__(**kwargs)
        self.set_area(kwargs)
        self.data = []
        self.x_is_dates = False
        self.x_is_datetimes = False
        self.x_s = {}
        self.y_number = 1

    def set_area(self, kwargs):
        self.show_area = kwargs.get('area', False)
        msg = 'area must be a boolean' 
        assert isinstance(self.show_area, bool), msg

    def plot(self, x, y, color=None, marker='o', label=None, type=None):
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
        self.data.append(x_data)
        self.data.append(y_data)
        self.x_s[y_series_label] = x_series_label
        if marker == 'o':
            self.show_points = True
        elif marker is None:
            self.show_points = False
        else:
            raise ValueError("Currently only 'o' and None supported for marker")
        if type is not None and type in valid_types:
            self.types[y_series_label] = type
        else:
            raise ValueError('type {} not recognised, use type from {}'.format(type, valid_types))

    def get_type(self):
        if self.show_area:
            self.chart_type = 'area'
        else:
            self.chart_type = 'line'

    def get_all_data_for_plot(self):
        for x_key in self.x_s.values():
            for idx, item in enumerate(self.data):
                if item[0] == x_key:
                    x_is_dates = [isinstance(x, datetime.date) for x in item[1:]]
                    x_is_datetimes = [isinstance(x, datetime.datetime) for x in item[1:]]
                    if all(x_is_dates) and not all(x_is_datetimes):
                        self.x_is_dates = True
                        self.data[idx] = [x.strftime(DATETIME_FORMAT) if isinstance(x, datetime.date) else x for x in item]
                    elif all(x_is_datetimes):
                        self.x_is_datetimes = True
                        self.data[idx] = [x.strftime(DATETIME_FORMAT) if isinstance(x, datetime.date) else x for x in item]
        all_data = self.data
        return all_data

    def get_data_for_json(self):
        self.get_type()
        self.check_chart_type()
        data = {
            'columns': self.get_all_data_for_plot(),
            'type': self.chart_type,
            'colors': self.colors,
            'xs': self.x_s
        }
        if self.x_is_datetimes:
            data['xFormat'] = DATETIME_FORMAT
        elif self.x_is_dates:
            data['xFormat'] = DATE_FORMAT
        return data

    def get_axis_for_json(self):
        if self.x_is_datetimes:
            axis = {
                'x': {
                    'type': 'timeseries',
                    'tick': {
                        'format': DATETIME_FORMAT
                    },
                },
                'y': {}
            }
        elif self.x_is_dates:
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
        if self.label_for_x:
            axis['x']['label'] = self.label_for_x
        if self.label_for_y:
            axis['y']['label'] = self.label_for_y
        if self.y_max:
            axis['y']['max'] = self.y_max
        if self.y_min:
            axis['y']['min'] = self.y_min
        return axis


    def check_chart_type(self):
        assert self.chart_type in valid_types, self.chart_type

    def show(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)


class SplineChart(LineChart):
    def __init__(self, **kwargs):
        super(SplineChart, self).__init__(**kwargs)

    def get_type(self):
        if self.show_area:
            self.chart_type = 'area-spline'
        else:
            self.chart_type = 'spline'


class StepChart(LineChart):
    def __init__(self, **kwargs):
        super(StepChart, self).__init__(**kwargs)

    def get_type(self):
        if self.show_area:
            self.chart_type = 'area-step'
        else:
            self.chart_type = 'step'


class ScatterChart(LineChart):
    def __init__(self, **kwargs):
        super(ScatterChart, self).__init__(**kwargs)

    def get_type(self):
        self.chart_type = 'scatter'
