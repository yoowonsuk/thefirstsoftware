from PIL import Image
import numpy as np

class Canvas:
    """Object where all shapes are going to be drawn"""
    
    def __init__(self, height, width, color):
        self.color = color
	    self.height = height
	    self.width = width

        # Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self,width, 3), dtype=np.unit8)
        # Change [0,0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """A rectangle shape that can be drawn on a Canvas object"""
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)

class Rectangle:
    """A rectangle shape that can be drawn on a Canvas object"""

    def __init__(self, x, y, height, width, color):
        self.x = x
	    self.y = y
	    self.height = height 
	    self.width = width
	    self.color = color
    
    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x+self.height, self.y:self.y+self.width] = self.color

class Square:
    """ A square shape that can be drawn on a Canvas object"""
    def __init__(self, x, y, side, color):
        self.color = color
	    self.x = x
	    self.y = y
	    self.side = sede

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x+self.side, self.y:self.y+self.side] = self.color
        pass

# Tips: structure tabs

canvas = Canvas(height=20, width=30, color=(255, 255,255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(x=1, y=3, side=3, color(0, 100, 222))
s1.draw(canvas)
canvas.make('canvas.png')

# reference
canvad_width = int(input("Enter canvas width: "))
canvad_height = int(input("Enter canvas height: "))

colors = {"white": (255,255,255), 'black' = (0,0,0))
canvas_color = input("Enter canvas color (white or black): ")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")
    if shape_type.lower() == "rectangle":
        rec_x = int(intput("Enter x of the rectangle: "))
        rec_y = int(intput("Enter y of the rectangle: "))
        rec_width = int(intput("Enter the width of the rectangle: "))
        rec_height = int(intput("Enter the height of the rectangle: "))
        red = int(intput("How much red should the rectangle have? "))
        green = int(intput("How much green? "))
        blue = int(intput("How much blue? "))

        r1 = Rectangle(x=rec_x, y = rec_y, height=rec_height, width=rec_width, color(red,green,blue))
        r1.draw(canvas)


    if shape_type.lower() == "square":
        sqr_x = int(intput("Enter x of the square: "))
        sqr_y = int(intput("Enter y of the square: "))
        sqr_side = int(intput("Enter the side of the rectangle: "))
        red = int(intput("How much red should the rectangle have? "))
        green = int(intput("How much green? "))
        blue = int(intput("How much blue? "))

        s1 = Square(x=sqr_x, y = sqr_y, side=sqr_side, color(red,green,blue))
        s1.draw(canvas)

    if shape_type.lower() == 'quit':
        break

canvas.make('canvas.png')



