import copy
import random

class SnakeSegment:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.x = 10
        self.y = 0
        self.size = 10
        self.body = [SnakeSegment(320, 240)] # Initialize the snake with one segment at (320, 240)

    def move(self):
         # Move each segment of the body to the position of its predecessor
        for i in range(len(self.body)-1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
         # Move the head of the snake
        self.body[0].x += self.x
        self.body[0].y += self.y
    
    def grow(self):
        # Add a new segment to the body at the same position as the current tail
        last_segment = copy.copy(self.body[-1]) 
        self.body.append(last_segment)
