import random

def QS_random(li):
    if len(li) <= 1:
        return li
    pivot = random.choice(li)
    s = [x for x in li if x < pivot]
    eq = [x for x in li if x == pivot]
    l = [x for x in li if x > pivot]
    return QS_random(s) + eq + QS_random(l)

# Example usage with a fixed input list:
li = [4, 2, 7, 1, 9, 3, 6, 8, 5, 0]

res = QS_random(li)

print(f"Input: {li} | Sorted list: {res}")
