import numbers

from c3pyo import C3Chart
from c3pyo.utils import is_iterable

try:
    import pandas as pd
    PANDAS = True
except ImportError:
    PANDAS = False


class PieChart(C3Chart):
    def __init__(self, **kwargs):
        super(PieChart, self).__init__(**kwargs)
        self.data = []
        self.chart_type = 'pie'

    def set_data(self, data):
        if is_iterable(data):
            for idx, value in enumerate(data):
                if isinstance(value, numbers.Number):
                    self.data.append(['y{}'.format(idx+1), value])
                else:
                    msg = 'Expected collection of numbers, received {}'
                    raise TypeError(msg.format(value))
        elif isinstance(data, dict):
            for key in data:
                if isinstance(data[key], numbers.Number):
                    self.data.append([key, data[key]])
                else:
                    msg = 'Expected number, received {} of type {}'
                    raise TypeError(msg.format(data[key], type(key)))
        elif PANDAS:
            if isinstance(data, pd.Series):
                for idx in data.index:
                    self.data.append([idx, data.loc[idx]])
            elif isinstance(data, pd.DataFrame):
                msg = "DataFrames not currently supported for {} charts, use Series"
                raise TypeError(msg.format(self.chart_type))
        else:
            msg = "data must be a collection or dict, received {} of type {}"
            raise TypeError(msg.format(data, type(data)))

    def get_data_for_json(self):
        return {
            'columns': self.data,
            'type': self.chart_type
            }

    def get_axis_for_json(self):
        return {}

    def plot(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)


class DonutChart(PieChart):
    def __init__(self, **kwargs):
        super(DonutChart, self).__init__(**kwargs)
        self.chart_type = 'donut'
