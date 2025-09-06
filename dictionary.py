student = {
    "name" : ["Shahed",],
    "subject": {
        "physics": 80,
        "chem": 88,
        "math": 90
    }
}

print(student["subject"]["math"])
print (list(student.keys()))
print (list(student.values()))

new = {"city": "Dhaka",
                "country": "Bangladesh",
                "age": 23 }

student.update(new)

print(student)