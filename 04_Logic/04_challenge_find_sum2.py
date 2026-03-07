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