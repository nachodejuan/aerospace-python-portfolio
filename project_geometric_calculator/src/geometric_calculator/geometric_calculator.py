"""
Geometric Calculator

Demonstrates use of Abstract Base Classes for robust design.

Author: Nacho de Juan
Date: 04/09/2025
"""

from abc import ABC, abstractmethod
import math
from typing import Union

class GeometricShape(ABC):
    """
    Abstract Base Class for geometric shapes.
    Enforces implementation of core geometric methods.
    """
    
    @abstractmethod
    def area(self) -> float:
        """Calculate shape area. Must be implemented by subclasses."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Calculate shape perimeter. Must be implemented by subclasses."""
        pass

class Circle(GeometricShape):
    """Concrete implementation of a Circle."""
    
    def __init__(self, radius: Union[int, float]):
        """
        Initialize circle with radius validation.
        
        Args:
            radius: Positive radius of the circle
        Raises:
            ValueError: If radius is not positive
        """
        if radius <= 0:
            raise ValueError("Radius must be a positive number")
        self.radius = float(radius)
    
    def area(self) -> float:
        """Calculate circle area."""
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        """Calculate circle circumference."""
        return 2 * math.pi * self.radius