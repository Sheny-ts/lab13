import turtle as t

def draw(l, n):
    if n==0:
        t.forward(l)
        return
    x = l / 3
    draw(x, n-1)
    t.left(60)
    draw(x, n-1)
    t.right(120)
    draw(x, n-1)
    t.left(60)
    draw(x, n-1)

draw(400,4)
input()
