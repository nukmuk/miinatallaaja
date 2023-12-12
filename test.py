def calculate_discriminant(factor_1, factor_2, constant):
    discriminant = factor_2**2 - 4 * factor_1 * constant
    return discriminant


print(calculate_discriminant(5 - 8, 4 * 3, 13))
