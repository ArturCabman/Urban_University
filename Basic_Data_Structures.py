grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_sort = sorted(students)
grad_1 = (grades[0])
grad_sum_1 = sum(grad_1) / len(grad_1)
grad_2 = (grades[1])
grad_sum_2 = sum(grad_2) / len(grad_2)
grad_3 = (grades[2])
grad_sum_3 = sum(grad_3) / len(grad_3)
grad_4 = (grades[3])
grad_sum_4 = sum(grad_4) / len(grad_4)
grad_5 = (grades[4])
grad_sum_5 = sum(grad_5) / len(grad_5)
diction = ((grad_sum_1), (grad_sum_2), (grad_sum_3), (grad_sum_4), (grad_sum_5))
stud_numb = (tuple(stud_sort))
grad_numb = (tuple(diction))
dictionary = dict(zip(stud_numb, grad_numb))
print(dictionary)
