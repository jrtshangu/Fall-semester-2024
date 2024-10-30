#opening the file
with open("hr_system.txt") as hr:
    seperation = hr.split(" ")
    name = seperation[0]
    id_number = seperation[1]
    job_title = seperation[2]
    salary = seperation[3]
    salary_bonus = salary + 1000

    analyzed_data = f"{name} (ID: {id_number}), {job_title.capitalize()} - ${salary}"
    print(salary)
