def binomial(n, k):
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
        for j in range(1, min(i,k)+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp[n][k]
 
print("3. Coeficientes binomiales")
print("  C(5,2) =", binomial(5,2))
print("  C(6,3) =", binomial(6,3))
print("  C(10,4) =", binomial(10,4))
print()
 