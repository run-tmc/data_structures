# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 17:00:54 2017

@author: trevo
"""

class node:
    def __init__ (self, data=None, previous=None, next=None):
        self.data=data
        self.next_node=next
        self.previous_node=previous
        
    def get_next(self):
        return self.next_node
        
    def get_previous(self):
        return self.previous_node
    
    def set_next(self,next):
        self.next_node = next
        
    def set_previous(self,previous):
        self.previous_node = previous
        
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
        # Establish new node and insert data
        new_node = node(data)
        # Determine if linked list exist
        if (self.root is None):
            # Set root pointer to newly created node
            self.root = new_node
        else:
            # Establish pointers to insert new data as root node
            # Point previous root node back to new root node
            self.root.set_previous(new_node)
            # Set new root node next pointer to previous root node
            new_node.set_next(self.root)
            # Sent new node as root node
            self.root = new_node
        self.size +=1
        
    def delete(self, data):
        this_node = self.root
        
        while (this_node):
            if (this_node.get_data()==data):
                next_node = this_node.get_next()
                prev_node = this_node.get_previous()
                if (next_node):
                    next_node.set_previous(prev_node)
                if (prev_node):
                    
                    prev_node.set_next(next_node)
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                # Data value not in this node...transition to next node
                
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


mydll = linked_list()
mydll.insert(20)
mydll.insert(30)
mydll.insert(45)
print mydll.search(20)
print mydll.delete(30)
