class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for n_f in range(1, new_floor + 1):
            if new_floor <= self.number_of_floors:
                print(n_f)
            else:
                print('Такого этажа не существует')
                break


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
     return self.number_of_floors


    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"


#h1 = House('ЖК Эльбрус', 10)
#h2 = House('ЖК Акация', 20)

#print(h1)
#print(h2)

#print(len(h1))
#print(len(h2))

#class House:
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __it__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

