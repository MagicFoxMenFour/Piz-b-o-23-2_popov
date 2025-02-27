import random

class Warrior:
    def __init__(self, name):
        self.health = 100
        self.name = name

    def attack(self, other):
        other.health -= 20
        print(f"Юнит {self.name} атаковал юнита {other.name}. У юнита {other.name} осталось {other.health} здоровья.")


def main():
    warrior1 = Warrior("Воин 1")
    warrior2 = Warrior("Воин 2")

    fighters = [warrior1, warrior2]

    while warrior1.health > 0 and warrior2.health > 0:
        attacker_index = random.randint(0, 1)  # Выбираем случайного атакующего КАЖДЫЙ раз
        attacker = fighters[attacker_index]
        defender = fighters[1 - attacker_index]

        attacker.attack(defender)

        if defender.health <= 0:
            print(f"Ресурс здоровья юнита {defender.name} закончился. Победил юнит {attacker.name}.")
            break

if __name__ == "__main__":
    main()