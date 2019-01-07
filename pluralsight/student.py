students=[]


class Student:

    school_name = "Springfield Elementary"  # Attibute

    def __init__(self, name, last_name, student_id=332):
        self.name = name
        self.last_name = last_name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name + self.last_name

    def get_name_capitalize(self):
        full_name = self.name + self.last_name
        return self.full_name.capitalize()

    def get_school_name(self):
        return self.school_name