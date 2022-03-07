from sys import builtin_module_names
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
TIME_COLORS = [(20, 23, 45),(15, 20, 35),(20, 23, 45),(20, 23, 45),(25, 27, 65),(30, 35, 75),(32,35, 90),
                arcade.color.RUST,arcade.color.RUST,arcade.color.RUST,arcade.color.RUST,
                arcade.color.RUST,arcade.color.RUST,arcade.color.RUST,arcade.color.RUST,
                arcade.color.RUST,arcade.color.RUST,(40, 60, 115),(40, 50, 105),(35, 40, 95),(32, 35, 90),(25, 35, 75),(25, 27, 65),(20, 23, 45)]
BACKGROUND_IMAGES = ["images/lockers.png","images/compsci.png","images/latin.png","images/history.png","images/lunch.png","images/lockers.png","images/ela.png","images/biology.png","images/math.png","images/lockers.png"]
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
        self.AHHHHH = 0
        self.notFirst = False
        self.notFirs = False
        self.stats_open = False
        self.isSleeping = False
        self.isHoming = False
        self.isCloning = False
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
        self.teacher_before = False
        self.assignment_before = False
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
        self.lower_frame = Rect(SCREEN_WIDTH, SCREEN_HEIGHT/4, SCREEN_WIDTH/2, SCREEN_HEIGHT/8, arcade.color.MSU_GREEN)
        self.time_frame = Rect(125, 50, 75, SCREEN_HEIGHT-35, arcade.color.GOLDEN_BROWN)
        self.teacher = Rect(SCREEN_WIDTH/5, SCREEN_HEIGHT/2, SCREEN_WIDTH/2,SCREEN_HEIGHT/2,arcade.color.RED_DEVIL)
        
        self.stats_button = arcade.gui.UIFlatButton(text="Stats",
                                               width=150)
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

        self.go_home_button1 = arcade.gui.UIFlatButton(text="Go Home", width=200) 
        self.go_home_button1.on_click = lambda event : self.act(event,4.5)

        self.go_home_button2 = arcade.gui.UIFlatButton(text="You Don't Have A Choice", width=200) 
        self.go_home_button2.on_click = lambda event : self.act(event,4.5)

        self.go_home_button3 = arcade.gui.UIFlatButton(text="Seriously, Just Go", width=200) 
        self.go_home_button3.on_click = lambda event : self.act(event,4.5)

        self.schoolwork_button = arcade.gui.UIFlatButton(text="Schoolwork", width=200) 
        self.schoolwork_button.on_click = lambda event : self.act(event,1)

        self.chat_button = arcade.gui.UIFlatButton(text="Chat With Friends", width=200) 
        self.chat_button.on_click = lambda event : self.act(event,3)

        self.study_button = arcade.gui.UIFlatButton(text="Study", width=200) 
        self.study_button.on_click = lambda event : self.act(event,1)

        self.ask_for_help_button = arcade.gui.UIFlatButton(text="Ask For Help", width=200) 
        self.ask_for_help_button.on_click = lambda event : self.act(event,1)

        self.test1_button = arcade.gui.UIFlatButton(text="Uh Oh!", width=200) 
        self.test1_button.on_click = lambda event : self.act(event,6)

        self.test2_button = arcade.gui.UIFlatButton(text="Time For A Test!", width=200) 
        self.test2_button.on_click = lambda event : self.act(event,6)

        self.test3_button = arcade.gui.UIFlatButton(text="Good Luck!", width=200) 
        self.test3_button.on_click = lambda event : self.act(event,6)

        self.time1_button = arcade.gui.UIFlatButton(text="Time's up!", width=200) 
        self.time1_button.on_click = lambda event : self.act(event,7)

        self.time2_button = arcade.gui.UIFlatButton(text="Go to your next class!", width=200) 
        self.time2_button.on_click = lambda event : self.act(event,7)

        self.time3_button = arcade.gui.UIFlatButton(text="NOW", width=200) 
        self.time3_button.on_click = lambda event : self.act(event,7)

        self.assignments = {}
        self.assignments_done = {}

        # Tried to make this a for loop, couldn't get it to work and I am tired
        # self.assignment_list = [(1,9),(1,15),(2,10),(2,14),(2,15),(3,14),(4,8),(4,13)]
        
        assignment0 = arcade.gui.UIFlatButton(text="(0,20)", width=200) 
        assignment0.on_click = lambda event : self.do_assignment(event,(0,20))

        self.assignments[(0,20)] = assignment0
        
        assignment05 = arcade.gui.UIFlatButton(text="Interest Calculator", width=200) 
        assignment05.on_click = lambda event : self.do_assignment(event,(1,8))

        self.assignments[(1,8)] = assignment05

        assignment075 = arcade.gui.UIFlatButton(text="Pearson Assigment", width=200) 
        assignment075.on_click = lambda event : self.do_assignment(event,(1,14))

        self.assignments[(1,14)] = assignment075

        assignment1 = arcade.gui.UIFlatButton(text="Memorizing Conjugations", width=200) 
        assignment1.on_click = lambda event : self.do_assignment(event,(1,9))

        self.assignments[(1,9)] = assignment1

        assignment2 = arcade.gui.UIFlatButton(text="Factoring Quadratics", width=200) 
        assignment2.on_click = lambda event : self.do_assignment(event,(1,15))

        self.assignments[(1,15)] = assignment2

        assignment3 = arcade.gui.UIFlatButton(text="Historical Investigation", width=200) 
        assignment3.on_click = lambda event : self.do_assignment(event,(2,10))

        self.assignments[(2,10)] = assignment3

        assignment34 = arcade.gui.UIFlatButton(text="Pearson Assigment", width=200) 
        assignment34.on_click = lambda event : self.do_assignment(event,(2,14))

        self.assignments[(2,14)] = assignment34

        assignment4 = arcade.gui.UIFlatButton(text="Factoring More Quadratics", width=200) 
        assignment4.on_click = lambda event : self.do_assignment(event,(2,15))

        self.assignments[(2,15)] = assignment4

        assignmentA = arcade.gui.UIFlatButton(text="Analyzing A Poem", width=200) 
        assignmentA.on_click = lambda event : self.do_assignment(event,(3,13))

        self.assignments[(3,14)] = assignmentA

        assignment5 = arcade.gui.UIFlatButton(text="Interest Calculator", width=200) 
        assignment5.on_click = lambda event : self.do_assignment(event,(4,8))

        self.assignments[(4,8)] = assignment5

        assignment45 = arcade.gui.UIFlatButton(text="Making A Map", width=200) 
        assignment45.on_click = lambda event : self.do_assignment(event,(4,14))

        self.assignments[(4,13)] = assignment45

        self.create_message("Welcome to your first day at ABC!\nYou should probably get some sleep for your first day!")


        
        
        
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
            self.stats_rect_main2 = Rect(200,40,SCREEN_WIDTH/2,SCREEN_HEIGHT*7/8, arcade.color.PURPLE_HEART)
            self.stats_rects.append(self.stats_rect_main)
            self.rectangle_appear(self.stats_rect_main)
            self.stats_rects.append(self.stats_rect_main2)
            self.rectangle_appear(self.stats_rect_main2)
            #self.okButton = arcade.gui.UIFlatButton(text = " X ", width = 50)
            
            #self.okButton.on_click =  ok_button_quit 
            #self.ok_box.add(self.okButton)
            self.stats_open = True
            
            self.stable = arcade.gui.UITextArea(text="STATS", x = 350, y = 500,
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
        if self.last_time == 5 and self.game.time==6:
            self.game.scene=0.5
            self.game.continues = 1
        if self.last_time == 15 and self.game.time==16:
            self.game.scene=1.5
        self.last_time = self.game.time

     
        self.output = f"{(self.game.time-1)%12+1:02d}:00 "
        if self.game.time >= 12:
            self.output += "PM"
        else:
            self.output += "AM"



        

        
       
        
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
                self.act_buttons = [self.sleep_button,self.study_button,self.games_button,  self.text_friends_button]
            elif self.game.scene == 0.5:
                #start of day (this is where things start becoming a mess)
                self.act_buttons = [self.go_to_school_button1,self.go_to_school_button2, self.go_to_school_button3]
                
            elif self.game.scene == 1:
                # In school
                if self.game.continues:
                    if self.game.teacher_present:
                        # Pay attention, stare out the window, classwork, (occasionally) test
                        
                        if ((self.game.day,self.game.time) in self.game.test_list):
                            self.act_buttons = [self.test1_button,self.test2_button, self.test3_button]
                        else:
                            self.act_buttons = [self.ask_for_help_button,self.study_button, self.games_button, self.chat_button]
                    elif not self.game.teacher_present:
                        # Study, school work, play games, skip class
                        self.act_buttons = [self.study_button, self.games_button, self.chat_button]
                else:
                    self.act_buttons = [self.time1_button,self.time2_button, self.time3_button]
            elif self.game.scene == 1.5:
                self.act_buttons = [self.go_home_button1,self.go_home_button2, self.go_home_button3]

            
            

        if self.act_open:
            act_quit(event)
        else:
            if self.stats_open:
                self.make_stats(event)
            if self.assign_open:
                self.make_assign(event)
            self.act_rect_main = Rect(500,400,SCREEN_WIDTH/2,SCREEN_HEIGHT/2, arcade.color.RED_DEVIL)
            self.act_rect_main2 = Rect(200,40,SCREEN_WIDTH/2,SCREEN_HEIGHT*7/8, arcade.color.RED_DEVIL)
            self.act_rects.append(self.act_rect_main)
            self.rectangle_appear(self.act_rect_main)
            self.act_rects.append(self.act_rect_main2)
            self.rectangle_appear(self.act_rect_main2)
            #self.okButton = arcade.gui.UIFlatButton(text = " X ", width = 50)
            
            #self.okButton.on_click =  ok_button_quit 
            #self.ok_box.add(self.okButton)
            self.act_open = True
            
            self.able = arcade.gui.UITextArea(text=" ACT ", x = SCREEN_WIDTH/2-40, y = 500,
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
            
            self.AHHHHH = 1
        elif key == 2:
            self.game.player.play_games()
            self.AHHHHH = 1
            
        elif key == 3:
            self.game.player.text_friends()
            self.AHHHHH = 1

        elif key == 4:
            self.isCloning = 1
        elif key == 4.5:
            self.isHoming = 1
        elif key == 5:
            self.AHHHHH = 1
        elif key == 6:
            result = self.game.player.take_test()
            self.create_message(result)
            self.AHHHHH = 1
        
           
        


        if key not in [0,4,4.5] and not (self.game.scene == 1 and self.game.continues):
            self.game.time_passes()
        
        if self.AHHHHH and self.game.scene == 1:
            self.game.continues = 0
        else:
            self.game.continues = 1
        self.AHHHHH = 0
        
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
            self.assign_rect_main2 = Rect(250,40,SCREEN_WIDTH/2,SCREEN_HEIGHT*7/8, arcade.color.GENERIC_VIRIDIAN)
            self.assign_rects.append(self.assign_rect_main)
            self.rectangle_appear(self.assign_rect_main)
            self.assign_rects.append(self.assign_rect_main2)
            self.rectangle_appear(self.assign_rect_main2)
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
            if ((self.game.day,self.game.time) in self.game.test_list):
                go_school_label = arcade.gui.UITextArea(text= f"You have to take a test now!", x = SCREEN_WIDTH/4, y = SCREEN_HEIGHT/2 + 50,
                                                width=500,
                                                height=30,
                                                font_size=15,
                                                font_name="Kenney Future")
                self.assign_labels.append(go_school_label)
                self.labels.append(go_school_label)
                self.manager.add(go_school_label)
            elif self.game.scene == 0.5:
                go_school_label = arcade.gui.UITextArea(text= f"You have to go to school now!", x = SCREEN_WIDTH/4, y = SCREEN_HEIGHT/2 + 50,
                                                width=500,
                                                height=30,
                                                font_size=15,
                                                font_name="Kenney Future")
                self.assign_labels.append(go_school_label)
                self.labels.append(go_school_label)
                self.manager.add(go_school_label)
            elif not self.game.continues:
                go_school_label = arcade.gui.UITextArea(text= f"You have to move classes now!", x = SCREEN_WIDTH/4, y = SCREEN_HEIGHT/2 + 50,
                                                width=500,
                                                height=30,
                                                font_size=15,
                                                font_name="Kenney Future")
                self.assign_labels.append(go_school_label)
                self.labels.append(go_school_label)
                self.manager.add(go_school_label)
            elif self.game.scene == 1.5:
                go_school_label = arcade.gui.UITextArea(text= f"You have to go to home now!", x = SCREEN_WIDTH/4, y = SCREEN_HEIGHT/2 + 50,
                                                width=500,
                                                height=30,
                                                font_size=15,
                                                font_name="Kenney Future")
                self.assign_labels.append(go_school_label)
                self.labels.append(go_school_label)
                self.manager.add(go_school_label)
            else:
                size = len(self.game.cur_assignments)  
                if size:
                    for i in range(len(self.game.cur_assignments)):
                        assignment = self.game.cur_assignments[i]
                        self.assign_buttons.append(self.assignments[assignment])
                        
                        assignmentlabel = arcade.gui.UITextArea(text= f"{self.assignments[assignment].text} \nis due {DAYS[(assignment[0]+1)%7]} at {assignment[1]}:00", x = SCREEN_WIDTH*1/2, y = SCREEN_HEIGHT/3 + 45 + (i - size/2)*-75+7*size,
                                                    width=300,
                                                    height=30,
                                                    font_size=10,
                                                    font_name="Kenney Future")
                    
                        self.assign_labels.append(assignmentlabel)
                        self.labels.append(assignmentlabel)
                        self.manager.add(assignmentlabel)
                else:
                    go_school_label = arcade.gui.UITextArea(text= f"You have no assignments! Yay!", x = SCREEN_WIDTH/4, y = SCREEN_HEIGHT/2 + 50,
                                                width=500,
                                                height=30,
                                                font_size=15,
                                                font_name="Kenney Future")
                    self.assign_labels.append(go_school_label)
                    self.labels.append(go_school_label)
                    self.manager.add(go_school_label)

                    

            for i in range(len(self.assign_buttons)):
                self.assign_buttons[i] = self.assign_buttons[i].with_space_around(bottom=10)
                self.assign_buttons_box.add(self.assign_buttons[i])

    def do_assignment(self,event,assignment):
        self.assignments_done[assignment] = 1
        self.game.cur_assignments.remove(assignment)
        self.game.do_assignment(assignment)
        self.act(event,5)

    def on_draw(self):
        """ Render the screen. """

        # Clear screen
        self.clear()
        arcade.set_background_color(TIME_COLORS[self.game.time])
        if self.game.scene == 0 or self.game.scene == 0.5:
            self.background = arcade.load_texture("images/bedroom.png")
        else:
            self.background = arcade.load_texture(BACKGROUND_IMAGES[self.game.time-7])

        arcade.draw_texture_rectangle(400, 300, 800,
                                      600, self.background)
        # Draw the rectangle
        if self.game.teacher_present:
            #self.teacher.draw()
            if not self.teacher_before:
                self.teacher_before = True
                self.create_message(f"Here is a teacher! They will give you assignments occassionally, sometimes without telling you!\nKeep checking your assignments so you don't miss any!")
        self.lower_frame.draw()
        
        for n in self.rect_list:
            n.draw()
        
        self.manager.draw()
         # Output the timer text.
        self.time_frame.draw()
        arcade.draw_text(self.output,
                         30, SCREEN_HEIGHT-20,
                         arcade.color.WHITE, 15,
                         anchor_x="left",
                         anchor_y="top")
        

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
        if self.isHoming:
            if self.sleep_state < 300:
                Rect(4000,4000, SCREEN_WIDTH, SCREEN_HEIGHT, (0,0,0,self.sleep_state)).draw()
            elif self.sleep_state < 600:
                self.game.time = 17
                self.game.scene = 0
                Rect(4000,4000, SCREEN_WIDTH, SCREEN_HEIGHT, (0,0,0,600-self.sleep_state)).draw() 
                if not self.notFirs:
                    self.create_message(f"Congrats! You've made it through your first day at ABC!\n")
                    self.notFirs = True          
            else:
                self.isHoming = 0
                self.sleep_state = 0
                
            self.sleep_state += 5
        if self.isCloning:
            if self.sleep_state < 300:
                Rect(4000,4000, SCREEN_WIDTH, SCREEN_HEIGHT, (0,0,0,self.sleep_state)).draw()
            elif self.sleep_state < 600:
                self.game.time = 7
                self.game.scene = 1
                Rect(4000,4000, SCREEN_WIDTH, SCREEN_HEIGHT, (0,0,0,600-self.sleep_state)).draw()
                if not self.notFirst:
                    self.create_message(f"Welcome to ABC! Classes will start soon!\nEvery time you act or do an assignment, time will move forward an hour!\nMake sure to do the right things!")
                    self.notFirst = True        
            else:
                self.isCloning = 0
                self.sleep_state = 0
                
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
        

# class Teacher(arcade.AnimatedWalkingSprite):
#     """ teacher sprite for classroom """

#     def __init__(self, pos_x: int, pos_y: int) -> None:
#         super().__init__(center_x=pos_x, center_y=pos_y)

#         # Where are the player images stored?
#         appear_texture = "images/teacher.png"

#         # Load them all now
#         self.appear_texture = [
#             arcade.load_texture(texture) for texture in walking_texture_path
#         ]

#         self.walk_right_textures = [
#             arcade.load_texture(texture, mirrored=True)
#             for texture in walking_texture_path
#         ]

#         self.stand_left_textures = [
#             arcade.load_texture(standing_texture_path, mirrored=True)
#         ]
#         self.stand_right_textures = [
#             arcade.load_texture(standing_texture_path)
#         ]

#         # Set the enemy defaults
#         self.state = arcade.FACE_LEFT
#         self.change_x = -PLAYER_MOVE_SPEED // 2

#         # Set the initial texture
#         self.texture = self.stand_left_textures[0]