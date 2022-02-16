class Game():
    def __init__(self, name):
        self.player = Player(name)
        self.time = 0
        self.scene = 0
        self.event_list = [0,0,1,0,0,2]
        self.teacher_present = False
        

    def time_passes(self):
        self.time += 1
        if self.event_list[self.time%6] == 1:
            self.teacher_appear()
        elif self.event_list[self.time%6] == 2:
            self.teacher_leave()
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
        self.stats["sleep"] = time*12

    def do_work(self):
        self.stats["work_ethic"] += 10
        self.stats["fun"] -= 5
    
    def take_test(self):
        self.cap()
        self.stats["grade"] = int(self.stats["work_ethic"]+self.stats["grade"])/2
    
    def play_games(self):
        self.stats["fun"] += 10
        self.stats["work_ethic"] -= 5
    
    def time_passes(self):
        self.cap()
        self.stats["grade"] -= int(100-self.stats["work_ethic"])/3
        self.cap()
        self.stats["happiness"] = int((self.stats["sleep"]+self.stats["grade"])/2)
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