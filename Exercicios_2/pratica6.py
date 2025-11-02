num = [1,2,3,75,4,5,8,7,15]
i=0
maior = 0
while i<len(num): 
    if maior < int(num[i]):
        maior = int(num[i])
    i+=1

print(f"O maior valor é: {maior}")