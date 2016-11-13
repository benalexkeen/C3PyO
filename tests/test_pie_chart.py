import json

from nose.tools import assert_equals

import c3pyo as c3


def test_pie_chart():
    chart = c3.PieChart()
    chart.plot(5, color='blue', label='var1')
    chart.plot(10, color='white', label='var2')
    chart.plot(7, color='green', label='var3')
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['data']['columns'], [['var1', 5], ['var2', 10], ['var3', 7]])
    assert_equals(res['data']['type'], 'pie')
    assert_equals(res['data']['colors']['var2'], '#FFFFFF')


def test_donut_chart():
    chart = c3.DonutChart()
    chart.plot([4, 5, 6], label='var4')
    chart.plot([7, 8, 9], label='var5')
    chart.donut_title('hello')
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['data']['columns'][0], ['var4', 4, 5, 6])
    assert_equals(res['data']['type'], 'donut')
    assert_equals(res['donut']['title'], 'hello')
