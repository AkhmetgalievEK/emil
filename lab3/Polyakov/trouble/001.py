import graph as g

g.windowSize(300, 400)
g.canvasSize(300, 400)


x0 = 20
y0 = 20
x1 = x0 + 256
y1 = y0 + 360
a = 0.26
x2 = x1
y2 = y0 + a * (y1 - y0)

b = 0.87
xc = x0 + b * (x1 - x0)
c = 0.1
yc = y0 + c * (y1 - y0)
d = 0.1
r = d * (x1 - x0)


g.penColor("#045FB4")
g.brushColor("#045FB4")
g.rectangle(x0, y0, x1, y1)

g.penColor("#81F7F3")
g.brushColor("#81F7F3")
g.rectangle(x0, y0, x2, y2)

g.penColor("yellow")
g.brushColor("yellow")
g.circle(xc, yc, r)









g.run()


