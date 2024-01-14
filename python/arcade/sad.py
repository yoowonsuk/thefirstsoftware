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

# finishing the renger
arcade.finish_render()

# running the code
arcade.run()
