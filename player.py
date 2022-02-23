class Game():
    def __init__(self, name):
        self.player = Player(name)
        self.time = 18
        self.scene = 0
        self.event_list = [0,0,0,0,0,0, 0,0,1,0,2,0, 0,1,0,2,0,3, 0,0,0,0,0,0]
                        
        self.teacher_present = False
        

    def time_passes(self):
        self.time += 1
        self.time %= 24
        if self.event_list[self.time] == 1:
            self.teacher_appear()
        elif self.event_list[self.time] == 2:
            self.teacher_leave()
        elif self.event_list[self.time] == 3:
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
        self.stats["sleep"] -= 5
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