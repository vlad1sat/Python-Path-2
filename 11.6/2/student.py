class Student:
    def __init__(self, full_name: str, group: str, marks: float):
        self.full_name = full_name
        self.group = group
        self.marks = marks

    def info_student(self):
        print("ФИО: {}. Группа: {}. Успеваемость: {}".format(
            self.full_name, self.group, self.marks
        ))
