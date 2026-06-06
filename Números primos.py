def primos(n):
    dp = [True] * (n+1)
    dp[0] = dp[1] = False
    for i in range(2, int(n**0.5)+1):
        if dp[i]:
            for j in range(i*i, n+1, i):
                dp[j] = False
    return [i for i in range(n+1) if dp[i]]
 
print("2. Numeros primos hasta 50")
print(" ", primos(50))
print()
 