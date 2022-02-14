class Game():
    def __init__(self, name):
        self.player = Player(name)
        self.time = 0
        self.scene = 1
        self.event_list = [0,0,1,0,0,2]
        self.teacher_present = False
        

    def time_passes(self):
        self.time += 1
        if self.event_list[self.time] == 1:
            self.teacher_appear()
        elif self.event_list[self.time] == 2:
            self.teacher_leave()
        self.student.time_passes()

    def teacher_appear(self):
        self.teacher_present = True
    def teacher_leave(self):
        self.teacher_present = False
    


class Player():
    def __init__(self, name):
        self.grade = 100
        self.sleep = 100
        self.happiness = 100
        self.work_ethic = 100
        self.fun = 100
        
        self.name = name.strip().capitalize()
    
    def sleep(self, time):
        self.sleep = time*12

    def do_work(self):
        self.work_ethic += 10
        self.fun -= 5
    
    def take_test(self):
        self.cap()
        self.grade = int(self.work_ethic+self.grade)/2
    
    def play_games(self):
        self.fun += 10
        self.work_ethic -= 5
    
    def time_passes(self):
        self.cap()
        self.grade -= int(100-self.work_ethic)/3
        self.cap()
        self.happiness = int((self.sleep+self.grade)/2)
        self.cap()


    def cap(self):
        self.grade = self.oor(self.grade,60,100)
        self.fun = self.oor(self.fun,0,100)
        self.sleep = self.oor(self.sleep,0,100)
        self.work_ethic = self.oor(self.work_ethic,0,100)
        self.happiness = self.oor(self.happiness,0,100)
    
    def oor(self, var, min, max):
        if var > max:
            var = max
        elif var < min:
            var = min
        return var