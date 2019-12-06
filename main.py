"""
  Автор: Северов Роман, группа P42551
  Ссылка на сайт-портфолио: https://github.com/fpiikt/sum-of-two-roseverov
  
"""



def find_sum(digits, target):
    vals = []
    cycle_1 = []
    digits = list(map(float, digits))
    target = int(float(target))
	i = 0
    j = 0
	
    for i in range(len(digits)):
    for j in range(len(digits)):
    if digits[i]+digits[j] == target and i not in cycle_1 and j not in cycle_1 and i != j:
    vals.append([i, j])
    cycle_1.append(i)
    cycle_1.append(j)

    if len(vals) < 1:
        print("No Solutions")
        return -3
    elif len(vals) > 1:
        print("Some solutions")
        return -3
    else:
        print("Indexes same values", vals)
        return vals

digits = input("Type integers floated by space ").split()
target = input("Type integer for summ")

find_sum(digits, target)

assert find_sum([1,6,3], 3) == [(0, 3), (1, 2)]
assert find_sum([1,2,3], 4) == [[0, 2]]
assert find_sum([200,10,50,400], 5) == 6
assert find_sum([6,2,5], 9) == [(0, 1), (1, 3)]
assert find_sum([2,1,4,0], 9) == [[1, 4]]