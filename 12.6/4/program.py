import random
import people

for _ in range(3):
    print(people.Manager('default', 'default', 18).get_salary())

for _ in range(3):
    count_hours = random.randint(10, 200)
    print(people.Agent('default', 'default', 18, count_hours).get_salary())

for _ in range(3):
    count_hours = random.randint(100, 200)
    print(people.Worker('default', 'default', 18, count_hours).get_salary())
