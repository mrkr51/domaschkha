import random

character_names = ["Shrek", "Donkey", "Puss in Boots", "Jack Horner"]


class MixinSpeakable:
    def speak(self):
        print(self.name + " says something!")


class MixinAnimated:
    def setup_animation(self, is_animated):
        self.is_animated = is_animated


class MixinFunny:
    def make_laugh(self):
        print(self.name + " is making a joke!")


class MixinPoseable:
    def pose(self):
        print(self.name + " is posing for a photo!")


class MixinBipedal:
    def walk(self):
        print(self.name + " walks on two legs!")


class MixinActionable:
    def perform_action(self):
        result = self.name + " is doing many actions right now!"
        return result


class MixinCollectable:
    def setup_collectable(self, can_collect):
        self.collectable = can_collect

    class_name = "Collectable Item"

    def check_if_collectable(self):
        if self.collectable == True:
            return self.name + " can be collected!"
        else:
            return self.name + " cannot be collected!"


class BaseCharacter(MixinSpeakable, MixinAnimated, MixinFunny):
    def __init__(self, name=None, is_animated=True):
        if name == None:
            self.name = random.choice(character_names)
        else:
            self.name = name

        MixinAnimated.setup_animation(self, is_animated)


class Shrek(BaseCharacter, MixinBipedal):
    def __init__(self):
        BaseCharacter.__init__(self, "Shrek", True)


class PussInBoots(BaseCharacter, MixinBipedal):
    def __init__(self):
        BaseCharacter.__init__(self, "Puss in Boots", True)


class Donkey(BaseCharacter):
    def __init__(self):
        BaseCharacter.__init__(self, "Donkey", True)


class BaseInActionCharacter(BaseCharacter, MixinActionable):
    def __init__(self, name):
        BaseCharacter.__init__(self, name, True)


class ShrekInAction(BaseInActionCharacter, Shrek):
    def __init__(self):
        BaseInActionCharacter.__init__(self, "Action Shrek")


class FunkoPop(MixinCollectable, BaseCharacter):
    def display(self):
        message = self.name + " is now a FunkoPop figure!"
        return message


class ShrekFunckoPop(FunkoPop, Shrek):
    def __init__(self):
        FunkoPop.__init__(self, "Shrek Funko")
        MixinCollectable.setup_collectable(self, True)


class BaseHuman:
    def __init__(self, human_name):
        self.human_name = human_name


class BaseCosplayer(BaseHuman, MixinPoseable):
    def __init__(self, character_object, human_name, costume_name):
        BaseHuman.__init__(self, human_name)
        self.name = character_object.name
        self.costume = costume_name


if __name__ == "__main__":
    random_char = BaseCharacter()
    print("Character name: " + random_char.name)
    random_char.speak()

    shrek_toy = ShrekFunckoPop()
    print(shrek_toy.display())
    print(shrek_toy.check_if_collectable())

    simple_shrek = Shrek()
    me = BaseCosplayer(simple_shrek, "Alex", "Green Mask")
    print("Cosplayer " + me.human_name + " is dressed as " + me.name)
    me.pose()