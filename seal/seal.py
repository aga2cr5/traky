# -*- coding: utf-8 -*-
#​‌‌‌​​​​‌‌​‌‌‌​ A class to describe a seal object
#​‌‌‌​​​​‌‌​‌‌‌​ Implement the missing functions here below

class Seal:

    def __init__(self, name):
        self.name = str(name)
        self.energy = int(3)
        self.friends = []
        self.location = "water"


    def eat(self):
        self.energy = 5
        return "{:} ate a fish!".format(self.name)


    def climb_on_rock(self):
        self.location = "rock"
        return "{:}: Such a nice rock! :3".format(self.name)


    def do_banana_pose(self):
        if self.location != "rock":
            return "{:} is not on a rock.".format(self.name)
        elif self.energy > 1:
            self.energy -= 1
            return "{:}: -__;3".format(self.name)
        else:
            return "{:}: I won't. ___:3".format(self.name)


    def add_friend(self, other_seal):
        if other_seal in self.friends:
            return
        self.friends.append(other_seal)
        other_seal.friends.append(self)



    def tell_friends(self):
        friends = []

        for seal in self.friends:
            friends.append(seal.name)

        return ", ".join(friends)


    def request_banana_pose(self):
        answers = []

        for friend in self.friends:
            answer = friend.do_banana_pose()
            answers.append(answer)
        return answers



    def __repr__(self):
        #​‌‌‌​​​​‌‌​‌‌‌​ Returns the representation of the object as a string:
        #​‌‌‌​​​​‌‌​‌‌‌​ the name of the seal and the unique identifier of this particular
        #​‌‌‌​​​​‌‌​‌‌‌​ Seal object. Reference for id():
        #​‌‌‌​​​​‌‌​‌‌‌​ https://docs.python.org/3/library/functions.html#id

        #​‌‌‌​​​​‌‌​‌‌‌​ You don't need to modify this method. It is used implicitly in the
        #​‌‌‌​​​​‌‌​‌‌‌​ unit tests to identify Seal objects that have been created in the
        #​‌‌‌​​​​‌‌​‌‌‌​ case some unit test does not pass.
        return "<Seal {}, id {}>".format(self.name, id(self))

if __name__ == "__main__":
    pass
    #​‌‌‌​​​​‌‌​‌‌‌​ You can experiment with the Seal class here
