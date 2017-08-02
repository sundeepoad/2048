# adding problem, logical tiles add,

import random
import pyglet
from pyglet.window import Window, mouse, gl, key
import copy
from copy import deepcopy

#Global win and lose defined
lose = False
win = False

mygame = Window(700, 450,
              resizable=False,  # Make sure it is not resizable
              caption="2048",  # Caption of window
              config=pyglet.gl.Config(double_buffer=True),  # Avoids flickers
              vsync=False  # For flicker-free animation
              )


# Background image use for game
bgimage = pyglet.resource.image('resources/dg.jpg')
# Get an instance of current platform
platform = pyglet.window.get_platform()
# Get an instance of current display
display = platform.get_default_display()
# Get an instance of current screen
screen = display.get_default_screen()


mygame.set_location(screen.width // 2 - 200, screen.height // 2 - 150)
# image for icon of game window
myicon = pyglet.image.load('resources/2048.png')
# Setting icon for game window
mygame.set_icon(myicon)  # setting icon

#Importing images in the program that will be used in the game

image0 = pyglet.resource.image("resources/0.png")
image2 = pyglet.resource.image("resources/2.png")
image4 = pyglet.resource.image("resources/4.png")
image8 = pyglet.resource.image("resources/8.png")
image16 = pyglet.resource.image("resources/16.png")
image32 = pyglet.resource.image("resources/32.png")
image64 = pyglet.resource.image("resources/64.png")
image128 = pyglet.resource.image("resources/128.png")
image256 = pyglet.resource.image("resources/256.png")
image512 = pyglet.resource.image("resources/512.png")
image1024 = pyglet.resource.image("resources/1024.png")
image2048 = pyglet.resource.image("resources/2048.png")


image = pyglet.resource.image("resources/direction3.png")       #Direction image
csprite = pyglet.sprite.Sprite(image,500,100)
csprite.visible = True

winlabel = pyglet.text.Label("",
                             font_name='Times New Roman',
                             font_size = 50,
                             x = 250, y = 225,
                             anchor_x='center', anchor_y='center',color=(0,0,0,255))

loselabel = pyglet.text.Label("",
                             font_name='Times New Roman',
                             font_size = 50,
                             x = 250, y = 225,
                             anchor_x='center', anchor_y='center',color=(0,0,255,255))

#Global Window
main_board= [[0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]
for i in range (2):               #Generating initial random number in 2 positions
    atmp = 0
    first_pos = [0,1,2,3]
    first_row = random.choice(first_pos)
    first_col = random.choice(first_pos)
    main_board[first_row][first_col] = 2

#Generating random number and Winning Situation
def rand_num(main_board):
    lst=[]      #Blank list to to store adresses of elements that contain zero
    for i in range(0,4):
        for j in range(0,4):
            if main_board[i][j]== 0:
                lst.append([i,j])            #Adding elements in a list that has zero number

    i,j= lst[random.randint(0,len(lst)-1)]         #Random function that runs in the times how many elements are present in the list
    u=(random.randint(0,9))
    if((u>7)):
        main_board[i][j]=4
    else:
        main_board[i][j]=2
    print("RAndom number board")
    p_board(main_board)
    return main_board

#A function that uses 2D Array and draws a Matrix to play game
def p_board(main_board):
    for list in main_board:
        for element in list:
            print(element, end = "  ")
        print("")

p_board(main_board)

##Function to control UPward movement
def up(main_board):
    i = 0
    for j in range (0,4):
        if main_board[i][j]!=0 or main_board[i+1][j]!=0 or main_board[i+2][j]!=0 or main_board[i+3][j]!=0:
            if main_board[i][j] == 0:
                while main_board[i][j] == 0:
                    main_board[i][j] =  main_board[i+1][j]
                    main_board[i+1][j] = main_board[i+2][j]
                    main_board[i+2][j] = main_board[i+3][j]
                    main_board[i+3][j] = 0
                    if main_board[i+1][j]==0 and main_board[i+2][j]==0 and main_board[i+3][j]==0:
                        break

            if main_board[i+1][j] ==0:
                while main_board[i+1][j]==0:
                    main_board[i+1][j] = main_board[i+2][j]
                    main_board[i+2][j] = main_board[i+3][j]
                    main_board[i+3][j] = 0
                    if main_board[i + 2][j]== 0 and main_board[i + 3][j]== 0:
                        break

            if main_board[i+2][j] ==0:
                while main_board[i+2][j]==0:
                    main_board[i+2][j] = main_board[i+3][j]
                    main_board[i+3][j] = 0
                    if main_board[i + 3][j]==0:
                        break
    print("UP",main_board)
#Function to control Left movement

def left(main_board):
    j = 0
    for i in range (0,4):
        if main_board[i][j]!=0 or main_board[i][j+1]!=0 or main_board[i][j+2]!=0 or main_board[i][j+3]!=0:
            if main_board[i][j]==0:
                while main_board[i][j]==0:
                    main_board[i][j] =  main_board[i][j+1]
                    main_board[i][j+1] = main_board[i][j+2]
                    main_board[i][j+2] = main_board[i][j+3]
                    main_board[i][j+3] = 0
                    if main_board[i][j+1]==0 and main_board[i][j+2]==0 and main_board[i][j+3]==0:
                        break

            if main_board[i][j+1] ==0:
                while main_board[i][j+1]==0:
                    main_board[i][j+1] = main_board[i][j+2]
                    main_board[i][j+2] = main_board[i][j+3]
                    main_board[i][j+3] = 0
                    if main_board[i][j+2]==0 and main_board[i][j+3]==0:
                        break

            if main_board[i][j+2] ==0:
                while main_board[i][j+2]==0:
                    main_board[i][j+2] = main_board[i][j+3]
                    main_board[i][j+3] = 0
                    if main_board[i][j+3]==0:
                        break
    
    return main_board

#Function to control Downward movement

def down(main_board):
    i = 0
    for j in range(0, 4):
        if main_board[i][j] != 0 or main_board[i + 1][j] != 0 or main_board[i + 2][j] != 0 or main_board[i + 3][j] != 0:
            if main_board[i+3][j] == 0:
                while main_board[i+3][j] == 0:
                    main_board[i+3][j] = main_board[i + 2][j]
                    main_board[i + 2][j] = main_board[i + 1][j]
                    main_board[i + 1][j] = main_board[i][j]
                    main_board[i][j] = 0
                    if main_board[i+3][j]==0 and main_board[i+2][j]==0 and main_board[i+1][j]==0:
                        break

            if main_board[i + 2][j] == 0:
                while main_board[i + 2][j] == 0:
                    main_board[i + 2][j] = main_board[i + 1][j]
                    main_board[i + 1][j] = main_board[i][j]
                    main_board[i][j] = 0
                    if main_board[i+2][j]==0 and main_board[i+1][j]==0:
                        break

            if main_board[i + 1][j] == 0:
                while main_board[i + 1][j] == 0:
                    main_board[i + 1][j] = main_board[i][j]
                    main_board[i][j] = 0
                    if main_board[i+1][j]==0:
                        break
    return main_board

#Function to control Right movement
def right(main_board):
    j=0
    for i in range(0,4):
        if main_board[i][j]!=0 or main_board[i][j+1]!=0 or main_board[i][j+2]!=0 or main_board[i][j+3]!=0:
            if main_board[i][j+3]==0:
                while main_board[i][j+3]==0:
                    main_board[i][j+3] =  main_board[i][j+2]
                    main_board[i][j+2] = main_board[i][j+1]
                    main_board[i][j+1] = main_board[i][j]
                    main_board[i][j] = 0
                    if main_board[i][j+3]==0 and main_board[i][j+2]==0 and main_board[i][j+1]==0:
                        break

            if main_board[i][j+2] ==0:
                while main_board[i][j+2]==0:
                    main_board[i][j+2] = main_board[i][j+1]
                    main_board[i][j+1] = main_board[i][j]
                    main_board[i][j] = 0
                    if main_board[i][j+2]==0 and main_board[i][j+1]==0:
                        break

            if main_board[i][j+1] ==0:
                while main_board[i][j+1]==0:
                    main_board[i][j+1] = main_board[i][j]
                    main_board[i][j] = 0
                    if main_board[i][j+1]==0:
                        break
    return main_board

#Additon functions

def up_add(main_board):
    global win
    global lose
    i=0
    for j in range(0,4):
        if main_board[i][j] == main_board[i+1][j]:
            main_board[i][j] = main_board[i][j] + main_board[i+1][j]
            main_board[i+1][j] = main_board[i+2][j]
            main_board[i + 2][j] = main_board[i + 3][j]
            main_board[i + 3][j] = 0

        if main_board[i+1][j] == main_board[i+2][j]:
            main_board[i+1][j] = main_board[i+1][j] + main_board[i+2][j]
            main_board[i+2][j] = main_board[i+3][j]
            main_board[i+3][j] = 0

        if main_board[i+2][j] == main_board[i+3][j]:
            main_board[i+2][j] = main_board[i+2][j] + main_board[i+3][j]
            main_board[i+3][j] = 0

    win = winning(main_board)
    print("UpAdd",main_board)

def down_add(main_board):
    global win
    global lose
    i=0
    for j in range(0,4):
        if main_board[i+3][j] == main_board[i+2][j]:
            main_board[i+3][j] = main_board[i+3][j] + main_board[i+2][j]
            main_board[i+2][j] = main_board[i+1][j]
            main_board[i+1][j] = 0

        if main_board[i+2][j] == main_board[i+1][j]:
            main_board[i+2][j] = main_board[i+2][j] + main_board[i+1][j]
            main_board[i+1][j] = 0

        if main_board[i+1][j] == main_board[i][j]:
            main_board[i+1][j] = main_board[i+1][j] + main_board[i][j]
            main_board[i][j] = 0
    p_board(main_board)
    win = winning(main_board)
    return main_board

def left_add(main_board):
    global win
    global lose
    j=0
    for i in range(0,4):
        if main_board[i][j] == main_board[i][j+1]:
            main_board[i][j] = main_board[i][j] + main_board[i][j+1]
            main_board[i][j+1] = main_board[i][j+2]
            main_board[i][j+2] = main_board[i][j+3]
            main_board[i][j+3] = 0


        if main_board[i][j+1] == main_board[i][j+2]:
            main_board[i][j+2] = main_board[i][j+1] + main_board[i][j+2]
            main_board[i][j + 2] = main_board[i][j + 3]
            main_board[i][j + 3] = 0

        if main_board[i][j+2] == main_board[i][j+3]:
            main_board[i][j + 2] == main_board[i][j + 2] + main_board[i][j + 3]
            main_board[i][j + 3] = 0
    p_board(main_board)
    win = winning(main_board)
    return main_board

def right_add(main_board):
    global win
    global lose

    j=0
    for i in range(0,4):
        if main_board[i][j+3] == main_board[i][j+2]:
            main_board[i][j+3] = main_board[i][j+3] + main_board[i][j+2]
            main_board[i][j+2] = main_board[i][j+1]
            main_board[i][j+1] = main_board[i][j]
            main_board[i][j] = 0

        if main_board[i][j+2] == main_board[i][j+1]:
            main_board[i][j+2] = main_board[i][j+1] + main_board[i][j+2]
            main_board[i][j + 1] = main_board[i][j]
            main_board[i][j] = 0

        if main_board[i][j+1] == main_board[i][j]:
            main_board[i][j + 1] == main_board[i][j + 1] + main_board[i][j]
            main_board[i][j] = 0

    p_board(main_board)
    win = winning(main_board)
    return main_board

#Main function of game in which game will work and other functions will be called
'''def main():

    while True:
        direc=input("Select A Direction: \n l : left \n r : right \n u : up \n d : down  \n q : quit \nChoice:  ")

        if direc == 'q':
            break

        elif direc == "u":
            up(main_board)
            up_add(main_board)
            rand_num(main_board)
            p_board(main_board)

        elif direc == "d":
            down(main_board)
            down_add(main_board)
            rand_num(main_board)
            p_board(main_board)

        elif direc == "l":
            left(main_board)
            left_add(main_board)
            rand_num(main_board)
            p_board(main_board)

        elif direc == "r":
            right(main_board)
            right_add(main_board)
            rand_num(main_board)
            p_board(main_board)

        else:
            print("Invalid Move")

        # if main_board != 0:
        #     print("Game Over")
        #rand_num(main_board)

#main()'''
def check_board(main_board):             ##Checks for losing condition
    c = 0
    for i in range(0,4):
        for j in range (0,4):
            if main_board[i][j] == 0:
                c = c + 1
    if c==0:
        kopy1 = deepcopy(main_board)
        kopy2 = deepcopy(main_board)
        kopy3 = deepcopy(main_board)
        kopy4 = deepcopy(main_board)
        kopy5 = deepcopy(main_board)
        kopy6 = deepcopy(main_board)
        kopy7 = deepcopy(main_board)
        kopy8 = deepcopy(main_board)


        kopy1 = up(kopy1)
        kopy2= up_add(kopy2)
        kopy3 = down(kopy3)
        kopy4 = down_add(kopy4)
        kopy5 = left(kopy5)
        kopy6 = left_add(kopy6)
        kopy7 = right(kopy7)
        kopy8 = right_add(kopy8)

        if main_board == kopy1 and main_board == kopy2 and main_board == kopy3 and main_board == kopy4 and main_board == kopy5 and main_board == kopy6 and main_board == kopy7 and main_board == kopy8:
            print("GAME OVER")
            loselabel.text= 'GAME OVER'
            return False
        else:
            return True

#Function for winning condition

def winning(main_board):
    for i in range (3,-1,-1):
        for j in range (0,4):
            if main_board[i][j] == 2048:
                print ("You Won")
                winlabel.text = 'YOU WON'

                return True

#Sacing index number in a blank list and then loading tiles on that index
def load_tiles(main_board):
    blank=[[],[],[],[]]
    y = 10
    for i in range (3,-1,-1):
        x = 10
        for j in range(0,4):
            #print(x,y)
            dash = main_board[i][j]
            eval('blank[i].append(pyglet.sprite.Sprite(image' + str(dash) + ',x,y))')
            exec('blank[i][j]' + '.visible = True')
            x = x + 110
        y = y + 110


    for a in range(0,4):         #Drawing the images that are saved in list
        for b in range(0,4):
            blank[a][b].draw()
        #print()

#KEYBOARD and MOUSE controls in a function
def run(main_board):
    @mygame.event
    def on_key_press(symbol,modifiers):
        global win
        global lose
        print(symbol)
        win = winning(main_board)
        if win != True:

            if symbol == key.UP:
                a = deepcopy(main_board)
                print("UP")
                up(main_board)
                up_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)
                load_tiles(main_board)

            elif symbol == key.DOWN:
                print("DOWN")
                a = deepcopy(main_board)
                down(main_board)
                down_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)
                load_tiles(main_board)

            elif symbol == key.LEFT:
                print("LEFT")
                a = deepcopy(main_board)
                left(main_board)
                left_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)
                load_tiles(main_board)


            elif symbol == key.RIGHT:
                print("RIGHT")
                a = deepcopy(main_board)
                right(main_board)
                right_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)
                load_tiles(main_board)


        lose = check_board(main_board)


