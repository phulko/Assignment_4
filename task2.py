def get_successful_students(students_list, passing_score=60):
    result = {}

    for student in students_list:
        name = student["name"]
        scores = student["scores"]

        passed = True
        total = 0
        count = 0

        for subject in scores:
            score = scores[subject]

            if score < passing_score:
                passed = False
            total += score
            count += 1

        if passed:
            avg = total / count
            result[name] = round(avg, 2)

    return result

students_math_results = [
    {"name": "Олександр",
     "scores":
        {
        "Calculus": 85,
        "Algebra": 90,
        "Discrete Math": 78
        }
     },
    {"name": "Марія",
     "scores":
        {
        "Calculus": 65,
        "Algebra": 55,
        "Discrete Math": 70
        }
     },
    {"name": "Іван",
     "scores":
        {
        "Calculus": 92,
        "Algebra": 88,
        "Discrete Math": 95
        }
     },
    {"name": "Анна",
     "scores":
        {
        "Calculus": 45,
        "Algebra": 60,
        "Discrete Math": 50
        }
     },
    {"name": "Перевірка_роботи_функції",
     "scores":
         {
         "Calculus": 60,
         "Algebra": 61,
         "Discrete Math": 60
         }
     }
]

successful_students = get_successful_students(students_math_results)
# print(successful_students)

for name in successful_students:
    avg = successful_students[name]
    print(f"Student: {name}")
    print(f"  Average score: {avg}\n")