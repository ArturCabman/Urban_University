grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
stud_sort = sorted(students)
grad_1 = (grades[0])
grad_sum_1 = sum(grad_1) / len(grad_1)
print(grad_1)
print(grad_sum_1)
stud_numb = (tuple(stud_sort))
grad_numb = (tuple(grades))
dictionary = dict(zip(stud_numb, grad_numb))
print(dictionary)
