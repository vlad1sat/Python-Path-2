class Parent:
    children = list()

    def __init__(self, name: str, age: int, count_children: int):
        self.name = name
        self.age = age
        self.get_children(count_children)

    def get_children(self, count):
        for _ in range(1, count + 1):
            child = input("Введите информацию о ребенке: ").split()
            if self.age - int(child[1]) < 16:
                print("Некорректные данные!")
            else:
                self.children.append(Child(child[0], int(child[1]), child[2]))

    def feed_child(self, index_child):
        self.children[index_child].is_hungry = False

    def cheep_up(self, index_child):
        index_mood = Child.moods.index(self.children[index_child].mood)
        self.children[index_child].mood = Child.moods[index_mood + 1] if index_mood < len(Child.moods) \
            else Child.moods[index_mood]


class Child:
    moods = ('very bad', 'bad', 'norm', 'good', 'cool')

    def __init__(self, name: str, age: int, mood: str):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.mood = mood if mood in self.moods else 'very bad'

