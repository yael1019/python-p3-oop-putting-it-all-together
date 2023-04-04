#!/usr/bin/env python3

class Book:
    def __init__(self, title):
        self.title = title
    def page_count(self, num):
        if(isinstance(num, int)):
            self.page_num = num
    # num = property(page_count)