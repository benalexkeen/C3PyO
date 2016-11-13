import json

from nose.tools import assert_equals, assert_is

import c3pyo as c3


def test_step_chart():
    x = [1, 2, 3, 4, 5, 6, 7]
    y1 = (x ** 2 for x in range(0, 7))

    chart = c3.StepChart()
    chart.plot(x, y1, color='k', marker=False, label="series_1")
    chart.y_range(1, 100)
    chart.subchart(True)
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['axis']['y']['min'], 1)
    assert_equals(res['axis']['y']['max'], 100)
    assert_equals(res['data']['colors']['series_1'], '#000000')
    assert_equals(res['data']['type'], 'step')
    assert_is(res['points']['show'], False)
    assert_is(res['subchart']['enabled'], True)
    assert_is(res['zoom']['enabled'], False)
