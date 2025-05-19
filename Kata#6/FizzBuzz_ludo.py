




def fizzBuzz(n):
    answer = []
    answer.extend([""] * n)
    for i in range(1, n):
        if i % 3 == 0 and i % 5 == 0:
            answer[i] = "FizzBuzz"
        elif i % 3 == 0:
            answer[i] = "Fizz"
        elif i % 5 == 0:
            answer[i] = "Buzz"
        else:
            answer[i] = str(i)
    print(answer)

print(fizzBuzz(3))
print(fizzBuzz(5))
print(fizzBuzz(15))






