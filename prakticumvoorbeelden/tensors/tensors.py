from abc import ABC, abstractmethod


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
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

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

    def __init__(self, val=0):
        self = val

    def __add__(self, other):
        return Scalar( float(self) + float(other) )

    def __mul__(self, other):
        return Scalar( float(self) * float(other) )

    def __str__(self):
        return str( float(self) )


# Inherits from Tensor
class Vector(Tensor, list):
    """
    Class to generate nr_of_rows x 1 Tensor objects
    overriding abstract methods of SuperClass Tensor
    """

    def __init__(self, numbers=None):
        # Define Vector as a list of Scalars
        if numbers is None:
            self.value = list()
        else:
            self.value = numbers

        self.value = numbers.copy() if numbers is not None else []

        if numbers is not None:
            for number in numbers:
                self.append(Scalar(number))

    def __len__(self):
        return len(self.getValue())

    def __add__(self, other):
        """
        :param other: Vector
        :return: Vector
        """
        # Check if vectors have equal length

    def __mul__(self, other):
        pass

    def __str__(self):
        vectorString = "["

        for val in self.getValue():
            vectorString = f"{vectorString}{val} "

        vectorString = f"{vectorString}]"

        return vectorString.replace(" ]", "]")


if __name__ == "__main__":
    print(Vector([0, 1]))