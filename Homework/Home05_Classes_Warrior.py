__author__ = 'stanislav-kuhtinski'

import random


class Warrior(object):
    def __init__(self, health):
        self.health = health

    def make_damage(self, enemy):
        enemy.health -= 20

robot1 = Warrior(100)
robot2 = Warrior(100)

while robot1.health > 0 and robot2.health > 0:
    rnd = random.randint(1, 2)
    if rnd == 1:
        robot1.make_damage(robot2)
        print('robot1 hits robot2')
        print('robot2 has {} health left' .format(robot2.health))
    else:
        robot2.make_damage(robot1)
        print('robot2 hits robot1')
        print('robot1 has {} health left'.format(robot1.health))

if robot2.health > robot1.health:
    print('robot2 wins the match!')
else:
    print('robot1 wits the match!')