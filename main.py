from planet import Planet
def my_func():
    print("YAY!")

#my_func()
mercury = Planet("Mercury") #, 28.88, 0, 1)
#print(mercury.moons)
venus = Planet("Venus") #, 177.7, 0, 2)
earth = Planet("Earth", num_moons = 1, surface_area= 196.9)#, 3)
#print(earth.moons)
#earth.moons[0] = "The Moon"
#print(earth.moons)
mars = Planet("Mars", 55.91 , 2, 4)
mars.moons[0] = "Phobos"
mars.moons[1] = "Deimos"


planets = [mercury, venus, earth, mars]

for planet in planets:
    planet.describe()
    planet.describe_moons()
#     #planet.bad_function()

#mars.compare_moons(earth)
def compare_moons(planet1, planet2):
    if len(planet1.moons) > len(planet2.moons):
        print(f"{planet1.this_name} has more moons than {planet2.this_name}")
    elif len(planet1.moons) == len(planet2.moons):
        print(f"{planet1.this_name} has the same number of moons as {planet2.this_name}")
    elif len(planet1.moons) < len(planet2.moons):
        print(f"{planet1.this_name} has the less moons than {planet2.this_name}")



compare_moons(earth, mars)