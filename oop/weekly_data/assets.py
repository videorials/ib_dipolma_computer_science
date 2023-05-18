# Polymorphism
# ===================================================================================================
# Objects take on different forms or behaviors depending on the context or the type of data fed in.
# >> Overloading: multiple methods with the same name but different parameters to exist. Python does
#    not support overloading. A workaround is to use *args (array of parameters), which enables the
#    constructor detect and manage different combinations of parameter[s].
# >> Overriding: child class provides different implementation of method in parent class.

# Inheritance
# ===================================================================================================
# A class can inherit and extend the properties and behavior of another class, promoting code reuse.

# Encapsulation
# ===================================================================================================
# Principle that combines data and methods within a class, allowing for controlled access to the
# internal components and protecting them from unwanted external interference.

import random

# >> Parent (super, base) class, stores n weeks of data in 2d array, and takes 1, 3, or 5 parameters.
class Weekly_data:

    # constructor method | creates and initializes an instance of the class
    def __init__(self, *args):

        # ---------------------------------- >> 0 parameters...
        self.qty_weeks = 1                      # > default number of weeks
        self.type = None                        # > no value
        self.units = None                       # > no value

        # ---------------------------------- >> 1 parameter...
        if len(args) == 1:
            self.qty_weeks = args[0]            # > integer assigned to qty_weeks

        # ---------------------------------- >> 3 parameters...
        elif len(args) >= 3:
            self.qty_weeks = args[0]            # > integer assigned to qty_weeks e.g. 52
            self.type = args[1]                 # > string assigned to type e.g. "Weights"
            self.units = args[2]                # > string assigned to units e.g. "KG

        # ---------------------------------- >> 5 parameters | create data structure...
        if len(args) == 5:
            self.data = self.reset_data(args[3], args[4])
        else:
            self.data = self.reset_data()

    # setter (mutator) methods | allows you to set or mutate the value of an attribute in a class
    def reset_data(self, *args):
        month = []
        for weeks in range(self.qty_weeks):
            week = []
            for days in range(7):
                if len(args) == 0:
                    week.append(None)
                else:
                    if isinstance(args[0],int):
                        week.append(round(random.randint(args[0],args[1])))
                    else:
                        week.append(round(random.uniform(args[0],args[1]),2))
            month.append(week)
        return month

    # getter (accessor) methods | allows you to access an attribute in a given class
    def get_type(self):
        return self.type

    def get_units(self):
        return self.units

    def get_data(self):
        return self.data

    # void (procedure) methods | a method that does not return a value
    def print_data(self):
        print(f"\nType: {self.type} | Unit: {self.units}")
        print(*self.data, sep="\n")

# >> Child (sub) class, inherits attributes and methods from the parent class, Weekly_data.
class Weekly_bodyweight(Weekly_data):

    # >> formats and print data stored in 2d array
    def print_data(self):
        print(f"\nType: {self.type} | Unit: {self.units}")
        print("=" * 41)
        for week in self.data:
            week_data = ""
            for day in week:
                if isinstance(day, float):
                    week_data += format(day,'.2f') + "|"
                else:
                    week_data += " ... " + "|"
            print(week_data[:-1])
        print("=" * 41 + "\n")