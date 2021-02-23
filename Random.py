# includes my Random class objects

import numpy as np
from math import *
from fractions import Fraction 

class Random:
    """My Random Number Generator"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        self.m_u = np.uint64(self.m_u * 2862933555777941757) + np.uint64(7046029254386353087)
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a uniform random floating point number between (0, 1) 
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    # function returns a random integer (1-6) using the rand() function
    # the probability for each number rolled can be tweaked in the argument
    def DiceRoll(self, p1=Fraction(1,6), p2=Fraction(1,6), p3=Fraction(1,6), p4=Fraction(1,6), p5=Fraction(1,6)):
        if p1 < 0. or p1 > 1. or p2 < 0. or p2 > 1. or p3 < 0. or p3 > 1. or p4 < 0. or p4 > 1. or p5 < 0. or p5 > 1.:
            return 1
  
        R = self.rand()

        if R < p1:
            return 1
        elif R > p1 and R < (p1+p2):
            return 2
        elif R > (p1+p2) and R < (p1+p2+p3):
            return 3
        elif R > (p1+p2+p3) and R < (p1+p2+p3+p4):
            return 4
        elif R > (p1+p2+p3+p4) and R < (p1+p2+p3+p4+p5):
            return 5
        else:
            return 6
