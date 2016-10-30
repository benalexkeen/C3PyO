import unittest
import json

from c3pyo import LineChart, SplineChart, StepChart

class TestLineChart(unittest.TestCase):
    def test_line_chart_list_input(self):
        chart1 = LineChart()
        data = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]]
        chart1.set_data(data)
        output_json = chart1.json()
        output = json.loads(output_json)

        self.assertIn("bindto", output)
        self.assertEqual(output['bindto'], '#chart_div')
        self.assertIn("points", output)
        self.assertIn("grid", output)
        self.assertIs(output['grid']['x']['show'], False)
        self.assertIs(output['grid']['y']['show'], False)
        self.assertIn("data", output)
        self.assertEqual(output['data']['xs']['y0'], 'x0')
        self.assertEqual(output['data']['type'], 'line')
        self.assertEqual(output['data']['columns'][0], ['x0', 1, 2, 3, 4, 5])
        self.assertEqual(output['data']['columns'][1], ['y0', 10, 20, 30, 40, 50])
        self.assertIs(output['legend']['show'], True)

    def test_line_chart_dict_input(self):
        chart2 = LineChart()
        data = {
            'var1': {
                'x': [2, 3, 4],
                'y': [5, 6, 7]
            },
            'var2': {
                'x': [2, 3, 4],
                'y': [8, 9, 10]
            },
            'var3': {
                'x': [2, 3, 4],
                'y': [11, 12, 13]
            }
        }
        chart2.set_data(data)
        output_json = chart2.json()
        output = json.loads(output_json)

        self.assertIn("bindto", output)
        self.assertEqual(output['bindto'], '#chart_div')
        self.assertIn("points", output)
        self.assertIn("grid", output)
        self.assertIs(output['grid']['x']['show'], False)
        self.assertIs(output['grid']['y']['show'], False)
        self.assertIn("data", output)
        self.assertEqual(output['data']['type'], 'line')
        self.assertIn(['x_var1', 2, 3, 4], output['data']['columns'])
        self.assertIn(['var1', 5, 6, 7], output['data']['columns'])
        self.assertIn(['var2', 8, 9, 10], output['data']['columns'])
        self.assertIn(['var3', 11, 12, 13], output['data']['columns'])
        self.assertIs(output['legend']['show'], True)

    def test_line_chart_dict_input_2(self):
        chart3 = LineChart()
        data = {"x": [14, 15, 16], "y": [17, 18, 19]}
        chart3.set_data(data)
        output_json = chart3.json()
        output = json.loads(output_json)

        self.assertEqual(output['data']['xs']['y'], 'x')
        self.assertEqual(output['data']['columns'][0], ['x', 14, 15, 16])
        self.assertIn(['y', 17, 18, 19], output['data']['columns'])

        


