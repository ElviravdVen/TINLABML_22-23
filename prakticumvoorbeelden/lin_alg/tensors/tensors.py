from abc import ABC, abstractmethod
from collections import Counter

# Inherits from Abstract class
class Tensor(ABC):
    """
    Abstract SuperClass to create Tensor Classes
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getDimensions(self):
        """
        :return: rows x columns
        """

    # Decorator
    @abstractmethod
    def __add__(self, other):
        """
        Addition of this Tensor with other Tensor
        :return: Tensor
        """    

    @abstractmethod
    def __mul__(self, other):
        """
        Multiplication of this Tensor with other Tensor
        :return: Tensor
        """    

    @abstractmethod
    def __str__(self):
        """
        String representation of this Tensor
        :return: str
        """

# Inherits from Tensor
class Scalar(Tensor, float):
    """
    Class to generate 1x1 Tensor objects
    overriding abstract methods of SuperClass Tensor
    """

    def __init__(self, val):
        self = val

    def getDimensions(self):
        # Scalars are always 1 x 1
        return (1, 1)

    def __add__(self, other):
        """
        :param other: Scalar
        :return: Scalar
        """
        return Scalar( float(self) + float(other) )

    def __mul__(self, other):
        """
        :param other: Scalar
        :return: Scalar
        """
        return Scalar( float(self) * float(other) )

    def __str__(self):
        return str( float(self) )


# Inherits from Tensor
class Vector(Tensor, tuple):
    """
    Class to generate nr_of_rows x 1 Tensor objects
    overriding abstract methods of SuperClass Tensor
    """

    def __init__(self, numList):
        # Define Vector as a tuple of Scalars
        self = (Scalar(num) for num in numList)
    
    def getDimensions(self):
        # Return number of scalars x 1
        return ( len([scalar for scalar in self]), 1)

    def __add__(self, other):
        """
        :param other: Vector
        :return: Vector
        """

        # Check if vectors have equal length        
        if self.getDimensions() != other.getDimensions():
            return None
        else:
            return Vector(float(a+b) for (a, b) in zip(self, other))
    
    def __mul__(self, other):
        """
        :param other: Vector
        :return: Scalar
        """

        # Check if vectors have equal length        
        if self.getDimensions() != other.getDimensions():
            return None
        else:
            # Inner Vector Product
            return sum(float(a*b) for (a, b) in zip(self, other))

    def __str__(self):
        return str( [float(scalar) for scalar in self] )
    
    
class Matrix(Tensor, list):
    
    def __init__(self, listOfnumLists):
        # Define Matrix as a list of Vectors
        for numList in listOfnumLists:
            self.append( Vector(numList) )

    def getDimensions(self):
        # Return number of RowVectors x number of ColVectors
        pass
        
    def getRow(self, i):
        # Return Row Vector
        return self[i]
    
    def getColumn(self, j):
        # Return Column Vector
        return Vector( [row[j] for row in self] )