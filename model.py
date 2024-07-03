import pandas as pd
import numpy as np
import seaborn as sb
from functools import cmp_to_key

percent_luck = 0.25

applied_students = 5000
accepted_students = 200

average_skill = 0.5
std_dev = 0.15

num_simulations = 1000

class Student:
    student_skill = 0
    student_luck = 0
    student_overall = 0

    def __init__(self):
        self.student_skill = np.random.normal(average_skill,std_dev)
        self.student_luck = np.random.default_rng().random()
        self.student_overall = (percent_luck)*(self.student_luck) + (1 - percent_luck)*(self.student_skill)

student_list = []

for _ in range(0,applied_students):
    student_list.append(Student())

def compare_by_overall(student1, student2):
    return student2.student_overall - student1.student_overall

student_list = sorted(student_list, key=cmp_to_key(compare_by_overall))

for i in range(0,accepted_students):
    print(student_list[i].student_overall)