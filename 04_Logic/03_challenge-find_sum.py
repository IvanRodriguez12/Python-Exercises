"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. 
Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def find_first_sum(nums, goal):
    for i in nums:
       for j in range(i + 1, len(nums)):
           if nums[i] + nums[j] == goal:
               print(f"Los numeros que alcanzan la meta de {goal} estan en la posicion {i} y {j}")
           else:
               print(None)


nums = [4, 5, 6, 2]
goal = 8
find_first_sum(nums, goal) 