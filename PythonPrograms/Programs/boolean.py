# Pet
def pet(name, age, bark, tweet):
        print(f"My pet is called {name}, he is {age} years old")
        print(f"Statement: {name} barks. {bark}")
        print(f"Statement: {name} tweets. {tweet}")

data = pet(input("Enter your pet's name: "), input("Enter your pet's age: "), input("Does your pet bark? True/False: "), input("Does your pet tweet? True/False: "))