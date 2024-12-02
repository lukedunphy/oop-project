import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power, is_dodging=False):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.is_dodging = is_dodging

    def attack(self, opponent):
        #print(f"{self.name} attacks {opponent.name}")
        if opponent.is_dodging:
            print(f"\n{self.name} attacks {opponent.name}")
            opponent.is_dodging = False
            opponent.dodge()
        else:
            random_number = random.randint(10,50)
            opponent.health -= random_number
            print(f"\n{self.name} attacks {opponent.name} for {random_number} damage!")
            # if opponent.health <= 0:
            #     print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"\n{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def heal(self):
        if self.health +10 < self.max_health:
            heal_amount = random.randint(10,15)
            self.health += heal_amount
        else:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health, now at {self.health}/{self.max_health} health!")

    def special_attack(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        return damage
    
    def dodge(self):
        self.is_dodging = True
        

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def special_attack(self, opponent):
        damage = super().special_attack(opponent)
        print(f"{self.name} the warrior, uses a power attack dealing {damage} damage!")
        

    def dodge(self):
        print(f"{self.name} uses their shield to block the attack, their health remains at {self.health}")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here
    def special_attack(self, opponent):
        damage = super().special_attack(opponent)
        print(f"{self.name} the mage, casts a spell dealing {damage} damage!")

    def dodge(self):
        print(f"{self.name} vanishes in a flash of light, dodging the attack, their health remains at {self.health}")


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=30)

    def special_attack(self, opponent):
        damage = super().special_attack(opponent)
        print(f"{self.name} the archer, uses a quick shot dealing {damage} damage!")

    def dodge(self):
        super().dodge()
        print(f"{self.name} the archer, dodges the attack, their health remains at {self.health}")



class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=20)

    def special_attack(self, opponent):
        damage = super().special_attack(opponent)
        print(f"{self.name} the Paladin, uses a holy strike dealing {damage} damage!")

    def dodge(self):
        print(f"{self.name} raises their holy shield blocking the attack, their health remains at {self.health}")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name, is_dodging=False):
        super().__init__(name, health=150, attack_power=15, is_dodging=is_dodging)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def dodge(self):
        print(f"{self.name} the evil wizard, deflects the attack, their health remains at {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ").title()

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            print("\nSelect a special ability below")
            while True:
                choice2 = input("(1) Powerful Attack (2) Dodge Opponent's Attack: ")
                print()
                if choice2 == '1':
                    player.special_attack(wizard)
                    break
                elif choice2 =='2':
                    player.is_dodging = True
                    break
                else:
                    print("Enter a valid input")
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
            continue
        else:
            print("Invalid choice, try again.")
            #continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.attack(player)
            wizard.regenerate()


        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"{wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()