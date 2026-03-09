def encontrar_suma_numeros(nums, goal):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                print(f"Se alcamzo el objetivo {goal} con la suma de los indices {i} y {j}")
            else:
                None



num = [2,3,7,4,5,6]
goal = 5
encontrar_suma_numeros(num,goal)


# Otra forma de hacerlo es usando un diccionario para guardar los numeros y sus indices, asi evitamos el doble for y reducimos la complejidad a O(n)

def encontrar_suma_numeros1(nums, goal):
    vistos = {}

    for index, value in enumerate(nums):
        no_visto = goal - vistos
        if no_visto in vistos: return [vistos[value], index]
        vistos[value] = no_visto

    return None 

num = [2,3,7,4,5,6]
goal = 5
encontrar_suma_numeros1(num, goal)