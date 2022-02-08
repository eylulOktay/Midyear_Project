import arcade
import arcade.gui

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NAME IN PROGRESS"

# Rectangle info

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
        
class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.rect_list = []


        self.v_box = arcade.gui.UIBoxLayout()

        # # Create our rectangle
        self.lower_frame = Rect(SCREEN_WIDTH, SCREEN_HEIGHT/3, SCREEN_WIDTH/2, SCREEN_HEIGHT/6, arcade.color.MSU_GREEN)
        self.teacher = Rect(SCREEN_WIDTH/5, SCREEN_HEIGHT/2, SCREEN_WIDTH/2,SCREEN_HEIGHT/2,arcade.color.RED_DEVIL)
        
        self.rect_list.append(self.lower_frame)
        self.rect_list.append(self.teacher)
        
        self.stats_button = arcade.gui.UIFlatButton(text="Stats",
                                               width=200)
        self.v_box.add(self.stats_button.with_space_around(bottom=10))

        # Set background color
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

                # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="top",
                
                child=self.v_box)
        )
        self.stats_button.on_click = self.rectangle_appear



    # This just updates the screen. Not sure why, and not sure I care. Just yet.
    def on_update(self, delta_time):
        # Move the rectangle
        pass

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()
        # Draw the rectangle
        for n in self.rect_list:
            n.draw()
        # self.teacher.draw()
        # self.lower_frame.draw()
        self.manager.draw()

    def rectangle_appear(self, event):
        print("Make rectangle")
        self.rectapp = Rect(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH/2, SCREEN_HEIGHT/6, arcade.color.PURPLE_HEART)
        self.rect_list.append(self.rectapp)