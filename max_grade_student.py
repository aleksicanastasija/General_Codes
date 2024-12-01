class Student:
    def __init__(self, name, year, grade1, grade2, grade3):
        self.name = name
        self.year = year
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3

    @property
    def average(self):
        return (self.grade1 + self.grade2 + self.grade3) / 3

    def __str__(self):
        return (f"Name: {self.name}, Year: {self.year}, Grades: ({self.grade1}, {self.grade2}, {self.grade3}), "
                f"Average: {self.average:.2f}")

def main():
    n = int(input("Enter the number of students: "))

    students = []
    for i in range(n):
        print("Name: ")
        name = input()

        print("Year: ")
        year = int(input())

        print("Grade1: ")
        grade1 = float(input())

        print("Grade2: ")
        grade2 = float(input())

        print("Grade3: ")
        grade3 = float(input())

        students.append(Student(name, year, grade1, grade2, grade3))

    highest_avg_student = max(students, key=lambda student: student.average)

    print(f"The student with the highest average is:\n{highest_avg_student}")

if __name__ == "__main__":
    main()