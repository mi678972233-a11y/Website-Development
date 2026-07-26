def SeiveofEratosthenes(num):
    prime = [True for i in range(num + 1)]
    p = 2
    while p * p <= num:
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2,num+1):
        if prime[p]:
            print(p)
num = (int(input("Enter a number")))
print("Following Are The Prime Numbers Smaller")
print("than or equal to",num)
SeiveofEratosthenes(num)

  



    