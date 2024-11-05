# Questão 5
import vector3d
vector1 = vector3d.vector([3, 2, 1])
vector2 = vector3d.vector([1, 2, 3])
print(vector1)
print(vector2)
print((vector1 * (vector1.dot_product(vector2))).dyadic_product(vector2))
print(vector2 * 5 - 2 * vector1)
print(vector1.dot_product(vector1 + vector2))
print(vector1.dot_product(vector2))