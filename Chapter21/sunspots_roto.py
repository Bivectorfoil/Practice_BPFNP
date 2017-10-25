# -*- coding:utf-8 -*-

from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF


data = [
    # YR MO   PREDICTED    HIGH    LOW
    (2017, 9, 17.4, 23.4, 1.4),
    (2017, 0, 17.5, 24.5, 0.5),
    (2017, 1, 17.5, 24.5, 0.5),
    (2017, 2, 17.7, 25.7, 9.7),
    (2018, 1, 17.9, 26.9, 8.9),
    (2018, 2, 17.6, 26.6, 8.6),
    (2018, 3, 16.7, 26.7, 6.7),
    (2018, 4, 15.6, 25.6, 5.6),
]

drawing = Drawing(200, 150)

pred = [row[2] + 50 for row in data]
high = [row[3] + 50 for row in data]
low = [row[4] + 50 for row in data]
times = [200 * ((row[0] + row[1] / 12.0) - 2017) - 110 for row in data]


drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
