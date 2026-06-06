def vacas(n, dias):
    # dp[i] = max vacas al dia i
    # cada vaca tarda 'dias' en dar cria, la cria tambien produce
    dp = [0] * (n+1)
    dp[0] = 1  # empieza con 1 vaca
    for i in range(1, n+1):
        dp[i] = dp[i-1]  # las vacas que ya habia
        if i >= dias:
            dp[i] += dp[i - dias]  # las crias nuevas
    return dp[n]
 
print("10. Problema de las vacas")
print("  vacas al dia 10 (cria cada 3 dias) =", vacas(10, 3))
print("  vacas al dia 20 (cria cada 3 dias) =", vacas(20, 3))
print("  vacas al dia 30 (cria cada 3 dias) =", vacas(30, 3))