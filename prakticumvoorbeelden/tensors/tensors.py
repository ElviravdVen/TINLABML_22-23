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

    @abstractmethod
    def getDimensions(self):
        pass


# Inherits from Tensor
class Scalar(Tensor, float):
    """
    Class to generate 1x1 Tensor objects
    overriding abstract methods of SuperClass Tensor
    """

    def __init__(self, val):
        self = val

    def __add__(self, other):
        return Scalar( float(self) + float(other) )

    def __mul__(self, other):
        return Scalar( float(self) * float(other) )

    def __str__(self):
        return str( float(self) )

    def getDimensions(self):
        return (1, 1)

# Inherits from Tensor
class Vector(Tensor, tuple):
    """
    Class to generate nr_of_rows x 1 Tensor objects
    overriding abstract methods of SuperClass Tensor
    """

    def __init__(self, numList):
        # Define Vector as a list of Scalars
        self = (Scalar(num) for num in numList)
    
    def __len__(self):
        # Return number of scalars contained in this Vector
        return len( [scalar for scalar in self] )

    def __add__(self, other):
        """
        :param other: Vector
        :return: Vector
        """
        # Check if vectors have equal length        
        return Vector(float(a+b) for (a, b) in zip(self, other))
    
    def __mul__(self, other):
        pass

    def __str__(self):
        pass