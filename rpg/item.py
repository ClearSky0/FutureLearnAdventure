class Item:
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description

    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.name + ": " + self.description)


class Container(Item):
    def __init__(self, item_name, item_description):
        super().__init__(item_name, item_description)
        self.contents = []

    def put_in(self, item):
        self.contents.append(item)

    def take_out(self, item):
        self.contents.remove(item)

    def look_in(self):
        print("Your " + self.name + " contains:")
        if len(self.contents) == 0:
            print("Nothing")
        else:
            for item in self.contents:
                item.describe()
