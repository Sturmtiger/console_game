from random import randint
from weights import WeightedChoice


class Player:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def __str__(self):
        return str(f'[{self.name}] player health: {self.health}hp.')

    # Heal yourself(18-25hp)
    def heal_yourself(self):
        hp = randint(18, 25)
        self.health += hp
        if self.health > 100:
            self.health = 100
        print(f'Player [{self.name}] has been healed. His health is now: {self.health}hp!')

    # Inflict middle damage(18-25hp) to the enemy
    def mid_damage_the_enemy(self, enemy):
        damage = randint(18, 25)
        enemy.health -= damage
        if enemy.health < 0:
            enemy.health = 0
        print(f'[{self.name}] inflicted medium damage(-{damage}hp) to [{enemy.name}]!')

    # Inflict middle damage(10-35hp) to the enemy
    def high_damage_the_enemy(self, enemy):
        damage = randint(10, 35)
        enemy.health -= damage
        if enemy.health < 0:
            enemy.health = 0
        print(f'[{self.name}] inflicted high damage(-{damage}hp) to [{enemy.name}]!')


class Computer(Player):
    def __init__(self):
        super().__init__('Computer')

    # selection of possible actions against an enemy
    def __actions_selection(self):
        actions = list()
        for action in dir(Player)[::-1]:
            if action.startswith('_'):
                break
            elif action == 'heal_yourself' and self.health > 82:  # if hp > 82 exclude possibility 'heal yourself'
                continue
            actions.append([action, 1])  # append action with its weight in list format
        return actions

    # method for auto move (special for Computer)
    def make_some_decision(self, enemy):
        actions = self.__actions_selection()
        actions_gen = WeightedChoice(actions)

        if self.health <= 35:
            actions_gen.increase_chance('heal_yourself', 3)  # increase chance by 3 times
        action = actions_gen.get_item()

        if action == 'heal_yourself':
            getattr(self, action)()
        else:
            getattr(self, action)(enemy)
