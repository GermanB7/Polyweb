from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Fraction:
    numerator: int
    denominator: int
    
    def __post_init__(self):
        if self.denominator == 0:
            raise ValueError("El denominador no puede ser cero")
        # Normalizar la fracción (simplificar y hacer positivo el denominador)
        gcd = math.gcd(abs(self.numerator), abs(self.denominator))
        num = self.numerator // gcd
        den = self.denominator // gcd
        
        # Si el denominador es negativo, mover el signo al numerador
        if den < 0:
            num = -num
            den = -den
            
        # Usar object.__setattr__ para modificar campos frozen
        object.__setattr__(self, 'numerator', num)
        object.__setattr__(self, 'denominator', den)
    
    def __add__(self, other: Fraction) -> Fraction:
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)
    
    def __mul__(self, other: Fraction) -> Fraction:
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
    
    def __neg__(self) -> Fraction:
        return Fraction(-self.numerator, self.denominator)
    
    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"
    
    def is_zero(self) -> bool:
        return self.numerator == 0
    
    def is_one(self) -> bool:
        return self.numerator == self.denominator
    
    def is_negative_one(self) -> bool:
        return self.numerator == -self.denominator
    
    @classmethod
    def from_int(cls, value: int) -> Fraction:
        return cls(value, 1)
