import Critter


def main():
    money = 0

    critters = [Critter.Seeddino(), Critter.Splashapin(), Critter.Singecko()]

    for i in range(len(critters)):
        pet_name = input(f"Name your critter ({i + 1}/{len(critters)}): ")
        critters[i].set_name(pet_name)

    while critters:

        spacer()

        for critter in critters:
            income = critter.playerAction()
            if income > 0:
                print(f"{critter.get_name()} sells for £{income}!")
                money += income

        spacer()
        temp = []
        for critter in critters:
            if critter.status() == 1:
                temp.append(critter)
        critters = temp

        print(f"You currently have £{money}, your goal is $100.")

    spacer()
    if money >= 100:
        print(f"You Win!\nYou made £{money}/100.")
    else:
        print(f"You Loose! \nYou only made £{money}/100.")


def spacer():
    print(f" {'-' * 10}")


if __name__ == '__main__':
    main()
