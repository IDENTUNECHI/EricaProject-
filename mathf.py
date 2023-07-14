import pygame, os

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, v):
        return ((v.x - self.x) ** 2 + (v.y - self.y) ** 2)
