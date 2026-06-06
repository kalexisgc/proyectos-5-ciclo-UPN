def monedas(monedas_list, monto):
    dp = [float('inf')] * (monto+1)
    dp[0] = 0
    for i in range(1, monto+1):
        for m in monedas_list:
            if m <= i and dp[i-m] + 1 < dp[i]:
                dp[i] = dp[i-m] + 1
    return dp[monto] if dp[monto] != float('inf') else -1
 
print("4. Problema de las monedas")
print("  monedas [1,5,10], monto 27 ->", monedas([1,5,10], 27), "monedas")
print("  monedas [2,5,10], monto 3  ->", monedas([2,5,10], 3))
print()