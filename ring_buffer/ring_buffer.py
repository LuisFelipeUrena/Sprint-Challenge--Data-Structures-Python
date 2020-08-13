# crete a list with a maximum capacity that's predifined as a parameter in the 
# class.
# if the list is empty or not at full capacity fill the list as a stack
# if the list is full replace each number in the list according to the index
# [1,2,3] is a full stack
# when adding 4 we should replace 1 with 4
# then 

from collections import deque
class RingBuffer:
    # the ring buffer has to be of a fixed size
    def __init__(self,size_max):
        self.capacity = size_max
        self.data = deque(maxlen=self.capacity)
        self.indicator = 0
    
    def append(self,value):
        # if the buffer is not filled up to capacity, it should
        # just append elements normally
        if self.capacity != len(self.data):
            self.data.append(value)
        else:
            self.data.remove(self.data[self.indicator])
            self.data.insert(self.indicator,value)
            self.indicator += 1
        
        if self.indicator == self.capacity:
            self.indicator = 0    
            
    
    
    # def __init__(self, capacity):
    #     self.capacity = capacity
    #     self.ls = deque([],maxlen=self.capacity)

        

    # def append(self, item):
    #     replacement = 0
    #     if len(self.ls) < self.capacity:
    #         return self.ls.append(item)
    #     if len(self.ls) == self.capacity:
    #         self.ls.remove(self.ls[replacement])
    #         self.ls.insert(replacement,item)
    #         replacement +=1
    #     if replacement == self.capacity:
    #         replacement = 0




 



             
        # else:
        #     self.ls.appendleft()        
        # self.ls.insert(0,item) 
        # if len(self.ls) == self.capacity:
        #     self.ls.popleft()
            
            
        
        # return self.ls    
         
         
         
            # self.capacity -=1
        # self.ls.append(item)
        # self.ls.append(item)
        # if len(self.ls) == self.capacity:
        #     self.ls.appendleft(item)
        # else:
        #     self.ls.append(item)    
        
        
        
        


        # # self.ls.insert(0,item)
        # if len(self.ls) == self.capacity:
        #     self.ls.pop(0)
        # # # if len(self.ls) is self.capacity+1:
        # # #     self.ls.insert(0,item)    
        # self.ls.append(item) 
         
    

    def get(self):
        return list(self.data)
        
        