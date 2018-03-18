# greet = "Hello " + input("What is your name? ")
# print(greet)
import matplotlib.pyplot as plot

def f(x):
    xs = list(range(-3, 3))
    ys = [x + 1]
    for x in xs:
        ys.append(f(x))

plot.plot(xs, ys)
plot.show()