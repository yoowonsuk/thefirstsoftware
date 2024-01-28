import arcade
import math

Window_Width=900
Window_Height=700

AXIS_X = Window_Width // 2
AXIS_Y = Window_Height // 2 
#Radians_per_Tick = 0.02
#Radians_per_Tick = 4
Radians_per_Tick = 60/360
Radar_needle_Length = 300

def on_draw(new_time):
    on_draw.angle += Radians_per_Tick

    x = Radar_needle_Length * math.sin(on_draw.angle) + AXIS_X
    y = Radar_needle_Length * math.cos(on_draw.angle) + AXIS_Y
    arcade.start_render()
    arcade.draw_line(AXIS_X,AXIS_Y,x,y,arcade.color.RED,5)
    
    arcade.draw_circle_outline(AXIS_X,AXIS_Y,Radar_needle_Length,arcade.color.DARK_BLUE,10)
on_draw.angle = 0


if __name__=="__main__":
    arcade.open_window(Window_Width, Window_Height, "RADAR SYSTEM")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 2)
    #arcade.schedule(on_draw, 1/1000)
    arcade.run()

