class Game():
    def __init__(self, name):
        self.player = Player(name)
        self.time = 20
        self.day = 0
        self.scene = 0
        self.event_list = [[0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0], 
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 2,1,0,0,2,0, 0,0,0,0,0,0],
                           [0,0,0,4,0,0, 0,0,1,0,0,2, 0,1,0,0,2,0, 0,0,0,0,0,0], 
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 0,1,0,0,2,0, 0,0,0,0,0,0],
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 0,1,0,0,2,0, 0,0,0,0,0,0], 
                           [0,0,0,0,0,0, 0,0,1,0,0,2, 0,1,0,0,2,0, 0,0,0,0,0,0],
                           [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0]]

                    # Lockers, CS, Latin, WH, Lockers, Lockers, ELA, Bio, Math
        self.assignment_list = [(1,9),(1,15),(2,10),(2,14),(2,15),(3,13),(4,8),(4,14)]
        self.test_list = [(1,15),(2,10),(5,9),(5,15)]

        # 1, 15 is for demonstration
        self.cur_assignments = []
        
                        
        self.teacher_present = False
        

    def time_passes(self):
        self.time += 1
        self.time %= 24
        print(self.day,self.time)
        
        if (self.day,self.time) in self.assignment_list:
            self.cur_assignments.append((self.day,self.time))
            

        if (self.day-2,self.time-1) in self.cur_assignments:
            
            self.cur_assignments.remove((self.day-2,self.time-1))
            self.player.grades.append(50)
        
        if self.event_list[self.day][self.time] == 1:
            self.teacher_appear()
        elif self.event_list[self.day][self.time] == 2:
            self.teacher_leave()
        elif self.event_list[self.day][self.time] == 3:
            self.scene=0
        self.player.time_passes()
        print(self.player.grades)

    def teacher_appear(self):
        self.teacher_present = True
    def teacher_leave(self):
        self.teacher_present = False
    def do_assignment(self,assignment):
        day_due = assignment[0]+1
        time_due = assignment[1];
        if self.day*24+self.time <= day_due*24 + time_due:
            self.player.grades.append(100)
        else:
            
            if day_due*24 + time_due - (self.day*24+self.time) < 5:
                self.player.grades.append(90)
            elif day_due*24 + time_due - (self.day*24+self.time) < 10:
                self.player.grades.append(80)
            elif day_due*24 + time_due - (self.day*24+self.time) < 15:
                self.player.grades.append(75)
            elif day_due*24 + time_due - (self.day*24+self.time) < 20:
                self.player.grades.append(70)
            else:
                self.player.grades.append(65)
    


class Player():
    def __init__(self, name):
        self.stats = {}
        self.stats["grade"] = 100
        self.stats["sleep"] = 100
        self.stats["happiness"] = 100
        self.stats["work_ethic"] = 100
        self.stats["fun"] = 100
        self.grades = [80]
        
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
        test_grade = self.stats["work_ethic"]
        test_grade += int((10 - self.stats["work_ethic"]/10)*7)
        self.cap()
        if self.stats["sleep"] < 80:
            test_grade -= 80 - self.stats["sleep"]
        self.grades.append(test_grade)
        self.grades.append(test_grade)
        if test_grade == 100:
            return "WOW! You got a 100! Stellar job!"
        elif test_grade >= 90:
            return f"Great work! You got a {test_grade}!"
        elif test_grade >= 80:
            return f"Nice! You got a {test_grade}!"
        else:
            return f"Uh oh! You got a {test_grade}! Might want to study a bit more next time!"
        
    
    def time_passes(self):
        self.stats["sleep"] -= 3
        self.stats["grade"] = sum(self.grades)/len(self.grades)
        self.cap()
        self.stats["happiness"] = ((self.stats["grade"]+self.stats["fun"])/2)
        self.cap()


    def cap(self):
        self.stats["grade"] = self.oor(self.stats["grade"],0,100)
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