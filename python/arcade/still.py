import random
import arcade

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

def SCREEN():
    ''' drawing the background screen'''
    # upper 2/3rd portion
    arcade.draw_rectangle_filled(WINDOW_WIDTH/2, WINDOW_HEIGHT*2/3,WINDOW_WIDTH-1,
            WINDOW_HEIGHT*2/3, arcade.color.SKY_MAGENTA)

    #lower 1/3rd portion
    arcade.draw_rectangle_filled(WINDOW_WIDTH/2, WINDOW_HEIGHT*1/6,WINDOW_WIDTH-1,
            WINDOW_HEIGHT*1/3, arcade.color.LIGHT_GREEN)


def birds(x,y):
    arcade.draw_arc_outline(x,y,20, 20, arcade.color.BLACK, 0,90)
    arcade.draw_arc_outline(x+20,y,20, 20, arcade.color.BLACK, 90,180)

def trees(AXIS_x, AXIS_y):
    #draw the trunks(rectangle)
    arcade.draw_rectangle_filled(AXIS_x, AXIS_y,20,40,arcade.color.DARK_BROWN)

    root_line = AXIS_y + 20
    list = ((AXIS_x-40, root_line), (AXIS_x,root_line+100), (AXIS_x+40, root_line)) # triangle cordinator
    arcade.draw_polygon_filled(list, arcade.color.DARK_GREEN)

if __name__ == "__main__":
    #open the window
    arcade.open_window(WINDOW_WIDTH,WINDOW_HEIGHT,"Still Imaging with the Arcade Module")

    #start the render
    arcade.start_render()

    #Drawing goes right in here
    SCREEN()
    for count in range(10):
        x=random.randrange(0,WINDOW_WIDTH)
        y=random.randrange(WINDOW_HEIGHT/3,WINDOW_HEIGHT-20)
        birds(x,y)
                                                                                                                            for a in range(45, WINDOW_WIDTH,90):
        trees(a, WINDOW_HEIGHT/3)
    for a in range(65, WINDOW_WIDTH,90):
        trees(a, WINDOW_HEIGHT/3-120)

    #Ending the render
    arcade.finish_render()

    #Run our code
    arcade.run()
