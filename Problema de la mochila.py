def mochila(pesos, valores, capacidad):
    n = len(pesos)
    dp = [[0]*(capacidad+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(capacidad+1):
            dp[i][w] = dp[i-1][w]
            if pesos[i-1] <= w:
                opcion = dp[i-1][w - pesos[i-1]] + valores[i-1]
                if opcion > dp[i][w]:
                    dp[i][w] = opcion
    return dp[n][capacidad]
 
print("5. Problema de la mochila")
pesos   = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
cap = 8
print(f"  pesos={pesos}, valores={valores}, capacidad={cap}")
print("  valor maximo =", mochila(pesos, valores, cap))
print()