# Base Character class
import random


class Character:
    def __init__(self, name, health, attack_power, special_ability):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.special_ability = special_ability
        self.evade_next = False

    def attack(self, opponent):
        if opponent.evade_next:
            opponent.evade_next = False
            print(f"{opponent.name} evaded {self.name}'s attack!")
            return

        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")


    def special_attack(self, opponent):
        if opponent.evade_next:
            opponent.evade_next = False
            print(f"{opponent.name} evaded {self.name}'s attack!")
            return

        damage = random.randint(1, self.special_ability)
        opponent.health -= damage
        print(f"{self.name} uses special attack on {opponent.name} for {damage} damage!")



    def evade_attack(self):
        self.evade_next = True
        print(f"{self.name} prepares to evade the next attack!")

    def heal(self):
        amount = random.randint(5, 15)
        self.health = min(self.health + amount, self.max_health)
        print(f"{self.name} heals {amount} health!")

    def display_stats(self):
        print(
            f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}"
        )


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25, special_ability=30)


    def sword_slash(self, opponent):
        damage = random.randint(5, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} uses sword slash, resulting in {damage} damage!")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35, special_ability=40)

    def crushing_pen(self, opponent):
        damage = random.randint(5, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} uses Crushing Pen, resulting in {damage} damage!")


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15, special_ability=20)
        self.turn_counter = 0

    def regenerate(self):
        self.health = min(self.health + 5, self.max_health)
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def the_caster(self, player):
        damage = random.randint(5, self.special_ability)
        player.health -= damage
        print(f"{self.name} uses The Caster!, resulting in {damage} damage!")

    def summon_minions(self, opponent):
        damage = random.randint(3, 10)
        opponent.health -= damage
        print(f"{self.name} summons minions! They deal {damage} damage to {opponent.name}!")

    def side_special_ability(self, opponent):
        self.turn_counter += 1

        if self.turn_counter >= random.randint(3, 6):
            self.summon_minions(opponent)
            self.turn_counter = 0


# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=20, special_ability=25)

    def quick_shot(self, opponent):
        shot_1 = random.randint(1, self.special_ability)
        shot_2 = random.randint(1, self.special_ability)
        opponent.health -= (shot_1 + shot_2)
        print(
            f"{self.name} uses Quick Shot! (2 arrows) on {opponent.name}, dealing {shot_1 + shot_2} damage!"
        )


# Create Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=25, special_ability=35)

    def noble_push(self, opponent):
        damage = random.randint(1, self.special_ability)
        opponent.health -= damage
        print(
            f"{self.name} uses Noble Push! on {opponent.name}, which resulted in {damage} damage."
        )


def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == "1":
        return Warrior(name)
    elif class_choice == "2":
        return Mage(name)
    elif class_choice == "3":
        return Archer(name)
    elif class_choice == "4":
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Evade Next Attack")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == "1":
            player.attack(wizard)
        elif choice == "2":
            player.special_attack(wizard)
        elif choice == "3":
            player.evade_attack()
        elif choice == "4":
            player.heal()
        elif choice == "5":
            player.display_stats()
            continue
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)
            wizard.side_special_ability(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")


def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
