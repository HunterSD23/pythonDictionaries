def main():
    fruits = {}
    
    fruit_num = int(input("Please enter how many fruits would you like to record: "))

    # Collect data for the number of fruits above from the user. Should include name, color, 
    # weight in lbs, and price. Once each set of data points is collected
    # Think about what kind of control structure to create to complete this process
    for fruits in fruit_num:
        fruits['set', fruit_num] = [input("Name of fruit: "), input("Fruit's color: "), int(input("Weight of Fruit")), float(input("Price of fruit: "))]

        # After each set of input statements, store the data in the dictionary
        

    # Output each of the fruit's data as a vertical list. This happens one time
    # for each of the fruits in the dictionary. 
    for fruit_num, name, color, weight, price in fruits.items():
        print(f"The {name} is {color}, weighs {weight:.2f} lbs, and costs ${price:.2f}.")

if __name__ == "__main__":
    main()