#Mouse movement
    @mygame.event
    def on_mouse_press(x, y, button, modifiers):
        win = winning(main_board)
        if win != True:

            if button == mouse.LEFT:
                print(x,y)
            if (x>506 and x<569) and (y > 180 and y<244):
                print("UP arrow clicked")
                a = deepcopy(main_board)
                up(main_board)
                up_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)

                load_tiles(main_board)

            elif (x > 580 and x < 642) and (y > 181 and y < 243):
                print("Right key")
                a = deepcopy(main_board)
                right(main_board)
                right_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)
                load_tiles(main_board)


            elif (x > 506 and x < 569) and (y > 109 and y < 171):
                print("Down")
                a = deepcopy(main_board)
                down(main_board)
                down_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)
                load_tiles(main_board)

            elif (x > 580 and x < 642) and (y > 109 and y < 171):
                print("Left")
                a = deepcopy(main_board)
                left(main_board)
                left_add(main_board)
                if a != main_board and win != True:
                    rand_num(main_board)
                load_tiles(main_board)
run(main_board)


@mygame.event
def on_draw():
    mygame.clear()
    bgimage.blit(0, 0)
    load_tiles(main_board)
    csprite.draw()
    if win == True:
        winlabel.draw()
    if lose == False:
        loselabel.draw()

pyglet.app.run()