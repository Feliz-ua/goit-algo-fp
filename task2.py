import turtle

def setup_turtle():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    return window, t

def draw_tree(t, length, angle, depth):
    if depth == 0:
        return
    t.forward(length)
    t.left(angle)
    draw_tree(t, length * 0.6, angle, depth - 1)
    t.right(2 * angle)
    draw_tree(t, length * 0.6, angle, depth - 1)
    t.left(angle)
    t.backward(length)

def main():
    depth = int(input("Введіть рівень рекурсії: "))
    window, t = setup_turtle()
    draw_tree(t, 100, 60, depth)
    window.exitonclick()

main()
     
