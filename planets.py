def weight_on_planets():
    # get user input
    num = float(input("What do you weigh on earth? "))
    # calculate weight
    mars_weight = num * 0.38
    jupiter_weight = num * 2.34
    # print out weight on Mars and Jupiter
    print(f"\nOn Mars you would weigh {mars_weight} pounds.\nOn Jupiter you would weigh {jupiter_weight} pounds.")


if __name__ == '__main__':
    weight_on_planets()
