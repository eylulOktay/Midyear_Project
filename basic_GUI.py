import arcade
import arcade.gui
from player import *

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
        self.game = Game("Gerald")
        self.color = [200,50,50]
        self.stats_rects = []
        self.stats = [self.game.player.grade, self.game.player.sleep, self.game.player.happiness, self.game.player.work_ethic, self.game.player.fun]
        self.isGoing = 0
        self.stats_open = False
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.rect_list = []


        self.stats_box = arcade.gui.UIBoxLayout()
        self.ok_box = arcade.gui.UIBoxLayout()


        # # Create our rectangle
        self.lower_frame = Rect(SCREEN_WIDTH, SCREEN_HEIGHT/3, SCREEN_WIDTH/2, SCREEN_HEIGHT/6, arcade.color.MSU_GREEN)
        self.teacher = Rect(SCREEN_WIDTH/5, SCREEN_HEIGHT/2, SCREEN_WIDTH/2,SCREEN_HEIGHT/2,arcade.color.RED_DEVIL)
        
        self.stats_button = arcade.gui.UIFlatButton(text="Stats",
                                               width=200)
        self.stats_box.add(self.stats_button)

        # Set background color
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

                # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="top",
                
                child=self.stats_box)
        )
        '''
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                
                child=self.ok_box)
        )
        '''
        

        
        
        def make_stats(event):
            def bar_construction(game):
                ''' Creates the stats view shown in the menus upon clicking the menu button'''
                # one big bar for the full metre, # one small bar showing magnititude
                
                # add name label here
                
                for i in range(len(self.stats)):
                    stat_rect = Rect(460,10,SCREEN_WIDTH/2, (3+i)*SCREEN_HEIGHT/9, arcade.color.BLUE_SAPPHIRE)
                    self.stats_rects.append(stat_rect)
                    self.rectangle_appear(stat_rect)
            
            def ok_button_quit(event): 
                # remove rectangle from list that shows rectangles
                
                for rect in self.stats_rects: # self.stats_rects = list of the ui created by the stats button
                    self.rect_list.remove(rect)
                self.stats_rects = []
                #self.ok_box.remove(self.okButton)
                self.stats_open = False
                


                
                
            if self.stats_open:
                ok_button_quit(event)
            else:
                self.stats_rect_main = Rect(500,400,SCREEN_WIDTH/2,SCREEN_HEIGHT/2, arcade.color.PURPLE_HEART)
                self.stats_rects.append(self.stats_rect_main)
                self.rectangle_appear(self.stats_rect_main)
                #self.okButton = arcade.gui.UIFlatButton(text = " X ", width = 50)
                
                #self.okButton.on_click =  ok_button_quit 
                #self.ok_box.add(self.okButton)
                self.stats_open = True
                bar_construction(self.game)
                
         
                
                    
        
        
      
    


        self.stats_button.on_click = make_stats

    # This just updates the screen. Not sure why, and not sure I care. Just yet.
    def on_update(self, delta_time):
        # Move the rectangle
        if self.isGoing:
            arcade.set_background_color((self.color[0],self.color[1],self.color[2]))
            if self.color[self.last_max] > 50:
                self.color[self.last_max] -=2
            if self.color[((self.last_max+1) % 3)] <200:
                self.color[((self.last_max+1) % 3)] += 2
            else:
                self.last_max +=1
                self.last_max %=3
        
        
    def time_passes(self,event):
        self.isGoing = 1 - self.isGoing
        print(f"color: {self.color}")


    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()
        # Draw the rectangle
        
        self.teacher.draw()
        self.lower_frame.draw()
        for n in self.rect_list:
            n.draw()
        
        self.manager.draw()
        

    def rectangle_appear(self, rectangle):
        print("Make rectangle")
        
        self.rect_list.append(rectangle)

        