names = ["Aarav", "Priya", "Dev", "Meera", "Kabir"]
scores = (90, 75, 88, 62, 95)
n = len(scores)
print("==== Score Tracker (n=" , n , ") ====")
for i in range(n):
    print("Name:", names[i], "| Score:",scores[i])
print()
steps = 1
print("Score at index", i, "is", list(scores)[i], "| steps = ", steps, "| Theta (1)-tight bound")
print()
target = "Aarav"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
    print("Found", target, "at index", list(names).index(target), "| steps = ", steps, "| Omega (1)-best case lower bound")
target = "Kabir"
steps = 0
for name in names:
    steps += 1
    if name == target:
        break
print("Found", target, "at index", list(names).index(target), "| steps = ", steps, "| O(n)-worst case upper bound")        
print()
steps = 0
target_sum = 150
print("Looking for a pair of scores that sum to", target_sum)
for i in range(n):
    for j in range(i + 1, n):
        steps += 1
        if (scores)[i] + (scores)[j] == target_sum:
            print(" ", names[i], "(", (scores)[i], ") +", names[j], "(", (scores)[j], ")")
print("Total Comparisons:", steps , "| O(n^2)-drop constants,keep n^2")
print()
print("===Asymptotic Summary===")
print("Theta (1) : index access - always 1 step tight bound")
print("Omega (1) : best case - found in 1 step , lower bound")
print("O(n) : worst case - found after n =" , n , "steps, upper bound")
print("O(n^2) : pair check - worst case - n^2 =" , n**2 , "steps, upper bound")
print()
print("Drop Constants. Keep the dominant term. That is asymptotic analysis !")
