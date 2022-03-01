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
DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturn"]
# Colors for all of the times
TIME_COLORS = [arcade.color.AERO_BLUE,arcade.color.AFRICAN_VIOLET,arcade.color.AIR_FORCE_BLUE]
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
        self.last_max = 0
        self.sleep_state = 0
        self.isGoing = 0
        self.stats_open = False
        self.isSleeping = False
        self.stats_rects = []
        self.stats_labels = []
        self.stats = self.game.player.stats
        self.act_open = False
        self.act_rects = []
        self.act_labels = []
        self.act_buttons = []
        self.assign_open = False
        self.assign_rects = []
        self.assign_labels = []
        self.assign_buttons = []
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.rect_list = []
        self.top_list = []
        self.labels = []
        
        self.last_time = 0
        #time
       
        self.output = "00:00:00"
    

        self.stats_box = arcade.gui.UIBoxLayout()
        


        # # Create our rectangle
        self.lower_frame = Rect(SCREEN_WIDTH, SCREEN_HEIGHT/3, SCREEN_WIDTH/2, SCREEN_HEIGHT/6, arcade.color.MSU_GREEN)
        self.time_frame = Rect(90, 50, 65, SCREEN_HEIGHT-35, arcade.color.ROYAL_PURPLE)
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
       
        # self.time_box = arcade.gui.UIBoxLayout()

        # self.time_button = arcade.gui.UIFlatButton(text="Time",
        #                                        width=200)
        
        # self.time_button.on_click = self.color_nonsense
        # self.time_box.add(self.time_button)


        # self.manager.add(
        #     arcade.gui.UIAnchorWidget(
        #         anchor_x="left",
        #         anchor_y="top",
                
        #         child=self.time_box)
        # )

        self.act_box = arcade.gui.UIBoxLayout()


        self.act_button = arcade.gui.UIFlatButton(text="ACT",
                                               width=200)
        self.act_button.on_click = self.make_act
        self.act_box.add(self.act_button)


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="bottom",
                align_x= 40,
                align_y= 40,
                
                child=self.act_box)
        )

      

        # Buttons Section

        self.act_buttons_box = arcade.gui.UIBoxLayout()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                y=30,
                child=self.act_buttons_box)
        )

        self.assign_box = arcade.gui.UIBoxLayout()


        self.assign_button = arcade.gui.UIFlatButton(text="ASSIGNMENTS",
                                               width=200)
        self.assign_button.on_click = self.make_assign
        self.assign_box.add(self.assign_button)


        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                align_x= -40,
                align_y= 40,
                
                child=self.assign_box)
        )

      

        # Buttons Section

        self.assign_buttons_box = arcade.gui.UIBoxLayout()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="left",
                anchor_y="center",
                align_x=175,
                y=30,
                child=self.assign_buttons_box)
        )

        self.assign_muttons_box = arcade.gui.UIBoxLayout()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="center",
                y=30,
                child=self.assign_muttons_box)
        )

        self.sleep_button = arcade.gui.UIFlatButton(text="Sleep", width=200) 
        self.sleep_button.on_click = lambda event : self.act(event,0)

        self.homework_button = arcade.gui.UIFlatButton(text="Homework", width=200) 
        self.homework_button.on_click = lambda event : self.act(event,1)

        self.games_button = arcade.gui.UIFlatButton(text="Games", width=200) 
        self.games_button.on_click = lambda event : self.act(event,2)

        self.text_friends_button = arcade.gui.UIFlatButton(text="Text Friends", width=200) 
        self.text_friends_button.on_click = lambda event : self.act(event,3)

        self.go_to_school_button1 = arcade.gui.UIFlatButton(text="Go To School", width=200) 
        self.go_to_school_button1.on_click = lambda event : self.act(event,4)

        self.go_to_school_button2 = arcade.gui.UIFlatButton(text="You Don't Have A Choice", width=200) 
        self.go_to_school_button2.on_click = lambda event : self.act(event,4)

        self.go_to_school_button3 = arcade.gui.UIFlatButton(text="Seriously, Just Go", width=200) 
        self.go_to_school_button3.on_click = lambda event : self.act(event,4)

        self.schoolwork_button = arcade.gui.UIFlatButton(text="Schoolwork", width=200) 
        self.schoolwork_button.on_click = lambda event : self.act(event,1)

        self.chat_button = arcade.gui.UIFlatButton(text="Chat With Friends", width=200) 
        self.chat_button.on_click = lambda event : self.act(event,3)

        self.study_button = arcade.gui.UIFlatButton(text="Study", width=200) 
        self.study_button.on_click = lambda event : self.act(event,1)

        self.ask_for_help_button = arcade.gui.UIFlatButton(text="Ask For Help", width=200) 
        self.ask_for_help_button.on_click = lambda event : self.act(event,1)

        self.assignments = {}
        self.assignments_done = {}

        # Tried to make this a for loop, couldn't get it to work and I am tired
        # self.assignment_list = [(1,9),(1,15),(2,10),(2,14),(2,15),(3,14),(4,8),(4,13)]
        
        assignment0 = arcade.gui.UIFlatButton(text="(0,20)", width=200) 
        assignment0.on_click = lambda event : self.do_assignment(event,(0,20))

        self.assignments[(0,20)] = assignment0

        assignment1 = arcade.gui.UIFlatButton(text="(1,9)", width=200) 
        assignment1.on_click = lambda event : self.do_assignment(event,(1,9))

        self.assignments[(1,9)] = assignment1

        assignment2 = arcade.gui.UIFlatButton(text="(1,15)", width=200) 
        assignment2.on_click = lambda event : self.do_assignment(event,(1,15))

        self.assignments[(1,15)] = assignment2

        assignment3 = arcade.gui.UIFlatButton(text="(2,10)", width=200) 
        assignment3.on_click = lambda event : self.do_assignment(event,(2,10))

        self.assignments[(2,10)] = assignment3

        assignment34 = arcade.gui.UIFlatButton(text="(2,14)", width=200) 
        assignment34.on_click = lambda event : self.do_assignment(event,(2,14))

        self.assignments[(2,14)] = assignment34

        assignment4 = arcade.gui.UIFlatButton(text="(2,15)", width=200) 
        assignment4.on_click = lambda event : self.do_assignment(event,(2,15))

        self.assignments[(2,15)] = assignment4

        assignmentA = arcade.gui.UIFlatButton(text="(3,14)", width=200) 
        assignmentA.on_click = lambda event : self.do_assignment(event,(3,14))

        self.assignments[(3,14)] = assignmentA

        assignment5 = arcade.gui.UIFlatButton(text="(4,8)", width=200) 
        assignment5.on_click = lambda event : self.do_assignment(event,(4,8))

        self.assignments[(4,8)] = assignment5

        assignment45 = arcade.gui.UIFlatButton(text="(4,13)", width=200) 
        assignment45.on_click = lambda event : self.do_assignment(event,(4,13))

        self.assignments[(4,13)] = assignment45

        self.create_message("Welcome to your first day at BCA!\nYou should probably get some sleep for your first day!")


        
        
        
    def make_stats(self,event):
        def bar_construction(game):
            ''' Creates the stats view shown in the menus upon clicking the menu button'''
            # one big bar for the full metre, # one small bar showing magnititude
            
            # collect the mag bars - access by index reference in self.mag_bars
            
            for i in range(len(self.stats)):
                stat_rect = Rect(460,10,SCREEN_WIDTH/2, (3+i)*SCREEN_HEIGHT/9 - 25, arcade.color.BLACK)
                self.stats_rects.append(stat_rect)
                self.rectangle_appear(stat_rect)

                # currently unfinished
                
                # todo - add text labels under or to the side of bars to tell you percentage of bar filled?

                # actual stats magnitude bar - only length altered (or width of the rectangle)
                mag_bar = Rect(self.stats[STAT_NAMES[i]] * 460 / 100, 10, SCREEN_WIDTH/2 - (100 - self.stats[STAT_NAMES[i]])*4.6/2, (3+i)*SCREEN_HEIGHT/9 -25, arcade.color.CADMIUM_GREEN)
                self.stats_rects.append(mag_bar)
                self.rectangle_appear(mag_bar)

            self.grade_label = arcade.gui.UITextArea(text=STAT_NAMES[0] + f": {int(self.game.player.stats[STAT_NAMES[0]])}%", x = SCREEN_WIDTH/4, y = 80*1 + 105,
                                        width=200,
                                        height=20,
                                        font_size=10,
                                        font_name="Kenney Future")
            self.sleep_label = arcade.gui.UITextArea(text=STAT_NAMES[1] + f": {int(self.game.player.stats[STAT_NAMES[1]])}%", x = SCREEN_WIDTH/4, y = 65*2+15 +105,
                                            width=200,
                                            height=20,
                                            font_size=10,
                                            font_name="Kenney Future")
            self.happiness_label = arcade.gui.UITextArea(text=STAT_NAMES[2] + f": {int(self.game.player.stats[STAT_NAMES[2]])}%", x = SCREEN_WIDTH/4, y = 65*3+15 +105,
                                            width=200,
                                            height=20,
                                            font_size=10,
                                            font_name="Kenney Future")
            self.work_ethic_label = arcade.gui.UITextArea(text=STAT_NAMES[3] + f": {int(self.game.player.stats[STAT_NAMES[3]])}%", x = SCREEN_WIDTH/4, y = 65*4+15 +105,
                                            width=200,
                                            height=20,
                                            font_size=10,
                                            font_name="Kenney Future")
            self.fun_label = arcade.gui.UITextArea(text=STAT_NAMES[4] + f": {int(self.game.player.stats[STAT_NAMES[4]])}%", x = SCREEN_WIDTH/4, y = 65*5+15 +105,
                                            width=200,
                                            height=20,
                                            font_size=10,
                                            font_name="Kenney Future")
            self.manager.add(self.grade_label)
            self.manager.add(self.sleep_label)
            self.manager.add(self.happiness_label)
            self.manager.add(self.work_ethic_label)
            self.manager.add(self.fun_label)
            self.manager.add(self.stable) # STATS label

            for slabel in [self.grade_label, self.sleep_label, self.happiness_label, self.work_ethic_label, self.fun_label, self.stable]:
                self.stats_labels.append(slabel)
                self.labels.append(slabel)

        def ok_button_quit(event): 
            # remove rectangle from list that shows rectangles
            
            for rect in self.stats_rects: # self.stats_rects = list of the ui created by the stats button
                self.rect_list.remove(rect)
            self.stats_rects = []
            for label in self.stats_labels:
                self.labels.remove(label)
                self.manager.remove(label)
            self.stats_labels = []
            #self.ok_box.remove(self.okButton)
            self.stats_open = False
            


            
            
        if self.stats_open:
            ok_button_quit(event)
        else:
            if self.act_open:
                self.make_act(event)
            if self.assign_open:
                self.make_assign(event)
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
            
            bar_construction(self.game)
            # self.stats[STAT_NAMES[random.randrange(5)]] -= 20
            # self.game.player.cap()
        
    


    # This just updates the screen. Not sure why, and not sure I care. Just yet.
    def on_update(self, delta_time):
        # Move the rectangle
        
        # if self.isGoing:
        #     arcade.set_background_color((self.color[0],self.color[1],self.color[2]))
        #     if self.color[self.last_max] > 50:
        #         self.color[self.last_max] -=2
        #     if self.color[((self.last_max+1) % 3)] <200:
        #         self.color[((self.last_max+1) % 3)] += 2
        #     else:
        #         self.last_max +=1
        #         self.last_max %=3
        # if len(self.top_list):
        #     print(self.top_list)
        if self.last_time > self.game.time:
            self.game.day += 1
        self.last_time = self.game.time
     
        self.output = f"{self.game.time:02d}:00"



        

        
       
        
    def color_nonsense(self,event):
        self.isGoing = 1 - self.isGoing
        print(f"color: {self.color}")
        self.stats[STAT_NAMES[random.randint(0,4)]] -= 10
        self.stats[STAT_NAMES[random.randint(0,4)]] += 10
                # self.game.player.cap()
        self.game.time_passes()
    
    def make_act(self,event):
        '''
        self.game.player.do_work()
        self.time_passes(event)
        print("doing work")
        '''
        def act_quit(event):
            for rect in self.act_rects: # self.stats_rects = list of the ui created by the stats button
                self.rect_list.remove(rect)
            self.act_rects = []
            for label in self.act_labels:
                self.labels.remove(label)
            self.act_labels = []
            #self.ok_box.remove(self.okButton)
            self.act_open = False
            self.manager.remove(self.able)
            for button in self.act_buttons:
                self.act_buttons_box.remove(button)
            self.act_buttons = []

        def add_buttons(event):
            if self.game.scene == 0:
                # Bedroom?
                self.act_buttons = [self.sleep_button,self.homework_button,self.games_button,  self.text_friends_button]
            elif self.game.scene == 0.5:
                #start of day (this is where things start becoming a mess)
                self.act_buttons = [self.go_to_school_button1,self.go_to_school_button2, self.go_to_school_button3]
                
            elif self.game.scene == 1:
                # In school
                if self.game.teacher_present:
                    # Pay attention, stare out the window, classwork, (occasionally) test
                    self.act_buttons = [self.ask_for_help_button,self.schoolwork_button, self.games_button, self.chat_button]
                elif not self.game.teacher_present:
                    # Study, school work, play games, skip class
                    self.act_buttons = [self.study_button,self.schoolwork_button, self.games_button, self.chat_button]
            

        if self.act_open:
            act_quit(event)
        else:
            if self.stats_open:
                self.make_stats(event)
            if self.assign_open:
                self.make_assign(event)
            self.act_rect_main = Rect(500,400,SCREEN_WIDTH/2,SCREEN_HEIGHT/2, arcade.color.RED_DEVIL)
            self.act_rects.append(self.act_rect_main)
            self.rectangle_appear(self.act_rect_main)
            #self.okButton = arcade.gui.UIFlatButton(text = " X ", width = 50)
            
            #self.okButton.on_click =  ok_button_quit 
            #self.ok_box.add(self.okButton)
            self.act_open = True
            
            self.able = arcade.gui.UITextArea(text=" ACT ", x = SCREEN_WIDTH/2-20, y = 500,
                                            width=450,
                                            height=40,
                                            font_size=20,
                                            font_name="Kenney Future")
            self.manager.add(self.able)
            add_buttons(event)
            for i in range(len(self.act_buttons)):
                self.act_buttons[i] = self.act_buttons[i].with_space_around(bottom=10)
                self.act_buttons_box.add(self.act_buttons[i])
            
    def act(self, event, key):
        if key == 0:
            self.time_slept = (6-self.game.time)%24
            self.game.player.sleep((6-self.game.time)%24)
            self.isSleeping = 1
            
        elif key == 1:
            self.game.player.do_work()
        elif key == 2:
            self.game.player.play_games()
        elif key == 3:
            self.game.player.text_friends()
        elif key == 4:
            self.game.scene = 1
        


        if key != 0:
            self.game.time_passes()
        if key!= 5:
            self.make_act(event)
        else:
            self.make_assign(event)
        self.game.player.cap()
       
    def make_assign(self,event):
        '''
        self.game.player.do_work()
        self.time_passes(event)
        print("doing work")
        '''
        def assign_quit(event):
            for rect in self.assign_rects: # self.stats_rects = list of the ui created by the stats button
                self.rect_list.remove(rect)
            self.assign_rects = []
            for label in self.assign_labels:
                self.labels.remove(label)
                self.manager.remove(label)
            self.assign_labels = []
            #self.ok_box.remove(self.okButton)
            self.assign_open = False
            self.manager.remove(self.gnable)
            for button in self.assign_buttons:
                self.assign_buttons_box.remove(button)
            self.assign_buttons = []
            

        if self.assign_open:
            assign_quit(event)
        else:
            if self.stats_open:
                self.make_stats(event)
            if self.act_open:
                self.make_act(event)
            self.assign_rect_main = Rect(500,400,SCREEN_WIDTH/2,SCREEN_HEIGHT/2, arcade.color.GENERIC_VIRIDIAN)
            self.assign_rects.append(self.assign_rect_main)
            self.rectangle_appear(self.assign_rect_main)
            #self.okButton = arcade.gui.UIFlatButton(text = " X ", width = 50)
            
            #self.okButton.on_click =  ok_button_quit 
            #self.ok_box.add(self.okButton)
            self.assign_open = True
            
            self.gnable = arcade.gui.UITextArea(text=" ASSIGNMENTS ", x = SCREEN_WIDTH/3+10, y = 500,
                                            width=450,
                                            height=40,
                                            font_size=20,
                                            font_name="Kenney Future")
            
            
            
            self.manager.add(self.gnable)
            for i in range(len(self.game.cur_assignments)):
                assignment = self.game.cur_assignments[i]
                self.assign_buttons.append(self.assignments[assignment])
                size = len(self.game.cur_assignments)
                assignmentlabel = arcade.gui.UITextArea(text= f"{assignment} is due {assignment[0]}:00", x = SCREEN_WIDTH*5/9, y = SCREEN_HEIGHT/2 + (i - size/2)*-100,
                                            width=200,
                                            height=20,
                                            font_size=10,
                                            font_name="Kenney Future")
            
                self.assign_labels.append(assignmentlabel)
                self.labels.append(assignmentlabel)
                self.manager.add(assignmentlabel)
                

            for i in range(len(self.assign_buttons)):
                self.assign_buttons[i] = self.assign_buttons[i].with_space_around(bottom=10)
                self.assign_buttons_box.add(self.assign_buttons[i])

    def do_assignment(self,event,assignment):
        self.assignments_done[assignment] = 1
        self.game.cur_assignments.remove(assignment)
        self.act(event,5)

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()
        # Draw the rectangle
        if self.game.teacher_present:
            self.teacher.draw()
        self.lower_frame.draw()
        
        for n in self.rect_list:
            n.draw()
        
        self.manager.draw()
         # Output the timer text.
        self.time_frame.draw()
        arcade.draw_text(self.output,
                         30, SCREEN_HEIGHT-20,
                         arcade.color.WHITE, 20,
                         anchor_x="left",
                         anchor_y="top")
        arcade.set_background_color(TIME_COLORS[self.game.time%3])
        if self.isSleeping:
            if self.sleep_state < 300:
                Rect(4000,4000, SCREEN_WIDTH, SCREEN_HEIGHT, (0,0,0,self.sleep_state)).draw()
            elif self.sleep_state < 600:
                self.game.time = 6
                self.game.scene = 0.5
                Rect(4000,4000, SCREEN_WIDTH, SCREEN_HEIGHT, (0,0,0,600-self.sleep_state)).draw()        
            else:
                self.isSleeping = 0
                self.sleep_state = 0
                self.create_message(f"You slept {self.time_slept} hours! It is now {DAYS[self.game.day]}!\nSleep quality at {self.game.player.stats['sleep']}%")
            self.sleep_state += 5

    def rectangle_appear(self, rectangle):
        # print("Make rectangle")
        
        self.rect_list.append(rectangle)

    def toptangle_appear(self, rectangle):
        # print("Make rectangle")
        
        self.top_list.append(rectangle)

    def create_message(self, message, button = "Ok"):
        message_box = arcade.gui.UIMessageBox(
        width=400,
        height=200,
        message_text=message,
        buttons=[button])
        self.manager.add(message_box)
        


       

        