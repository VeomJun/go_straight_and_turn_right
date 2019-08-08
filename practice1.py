import turtle as a

a.speed(1)
a.shape('classic')
a.begin_fill()
a.width(15)
a.color('green')
a.end_fill()
def go(n):
    while n:
        a.fd(n * 30)
        a.rt(90)
        n = n + 1
        if n > 15:
            break
go(1)
a.done()