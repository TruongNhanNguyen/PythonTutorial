from math import sqrt, acos


class Vector:
    """ Represent a vector in the multidimensional space """

    def __init__(self, dimensions):
        """ Create d-dimensional vector of zeroes """
        self._coords = [0]*dimensions

    def __len__(self):
        """ Return the dimension of the vector """
        return len(self._coords)

    def __getitem__(self, index):
        """ Return j-th coordinate of vector """
        return self._coords[index]

    def __setitem__(self, index, value):
        """ Set j-th coordinate of vector to given value """

        if not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric type")

        self._coords[index] = value

    def __add__(self, other):
        """ Return sum of two vectors """

        if len(self) != len(other):  # rely on __len__() method
            raise ValueError("Dimensions must be agree")

        result = Vector(len(self))  # begin with zeroes-vector

        for index in range(len(self)):
            result[index] = self[index] + other[index]
        return result

    def __sub__(self, other):
        """ Return subtraction of two vectors """

        if(len(self) != len(other)):
            raise ValueError("Dimensions must be agree")

        result = Vector(len(self))

        for index in range(len(self)):
            result[index] = self[index] - other[index]
        return result

    def __eq__(self, other):
        """ Return true if vectors have same coordinates as other """
        return self._coords == other._coords

    def __ne__(self, other):
        """ Return true if vector differ from other """
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """ Procedure string representation of vector """
        return "<" + str(self._coords)[1:-1] + ">"  # adapt list representation

    def setVector(self, compLists):
        """ Assign values for vector's components from given list"""

        if len(self) != len(compLists):
            raise ValueError("Dimensions must be agree")

        self._coords = compLists

    def norm(self):
        """ Return length of vector """

        result = sqrt(sum(x * x for x in self._coords))
        return result

    def scalarProduct(self, other):
        """ Return scalar product of two vector """

        if len(self) != len(other):
            raise ValueError("Dimensions must be agree")

        result = sum(self[index] * other[index] for index in range(len(self)))
        return result

    def angleWith(self, other):
        """ Return angle between self and other in radian (from 0 to 2pi)"""

        result = (self.scalarProduct(other)) / (self.norm() * other.norm())
        return acos(result)


if __name__ == '__main__':
    u = Vector(4)
    v = Vector(4)
    u.setVector([1, 0, 1, 3])
    v.setVector([1, 1, 2, 0])

    add, sub, length_u, length_v, scalProd, angle_u_v = u + v,\
    u - v, u.norm(), v.norm(), u.scalarProduct(v), u.angleWith(v)

    print("u = ", u)
    print("v = ", v)
    print("u + v = ", add)
    print("u - v = ", sub)
    print("|u|  = ", length_u)
    print("|v| = ", length_v)
    print("u.v = ", u.scalarProduct(v))
    print("(u, v) = ", angle_u_v, "(rad)")
    