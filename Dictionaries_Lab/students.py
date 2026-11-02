student_dict = {}
command = input()
while ":" in command:
    info = command.split(":")
    name, id, course = info[0], info[1], info[2]
    if course not in student_dict:
        student_dict[course] = {}
    student_dict[course][id] = name
    command = input()

course = " ".join(command.split("_"))
for key, value in student_dict.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")