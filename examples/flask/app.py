import os
import datetime

import c3pyo as c3
from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)


def get_line_chart_json():
    # data
    x = [1, 2, 3, 4, 5, 6, 7]
    y1 = [150, 450, 200, 100, 300, 0, 325]
    y2 = [230, 220, 150, 400, 105, 50, 302]

    # chart
    chart = c3.LineChart()
    chart.plot(x, y1, label='Series 1')
    chart.plot(x, y2, label='Series 2')
    chart.bind_to('line_chart_div')

    return chart.json()


@app.route("/", methods=['GET', 'POST'])
def index():
    chart_json = get_line_chart_json()
    return render_template("index.html", chart_json=chart_json)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)