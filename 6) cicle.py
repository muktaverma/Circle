from turtle import *
import turtle
color('blue', 'green')
bgcolor('black')
speed (10)
begin_fill()
while True:
    forward(200)
    left(155)
    if abs(pos()) < 1:
        break
end_fill()
done ()