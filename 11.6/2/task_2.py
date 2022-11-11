from student import Student


def create_students():
    for _ in range(3):
        user_student = input("Введите данные студента через пробел: ").split()
        try:
            students.append(Student(' '.join([user_student[0], user_student[1]]), user_student[2],
                                    float(user_student[3])))
        except ValueError:
            print("Неккоректно введены данные!")


students = list()
create_students()
students.sort(key=lambda x: x.marks)
for student in students:
    student.info_student()

