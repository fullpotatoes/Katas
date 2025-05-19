ma_liste = ['pomme', 'banane', 'cerise']

# Utilisation de len() pour parcourir les indices
for i in range(len(ma_liste)):
    print(f"Index {i} : {ma_liste[i]}")

for i, fruit in enumerate(ma_liste):
    print(f"Index {i} : {fruit}")