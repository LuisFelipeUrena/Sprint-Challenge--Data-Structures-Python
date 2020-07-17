from collections import deque
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ls = []

        

    def append(self, item):
        if len(self.ls) == self.capacity:
            self.ls.pop(0)
        # if len(self.ls) is self.capacity+1:
        #     self.ls.insert(0,item)    
        self.ls.append(item) 
         
    

    def get(self):
        return self.ls
        
        