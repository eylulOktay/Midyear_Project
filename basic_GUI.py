import arcade

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NAME IN PROGRESS"

# Rectangle info



BACKGROUND_COLOR = arcade.color.AIR_FORCE_BLUE


class Rect:
    """ This class represents our rectangle """

    def __init__(self, width, height, x, y, color):

        self.width = width
        self.height = height
        self.center_x = x
        self.center_y = y
        self.color = color

    def draw(self):
        # Draw the rectangle
        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     self.width,
                                     self.height,
                                     self.color)
    def destroy(self):
        self.destroy()
        
class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Create our rectangle
        self.lower_frame = Rect(SCREEN_WIDTH, SCREEN_HEIGHT/3, SCREEN_WIDTH/2, SCREEN_HEIGHT/6, arcade.color.MSU_GREEN)
        self.teacher = Rect(SCREEN_WIDTH/5, SCREEN_HEIGHT/2, SCREEN_WIDTH/2,SCREEN_HEIGHT/2,arcade.color.RED_DEVIL)
        

        # Set background color
        arcade.set_background_color(BACKGROUND_COLOR)

    # This just updates the screen. Not sure why, and not sure I care. Just yet.
    def on_update(self, delta_time):
        # Move the rectangle
        pass

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()
        # Draw the rectangle
        self.teacher.draw()
        self.lower_frame.draw()
        


def main():
    """ Main function """
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()