# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 17:22:55 2019

@author: Manas Sharma
"""
import time
import turtle
import random 
def changeup():
    if eyes.direction!="down":
        eyes.direction="up"
def changedown():
    if eyes.direction!="up":
        eyes.direction="down"
def changeleft():
    if eyes.direction!="right":
        eyes.direction="left"
def changeright():
    if eyes.direction!="left":
        eyes.direction="right"    
def init():
    eyes.speed(0) #0 lag 
    eyes.shape("square")
    eyes.color("red")
    eyes.penup()#dont draw useless things
    eyes.goto(0,0)
    eyes.direction = "stop"
# initialising done 
def move():
    if eyes.direction=="up":
        eyes.sety(eyes.ycor()+20)
    elif eyes.direction=="down":
        eyes.sety(eyes.ycor()-20)
    elif eyes.direction=="left":
        eyes.setx(eyes.xcor()-20)
    elif eyes.direction=="right":
        eyes.setx(eyes.xcor()+20)
delay = 0.1 
score = 0     
display = turtle.Screen()
display.bgcolor("BLACK")
display.setup(width=900,height=600)
display.tracer(0) 
"""Stops the animation"""
eyes = turtle.Turtle()
init()
body = []
draw = turtle.Turtle()
draw.speed(0)
draw.shape("circle")
draw.color("yellow")
draw.penup()
draw.hideturtle()
draw.goto(0,250)
draw.write("Score = {}".format(score), align="center", font=("Courier", 20, "normal"))
food = turtle.Turtle()
food.speed(0) #0 lag 
food.shape("circle")
food.color("blue")
food.penup()#dont draw useless things
foodx = random.randint(-440,440)
foody = random.randint(-290,290)
food.goto(foodx,foody)
display.listen()
display.onkeypress(changeup,"w")
#display.onkeypress(changeup,"up")
display.onkeypress(changedown,"s")
#display.onkeypress(changedown,"down")
display.onkeypress(changeleft,"a")
#display.onkeypress(changeleft,"left")
#display.onkeypress(changeright,"right")
display.onkeypress(changeright,"d")
while 1:
    display.update()
    if abs(eyes.xcor())>440 or abs(eyes.ycor())>290:
        time.sleep(2)
        eyes.direction="stop"
        score=0
        for i in body:
            i.goto(1000,1000)
        eyes.goto(0,0)    
        body=[]
    if eyes.distance(food)<20:
        score+=1
        draw.clear()
        draw.write("Score = {}".format(score), align="center", font=("Courier", 20, "normal"))
        foodx = random.randint(-440,440)
        foody = random.randint(-290,290)
        food.goto(foodx,foody)
        organ = turtle.Turtle()
        organ.speed(0) #0 lag 
        organ.shape("square")
        organ.color("green")
        organ.penup()#dont draw useless things
        body.append(organ)
    for i in range(len(body)-1,0,-1):
        body[i].goto(body[i-1].xcor(),body[i-1].ycor())
    if len(body)>0:
        body[0].goto(eyes.xcor(),eyes.ycor())    
    move()
    for i in body:
        if i.distance(eyes)<20:
            score=0
            time.sleep(2)
            eyes.direction="stop"
            for i in body:
                i.goto(1000,1000)
            eyes.goto(0,0)    
            body=[]    
    time.sleep(delay)
display.mainloop()