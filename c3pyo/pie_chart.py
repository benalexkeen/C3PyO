import numbers

from c3pyo import C3Chart


class PieChart(C3Chart):
    def __init__(self, **kwargs):
        super(PieChart, self).__init__(**kwargs)
        self.data = []
        self.chart_type = 'pie'
        self.y_number = 1

    def plot(self, y, color=None, label=None):
        if not label:
            y_series_label = "y{}".format(self.y_number)
        else:
            y_series_label = label
        if isinstance(y, numbers.Number):
            y_data = [y_series_label, y]
        else:
            y_data = [y_series_label]
            y_data.extend(y)
        self.data.append(y_data)

    def get_data_for_json(self):
        return {
            'columns': self.data,
            'type': self.chart_type
            }

    def get_axis_for_json(self):
        return {}

    def show(self):
        chart_json = self.get_chart_json()
        self.plot_graph(chart_json)


class DonutChart(PieChart):
    def __init__(self, **kwargs):
        super(DonutChart, self).__init__(**kwargs)
        self.chart_type = 'donut'
        self.donut_title_value = kwargs.get('donut_title', None)

    def donut_title(self, title):
        self.donut_title_value = title

    def get_donut_for_json(self):
        if not self.donut_title_value:
            return None
        else:
            return {'title': self.donut_title_value}
