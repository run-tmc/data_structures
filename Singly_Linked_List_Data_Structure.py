# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:00:54 2017

@author: trevo
"""

class node:
    def __init__ (self, data=None, next=None):
        self.data=data
        self.next_node=next
        
    def get_next(self):
        return self.next_node
    
    def set_next(self,next):
        self.next_node = next
        
    def get_data(self):
        return self.data
        
    def set_data(self, data):
        self.data = data
        
class linked_list:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
        
    def get_size(self):
        return self.size
        
    """Insert new data at root location"""    
    def insert(self, data):
        new_node = node(data)
        new_node.set_next(self.root)
        self.root = new_node
        self.size +=1
        
    def delete(self, data):
        this_node = self.root
        prev_node = None
        while (this_node):
            if (this_node.get_data()==data):
                if (prev_node):
                    # Sets previous node next node link to the deleted 
                    # data next node link
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                # Data value not in this node...transition to next node
                prev_node = this_node
                this_node = this_node.get_next()
        return False
        
    def search(self, data):
        this_node = self.root
        while (this_node):
            if (this_node.get_data()== data):
                return data
            else:
                this_node = this_node.get_next()
        return None


mysll = linked_list()
mysll.insert(20)
mysll.insert(30)
mysll.insert(45)
print mysll.search(45)
print mysll.delete(30)
