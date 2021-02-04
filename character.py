"""Lexi Iocca
Character Classes
Oct 31, 2017
"""

import easygui


class Character:
    def __init__(self):
        self.inventory = []

    def addToInventory(self, item):
        self.inventory.append(item)

    def checkInventory(self, item):
        if item in self.inventory:
            return True
        else:
            return False

    def removeFromInventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
