class Planet:
    def __init__(self, name, surface_area = 0, num_moons = 0, order_from_sun = 10):
        self.this_name = name
        self.surface_area = surface_area
        self.num_moons = num_moons
        self.order_from_sun = order_from_sun
        self.moons = ['moon'] * num_moons

    def compare_moons(self, other_planet):
        if len(self.moons) > len(other_planet.moons):
            print(f"{self.this_name} has more moons than {other_planet.this_name}")
        elif len(self.moons) == len(other_planet.moons):
            print(f"{self.this_name} has the same number of moons as {other_planet.this_name}")
        elif len(self.moons) < len(other_planet.moons):
            print(f"{self.this_name} has the less moons than {other_planet.this_name}")
    
    def describe(self):
        print(f"The planet {self.this_name} is the {self.order_to_string()} planet from the sun and it has a surface area of {self.surface_area} million miles squared")


    def describe_moons(self):
        if not self.moons:
            print(f"The planet {self.this_name} has no moons")
        else:
            moon_count = len(self.moons)
            moon_text = ""
            if moon_count == 1:
                moon_text = "1 moon"
            else:
                moon_text = f"{moon_count} moons"
            moon_str = (', ').join(self.moons)
            print(f"The planet {self.this_name} has {moon_text}: {moon_str}")



    def order_to_string(self):
        if self.order_from_sun == 1:
            return "1st"
        elif self.order_from_sun == 2:
            return "2nd"
        elif self.order_from_sun == 3:
            return "3rd"
        else:
            return f"{self.order_from_sun}th"
    
    def bad_function(self):
        self.really_bad_function()