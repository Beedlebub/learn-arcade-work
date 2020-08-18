"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.

Lab 02: Draw a Picture
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "My Drawing")

# Set the background color
arcade.set_background_color(arcade.csscolor.BLACK)

# Get ready to draw
arcade.start_render()

# Start of my Drawing
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.LIGHT_GREY)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.LIGHT_GREY)
arcade.draw_lrtb_rectangle_filled(470, 530, 320, 100, arcade.csscolor.GREY)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
