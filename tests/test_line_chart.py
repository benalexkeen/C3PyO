import unittest
import json

from c3pyo import LineChart


class TestLineChart(unittest.TestCase):
    def test_line_chart_list_input(self):
        chart1 = LineChart()
        data = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]]
        chart1.plot(data[0], data[1])
        chart1.bind_to('a_div_name')
        output_json = chart1.json()
        output = json.loads(output_json)

        self.assertIn("bindto", output)
        self.assertEqual(output['bindto'], '#a_div_name')
        self.assertIn("points", output)
        self.assertIn("grid", output)
        self.assertIs(output['grid']['x']['show'], False)
        self.assertIs(output['grid']['y']['show'], False)
        self.assertIn("data", output)
        self.assertEqual(output['data']['xs']['y1'], 'x_y1')
        self.assertEqual(output['data']['type'], 'line')
        self.assertEqual(output['data']['columns'][0], ['x_y1', 1, 2, 3, 4, 5])
        self.assertEqual(output['data']['columns'][1], ['y1', 10, 20, 30, 40, 50])
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
        chart2.plot(data['var1']['x'], data['var1']['y'], label='var1')
        chart2.plot(data['var2']['x'], data['var2']['y'], label='var2')
        chart2.plot(data['var3']['x'], data['var3']['y'], label='var3')
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
        chart3.plot(data['x'], data['y'], label='y')
        output_json = chart3.json()
        output = json.loads(output_json)

        self.assertEqual(output['data']['xs']['y'], 'x_y')
        self.assertEqual(output['data']['columns'][0], ['x_y', 14, 15, 16])
        self.assertIn(['y', 17, 18, 19], output['data']['columns'])
