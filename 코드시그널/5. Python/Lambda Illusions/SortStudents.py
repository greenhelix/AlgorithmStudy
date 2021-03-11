def sortStudents(students):
    students.sort(key=lambda x: x.split()[-1])
    print("John Smith".split()[-1])  # Smith
    return students


sample = ["John Smith",
          "Jacky Mon Simonoff",
          "Lucy Smith",
          "Angela Zimonova"]
print(sortStudents(sample))
