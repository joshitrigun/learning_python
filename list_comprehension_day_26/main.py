name = "Trigun"
#
# array_2 = []
#
# for a in array_1:
#     new_add = a + 1
#     array_2.append(new_add)
#
# print(array_2)
#
# new_arr1 = [item for item in name]
#
# print(new_arr1)

#
# primes = [num for num in range(2, 20) if
#           True not in [True for divisor in range(2, (int(num / 2) + 1)) if num % divisor == 0 and num != 2]]
#
# print(primes)
import random
names = ["sanu", "rita", "trija", "tripti", "trigun", "zaha", "sarthak", "saisa", "sagun"]


student_scores = {student: random.randint(80, 100) for student in names}

excellent_students = {student:score for (student, score) in student_scores.items() if score >= 90}
print(excellent_students)