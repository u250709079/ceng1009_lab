# def sumTo(n):
# total = n * (n + 1) / 2
# return total
#
# print(sumTo(10))
#
# n = int(input("Please enter a number: "))
# print("Sum is",sumTo(n))


# import turtle
#
# def drawStart(t, n , size):
# angle = 180 - 180 / n
# for i in range(n):
# t.forward(size)
# t.right(angle)
#
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
# drawStart(t, 11,100)
# wn.exitonclick()

# def sumTo(n):
#   total = 0
#   for i in range (1,n+1):
#       total += i
#    return total
# print(sumTo(10))
# n = int(input("Enter a number: "))
# print("Sum is",sumTo(n))


# import turtle
#
# def drawSprite(someturtle, legs, length):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
#
# def fancySquare(t,size):
#     for corner in range(4):
#         drawSprite(t,8,20)
#         t.forward(size)
#         t.left(90)
#
#
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color("yellow")
# t.pensize(2)
#
# fancySquare(t, 100)
# wn.exitonclick()




# def checkSign(x):
#     if x > 0:
#         return "The number is positive"
#     elif x < 0:
#         return "The number is negative"
#     else:
#         return "The number is zero"
#
# numbers = [-7 , 5, 0]
#
# for number in numbers:
#     print(number,"is", (checkSign(number)))
#
# n = int(input("Enter a number: "))
# print(checkSign(n))


# import turtle
# def drawBar(t, heigth, gap):
#     t.penup()
#     t.left(90)
#     t.forward(heigth + gap)
#     t.write(" " + str(heigth))
#     t.backward(heigth + gap)
#     t.right(90)
#     t.pendown()
#
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(heigth)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(heigth)
#     t.left(90)
#     t.end_fill()
#
#
# def barChart(data):
#     maxheight = max(data)
#     num_bars = len(data)
#     border = 10
#
#     gap = ( maxheight - border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("black")
#
#     right = 40 * num_bars + border
#     top = maxheight + 4 * border
#
#
#     wn.setworldcoordinates(-border, -border, right, top)
#     t = turtle.Turtle()
#     t.color("white")
#     t.fillcolor("red")
#     t.pensize(3)
#
#
#     for height in data:
#         drawBar(t, height, gap)
#
#     wn.exitonclick()
#
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)
#
# 
