student = {"name":"yokota","age":23}
student["age"] = 25
print(student)
student["hobby"] = "baseball"
print(student)
del student["hobby"]
print(student)

name = student.pop("name")
print(student)
print(name)