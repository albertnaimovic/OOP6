# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height

#     def area(self) -> float:
#         return self.width * self.height

#     @classmethod
#     def from_square(cls, side_length: float) -> "Rectangle":
#         return cls(side_length, side_length)


# rectangle1: Rectangle = Rectangle(3.0, 4.0)
# rectangle2: Rectangle = Rectangle.from_square(2.0)

# print(rectangle1.area())  # 12.0
# print(rectangle2.area())  # 4.0


# import datetime


# class Person:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(cls, name: str, birth_year: int) -> "Person":
#         age = cls.get_age(birth_year)
#         return cls(name, age)

#     @staticmethod
#     def get_age(birth_year: int) -> int:
#         return datetime.date.today().year - birth_year


# person: Person = Person.from_birth_year("John", 1990)
# print(person.name)  # John
# print(person.age)  # 33


# class Car:
#     total_cars_sold: int = 0

#     def __init__(self, make: str, model: str):
#         self.make = make
#         self.model = model
#         Car.total_cars_sold += 1

#     def get_model(self) -> str:
#         return self.model

#     @classmethod
#     def get_total_cars_sold(cls) -> int:
#         return cls.total_cars_sold


# car1: Car = Car("Toyota", "Camry")
# print(car1.get_model())
# print(car1.model)
# car2: Car = Car("Honda", "Civic")

# print(Car.get_total_cars_sold())  # 2
# print(Car.total_cars_sold)


# class Point:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y

#     @classmethod
#     def from_tuple(cls, point_tuple: tuple[float, float]) -> "Point":
#         x, y = point_tuple
#         return cls(x, y)

#     @staticmethod
#     def get_coordinates(coordinates: tuple[float, float]) -> tuple:
#         x, y = coordinates
#         return x + 25, y + 25


# point: Point = Point.from_tuple((3, 4))
# print(point.x)  # 3
# print(point.y)  # 4


class Student:
    all_students: list["Student"] = []

    def __init__(self, name: str, grade: float):
        self.name = name
        self.grade = grade
        Student.all_students.append(self)

    @classmethod
    def get_highest_grade(cls) -> "Student":
        return max(cls.all_students, key=lambda student: student.grade)

    @classmethod
    def get_lowest_grade(cls) -> "Student":
        return min(cls.all_students, key=lambda student: student.grade)


student1: Student = Student("John", 90)
student2: Student = Student("Jane", 95)
student3: Student = Student("Alice", 80)

print(Student.get_highest_grade().name)  # Jane
print(Student.get_lowest_grade().name)  # Alice

