'''
╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╭╮╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╭╮╱╱╱╰╮╭╮┃╱╱┃┃╱╱╱╱┃┃╱╭╯╰╮
┃┃╱┃┣━┳╮╱╭┳━━┫┣━━╮╱┃┃┃┣━━┫┃╭┳━━┫╰━╋╮╭╯
┃╰━╯┃╭┫┃╱┃┃╭╮┣┫━━┫╱┃┃┃┃┃━┫┃┣┫╭╮┃╭╮┃┃┃
┃╭━╮┃┃┃╰━╯┃╭╮┃┣━━┃╭╯╰╯┃┃━┫╰┫┃╰╯┃┃┃┃┃╰╮
╰╯╱╰┻╯╰━╮╭┻╯╰╯╰━━╯╰━━━┻━━┻━┻┻━╮┣╯╰╯╰━╯
╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
» A project made by:
  ➥ Aleem      (U1821548E)
  ➥ Arya       (         )
  ➥ Brendon    (U1821638D)
'''

import pygame
import os
from time import sleep

screen = pygame.display.set_mode((900,700))
screen.fill((255,255,255))
pygame.display.set_caption("Arya's Delight")

'''
###########################
──╔╗────╔╗
──║║───╔╝╚╗
╔═╝╠╦══╬╗╔╬╦══╦═╗╔══╦═╦╗─╔╗
║╔╗╠╣╔═╝║║╠╣╔╗║╔╗╣╔╗║╔╣║─║║
║╚╝║║╚═╗║╚╣║╚╝║║║║╔╗║║║╚═╝║
╚══╩╩══╝╚═╩╩══╩╝╚╩╝╚╩╝╚═╗╔╝
──────────────────────╔═╝║
──────────────────────╚══╝
###########################
● Database is stored here
● Updating is relatively simple
● Since we run on pygame, it is a bit hard to update it without text input
● However, it can easily be done on shell/console
'''
# Food court lists sorted by [Highest Cost, Lowest Cost, Cuisine Available, Closing Time, Food Preference Available, Coordinates on NTU Map]
canteen_list = {
    "Food Court 1": [12, 3.5, ["Korean", "Japanese", "Western"], 2100, ["Halal", "Non-Halal/Non-Vegetarian"], (442, 473)],
    "Food Court 2": [10, 3.6, ["Korean", "Chinese", "Malay", ], 2100, ["Halal", "Vegetarian", "Non-Halal/Non-Vegetarian"], (477, 409)],
    "Food Court 4": [10, 3, ["Chinese", "Western"], 2100, ["Non-Halal/Non-Vegetarian"], (358,526)],
    "Food Court 9": [10, 3.5, ["Chinese"], 2100, ["Halal", "Vegetarian", "Non-Halal/Non-Vegetarian"], (582, 288)],
    "Food Court 11": [10, 2.5, ["Chinese", "Indian", "Japanese", "Western"], 2100, ["Halal", "Vegetarian", "Non-Halal/Non-Vegetarian"], (682, 243)],
    "Food Court 13": [9, 2, ["Western", "Korean", "Japanese", "Chinese"], 2100, ["Halal", "Vegetarian", "Non-Halal/Non-Vegetarian"], (445, 176)],
    "Food Court 14": [8, 3, ["Western", "Chinese", "Korean", "Malay"], 2100, ["Halal", "Vegetarian", "Non-Halal/Non-Vegetarian"], (509, 182)],
    "Food Court 16": [10, 3.3, ["Japanese", "Chinese", "Korean", "Indian"], 2100, ["Halal", "Vegetarian", "Non-Halal/Non-Vegetarian"], (405, 221)],
    "Tamarind Food Court": [10, 3, ["Malay", "Chinese", "Korean", "Western"], 2100, ["Halal", "Non-Halal", "Vegetarian","Non-Halal/Non-Vegetarian"], (627, 200)],
    "Pioneer Food Court": [20, 2.3, ["Thai", "Chinese"], 0000, ["Vegetarian", "Non-Halal/Non-Vegetarian"], (497, 561)],
    "North Spine Food Court": [10, 2.5, ["Korean", "Japanese", "Chinese", "Western", "Malay"], 2100, ["Vegetarian", "Non-Halal/Non-Vegetarian"], (275, 293)],
    "North Spine Plaza": [10, 4, ["Western", "Korean"], 2130, ["Vegetarian", "Halal", "Non-Halal/Non-Vegetarian"], (287, 339)],
    "South Spine Food Court": [10, 2, ["Chinese", "Malay", "Korean", "Japanese", "Western"], 2100, ["Vegetarian", "Halal", "Non-Halal/Non-Vegetarian"], (227, 496)],
    "Quad Cafe": [10, 2.4, ["Korean", "Chinese", "Indian", "Malay"], 2100, ["Vegetarian", "Halal", "Non-Halal/Non-Vegetarian"], (224, 351)],
    "Coffee Bean": [20, 4, ["Western"], 2000, ["Vegetarian", "Halal", "Non-Halal/Non-Vegetarian"], (219, 389)],
    "North Hill Food Court": [10, 3.8, ["Chinese", "Malay", "Indian"], 2100, ["Vegetarian", "Halal", "Non-Halal/Non-Vegetarian"], (720,314)]
    }

