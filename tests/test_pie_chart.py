import json

from nose.tools import assert_equals

import c3pyo as c3


def test_pie_chart():
    chart = c3.PieChart()
    chart.plot(5, color='blue', label='Var1')
    chart.plot(10, color='white', label='Var2')
    chart.plot(7, color='green', label='Var3')
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['data']['columns'], [['Var1', 5], ['Var2', 10], ['Var3', 7]])
    assert_equals(res['data']['type'], 'pie')
    assert_equals(res['data']['colors']['Var2'], '#FFFFFF')
