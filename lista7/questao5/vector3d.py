class vector:
    def __init__(self, inputs):
        self.coords = inputs

    def __str__(self):
        return str(self.coords)

    def __add__(self, other_vector):
        new_vector = vector([0, 0, 0])
        for i in range(3):
            new_vector.coords[i] = self.coords[i] + other_vector.coords[i]
        return new_vector
    
    def __sub__(self, other_vector):
        new_vector = vector([0, 0, 0])
        for i in range(3):
            new_vector.coords[i] = self.coords[i] + (other_vector.coords[i] * (-1))
        return new_vector
    
    def __mul__(self, scalar):
        new_vector = vector([0, 0, 0])
        for i in range(3):
            new_vector.coords[i] = scalar * self.coords[i]
        return new_vector
    
    def __rmul__(self, scalar):
        return self * scalar
    
    def dot_product(self, other_vector):
        product = 0
        for i in range(3):
            product += self.coords[i] * other_vector.coords[i]
        return product
    
    def dyadic_product(self, other_vector):
        product = []
        for i in range(3):
            product.append([])
            for j in range(3):
                product[i].append(self.coords[i] * other_vector.coords[j])
        return product

if __name__ == '__main__':
    vector1 = vector([5, 7, 9])
    vector2 = vector([1, 6, 2])
    dyadic = vector1.dyadic_product(vector2)
    print('V =', vector1, 'W =', vector2)
    print('V + 3W =', vector1 + (3 * vector2))
    print('5 * V =', 5 * vector1)
    print('W * 2 =', vector2 * 2)
    print('V - W =', vector1 - vector2)
    print('<V, W> =', vector1.dot_product(vector2))
    print('V x W =')
    for i in range(len(vector1.coords)):
        print(dyadic[i])