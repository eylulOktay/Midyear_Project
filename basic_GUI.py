import arcade
import arcade.gui
from player import *
import random

# --- Set up the constants

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "NAME IN PROGRESS"

STAT_NAMES = ["grade","sleep","happiness","work_ethic","fun"]

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
        self.stats = self.game.player.stats
        self.last_max = 0
        self.isGoing = 0
        self.stats_open = False
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.rect_list = []
        self.labels = []
    

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
        self.stats_button.on_click = self.make_stats
       
        self.time_box = arcade.gui.UIBoxLayout()

        self.time_button = arcade.gui.UIFlatButton(text="Time",
                                               width=200)
        self.time_button.on_click = self.time_passes
        self.time_box.add(self.time_button)


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="top",
                
                child=self.time_box)
        )

        self.act_box = arcade.gui.UIBoxLayout()

        self.act_button = arcade.gui.UIFlatButton(text="ACT",
                                               width=200)
        self.act_button.on_click = self.act
        self.act_box.add(self.act_button)


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="bottom",
                align_x= 40,
                align_y= 40,
                
                child=self.act_box)
        )

        
        
    def make_stats(self,event):
        def bar_construction(game):
            ''' Creates the stats view shown in the menus upon clicking the menu button'''
            # one big bar for the full metre, # one small bar showing magnititude
            
            # collect the mag bars - access by index reference in self.mag_bars
            
            for i in range(len(self.stats)):
                stat_rect = Rect(460,10,SCREEN_WIDTH/2, (3+i)*SCREEN_HEIGHT/9, arcade.color.BLACK)
                self.stats_rects.append(stat_rect)
                self.rectangle_appear(stat_rect)

                # currently unfinished
                
                # todo - add text labels under or to the side of bars to tell you percentage of bar filled?

                # actual stats magnitude bar - only length altered (or width of the rectangle)
                mag_bar = Rect(self.stats[STAT_NAMES[i]] * 460 / 100, 10, SCREEN_WIDTH/2 - (100 - self.stats[STAT_NAMES[i]])*4.6/2, (3+i)*SCREEN_HEIGHT/9, arcade.color.CADMIUM_GREEN)
                self.stats_rects.append(mag_bar)
                self.rectangle_appear(mag_bar)

            self.grade_label = arcade.gui.UITextArea(text=STAT_NAMES[i] + f"{self.game.player.stats[STAT_NAMES[i]]/100:2f}", x = SCREEN_WIDTH/2, y = (3+i)*SCREEN_HEIGHT/9 + 30,
                                        width=50,
                                        height=20,
                                        font_size=20,
                                        font_name="Kenney Future")
            self.sleep_label = arcade.gui.UITextArea(text=STAT_NAMES[i] + f"{self.game.player.stats[STAT_NAMES[i]]/100:2f}", x = 200, y = 500,
                                              width=50,
                                              height=20,
                                              font_size=20,
                                              font_name="Kenney Future")
            self.happiness_label = arcade.gui.UITextArea(text=STAT_NAMES[i] + f"{self.game.player.stats[STAT_NAMES[i]]/100:2f}", x = 200, y = 500,
                                              width=50,
                                              height=20,
                                              font_size=20,
                                              font_name="Kenney Future")
            self.work_ethic_label = arcade.gui.UITextArea(text=STAT_NAMES[i] + f"{self.game.player.stats[STAT_NAMES[i]]/100:2f}", x = 200, y = 500,
                                              width=50,
                                              height=20,
                                              font_size=20,
                                              font_name="Kenney Future")
            self.fun_label = arcade.gui.UITextArea(text=STAT_NAMES[i] + f"{self.game.player.stats[STAT_NAMES[i]]/100:2f}", x = 200, y = 500,
                                              width=50,
                                              height=20,
                                              font_size=20,
                                              font_name="Kenney Future")
            self.manager.add(self.grade_label)
            self.manager.add(self.sleep_label)
            self.manager.add(self.happiness_label)
            self.manager.add(self.work_ethic_label)
            self.manager.add(self.fun_label)
            self.manager.add(self.stable)

        def ok_button_quit(event): 
            # remove rectangle from list that shows rectangles
            
            for rect in self.stats_rects: # self.stats_rects = list of the ui created by the stats button
                self.rect_list.remove(rect)
            self.stats_rects = []
            for slabel in self.labels:
                self.labels.remove(slabel)
            self.labels = []
            #self.ok_box.remove(self.okButton)
            self.stats_open = False
            self.manager.remove(self.stable)
            


            
            
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
            
            self.stable = arcade.gui.UITextArea(text="STATS", x = 200, y = 500,
                                            width=450,
                                            height=40,
                                            font_size=20,
                                            font_name="Kenney Future")
            self.manager.add(self.stable)
            bar_construction(self.game)
            self.stats[STAT_NAMES[random.randrange(5)]] -= 20
            self.game.player.cap()
            
        


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
        self.stats[STAT_NAMES[random.randint(0,4)]] -= 10
        self.stats[STAT_NAMES[random.randint(0,4)]] += 10
                # self.game.player.cap()
        self.game.time_passes()
    
    def act(self,event):
        self.game.player.do_work()
        self.time_passes(event)
        print("doing work")
        


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
        # print("Make rectangle")
        
        self.rect_list.append(rectangle)



       

        