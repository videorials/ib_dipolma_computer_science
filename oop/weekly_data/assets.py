import random

class Weekly_data:

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

    def get_type(self):
        return self.type

    def get_units(self):
        return self.units

    def get_data(self):
        return self.data

    def print_data(self):
        print(f"\nType: {self.type} | Unit: {self.units}")
        print(*self.data, sep="\n")

class Weekly_bodyweight(Weekly_data):

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