dog = {"name":"buddy", "color":"Black", "breed":"German Shepard", "legs":4, "age":3}
student = { "first_name":"Mythreyi", "last_name":"Nalluri", "gender":"female", "age":23, "marital_status":"Unmarried", "skills":["Python","Java"], "country":"India", "city":"Vijayawada", "address":"Bank Colony"}

print(len(student))
print(student["skills"],type(student["skills"]))
student["skills"].append("learning")
student["skills"].append("Cooking")
print(student.keys())
print(student.values())