'''
###########################################
───╔╗───────────╔═╗─────╔╗─────╔╗─╔╗
───║║───────────║╔╝─────║║────╔╝╚╦╝╚╗
╔══╣║╔══╦══╦══╗╔╝╚╦══╦═╗║╚═╦╗╔╬╗╔╩╗╔╬══╦═╗
║╔═╣║║╔╗║══╣══╣╚╗╔╣╔╗║╔╝║╔╗║║║║║║─║║║╔╗║╔╗╗
║╚═╣╚╣╔╗╠══╠══║─║║║╚╝║║─║╚╝║╚╝║║╚╗║╚╣╚╝║║║║
╚══╩═╩╝╚╩══╩══╝─╚╝╚══╩╝─╚══╩══╝╚═╝╚═╩══╩╝╚╝
###########################################
● I had a bit of help from online to workout the button
● A bit of tweaked to the tutorial I learn -Aleem
● ref: https://www.youtube.com/watch?v=4_9twnEduFA
'''
class button():
    def __init__(self, colour, x, y, width, height, text=''):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        if outline:
            #draw a bigger rectangle behind to create a border
            pygame.draw.rect(win, outline, (self.x-2, self.y-2, self.width+4, self.height+4),0)
        #draw the button rectangle
        pygame.draw.rect(win, self.colour, (self.x, self.y, self.width, self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans.ttf', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #pos is the mouse position (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

'''
##################################
─╔═╗─────────╔╗
─║╔╝────────╔╝╚╗
╔╝╚╦╗╔╦═╗╔══╬╗╔╬╦══╦═╗╔══╗
╚╗╔╣║║║╔╗╣╔═╝║║╠╣╔╗║╔╗╣══╣
─║║║╚╝║║║║╚═╗║╚╣║╚╝║║║╠══║
─╚╝╚══╩╝╚╩══╝╚═╩╩══╩╝╚╩══╝
##################################
╔═╗────────╔╗
║═╬═╦╦╗╔═╦╦╬╣
║╔╣╬║╔╝║╬║║║║
╚╝╚═╩╝─╠╗╠═╩╝
───────╚═╝
#################
● Most of the functions here help to draw out the different states of the screen
● The redraw functions help to update the display based on it's states
'''
#3 functions here controls the Surface Text
def text(text,win,x,y):
    font = pygame.font.SysFont('freesansbold.ttf', 50)
    phrase = font.render(text, 1, (0,0,0))
    win.blit(phrase, (x,y))

def instructionText(text,win,x,y):
    font = pygame.font.SysFont('Arial', 20)
    phrase = font.render(text, 1, (0,0,0))
    win.blit(phrase, (x,y))

def header(text,win,x,y):
    font = pygame.font.SysFont('TimesNewRoman', 70)
    phrase = font.render(text, 1, (0,0,0))
    win.blit(phrase, (x,y))

def mouseClick(screen):
    #checks for mouseclick event
    x,y = pygame.mouse.get_pos()
    
    if (x >= 65 and x <=727) and (y >=82 and y <= 618):
        #print(event.button)
        pygame.draw.circle(screen, (255,0,150), (x,y), 15)
        return True,x,y
    else:
        print("Out of bounds!")
        return False,x,y

def skeleExit(win):
    #exit event
    aryadelight = pygame.image.load(os.path.join("aryadelight.png"))
    win.blit(aryadelight,(0,0))
    pygame.display.update()
    xaxis = 100
    for i in range(1,42):
        image = str(i) + ".png"
        skele = pygame.image.load(os.path.join(image))
        win.blit(skele, (250,200))
        text("Exitting...", win, (xaxis+20), 600)
        pygame.display.update()
        sleep(0.09)

def loading(win):
    #loading screen
    x = 0
    while x < 3:
        load0 = pygame.image.load(os.path.join("load0.png"))
        win.blit(load0, (0,0))
        pygame.display.update()
        sleep(0.3)
        load1 = pygame.image.load(os.path.join("load1.png"))
        win.blit(load1, (0,0))
        pygame.display.update()
        sleep(0.3)
        load2 = pygame.image.load(os.path.join("load2.png"))
        win.blit(load2, (0,0))
        pygame.display.update()
        sleep(0.3)
        load3 = pygame.image.load(os.path.join("load3.png"))
        win.blit(load3, (0,0))
        pygame.display.update()
        sleep(0.3)
        x += 1
            
def redrawMap(screen):
    #draw the NTU map
    NTUmap = pygame.image.load(os.path.join("NTUMap.jpg"))
    screen.blit(NTUmap, (0,0))
    for x in range(50,900,50):
        #y grids
        pygame.draw.rect(screen, (255,0,0), (x, 0, 1, 700), 0)
    for y in range(50,700,50):
        #x grids
        pygame.draw.rect(screen, (255,0,0), (0, y, 900, 1), 0)
    text('Please click your current location!',screen,200,100)

def redrawGPSMap(screen, top3, x, y):
    #redraw NTU map but this time with coordinates
    NTUmap = pygame.image.load(os.path.join("NTUMap.jpg"))
    screen.blit(NTUmap, (0,0))
    redGPS = pygame.image.load(os.path.join("redgps.png"))
    screen.blit(redGPS, (x-16,y-32))
    instructionText("You are HERE!", screen, x+4, y-10)
    counter = 1
    for i in top3:
        coor = canteen_list[i][5]
        if counter == 1:
            blueGPS = pygame.image.load(os.path.join("bluegps.png"))
            screen.blit(blueGPS, (coor[0]-12,coor[1]-24))
            instructionText(i, screen, coor[0]-24, coor[1])
            pass
        if counter == 2:
            blackGPS = pygame.image.load(os.path.join("blackgps.png"))
            screen.blit(blackGPS, (coor[0]-12,coor[1]-24))
            instructionText(i, screen, coor[0]-24, coor[1])
            pass
        if counter == 3:
            yellowGPS = pygame.image.load(os.path.join("yellowgps.png"))
            screen.blit(yellowGPS, (coor[0]-12,coor[1]-24))
            instructionText(i, screen, coor[0]-24, coor[1])
            pass
        counter += 1
    restartButton.draw(screen, (0,0,0))

def redrawMainWin(screen):
    #controls what is displayed on the main window
    aryadelight = pygame.image.load(os.path.join("aryadelight.png"))
    screen.blit(aryadelight,(0,0))
    mapButton.draw(screen, (0,0,0))
    instructionText("(Choose your cuisines, preferences and budget here!)",screen,215,320)
    predictButton.draw(screen, (0,0,0))
    instructionText("(Find the nearest canteen!)",screen,132,470)
    exitButton.draw(screen, (0,0,0))
    ice = pygame.image.load(os.path.join("ice.png"))
    screen.blit(ice, (500,670))
    font = pygame.font.SysFont('verdana', 20)
    creator = font.render("Made by Aleem, Arya and Brendon", 1, (0,0,200))
    screen.blit(creator, (535,670))

def redrawCustWin(screen):
    #controls what is displayed on the customisation window
    bp = pygame.image.load(os.path.join("gradient.jpg"))
    screen.blit(bp,(0,0))
    instructionText('Left click again to reset!',screen,300,20)
    text('Please select your food preference: ', screen, 100, 50)
    halalButton.draw(screen, (0,0,0))
    vegButton.draw(screen, (0,0,0))
    nonhalalButton.draw(screen, (0,0,0))
    text('Please select your cuisine type: ', screen, 100, 200)
    koreanButton.draw(screen, (0,0,0))
    malayButton.draw(screen, (0,0,0))
    japanButton.draw(screen, (0,0,0))
    chineseButton.draw(screen, (0,0,0))
    indianButton.draw(screen, (0,0,0))
    westernButton.draw(screen, (0,0,0))
    text('Please select your maximum budget: ', screen, 100, 430)
    button3.draw(screen, (0,0,0))
    button5.draw(screen, (0,0,0))
    button7.draw(screen, (0,0,0))
    button9.draw(screen, (0,0,0))
    nextButton.draw(screen, (0,0,0))

def redrawSearchWin(screen,x,y):
    #gives the top 3 for the prediction tab
    bp = pygame.image.load(os.path.join("aryadelight.png"))
    screen.blit(bp,(0,0))
    mina = pygame.image.load(os.path.join("mina.png"))
    screen.blit(mina, (400,100))
    distList = []
    for i in canteen_list:
        distList.append(i)
    print(distList)
    top3 = nearest_can(distList, x, y)
    print(top3)
    text("Nearest Canteen:",screen,110,400)
    yaxis = 490
    canteenCount = 1
    for k in top3:
        if canteenCount == 1:
            if k == "Food Court 1":
                canteenPic = pygame.image.load(os.path.join("Canteen1.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 2":
                canteenPic = pygame.image.load(os.path.join("Canteen2.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 4":
                canteenPic = pygame.image.load(os.path.join("Canteen4.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 9":
                canteenPic = pygame.image.load(os.path.join("Canteen9.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 11":
                canteenPic = pygame.image.load(os.path.join("Canteen11.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 13":
                canteenPic = pygame.image.load(os.path.join("Canteen13.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 14":
                canteenPic = pygame.image.load(os.path.join("Canteen14.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 16":
                canteenPic = pygame.image.load(os.path.join("Canteen16.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Tamarind Food Court":
                canteenPic = pygame.image.load(os.path.join("Tamarind.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "Pioneer Food Court":
                canteenPic = pygame.image.load(os.path.join("Pioneer.png"))
                screen.blit(canteenPic, (150,200))
            if k == "North Spine Food Court":
                canteenPic = pygame.image.load(os.path.join("NorthSpine.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "North Spine Plaza":
                canteenPic = pygame.image.load(os.path.join("NorthSpinePlaza.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "South Spine Food Court":
                canteenPic = pygame.image.load(os.path.join("SouthSpine.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Quad Cafe":
                canteenPic = pygame.image.load(os.path.join("Quad.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "Coffee Bean":
                canteenPic = pygame.image.load(os.path.join("Coffee.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "North Hill Food Court":
                canteenPic = pygame.image.load(os.path.join("NorthHill.jpg"))
                screen.blit(canteenPic, (150,200))
        text(str(canteenCount), screen, 110, yaxis)
        text(".", screen, 135, yaxis)
        text(k,screen,150,yaxis)
        canteenCount += 1
        yaxis += 70
    return top3

def complicatedSearchWin(screen,top3):
    #displays the top3 for after clicking customisation
    bp = pygame.image.load(os.path.join("aryadelight.png"))
    screen.blit(bp,(0,0))
    mina = pygame.image.load(os.path.join("mina.png"))
    screen.blit(mina, (400,100))
    text("Nearest Canteen:",screen,110,400)
    yaxis = 490
    canteenCount = 1
    for k in top3:
        if canteenCount == 1:
            if k == "Food Court 1":
                canteenPic = pygame.image.load(os.path.join("Canteen1.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 2":
                canteenPic = pygame.image.load(os.path.join("Canteen2.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 4":
                canteenPic = pygame.image.load(os.path.join("Canteen4.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 9":
                canteenPic = pygame.image.load(os.path.join("Canteen9.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 11":
                canteenPic = pygame.image.load(os.path.join("Canteen11.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 13":
                canteenPic = pygame.image.load(os.path.join("Canteen13.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 14":
                canteenPic = pygame.image.load(os.path.join("Canteen14.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Food Court 16":
                canteenPic = pygame.image.load(os.path.join("Canteen16.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Tamarind Food Court":
                canteenPic = pygame.image.load(os.path.join("Tamarind.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "Pioneer Food Court":
                canteenPic = pygame.image.load(os.path.join("Pioneer.png"))
                screen.blit(canteenPic, (150,200))
            if k == "North Spine Food Court":
                canteenPic = pygame.image.load(os.path.join("NorthSpine.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "North Spine Plaza":
                canteenPic = pygame.image.load(os.path.join("NorthSpinePlaza.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "South Spine Food Court":
                canteenPic = pygame.image.load(os.path.join("SouthSpine.png"))
                screen.blit(canteenPic, (150,200))
            if k == "Quad Cafe":
                canteenPic = pygame.image.load(os.path.join("Quad.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "Coffee Bean":
                canteenPic = pygame.image.load(os.path.join("Coffee.jpg"))
                screen.blit(canteenPic, (150,200))
            if k == "North Hill Food Court":
                canteenPic = pygame.image.load(os.path.join("NorthHill.jpg"))
                screen.blit(canteenPic, (150,200))
        text(str(canteenCount), screen, 110, yaxis)
        text(".", screen, 135, yaxis)
        text(k,screen,150,yaxis)
        canteenCount += 1
        yaxis += 70

'''
╔═╗────╔═╗───╔╗╔╗
║═╬═╦╦╗║═╬═╦╦╣╚╬╬═╦╦═╗
║╔╣╬║╔╝╠═║╬║╔╣╔╣║║║║╬║
╚╝╚═╩╝─╚═╩═╩╝╚═╩╩╩═╬╗║
───────────────────╚═╝
###########################
● Functions below control how we do the sorting for the distance
  and the different cuisines
'''
#function by ARYA
#function to compile a list of all the suitable food courts
def final_list(user_budget, user_cuisine, user_preference):
    new_list = []

    #making a list of all food courts that fit in the user's budget
    for i in canteen_list:
        if  user_budget >= canteen_list[i][1]:
            new_list.append(i) 
    
    #making a list of all food courts according to the cuisine constraints
    for c in user_cuisine:
        for i in canteen_list:
            if c in canteen_list[i][2]:
                new_list.append(i)

    #adding to the list all the food courts according to the food preference
    for c in user_preference:
        for i in canteen_list:
            if c in canteen_list[i][4]:
                new_list.append(i)

    #eliminating all the repeated options
    new_list = list(set(new_list))

    #if new_list is empty due to no selection
    if len(new_list) == 0:
        for i in canteen_list:
            new_list.append(i)
    return(new_list)

#function to calulate the distance
def calc_dis(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**1/2

#function to find out the nearest suitable food court
def nearest_can(new_list, x, y):
    top3 = []
    copy_list = new_list.copy()
    while len(top3) != 3:
        j = copy_list[0]
        coor = canteen_list[j][5]
        Min = calc_dis(x, y, coor[0], coor[1])
        food_court = ''
        for k in copy_list:
            #coordinates of the food court
            coor = canteen_list[k][5]
            dist = calc_dis(x, y, coor[0], coor[1])
            if Min >= dist:
                Min = dist
                food_court = k
        index = copy_list.index(food_court)
        copy_list.pop(index)
        top3.append(food_court)
        print(top3)
    return top3

'''
#########################
╔╗─────╔╗─╔╗
║║────╔╝╚╦╝╚╗
║╚═╦╗╔╬╗╔╩╗╔╬══╦═╗╔══╗
║╔╗║║║║║║─║║║╔╗║╔╗╣══╣
║╚╝║╚╝║║╚╗║╚╣╚╝║║║╠══║
╚══╩══╝╚═╝╚═╩══╩╝╚╩══╝
#########################
● This is where the buttons are defined. Using the class...
● They are self-explanatory
'''

#buttons for the main
mapButton = button((255,255,255), 200, 250, 500, 100, 'Canteen Customisation')
predictButton = button((255,255,255), 100, 400, 300, 100, 'Prediction')
exitButton = button((255,255,255), 500, 400, 300, 100, 'Exit')

#buttons for the custimisation screen
halalButton = button((255,255,255), 50, 120, 250, 50, 'Halal')
vegButton = button((255,255,255), 320, 120, 250, 50, 'Vegetarian')
nonhalalButton = button((255,255,255), 590, 120, 250, 50, 'Non-Halal')
koreanButton = button((255,255,255), 50, 270, 250, 50, 'Korean')
malayButton = button((255,255,255), 320, 270, 250, 50, 'Malay')
japanButton = button((255,255,255), 590, 270, 250, 50, 'Japanese')
chineseButton = button((255,255,255), 50, 340, 250, 50, 'Chinese')
indianButton = button((255,255,255), 320, 340, 250, 50, 'Indian')
westernButton = button((255,255,255), 590, 340, 250, 50, 'Western')
button3 = button((255,255,255), 235, 490, 70, 50, '$3')
button5 = button((255,255,255), 355, 490, 70, 50, '$5')
button7 = button((255,255,255), 475, 490, 70, 50, '$7')
button9 = button((255,255,255), 595, 490, 70, 50, '$10')
nextButton = button((255,255,255), 730, 580, 120, 70, 'Next')

#buttons to show GPS
gpsButton = button((255,255,255), 700, 600, 170, 50, 'to Map')
restartButton = button((255,255,255), 700, 600, 190, 50, 'Restart?')

'''
#############################
────╔╗────╔╗
───╔╝╚╗──╔╝╚╗
╔══╬╗╔╬══╬╗╔╬══╦══╗
║══╣║║║╔╗║║║║║═╣══╣
╠══║║╚╣╔╗║║╚╣║═╬══║
╚══╝╚═╩╝╚╝╚═╩══╩══╝
#############################
● Since I'm only using one while loop and all the functions are in here,
  it is important to note that none of the "if" statements interfere with
  one another
● Acts like a flip-flop which stores the data of the different states
'''
#originalstate of customisation buttons
halalButtonPressed = False
vegButtonPressed = False
nonhalalButtonPressed = False
koreanButtonPressed = False
malayButtonPressed = False
japanButtonPressed = False
chineseButtonPressed = False
indianButtonPressed = False
westernButtonPressed = False
button3Pressed = False
button5Pressed = False
button7Pressed = False
button9Pressed = False
nextButtonPressed = False
gpsButtonPressed = False

#original state of events
checkButton = True
mapCoor = False
customisationMenu = False
mapCoor2 = False
easySearch = False
complicatedMenu = False
oneTime = True

'''
####################################
╔═╗╔═╗───────╔═══╗
║║╚╝║║───────║╔═╗║
║╔╗╔╗╠══╦╦═╗─║╚═╝╠═╦══╦══╦═╦══╦╗╔╗
║║║║║║╔╗╠╣╔╗╗║╔══╣╔╣╔╗║╔╗║╔╣╔╗║╚╝║
║║║║║║╔╗║║║║║║║──║║║╚╝║╚╝║║║╔╗║║║║
╚╝╚╝╚╩╝╚╩╩╝╚╝╚╝──╚╝╚══╩═╗╠╝╚╝╚╩╩╩╝
──────────────────────╔═╝║
──────────────────────╚══╝
####################################
● It involves a lot of states, turn on and off to display
  multiple things without them interfering with each
  other
● Eg. Clicking customisation button will disable itself, hence
  if the mouse is clicked over at the same area, it will not
  be activated once again
● This is every important! :)
● Also left some debugging messages in the console to help
  understand what is going on behind the scenes
'''
pygame.init()
run = True
clock = pygame.time.Clock()
#start the pygame
while run:
    #if true, redraws the main window
    if checkButton:
        redrawMainWin(screen)
    #if true, redraws the customisation window
    if customisationMenu:
        redrawCustWin(screen)
    if easySearch:
        if oneTime:
            nearest_canteen = redrawSearchWin(screen,x,y)
            sleep(2)
            oneTime = False
        gpsButton.draw(screen, (0,0,0))
    #if true, redraws the complicated cusomisation results
    if complicatedMenu:
        if oneTime:
            complicatedSearchWin(screen, nearest_canteen)
            sleep(2)
            oneTime = False
        gpsButton.draw(screen, (0,0,0))
    #redraws the GPS map, with point locaters
    if gpsButtonPressed == True:
        redrawGPSMap(screen, nearest_canteen, x, y)
    pygame.display.update()
    clock.tick(30)

    #checks event
    for event in pygame.event.get():
        #gets the mouse position
        pos = pygame.mouse.get_pos()

        #quits the pygame
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if gpsButtonPressed:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restartButton.isOver(pos):
                    restartButton.colour = (50,50,50)
                    restartButton.draw(screen, (0,0,0))
                    pygame.display.update()
                    print('clicked the restart button')
                    #originalstate of customisation buttons
                    halalButtonPressed = False
                    vegButtonPressed = False
                    nonhalalButtonPressed = False
                    koreanButtonPressed = False
                    malayButtonPressed = False
                    japanButtonPressed = False
                    chineseButtonPressed = False
                    indianButtonPressed = False
                    westernButtonPressed = False
                    button3Pressed = False
                    button5Pressed = False
                    button7Pressed = False
                    button9Pressed = False
                    nextButtonPressed = False
                    gpsButtonPressed = False
                    #original state of events
                    checkButton = True
                    mapCoor = False
                    customisationMenu = False
                    mapCoor2 = False
                    easySearch = False
                    complicatedMenu = False
                    oneTime = True

            if event.type == pygame.MOUSEMOTION:
                if restartButton.isOver(pos):
                    restartButton.colour = (0,255,0)
                    continue
                else:
                    restartButton.colour = (255,255,255)
                    continue

        if easySearch == True or complicatedMenu == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if gpsButton.isOver(pos):
                    gpsButton.colour = (50,50,50)
                    gpsButton.draw(screen, (0,0,0))
                    pygame.display.update()
                    print('clicked gps button')
                    gpsButtonPressed = True
                    easySearch = False
                    complicatedMenu = False
                    continue

            if event.type == pygame.MOUSEMOTION:
                if gpsButton.isOver(pos):
                    gpsButton.colour = (0,255,0)
                    continue
                else:
                    gpsButton.colour = (255,255,255)
                    continue
        
        #if mouse is clicked over buttons (main)
        if checkButton:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mapButton.isOver(pos):
                    mapButton.colour = (0,255,0)
                    redrawMainWin(screen)
                    pygame.display.update()
                    print('clicked map button')
                    sleep(0.5)
                    redrawMap(screen)
                    checkButton = False
                    mapCoor = True
                    continue
                
                if predictButton.isOver(pos):
                    predictButton.colour = (0,255,0)
                    redrawMainWin(screen)
                    pygame.display.update()
                    print('clicked predict button')
                    sleep(0.5)
                    redrawMap(screen)
                    checkButton = False
                    mapCoor2 = True
                    continue

                if exitButton.isOver(pos):
                    exitButton.colour = (0,255,0)
                    print('Exiting...')
                    skeleExit(screen)
                    pygame.quit()
                    run = False
                    exit()

        #if mouse hovered over the button (main)
            if event.type == pygame.MOUSEMOTION:
                if mapButton.isOver(pos):
                    mapButton.colour = (255,0,0)
                else:
                    mapButton.colour = (255,255,255)

                if predictButton.isOver(pos):
                    predictButton.colour = (255,0,0)
                else:
                    predictButton.colour = (255,255,255)

                if exitButton.isOver(pos):
                    exitButton.colour = (255,0,0)
                else:         
                    exitButton.colour = (255,255,255)

    #clicking buttons in the customisation menu
        if customisationMenu:
            if event.type == pygame.MOUSEMOTION:
                if nextButton.isOver(pos):
                    nextButton.colour = (0,0,255)
                else:
                    nextButton.colour = (255,255,255)
                continue
            if event.type == pygame.MOUSEBUTTONDOWN:

                #click next button
                if nextButton.isOver(pos):
                    nextButton.colour = (255,255,0)
                    nextButtonPressed = True
                    customisationMenu = False
                    continue

                if halalButton.isOver(pos):
                    if halalButtonPressed == False:
                        if nonhalalButtonPressed:
                            nonhalalButton.colour = (255,255,255)
                            nonhalalButtonPressed = False
                        halalButton.colour = (0,255,0)
                        print('clicked halal button')
                        halalButtonPressed = True
                        continue
                    else:
                        halalButton.colour = (255,255,255)
                        halalButtonPressed = False
                        continue
                
                if vegButton.isOver(pos):
                    if vegButtonPressed == False:
                        if nonhalalButtonPressed:
                            nonhalalButton.colour = (255,255,255)
                            nonhalalButtonPressed = False
                        vegButton.colour = (0,255,0)
                        print('clicked vegetarian button')
                        vegButtonPressed = True
                        continue
                    else:
                        vegButton.colour = (255,255,255)
                        vegButtonPressed = False
                        continue

                if nonhalalButton.isOver(pos):
                    if nonhalalButtonPressed == False:
                        if halalButtonPressed:
                            halalButton.colour = (255,255,255)
                            halalButtonPressed = False
                        if vegButtonPressed:
                            vegButton.colour = (255,255,255)
                            vegButtonPressed = False
                        nonhalalButton.colour = (0,255,0)
                        print('clicked non-halal button')
                        nonhalalButtonPressed = True
                        continue
                    else:
                        nonhalalButton.colour = (255,255,255)
                        nonhalalButtonPressed = False

                if koreanButton.isOver(pos):
                    if koreanButtonPressed == False:
                        koreanButton.colour = (0,255,0)
                        print('clicked korean button')
                        koreanButtonPressed = True
                        continue
                    else:
                        koreanButton.colour = (255,255,255)
                        koreanButtonPressed = False

                if malayButton.isOver(pos):
                    if malayButtonPressed == False:
                        malayButton.colour = (0,255,0)
                        print('clicked malay button')
                        malayButtonPressed = True
                        continue
                    else:
                        malayButton.colour = (255,255,255)
                        malayButtonPressed = False

                if japanButton.isOver(pos):
                    if japanButtonPressed == False:
                        japanButton.colour = (0,255,0)
                        print('clicked japan button')
                        japanButtonPressed = True
                        continue
                    else:
                        japanButton.colour = (255,255,255)
                        japanButtonPressed = False

                if chineseButton.isOver(pos):
                    if chineseButtonPressed == False:
                        chineseButton.colour = (0,255,0)
                        print('clicked chinese button')
                        chineseButtonPressed = True
                        continue
                    else:
                        chineseButton.colour = (255,255,255)
                        chineseButtonPressed = False

                if indianButton.isOver(pos):
                    if indianButtonPressed == False:
                        indianButton.colour = (0,255,0)
                        print('clicked indian button')
                        indianButtonPressed = True
                        continue
                    else:
                        indianButton.colour = (255,255,255)
                        indianButtonPressed = False

                if westernButton.isOver(pos):
                    if westernButtonPressed == False:
                        westernButton.colour = (0,255,0)
                        print('clicked western button')
                        westernButtonPressed = True
                        continue
                    else:
                        westernButton.colour = (255,255,255)
                        westernButtonPressed = False
                
                if button3.isOver(pos):
                    if button3Pressed == False:
                        if button5Pressed == True:
                            button5.colour = (255,255,255)
                            button5Pressed = False
                        if button7Pressed == True:
                            button7.colour = (255,255,255)
                            button7Pressed = False
                        if button9Pressed == True:
                            button9.colour = (255,255,255)
                            button9Pressed = False
                        button3.colour = (0,255,0)
                        print('clicked $3')
                        button3Pressed = True
                        continue
                    else:
                        button3.colour = (255,255,255)
                        button3Pressed = False
                
                if button5.isOver(pos):
                    if button5Pressed == False:
                        if button3Pressed == True:
                            button3.colour = (255,255,255)
                            button3Pressed = False
                        if button7Pressed == True:
                            button7.colour = (255,255,255)
                            button7Pressed = False
                        if button9Pressed == True:
                            button9.colour = (255,255,255)
                            button9Pressed = False
                        button5.colour = (0,255,0)
                        print('Clicked $5')
                        button5Pressed = True
                        continue
                    else:
                        button5.colour = (255,255,255)
                        button5Pressed = False

                if button7.isOver(pos):
                    if button7Pressed == False:
                        if button3Pressed == True:
                            button3.colour = (255,255,255)
                            button3Pressed = False
                        if button5Pressed == True:
                            button5.colour = (255,255,255)
                            button5Pressed = False
                        if button9Pressed == True:
                            button9.colour = (255,255,255)
                            button9Pressed = False
                        button7.colour = (0,255,0)
                        print('Clicked $7')
                        button7Pressed = True
                        continue
                    else:
                        button7.colour = (255,255,255)
                        button7Pressed = False

                if button9.isOver(pos):
                    if button9Pressed == False:
                        if button3Pressed == True:
                            button3.colour = (255,255,255)
                            button3Pressed = False
                        if button5Pressed == True:
                            button5.colour = (255,255,255)
                            button5Pressed = False
                        if button7Pressed == True:
                            button7.colour = (255,255,255)
                            button7Pressed = False
                        button9.colour = (0,255,0)
                        print('Clicked $10')
                        button9Pressed = True
                        continue
                    else:
                        button9.colour = (255,255,255)
                        button9Pressed = False 

        #if mousebuttondown and map is already displayed
        if mapCoor == True and event.type == pygame.MOUSEBUTTONDOWN:
             mouseclick = mouseClick(screen)
             if mouseclick[0]:
                    pygame.display.update()
                    x = mouseclick[1]
                    y = mouseclick[2]
                    print(x, ',', y)
                    #pygame.time.delay(2000) 
                    mapCoor = False
                    sleep(1)
                    customisationMenu = True

        #if prediction button is clicked
        if mapCoor2 == True and event.type == pygame.MOUSEBUTTONDOWN:
             mouseclick = mouseClick(screen)
             if mouseclick[0]:
                    pygame.display.update()
                    x = mouseclick[1]
                    y = mouseclick[2]
                    print(x, ',', y)
                    #pygame.time.delay(2000) 
                    mapCoor2 = False
                    sleep(1)
                    loading(screen)
                    easySearch = True

        #things that happen after the next button is pressed
        if nextButtonPressed:
            sleep(1)
            loading(screen)
            user_prefList = []
            user_cuisineList = []
            user_budget = 0
            if halalButtonPressed:
                user_prefList.append("Halal")
            if vegButtonPressed:
                user_prefList.append("Vegetarian")
            if nonhalalButtonPressed:
                user_prefList.append("Non-Halal/Non-Vegetarian")
            if koreanButtonPressed:
                user_cuisineList.append("Korean")
            if malayButtonPressed:
                user_cuisineList.append("Malay")
            if japanButtonPressed:
                user_cuisineList.append("Japanese")
            if chineseButtonPressed:
                user_cuisineList.append("Chinese")
            if indianButtonPressed:
                user_cuisineList.append("Indian")
            if westernButtonPressed:
                user_cuisineList.append("Western")
            if button3Pressed:
                user_budget = 3
            if button5Pressed:
                user_budget = 5
            if button7Pressed:
                user_budget = 7
            if button9Pressed:
                user_budget = 9
            #debug
            print(user_cuisineList)
            print(user_prefList)
            print(user_budget)
            #continue#
            finalID = final_list(user_budget, user_cuisineList, user_prefList)
            print(finalID)
            nearest_canteen = nearest_can(finalID, x, y)
            print(nearest_canteen)
            sleep(1)
            nextButtonPressed = False
            complicatedMenu = True
            