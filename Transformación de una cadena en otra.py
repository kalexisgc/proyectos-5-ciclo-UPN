def distancia_edit(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],    # eliminar
                                    dp[i][j-1],    # insertar
                                    dp[i-1][j-1])  # reemplazar
    return dp[n][m]
 
print("8. Transformacion de cadena")
print('  "kitten" -> "sitting" =', distancia_edit("kitten", "sitting"), "operaciones")
print('  "perro"  -> "gato"    =', distancia_edit("perro", "gato"), "operaciones")
print()