import unittest
import json

from c3pyo import LineChart, SplineChart, StepChart

class TestLineChart(unittest.TestCase):
    def test_line_chart_list_input(self):
        chart1 = LineChart()
        x_data = [1, 2, 3, 4, 5]
        y_data = [10, 20, 30, 40, 50]
        chart1.set_x_data(x_data)
        chart1.set_y_data(y_data)
        output_json = chart1.json()
        output = json.loads(output_json)

        self.assertIn("bindto", output)
        self.assertEqual(output['bindto'], '#chart_div')
        self.assertIn("points", output)
        self.assertIn("grid", output)
        self.assertIs(output['grid']['x']['show'], False)
        self.assertIs(output['grid']['y']['show'], False)
        self.assertIn("data", output)
        self.assertEqual(output['data']['x'], 'x')
        self.assertEqual(output['data']['type'], 'line')
        self.assertEqual(output['data']['columns'][0], ['x', 1, 2, 3, 4, 5])
        self.assertEqual(output['data']['columns'][1], ['y1', 10, 20, 30, 40, 50])
        self.assertIs(output['legend']['show'], True)

    def test_line_chart_dict_input(self):
        chart2 = LineChart()
        x_data = {"x_name": [2, 3, 4]}
        y_data = {"y_name_1": [5, 6, 7], "y_name_2": [8, 9, 10], "y_name_3": [11, 12, 13]}
        chart2.set_x_data(x_data)
        chart2.set_y_data(y_data)
        output_json = chart2.json()
        output = json.loads(output_json)

        self.assertIn("bindto", output)
        self.assertEqual(output['bindto'], '#chart_div')
        self.assertIn("points", output)
        self.assertIn("grid", output)
        self.assertIs(output['grid']['x']['show'], False)
        self.assertIs(output['grid']['y']['show'], False)
        self.assertIn("data", output)
        self.assertEqual(output['data']['x'], 'x_name')
        self.assertEqual(output['data']['type'], 'line')
        self.assertEqual(output['data']['columns'][0], ['x_name', 2, 3, 4])
        self.assertEqual(output['data']['columns'][1], ['y_name_1', 5, 6, 7])
        self.assertEqual(output['data']['columns'][2], ['y_name_2', 8, 9, 10])
        self.assertEqual(output['data']['columns'][3], ['y_name_3', 11, 12, 13])
        self.assertIs(output['legend']['show'], True)

    def test_line_chart_missing_x_data(self):
        chart3 = LineChart()
        y_data = {"y_name_1": [14, 15, 16], "y_name_2": [17, 18, 19]}
        chart3.set_y_data(y_data)
        output_json = chart3.json()
        output = json.loads(output_json)

        self.assertEqual(output['data']['x'], 'x')
        self.assertEqual(output['data']['columns'][0], ['x', 1, 2, 3])
        self.assertEqual(output['data']['columns'][1], ['y_name_1', 14, 15, 16])
        self.assertEqual(output['data']['columns'][2], ['y_name_2', 17, 18, 19])

        chart4 = LineChart()
        y_data = [20, 21, 22, 23, 24]
        chart4.set_y_data(y_data)
        output_json = chart4.json()
        output = json.loads(output_json)

        self.assertEqual(output['data']['x'], 'x')
        self.assertEqual(output['data']['columns'][0], ['x', 1, 2, 3, 4, 5])
        self.assertEqual(output['data']['columns'][1], ['y1', 20, 21, 22, 23, 24])
        


