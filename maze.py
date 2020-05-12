# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:16:33 2019

@author: kotaro
"""

import random

class Digger:
    def __init__(self, x, y, field):
        self.point_list = [[x, y]]
        self.x = x
        self.y = y
        self.direction = 0
        field.field[y][x] = 0
        field.stop_list.append([x, y])
    
    def dig(self, field, value):
        if self.direction == 0:
            field.field[self.y-1][self.x] = value
            field.field[self.y-2][self.x] = value
            self.move(field)
        elif self.direction == 1:
            field.field[self.y][self.x+1] = value
            field.field[self.y][self.x+2] = value
            self.move(field)
        elif self.direction == 2:
            field.field[self.y+1][self.x] = value
            field.field[self.y+2][self.x] = value
            self.move(field)
        else:
            field.field[self.y][self.x-1] = value
            field.field[self.y][self.x-2] = value
            self.move(field)
    
    def move(self, field):
        if self.direction == 0:
            self.y -= 2
        elif self.direction == 1:
            self.x += 2
        elif self.direction == 2:
            self.y += 2
        else:
            self.x -= 2
        if not [self.x, self.y] in self.point_list:
            self.point_list.append([self.x, self.y])
    
    def look(self, field, step, direction):
        if direction == 0:
            return True if field.field[self.y-step][self.x] == 1 else False
        elif direction == 1:
            return True if field.field[self.y][self.x+step] == 1 else False
        elif direction == 2:
            return True if field.field[self.y+step][self.x] == 1 else False
        else:
            return True if field.field[self.y][self.x-step] == 1 else False
    
    def work(self, field):
        self.go_ahead(field)
        for i in range(((field.size - 1) // 2)**2):
            self.go_back(field)
    
    def go_ahead(self, field):
        self.direction = random.randrange(4)
        count = 0
        while count < 4:
            if self.look(field, 2, self.direction):
                self.dig(field, 0)
                self.direction = random.randrange(4)
                count = 0
            else:
                count += 1
                self.direction = (self.direction + 1) % 4
    
    def go_back(self, field):
        look_list = [self.look(field, 2, i) for i in range(4)]
        while not True in look_list:
            look_list = []
            look_list2 = [self.look(field, 1, i) for i in range(4)]
            if look_list2.count(False) == 1 and not [self.x, self.y] in field.stop_list:
                field.stop_list.append([self.x, self.y])
            a, b = 1, 0
            while look_list2[(self.direction+a-b)%4]:
                b += 1
            self.direction = (self.direction + a - b) % 4
            self.move(field)
            if len(self.point_list) == ((field.size - 1) // 2)**2:
                break
            for i in range(4):
                look_list.append(self.look(field, 2, i))
        self.go_ahead(field)


class Field:
    def __init__(self, size):
        self.field = []
        self.size = size
        self.stop_list = []
        self.start = []
        self.goal = []
        for i in range(self.size+2):
            if i == 0 or i == self.size+1:
                self.field.append([0 for j in range(self.size+2)])
            else:
                self.field.append([0 if j == 0 or j == self.size+1 else 1 for j in range(self.size+2)])

    def view_field(self):
        self.set_start_and_goal()
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                output = "++" if self.field[i][j] == 1 else "  "
                output = "St" if i == self.start[1] and j == self.start[0] else output
                output = "Go" if i == self.goal[1] and j == self.goal[0] else output
                print(output, end="")
            print()
            
    def set_start_and_goal(self):
        self.start = self.stop_list.pop(random.randrange(len(self.stop_list)))
        self.goal = self.stop_list.pop(random.randrange(len(self.stop_list)))
        
    def view_answer(self, method):
        for i in range(1, self.size+1):
            for j in range(1, self.size+1):
                output = "++" if self.field[i][j] == 1 else "  "
                output = ".." if self.field[i][j] == 3 else output
                output = "//" if self.field[i][j] == 2 else output
                output = "St" if i == self.start[1] and j == self.start[0] else output
                output = "Go" if i == self.goal[1] and j == self.goal[0] else output
                print(output, end="")
            print()        


class Method:
    def __init__(self, field):
        self.start_x = field.start[0]
        self.start_y = field.start[1]
        self.opened_list = [[self.start_x, self.start_y, 0]]
        self.closed_list = []
        self.opened_list_mini = [[self.start_x, self.start_y]]
        self.closed_list_mini = []
        self.road = []
        

class HorizontalType(Method):
    def __init__(self, field):
        super().__init__(field)
        self.counter = 0
    
    def search(self, mazerunner, field):
        while True:
            mazerunner.x, mazerunner.y = self.opened_list[0][0], self.opened_list[0][1]
            look_list = [mazerunner.look(field, 1, j) for j in range(4)]
            self.opened_list.append([mazerunner.x, mazerunner.y-2] + [self.counter]) if not look_list[0] and not [mazerunner.x, mazerunner.y-2] in self.opened_list_mini else None
            self.opened_list.append([mazerunner.x+2, mazerunner.y] + [self.counter]) if not look_list[1] and not [mazerunner.x+2, mazerunner.y] in self.opened_list_mini else None
            self.opened_list.append([mazerunner.x, mazerunner.y+2] + [self.counter]) if not look_list[2] and not [mazerunner.x, mazerunner.y+2] in self.opened_list_mini else None
            self.opened_list.append([mazerunner.x-2, mazerunner.y] + [self.counter]) if not look_list[3] and not [mazerunner.x-2, mazerunner.y] in self.opened_list_mini else None
            self.opened_list_mini.append([mazerunner.x, mazerunner.y-2]) if not look_list[0] and not [mazerunner.x, mazerunner.y-2] in self.opened_list_mini else None
            self.opened_list_mini.append([mazerunner.x+2, mazerunner.y]) if not look_list[1] and not [mazerunner.x+2, mazerunner.y] in self.opened_list_mini else None
            self.opened_list_mini.append([mazerunner.x, mazerunner.y+2]) if not look_list[2] and not [mazerunner.x, mazerunner.y+2] in self.opened_list_mini else None
            self.opened_list_mini.append([mazerunner.x-2, mazerunner.y]) if not look_list[3] and not [mazerunner.x-2, mazerunner.y] in self.opened_list_mini else None
            move_list = self.opened_list.pop(0)
            self.closed_list.append(move_list + [self.counter])
            move_list = self.opened_list_mini.pop(0)
            self.closed_list_mini.append(move_list)
            self.counter += 1
            if field.goal in self.closed_list_mini:
                break
        index = len(self.closed_list) - 1
        self.road.append(self.closed_list_mini.pop(index))
        while not self.road[len(self.road)-1] == field.start:
            along_load = self.closed_list.pop(index)
            for i in self.closed_list:
                if along_load[2] == i[3]:
                    index = self.closed_list.index(i)
            self.road.append(self.closed_list_mini.pop(index))


class ASter(Method):
    def __init__(self, field):
        super().__init__(field)
        self.goal_x = field.goal[0]
        self.goal_y = field.goal[1]
        
    def heuristic_function(self):
        pass


class MazeRunner(Digger):
    def __init__(self, field):
        super().__init__(field.start[0], field.start[1], field)
        self.start_x = field.start[0]
        self.start_y = field.start[1]
        
    def run_road(self, road, field, value):
        for i in range(len(road)-1):
            self.x, self.y = road[i][0], road[i][1]
            dx, dy = road[i][0] - road[i+1][0], road[i][1] - road[i+1][1]
            self.direction = 0 if dx == 0 and dy == 2 else self.direction
            self.direction = 1 if dx == -2 and dy == 0 else self.direction
            self.direction = 2 if dx == 0 and dy == -2 else self.direction
            self.direction = 3 if dx == 2 and dy == 0 else self.direction
            self.dig(field, value)
    

field = Field(21)
digger = Digger(random.randrange(1, (field.size-1)//2)*2, random.randrange(1, (field.size-1)//2)*2, field)
digger.work(field)
#field.view_field()
field.set_start_and_goal()
mazerunner = MazeRunner(field)
horizontaltype = HorizontalType(field)
horizontaltype.search(mazerunner, field)
#mazerunner.run_road(horizontaltype.closed_list_mini, field, 3)
mazerunner.run_road(horizontaltype.road, field, 2)
field.view_answer(horizontaltype)
#print(horizontaltype.road)
"""
print(field.start)
print(horizontaltype.closed_list)
print(horizontaltype.closed_list_mini)
print(horizontaltype.opened_list)
print(horizontaltype.opened_list_mini)
"""
