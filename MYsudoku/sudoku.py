#!/usr/bin/env python
# coding: utf-8

# # import tools

# In[1]:


import numpy as np
import pandas as pd
from IPython.display import display, HTML
import matplotlib.pyplot as plt


# In[3]:


class Solution():
    def __init__(self, question_):
        self.question = question_
        self.board = question_
        self.find_blank_position()
        
        # some control signal need in sol
        self.blank_position_index = 0
        self.stop_signal = False
        
        # record answer
        self.answer = []


        
    def find_blank_position(self):
        blank_position = []
        for row in range(9):
            for col in range(9):
                if( self.question[row][col] == "" ):
                     blank_position = blank_position + [(row, col)]
        self.blank_position = blank_position 
        
    def draw(self):
        col = row = 9
        matrix = np.array(self.board)
        df = pd.DataFrame(matrix)
        plt.figure(1, figsize=(5, 5))
        tb = plt.table(cellText=matrix, loc=(0,0), cellLoc='center')

        tc = tb.properties()['child_artists']
        for cell in tc: 
            cell.set_height(1.0/row)
            cell.set_width(1.0/col)

        ax = plt.gca()
        ax.set_xticks([])
        ax.set_yticks([])

        plt.show()
    
    def find_candidate(self, row, col):
        row_element = self.board[row]
        col_element = [row[col] for row in self.board]
        buf = np.array(self.board)[row//3*3 : row//3*3+3 , col//3*3 : col//3*3+3]
        block_element = buf.flatten().tolist()

        buf_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", ""]
        buf_2 = set(row_element + col_element + block_element)
        possible_element = list(set(buf_1) - set(buf_2))
        possible_element.sort()
        return(possible_element)
    
    def sol(self, draw_ = False):
        if( self.blank_position_index == len(self.blank_position)):
            self.stop_signal = True
            ##!! list 不能直接 copy 
            self.answer = np.array(self.board)
        else:
            row, col = self.blank_position[self.blank_position_index]
            self.blank_position_index = self.blank_position_index + 1
            for fill_in in self.find_candidate(row, col):
                self.board[row][col] = fill_in
                if( draw_ ):
                    self.draw()
                self.sol(draw_)
                
                if( self.stop_signal):
                    break
            self.board[row][col] = ""
            self.blank_position_index = self.blank_position_index - 1