#note:y down x left
# C:/Users/minh/Anaconda3/python.exe c:/Users/minh/Desktop/snek/snek.py
#imports
#import collections
import time
import copy
import msvcrt
import itertools
import curses
import random
stdscr = curses.initscr()

#set variables

map=[
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],]
blank=[
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],
    ["-","-","-","-","-","-","-","-","-","-"],]
snake=[[2,3],[2,2],[2,1]]
body_count=len(snake)-1
direction='right'
fruit=[0,0]
state=0
#functions

def control(direction):
    if msvcrt.kbhit():
        move=str(msvcrt.getch().decode("utf-8"))
        if move=='d' and direction != 'left':
            direction='right'
        elif move=='a' and direction != 'right':
            direction='left'
        elif move=='w' and direction != 'down':
            direction='up'
        elif move=='s' and direction != 'up':
            direction='down'
    return direction

def movement(direction):
    tmp_snake=copy.deepcopy(snake)
    if direction=='right':
        snake[0][1]+=1
    elif direction=='left':
        snake[0][1]-=1
    elif direction=='up': 
        snake[0][0]-=1
    elif direction=='down':
        snake[0][0]+=1
    for i in range(body_count):
        snake[i+1]=tmp_snake[i]
	#l=' '.join([str(elem) for elem in snake]) 
    print(snake)


def draw():
    map[fruit[0]][fruit[1]]='F'
    map[snake[0][0]][snake[0][1]]='H'
    for i in range(body_count):
        map[snake[i+1][0]][snake[i+1][1]]='B'
    for i in range(len(map)):
        li=' '.join([str(elem) for elem in map[i]]) 
        stdscr.addstr(i,0,li)
        
def spawnFruit():
    coord=[]
    for i in range(10):
        for n in range (10):
            tmp_coord=[i,n]
            coord.append(tmp_coord)
    for i in range(len(snake)):
        if snake[i] in coord:
            del coord[coord.index(snake[i])]
    randF=random.choice(coord)
    fruit[0]=randF[0]
    fruit[1]=randF[1]
def check():
    new_snake = []
    for elem in snake:
        if elem not in new_snake:
            new_snake.append(elem)
    if snake!=new_snake:
        print('colide')
        return 1
    else:
        return 0



#execute
spawnFruit()
while state==0:
    stdscr.refresh()
    direction=control(direction)
    if direction=='up' and snake[0][0]==fruit[0]+1 and snake[0][1]==fruit[1] or direction=='down' and snake[0][0]==fruit[0]-1 and snake[0][1]==fruit[1] or direction=='left' and snake[0][1]==fruit[1]+1 and snake[0][0]==fruit[0] or direction=='right' and snake[0][1]==fruit[1]-1 and snake[0][0]==fruit[0]:
        snake.insert(0,fruit)
        fruit=[0,0]
        body_count+=1
        spawnFruit()
    else:
        movement(direction)
    state=check()
    if snake[0][0]>=0 and snake[0][0]<10 and snake[0][1]>=0 and snake[0][1]<10 and state==0:
        draw()
        map=copy.deepcopy(blank)
        time.sleep(0.5)
    else:
        state=1
else:
    curses.endwin()
    print('you lose')













