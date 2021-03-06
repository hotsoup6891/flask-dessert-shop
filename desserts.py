"""Dessert class for RESTful JSON API"""


class Dessert:
    def __init__(self, id, name, description, calories):
        """Create a dessert with a name, description, and calorie count"""

        self.id = id
        self.name = name
        self.description = description
        self.calories = calories

    def __repr__(self):
        """Nice formatting of dessert objects in Python shell"""

        return f"<Dessert, id={self.id}, name=\"{self.name}\", calories={self.calories}>"

    def serialize(self):
        """Convert dessert data to a dictionary to play nice with JSON"""

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "calories": self.calories
        }


class DessertList:
    def __init__(self):
        """Create a dessert list with empty list of desserts"""

        self.desserts = []
        self.next_id = 1

    def __repr__(self):
        """Nice formatting of dessert list objects in Python shell"""

        string = ""

        for dessert in self.desserts:
            string += repr(dessert) + '\n'

        return string

    def add(self, name, description, calories):
        """Add a new dessert given dessert data and append to our list"""

        new_dessert = Dessert(self.next_id, name, description, calories)
        self.next_id += 1
        self.desserts.append(new_dessert)

    def serialize(self):
        """Convert dessert list data to a list of dictionaries,
        which will play nice with JSON"""

        json_dict = []
        for dessert in self.desserts:
            json_dict.append(dessert.serialize())

        return json_dict


# make a dessert list and put some desserts in it
dessert_list = DessertList()
dessert_list.add("Chocolate chip cookie",
                 "C is for cookie, that's good enough for me", 200)
dessert_list.add("Banana split", "I'm going to eat all of my feelings", 600)
dessert_list.add("Glazed Donut", "Perfect with a cup of coffee", 300)
