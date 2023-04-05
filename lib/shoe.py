#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size = 0):
        self.brand = brand
        self.size = size
    
    def get_size(self):
        return self._brand

    def set_size(self, size):
        if isinstance(size, int):
            self._brand = size 
        else:
            print("size must be an integer")
    
    size = property(get_size, set_size)

    def cobble(self, condition = 'Used'):
        print("Your shoe is as good as new!")
        self.condition = 'New'
