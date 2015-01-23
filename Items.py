__author__ = 'dgrayson'

class Item:

    def __init__(self):
        self.name = ' '
        self.value =  0
        self.description = ' '
        self.type = ' '

    def useItem(self, player):

        if self.type == 'rec':
            if self.name == 'Potion':
                player.currHP += self.value
            elif self.name == 'Ether':
                player.currMP += self.value


class Potion(Item):

    def __init__(self):
        Item.__init__(self)
        self.name = "Potion"
        self.value = 10
        self.description = "Recovers 10HP"
        self.type = "rec"


class Ether(Item):

    def __init__(self):
        Item.__init__(self)
        self.name = "Ether"
        self.value = 10
        self.description = "Recovers 10MP"
        self.type = "rec"
