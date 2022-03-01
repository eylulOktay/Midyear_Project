class Game():
    def __init__(self, name):
        self.player = Player(name)
        self.time = 18
        self.day = 0
        self.scene = 0
        self.event_list = [[0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0], 
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 0,1,0,0,2,3, 0,0,0,0,0,0],
                           [0,0,0,4,0,0, 0,0,1,0,0,2, 0,1,0,0,2,3, 0,0,0,0,0,0], 
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 0,1,0,0,2,3, 0,0,0,0,0,0],
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 0,1,0,0,2,3, 0,0,0,0,0,0], 
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 0,1,0,0,2,3, 0,0,0,0,0,0],
                           [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0]]
        self.assignment_list = [(0,20),(1,9),(1,15),(2,10),(2,14),(2,15),(3,14),(4,8),(4,13)]
        self.test_list = [(3,10),(5,9),(5,15)]
        self.cur_assignments = []
                        
        self.teacher_present = False
        

    def time_passes(self):
        self.time += 1
        self.time %= 24
        print(self.day,self.time)
        
        if (self.day,self.time) in self.assignment_list:
            self.cur_assignments.append((self.day,self.time))
        
        if self.event_list[self.day][self.time] == 1:
            self.teacher_appear()
        elif self.event_list[self.day][self.time] == 2:
            self.teacher_leave()
        elif self.event_list[self.day][self.time] == 3:
            self.scene=0
        self.player.time_passes()

    def teacher_appear(self):
        self.teacher_present = True
    def teacher_leave(self):
        self.teacher_present = False
    


class Player():
    def __init__(self, name):
        self.stats = {}
        self.stats["grade"] = 100
        self.stats["sleep"] = 100
        self.stats["happiness"] = 100
        self.stats["work_ethic"] = 100
        self.stats["fun"] = 100
        
        self.name = name.strip().capitalize()
    
    def sleep(self, time):
        self.stats["sleep"] += time*12
        

    def do_work(self):
        self.stats["work_ethic"] += 10
        self.stats["fun"] -= 7
    
    def play_games(self):
        self.stats["fun"] += 10
        self.stats["work_ethic"] -= 7

    def text_friends(self):
        self.stats["fun"] += 18
        self.stats["work_ethic"] -= 12

    def take_test(self):
        self.cap()
        self.stats["grade"] = (self.stats["work_ethic"]+self.stats["grade"])/2
    
    def time_passes(self):
        self.stats["sleep"] -= 3
        self.cap()
        self.stats["grade"] -= ((90-self.stats["work_ethic"])+abs((90-self.stats["work_ethic"]))+(90-self.stats["sleep"])+abs((90-self.stats["sleep"])))/12
        self.cap()
        self.stats["happiness"] = ((self.stats["grade"]+self.stats["fun"])/2)
        self.cap()


    def cap(self):
        self.stats["grade"] = self.oor(self.stats["grade"],60,100)
        self.stats["fun"] = self.oor(self.stats["fun"],0,100)
        self.stats["sleep"] = self.oor(self.stats["sleep"],0,100)
        self.stats["work_ethic"] = self.oor(self.stats["work_ethic"],0,100)
        self.stats["happiness"] = self.oor(self.stats["happiness"],0,100)
    
    def oor(self, var, min, max):
        if var > max:
            var = max
        elif var < min:
            var = min
        return var