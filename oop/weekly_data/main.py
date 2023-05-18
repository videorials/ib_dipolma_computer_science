from assets import *

def main():

    andy_weights = Weekly_data()
    andy_weights.print_data()
    andy_weights = Weekly_data(8,"Bodyweight", "Kilograms")
    andy_weights.print_data()
    andy_weights = Weekly_data(8,"Bodyweight", "Kilograms", 71.3, 75.9)
    andy_weights.print_data()

    andy_weights = Weekly_bodyweight(8,"Bodyweight", "Kilograms", 71.3, 75.9)
    andy_weights.print_data()

if __name__ == "__main__":
    main()