#!/usr/bin/env python
# coding: utf-8
# Day 10 - Problem 13
# In[2]:


# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# --------------------------------------------------------------
# Write a Python program to construct the following pattern, using a nested loop number.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

def num_pattern(n):
    """
    Print a pattern as above with a loop.

    :params n:
    """
    for i in range(n+1):
        print(str(i)*i)

num_pattern(9)
