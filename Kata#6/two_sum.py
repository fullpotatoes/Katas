
numbers = [2, 7, 11, 15]
target = 9

def twoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if target == numbers[i] + numbers[j]:
                return [i, j]

    return []

print(twoSum(numbers, target))


    # return indices des deux numbers

    # target  doit être égal à deux des chiffes de numbers


    #retourne [0, 1]
