import arcade #pip install arcade

# SETTING SIZE FOR MAIN WINDOW
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700

#careting and opening the window
arcade.open_window(WINDOW_WIDTH, WINDOW_HEIGHT,"SAD FACE")

# setting background color
arcade.set_background_color(arcade.color.WHITE) # RED

# starting the render
arcade.start_render()

# Drawing starts from here...

#draw the outline of the face
y = x = 350
radius = 200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

# drawing the right eye
x = 420
y = 420
radius = 25
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

# drawing the left eye
x = 290 
y = 420
radius = 25
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

# drwing the sad smile
x = 350
y = 240 # 310 smile
width = 120
height = 100
starting_angle = 0 # 180 smile
end_angle = 180 # 360 smile
arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, starting_angle,
                end_angle, 10)


#draw the outline of the face
y = x = 350
radius = 200
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

# finishing the render
arcade.finish_render()

# running the code
arcade.run()
