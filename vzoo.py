class Animal:
    def __init__(self, name, species, age, health_status="Healthy"):
        self.name = name
        self.species = species
        self.age = age
        self.health_status = health_status

    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Health: {self.health_status}"

    def feed(self):
        print(f"{self.name} has been fed.")

    def get_older(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old.")


class Habitat:
    def __init__(self, habitat_type, capacity):
        self.habitat_type = habitat_type
        self.capacity = capacity
        self.current_occupants = []

    def add_animal(self, animal):
        if len(self.current_occupants) < self.capacity:
            self.current_occupants.append(animal)
            print(f"{animal.name} has been added to the {self.habitat_type}.")
        else:
            print(f"The {self.habitat_type} is full!")

    def remove_animal(self, animal):
        if animal in self.current_occupants:
            self.current_occupants.remove(animal)
            print(f"{animal.name} has been removed from the {self.habitat_type}.")
        else:
            print(f"{animal.name} is not in this habitat.")

    def list_all_animals(self):
        return [animal.name for animal in self.current_occupants]


class Caretaker:
    def __init__(self, name):
        self.name = name
        self.assigned_habitats = []

    def assign_to_habitat(self, habitat):
        self.assigned_habitats.append(habitat)
        print(f"{self.name} has been assigned to the {habitat.habitat_type}.")

    def feed_all_animals(self):
        for habitat in self.assigned_habitats:
            for animal in habitat.current_occupants:
                animal.feed()

    def check_on_animals(self):
        for habitat in self.assigned_habitats:
            for animal in habitat.current_occupants:
                print(animal.display_info())


class Zoo:
    def __init__(self, name):
        self.name = name
        self.list_of_habitats = []
        self.list_of_caretakers = []
        self.list_of_animals = []

    def add_habitat(self, habitat):
        self.list_of_habitats.append(habitat)

    def add_caretaker(self, caretaker):
        self.list_of_caretakers.append(caretaker)

    def add_animal(self, animal):
        self.list_of_animals.append(animal)

    def daily_report(self):
        print(f"--- Daily Report for {self.name} Zoo ---")
        for caretaker in self.list_of_caretakers:
            caretaker.check_on_animals()

zoo = Zoo("Central")
tiger = Animal("Tiger", "Bengal Tiger", 5)
pen_habitat = Habitat("pen", 5)

zoo.add_animal(tiger)
zoo.add_habitat(pen_habitat)

pen_habitat.add_animal(tiger)

jane = Caretaker("Jane")
zoo.add_caretaker(jane)

jane.assign_to_habitat(pen_habitat)
jane.feed_all_animals()

zoo.daily_report()