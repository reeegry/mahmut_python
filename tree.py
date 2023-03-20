import turtle
import random

turtle.colormode(255)

def rand_angle(a):
    return random.randint(1, a)

def tree(branchLen,t):
    if branchLen > 5:
        size = branchLen // 10
        t.pensize(size)
        angle = rand_angle(45)
        t.forward(branchLen)
        t.right(angle)
        len_branch = random.triangular(0.7, 0.9)
        tree(branchLen * len_branch, t)
        t.left(angle * 2)
        tree(branchLen * len_branch,t)
        chance_leaf = random.randrange(1, 100)
        if branchLen <= tree_hight // 10 and chance_leaf <= 50:
            color_1 = random.randrange(55, 90)
            color_2 = random.randrange(100, 210)
            color_3 = random.randrange(50, 68)
            trea_leaf_size = random.randrange(3, 5)
            t.color(color_1, color_2, color_3)
            t.pensize(5)
            t.right(30)
            t.forward(trea_leaf_size)
            t.left(60)
            t.forward(trea_leaf_size)
            t.left(120)
            t.forward(trea_leaf_size)
            t.left(60)
            t.forward(trea_leaf_size)
            t.left(150)
            t.color(101, 67, 33)
            if random.randrange(0, 2):
                color_1_a = random.randrange(200, 230)
                color_2_a = random.randrange(0, 20)
                color_3_a = random.randrange(0, 20)
                t.pencolor(color_1_a, color_2_a, color_3_a)
                t.pensize(4)
                t.circle(random.randrange(1, 3))
            t.color(101, 67, 33)
        t.right(angle)
        t.pensize(size)
        t.backward(branchLen)

def main():
    global tree_hight
    tree_hight = int(input())
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color(101, 67, 33)
    tree(75,t)
    myWin.exitonclick()

main()
