from collections import deque
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.ls = deque(maxlen=self.capacity)

        

    def append(self, item):
        # self.ls.append(item)
        if len(self.ls) == self.capacity:
            self.ls.appendleft(item)
        else:
            self.ls.append(item)    
        
        
        
        


        # # self.ls.insert(0,item)
        # if len(self.ls) == self.capacity:
        #     self.ls.pop(0)
        # # # if len(self.ls) is self.capacity+1:
        # # #     self.ls.insert(0,item)    
        # self.ls.append(item) 
         
    

    def get(self):
        return list(self.ls)
        
        