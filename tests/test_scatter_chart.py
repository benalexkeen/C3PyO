import json

from nose.tools import assert_equals, assert_is

import c3pyo as c3


def test_scatter_chart():
    x1 = [5, 10, 15, 20, 25, 30, 35]
    y1 = (x ** 2 - x for x in range(0, 7))
    x2 = [2, 4, 6, 8]
    y2 = [32, 12, 26, 78]

    chart = c3.StepChart()
    chart.plot(x1, y1, color='green', label="series_1")
    chart.plot(x2, y2, color='lightskyblue', label="series_2")
    chart.legend_position('right')
    chart.zoom(True)
    chart.gridlines(True, False)
    chart.tooltip(False)
    chart.area(True)
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['data']['type'], 'area-step')
    assert_equals(res['data']['colors']['series_2'], '#87CEFA')
    assert_equals(res['data']['colors']['series_1'], '#008000')
    assert_equals(res['legend']['position'], 'right')
    assert_is(res['grid']['x']['show'], True)
    assert_is(res['grid']['y']['show'], False)
    assert_is(res['tooltip']['show'], False)
    assert_is(res['subchart']['enabled'], False)
    assert_is(res['zoom']['enabled'], True)
