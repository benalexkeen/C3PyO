from nose.tools import assert_raises, assert_in

from c3pyo import LineChart


def test_validation():
    chart = LineChart()
    failing_test_cases = [
        (TypeError, chart.area, 'String'),
        (TypeError, chart.area, 4),
        (TypeError, chart.legend, 'String'),
        (TypeError, chart.legend, {'key': 'value'}),
        (TypeError, chart.legend, ['my', 'test', 'list']),
        (TypeError, chart.zoom, 'True'),
        (TypeError, chart.zoom, 'False'),
        (TypeError, chart.subchart, ('my', 'test', 'tuple')),
        (TypeError, chart.subchart, [True, False]),
        (TypeError, chart.height, True),
        (TypeError, chart.height, '243'),
        (TypeError, chart.width, False),
        (TypeError, chart.width, 'String'),
        (ValueError, chart.legend_position, 'left'),
        (ValueError, chart.legend_position, 'top'),
        (ValueError, chart.legend_position, True),
        (TypeError, chart.tooltip, 'String')
    ]

    passing_test_cases = [
        (chart.area, True),
        (chart.area, False),
        (chart.legend, True),
        (chart.legend, False),
        (chart.zoom, True),
        (chart.zoom, False),
        (chart.subchart, True),
        (chart.subchart, False),
        (chart.height, 0),
        (chart.height, 500),
        (chart.height, 500.46),
        (chart.width, 0),
        (chart.width, 3000),
        (chart.width, 205.3),
        (chart.legend_position, 'bottom'),
        (chart.legend_position, 'inset'),
        (chart.legend_position, 'right'),
        (chart.tooltip, True),
        (chart.tooltip, False),
    ]

    def check_failing_test_case(error, _func, _arg):
        assert_raises(error, _func, _arg)

    def check_passing_test_case(_func, _arg):
        _func(_arg)

    for error, _func, _arg in failing_test_cases:
        yield check_failing_test_case, error, _func, _arg

    for _func, _arg in passing_test_cases:
        yield check_passing_test_case, _func, _arg


def test_add_color():
    chart = LineChart()
    passing_test_cases = [
        ('r', 'color1', '#FF0000'),
        ('c', 'color2', '#00FFFF'),
        ('yellow', 'color3', '#FFFF00'),
        ('PINK', 'color4', '#FFC0CB'),
        ('InDiGo', 'color5', '#4B0082'),
        ('#FA8072', 'color6', '#FA8072'),
        ('#ffaab2', 'color7', '#ffaab2'),
        ('#2ae', 'color8', '#2ae'),
        ('#abcdef', 'color9', '#abcdef'),
        ('876553', 'color10', '#876553'),
        ('a3f', 'color11', '#a3f'),
    ]

    def check_passing_test_case(color, y_label, hex_code):
        chart.add_color(color, y_label)
        assert_in(hex_code, chart._colors.values())

    failing_test_cases = [
        '#a', '#ab', '#aeg', '#12', '12', '1894', '#9802', '#aef31',
        '#abcdef3', '#0123456', 'abcdef3', '327yes', '#807yfe', 'd',
        'skybluepink'
    ]

    def check_failing_test_case(color):
        assert_raises(ValueError, chart.add_color, color, 'test_y_label')

    for color, y_label, hex_code in passing_test_cases:
        yield check_passing_test_case, color, y_label, hex_code

    for color in failing_test_cases:
        yield check_failing_test_case, color


def test_y_range():
    chart = LineChart()
    chart.y_range(50, 504)
    chart.y_range(50.0313, 504.2130)
    chart.y_range(0, 0)
    chart.y_range(None, None)
    chart.y_range(None, 500)
    chart.y_range(300)
    chart.y_range(250.32, None)
    assert_raises(TypeError, chart.y_range, True, False)
    assert_raises(TypeError, chart.y_range, '100', '300')
    assert_raises(TypeError, chart.y_range, None, '300')
    assert_raises(TypeError, chart.y_range, None, True)
    assert_raises(TypeError, chart.y_range, 'String', 102)


def test_gridlines():
    chart = LineChart()
    chart.gridlines(True, False)
    chart.gridlines(True, True)
    chart.gridlines(False, False)
    chart.gridlines(None, None)
    assert_raises(TypeError, chart.gridlines, True, 100)
    assert_raises(TypeError, chart.gridlines, 10, 100)
    assert_raises(TypeError, chart.gridlines, 'String', True)
    assert_raises(TypeError, chart.gridlines, None, 12.31)
