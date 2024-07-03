import matplotlib.pyplot as plt
import numpy as np
from functools import cmp_to_key

percent_luck = 0.5
acceptance_rate = 0.08

applied_students = 10000
accepted_students = int(applied_students*acceptance_rate)

average_skill = 0.5
std_dev = 0.15

num_simulations = 100

# simulation_output_file = open('.\\simulation_data.txt','w')

class Student:
    student_skill = 0
    student_luck = 0
    student_overall = 0

    def __init__(self):
        self.student_skill = np.random.normal(average_skill,std_dev)
        self.student_luck = np.random.default_rng().random()
        self.student_overall = (percent_luck)*(self.student_luck) + (1 - percent_luck)*(self.student_skill)

simulation_averages_admitted_skill = []
simulation_averages_admitted_luck = []
simulation_averages_top20_skill = []
simulation_averages_top20_luck = []
simulation_average_threshold = []

simulation_std_admitted_skill = []
simulation_std_admitted_luck = []
simulation_std_top20_skill = []
simulation_std_top20_luck = []

for _ in range(0,num_simulations):
    student_list = []

    for __ in range(0,applied_students):
        student_list.append(Student())

    def compare_by_overall(student1, student2):
        return student2.student_overall - student1.student_overall

    student_list = sorted(student_list, key=cmp_to_key(compare_by_overall))

    admitted_students = student_list[0:accepted_students]
    top_20pct_not_admitted = student_list[accepted_students+1:6*accepted_students+1]

    admitted_students_skill = [s.student_skill for s in admitted_students]
    admitted_students_luck = [s.student_luck for s in admitted_students]
    top_20_skill = [s.student_skill for s in top_20pct_not_admitted]
    top_20_luck = [s.student_luck for s in top_20pct_not_admitted]
    threshold = admitted_students[-1].student_overall

    simulation_averages_admitted_skill.append(np.average(admitted_students_skill))
    simulation_averages_admitted_luck.append(np.average(admitted_students_luck))
    simulation_averages_top20_skill.append(np.average(top_20_skill))
    simulation_averages_top20_luck.append(np.average(top_20_luck))
    simulation_average_threshold.append(threshold)

    simulation_std_admitted_skill.append(np.std(admitted_students_skill))
    simulation_std_admitted_luck.append(np.std(admitted_students_luck))
    simulation_std_top20_skill.append(np.std(top_20_skill))
    simulation_std_top20_luck.append(np.std(top_20_luck))

average_threshold = np.average(simulation_average_threshold)

average_skill = np.average(simulation_averages_admitted_skill)

print(average_skill)

skill_range = np.linspace(0,1)
probability = 1 - ((average_threshold - (skill_range)*(1 - percent_luck))/ percent_luck)

plt.figure(figsize=(8, 6))
plt.plot(skill_range, probability)
plt.title('Skill vs. Probability')
plt.legend()
plt.grid(True)
plt.show()