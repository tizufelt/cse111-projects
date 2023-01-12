# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

import tkinter as tk
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)
    
    

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    
    draw_sky(canvas, scene_width, scene_height)
    draw_mountain(canvas, 400, 150, 335)
    draw_mountain(canvas, 300, 150, 335)
    draw_mountain(canvas, 500, 150, 335)
    draw_cloud(canvas, 150, 350, 400)
    draw_cloud(canvas, 700, 425, 400)
    draw_grass(canvas, scene_width, scene_height)
    draw_pine_tree(canvas, 550, 100, 150)
    draw_pine_tree(canvas, 700, 75, 200)
    draw_pine_tree(canvas, 625, 100, 200)
    draw_pine_tree(canvas, 50, 75, 200)
    draw_pine_tree(canvas, 125, 100, 200)
    draw_pine_tree(canvas, 200, 50, 200)
    draw_birds(canvas, scene_width, scene_width, num_birds=12)
    draw_grid(canvas, scene_width, scene_height, 50)
    
   
    
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


    #Draw for GRID
def draw_grid(canvas, width, height, interval):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
        
    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")
     
 
    
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="cadetBlue2")
    
def draw_grass(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="paleGreen3")
        
def draw_mountain(canvas, center_x, bottom, height):
    skirt_width = height / 2
    skirt_height = height - height
    trunk_top = skirt_height + skirt_width
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="slateGray")

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 4
    left_trunk = center_x - trunk_width / 2
    bottom_trunk = bottom
    right_trunk = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height
    draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, trunk_top, fill="tan4")
    
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom + height
    draw_polygon(canvas, skirt_left, skirt_bottom, peak_x, peak_y, skirt_right, skirt_bottom, fill="forestGreen")
  
def draw_cloud(canvas, center_x, bottom, height):
    #first part of cloud body.
    main_cloud_width = height / 2
    main_cloud_height = height / 6
    main_cloud_left = center_x - main_cloud_width / 2
    main_cloud_bottom = bottom
    main_cloud_right = center_x + main_cloud_width / 2
    main_cloud_top = bottom + main_cloud_height
    draw_oval(canvas, main_cloud_left, main_cloud_bottom, main_cloud_right, main_cloud_top, width = 0, fill = "honeydew2")
    #Left part of cloud.
    main_cloud_width = height / 12
    main_cloud_height = height / 8
    main_cloud_left = (center_x - main_cloud_width / 2) - 100
    main_cloud_bottom = bottom - 10
    main_cloud_right = center_x + main_cloud_width / 2
    main_cloud_top = (bottom + main_cloud_height) - 10
    draw_oval(canvas, main_cloud_left, main_cloud_bottom, main_cloud_right, main_cloud_top, width = 0, fill = "honeydew1")
    #Right part of cloud.
    main_cloud_width = height / 12
    main_cloud_height = height / 8
    main_cloud_left = (center_x - main_cloud_width / 2)
    main_cloud_bottom = bottom - 25
    main_cloud_right = center_x + main_cloud_width / 2 + 100
    main_cloud_top = (bottom + main_cloud_height) - 25
    draw_oval(canvas, main_cloud_left, main_cloud_bottom, main_cloud_right, main_cloud_top, width = 0, fill = "ivory1")
  

def draw_birds(canvas, scene_width, scene_height, num_birds=12):
    for i in range(num_birds):
        x = random.randint(0, scene_width-50 )
        y = random.randint(250, scene_height-55)
        draw_arc(canvas, x, y, x+25, y+15, start=360, extent=90, width=1, outline="gray20",)
        draw_arc(canvas, x+25, y, x+50, y+15, start=90, extent=90, width=1, outline="gray20",)
  
    
    
    
    
    
    
    
    
    
# Call the main function so that
# this program will start executing.
main() 