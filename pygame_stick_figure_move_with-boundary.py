import pygame as pu
import random
from time import *


pu.init()

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
pi = 3.14285714

size = [1100,700]
screen = pu.display.set_mode(size)

def draw_line(screen,start_x,start_y,end_x,end_y,size):
    pu.draw.line(screen,red,[start_x,start_y],[end_x,end_y],size)
    
def draw_ellipse(screen,x,y,width,height,size):
    pu.draw.ellipse(screen,green,[100,100,250,100],3)
    #similar to rectangle
    
def draw_rect(screen,x,y,width,height,size):
    pu.draw.rect(screen,black,[x,y,width,height],size)
    #[x,y,width,height] x,y is the top left corner of the rectangle

def draw_arc(screen,x,y,width,height,size,start_angle,end_angle):
    pu.draw.arc(screen,blue,[x,y,width,height],start_angle,end-angle,size)
    #similar to rectangle but add the starting and ending angles of the arc in radians 

def draw_polygon(screen,list_of_vertices,size):
    pu.draw.polygon(screen,darkBlue,list_of_vertices,size)
    #give the vertices needed to connect


def font(font_path,font_size,text,color,text_pos_in_list):
    #writing text
    font_wanted = pu.font.Font(font_path,font_size)
    #(fontstyle,fontsize)
    text_stamp = font_wanted.render(text,True,color)
    #(text,true=smooth else ragged,color) creating a stamp
    screen.blit(text_stamp,text_pos_in_list)
    #stamp it
    #end


def get_mouse_pos():
    screen.fill(white)
    pu.mouse.set_visible(1)
    pos = pu.mouse.get_pos()
    return pos

def draw_a_man(x,y):
    screen.fill(white)
    pu.draw.ellipse(screen,black,[x,y,30,30])
    pu.draw.line(screen,black,[x+15,y+30],[x+15,y+60],4)
    pu.draw.line(screen,black,[x+15,y+30],[x+8,y+42],4)
    pu.draw.line(screen,black,[x+8,y+42],[x+15,y+52],4)
    pu.draw.line(screen,black,[x+15,y+61],[x+5,y+80],4)
    pu.draw.line(screen,black,[x+15,y+61],[x+25,y+80],4)
    pu.display.flip()

def draw_a_man_straight(x,y):
    screen.fill(white)
    pu.draw.ellipse(screen,black,[x,y,30,30])
    pu.draw.line(screen,black,[x+15,y+30],[x+15,y+60],4)
    pu.draw.line(screen,black,[x+15,y+30],[x+8,y+42],4)
    pu.draw.line(screen,black,[x+8,y+42],[x+15,y+52],4)
    pu.draw.line(screen,black,[x+15,y+61],[x+15,y+80],4)
    pu.display.flip()

pu.display.set_caption("GAME")

done = False

clock = pu.time.Clock()

x_cord = 100
y_cord = 100
x_speed = 0
y_speed = 0

while done == False:

    for event in pu.event.get():
        if event.type == pu.QUIT:
            pu.QUIT
            done = True
            
        if event.type == pu.KEYDOWN:
            if event.key == pu.K_LEFT:
                x_speed = -10
            if event.key == pu.K_RIGHT:
                x_speed = 10
            if event.key == pu.K_UP:
                y_speed = -10
            if event.key == pu.K_DOWN:
                y_speed = +10
                
        if event.type == pu.KEYUP:
            if event.key == pu.K_LEFT:
                x_speed = 0
            if event.key == pu.K_RIGHT:
                x_speed = 0
            if event.key == pu.K_UP:
                y_speed = 0
            if event.key == pu.K_DOWN:
                y_speed = 0
            
            

    #game logic starts
#    pos = get_mouse_pos()
    if x_cord in range(0,size[0]):
        x_cord += x_speed
    else:
        x_cord -= x_speed
    if y_cord in range(0,size[1]):
        y_cord += y_speed
    else:
        y_cord -= y_speed
    #game logic stops

    #draw code start        
    screen.fill(white)
    draw_a_man(x_cord,y_cord)
#moving stick figuere
##    for i in range(30,size[0],40):
##        sleep(0.17)        
##        draw_a_man(i,100)
##        sleep(0.17)
##        draw_a_man_straight(i+20,100)
        
    
##    pu.display.flip()
    #draw code end

    clock.tick(20)

pu.QUIT
