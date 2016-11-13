import json

from nose.tools import assert_equals

import c3pyo as c3

men_height = [175, 176, 172, 172, 177]
women_height = [156, 162, 158, 160, 164]
countries = ('UK', 'USA', 'Japan', 'China', 'Russia')


def test_bar_chart():
    chart = c3.BarChart()
    chart.plot(men_height, label='Men_Heights')
    chart.plot(women_height, label='Women_Heights')
    chart.set_xticklabels(countries)
    chart.bar_width(0.5)
    chart.ylabel('Height (cm)')
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['axis']['x']['categories'], list(countries))
    assert_equals(res['axis']['x']['type'], 'category')
    assert_equals(res['axis']['y']['label'], 'Height (cm)')
    assert_equals(res['bar']['width']['ratio'], 0.5)
    assert_equals(res['grid']['y']['lines'][0]['value'], 0)


def test_stacked_bar_chart():
    chart = c3.BarChart()
    chart.plot(men_height, label='Men_Heights')
    chart.plot(women_height, label='Women_Heights')
    chart.set_xticklabels(countries)
    chart.stacked(True)
    chart.ylabel('Height (cm)')
    res = chart.json()
    res = json.loads(res)
    assert_equals(res['data']['groups'], [['Men_Heights', 'Women_Heights']])
