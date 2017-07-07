class Animal:

    def __init__(self,name,sound_effect):
        self.name = name
        self.make_sound=sound_effect

def moo():
    print("moo")

def quack():
    print("quack")

def bah():
    print("bah")

a=Animal("cow",moo)
a.make_sound()