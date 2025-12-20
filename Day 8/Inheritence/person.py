class person:
    def show_person(self):
        print("i am person1")

class student(person):
    def show_student(self):
        print("i am student")
        # print(show_pe)

s1=student()
s1.show_student()
s1.show_person()