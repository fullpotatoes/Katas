numbers = [2, 7, 11, 15]
target = 9

def tree_sum(numbers, target):
    seen = {}
    for i in range(len(numbers)):
        current = numbers[i]
        complement = target - current
        if complement in seen:
            return [seen[complement], i]  # Retourne les indices
        seen[current] = i  # Enregistre le numéro actuel avec son index
    return []  # Retourne une liste vide si aucun résultat

print(tree_sum(numbers, target))