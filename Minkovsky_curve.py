import turtle as t
def draw(l,n):
    if n == 0:
        t.forward(l)
        return
    x = l/4
    draw(x, n - 1)
    t.left(90)
    draw(x, n - 1)
    t.right(90)
    draw(x, n - 1)
    t.right(90)
    draw(x, n - 1)
    draw(x, n - 1)
    t.left(90)
    draw(x, n - 1)
    t.left(90)
    draw(x, n - 1)
    t.right(90)
    draw(x, n - 1)
draw(300,3)
input()