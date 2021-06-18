from tkinter import Tk, Canvas, Frame, BOTH
import math


def main():
    # Create the root Tk object.
    root = Tk()

    # Create a Scene window. Creating an object
    # calls the __init__ function in the class.
    Scene()

    root.geometry("800x600")
    root.mainloop()


class Scene(Frame):
    """A Scene object is a Frame that uses the tkinter library
    to draw a somewhat realistic outdoor scene in the frame.
    """

    def __init__(self):
        """Initialize a Scene object."""

        # Call __init__ in the parent class.
        super().__init__()

        self.master.title("Scene")
        self.pack(fill=BOTH, expand=1)

        # Get a canvas object that will draw into this Scene object.
        canvas = Canvas(self)
        canvas.pack(fill=BOTH, expand=1)

        # Call the draw_scene function.
        draw_scene(canvas, 0, 0, 799, 599)

     

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):


        
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.

    param scene_left - left side of region; less than scene_right
    param scene_top - top of the region; less than scene_bottom
    param scene_right - right side of the region
    param scene_bottom - bottom of the region

    The width and height of the region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
        
    

    canvas.create_rectangle(scene_left +0, scene_top + 0,
            scene_right + 5, scene_bottom + 10,
            outline = "#99e0e8", fill = "#99e0e8")

    canvas.create_rectangle(scene_left +0, scene_top +430,
            scene_right +5, scene_bottom +10,
            outline = "#6b5045", fill = "#6b5045")
    
    canvas.create_oval(30,65,300,0,
            outline = "#ffffff", width = 5, fill = "#ffffff" )

    canvas.create_oval(60,50,350,100,
            outline = "#ffffff", width = 6, fill = "#ffffff" )

    canvas.create_oval(400,60,250,20,
            outline = "#ffffff", width = 4, fill = "#ffffff" )
    
    canvas.create_oval(700,100,350,200,
            outline = "#ffffff", width = 4, fill = "#ffffff" )

    canvas.create_oval(800,70,500,150,
            outline = "#ffffff", width = 3, fill = "#ffffff" )

    canvas.create_oval(900,50,600,200,
            outline = "#ffffff", width = 4, fill = "#ffffff" )

    
        


    draw_grass(canvas,scene_left,scene_top,scene_right,scene_bottom,20)
    draw_leaf(canvas,scene_left,scene_top,scene_right,scene_bottom,30)
    draw_field(canvas,scene_left,scene_top,scene_right,scene_bottom,14)
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 350
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    draw_sun(canvas, 70, 60)
    
     

def draw_grass(canvas, left, top, right, bottom, grid_spacing):
     
        for i in range(left,right,grid_spacing):
                  canvas.create_line(i,470,i,bottom,
                fill = "#419127", width = 6) 
def draw_leaf(canvas, left, top, right, bottom, grid_spacing):

        for i in range(left,right,grid_spacing):
                  canvas.create_line(i,450,i,bottom,
                fill = "#386b28", width = 5) 
def draw_field(canvas, left, top, right, bottom, grid_spacing):

        for i in range(left,right,grid_spacing):
                  canvas.create_line(i,460,i,bottom,
                fill = "#37801f", width = 5) 

def draw_sun(canvas, sun_left, sun_top):
        sun_width = 100
        sun_height = 100
        ray_length = 100
        ray_width = 3
        ray_count = 10

        sun_right = sun_left + sun_width
        sun_bottom = sun_top + sun_height
        sun_center_x = sun_left + (sun_width / 2)  
        sun_center_y = sun_top +(sun_height/ 2)
        
        canvas.create_oval(sun_left, sun_top, sun_right, sun_bottom, fill ="#FFF7B4", width= False) 

      

        for i in range(ray_count):
                angle = (2 * math.pi / ray_count) * i
                ray_x = sun_center_x + math.cos(angle) * ray_length
                ray_y = sun_center_y + math.sin(angle) * ray_length
                canvas.create_line(sun_center_x, sun_center_y, ray_x, ray_y, width = ray_width, fill = "#FFF7B4")       
def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")
        




        

        


    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


# Call the main function so that
# this program will start executing.
main()