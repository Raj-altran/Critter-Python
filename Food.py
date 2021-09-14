class Food:
    def applyfood(self, critter):
        pass

    def get_name(self):
        pass


class Steak(Food):
    def get_name(self):
        return "Steak"

    def applyfood(self, critter):
        critter.alter_food_tired_fit(2, 1, 1)


class Cake(Food):
    def get_name(self):
        return "Cake"

    def applyfood(self, critter):
        critter.alter_food_tired_fit(3, 2, -1)


class Oats(Food):
    def get_name(self):
        return "Oats"

    def applyfood(self, critter):
        critter.alter_food_tired_fit(2, 1, 0)
