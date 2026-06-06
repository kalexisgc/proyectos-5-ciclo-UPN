def viaje_rio(costos):
    # costos[i][j] = costo de parar i hasta parar j
    n = len(costos)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            if dp[j] + costos[j][i] < dp[i]:
                dp[i] = dp[j] + costos[j][i]
    return dp[n-1]
 
print("7. Viaje mas barato por el rio")
# 4 paradas, costos entre ellas
costos = [
    [0,  3,  7,  15],
    [0,  0,  2,   8],
    [0,  0,  0,   3],
    [0,  0,  0,   0],
]
print("  costo minimo de parada 0 a 3 =", viaje_rio(costos))
print()
 
 