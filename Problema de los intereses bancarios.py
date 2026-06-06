def interes(capital, tasa, years):
    # dp[i] = capital al final del año i
    dp = [0.0] * (years+1)
    dp[0] = capital
    for i in range(1, years+1):
        dp[i] = round(dp[i-1] * (1 + tasa), 2)
    return dp
 
print("9. Intereses bancarios")
resultado = interes(1000, 0.05, 5)
for i, val in enumerate(resultado):
    print(f"  año {i}: S/ {val}")
print()