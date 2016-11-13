import datetime
import json

from nose.tools import assert_in, assert_equals

import c3pyo as c3


def test_spline_chart_datetimes():
    dts = [datetime.datetime(2015, 3, 5, x) for x in [10, 11, 12, 13, 14]]
    y1 = [10, 20, 30, 20, 10]
    y2 = [20, 10, 30, 40, 0]

    chart = c3.SplineChart()
    chart.plot(dts, y1, label="series_1")
    chart.plot(dts, y2, label="series_2")
    chart.legend_position('inset')
    chart.area(True)
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['axis']['x']['tick']['format'], '%Y-%m-%d %H:%M:%S')
    assert_equals(res['axis']['x']['type'], 'timeseries')
    assert_equals(len(res['data']['columns']), 4)
    assert_equals(res['data']['columns'][0][1], '2015-03-05 10:00:00')
    assert_equals(res['data']['type'], 'area-spline')
    assert_equals(res['legend']['position'], 'inset')
    assert_in(['series_1', 10, 20, 30, 20, 10], res['data']['columns'])


def test_spline_chart_dates():
    dates = [datetime.date(2017, 1, x) for x in [1, 2, 3, 4, 5]]
    y1 = [32.4, 15, 20, 12, 32]

    chart = c3.SplineChart()
    chart.plot(dates, y1, label='date_series')
    chart.gridlines(y=True)
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['axis']['x']['tick']['format'], '%Y-%m-%d')
    assert_equals(res['axis']['x']['type'], 'timeseries')
    assert_in('2017-01-04', res['data']['columns'][0])
    assert_equals(res['data']['type'], 'spline')
    assert_equals(res['grid']['x']['show'], False)
    assert_equals(res['grid']['y']['show'], True)
