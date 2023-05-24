# Precedência entre os operadores aritméticos
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = 1 + 1 ** 5 + 5
conta_2 = (1 + 1) ** (5 + 5)
print(conta_1, conta_2)