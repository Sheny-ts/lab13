import turtle as t
def draw(l,n):
    if n == 0:
        t.forward(l)
        return
    t.left(45)
    x = l/n
    draw(x, n - 1)
    t.right(90)
    draw(x, n - 1)
    t.right(45)
    t.left(90)


draw(5000,6)
input()