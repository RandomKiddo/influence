class Fraction:
        def __init__(self, num, denom):
                self.num = num
                self.denom = denom
        def simplify(self):
                current_value = 1
                while (current_value <= self.denom):
                        if self.num % current_value == 0 and self.denom % current_value == 0:
                                self.num = self.num / current_value
                                self.denom = self.denom / current_value
                        current_value += 1
        def __float__(self):
                return float(self.num) / float(self.denom)
        def __int__(self):
                return int(self.num / self.denom)
        def __str__(self):
                return f'{self.num}/{self.denom}'
        def equals(self, other):
                if (self.num == other.num and self.denom == other.denom) or (self.float() == other.float()):
                        return True
                return False
        def compare_to(self, other):
                return self.int() - other.int()
        def to_mixed_number(self):
                coeff = 0
                copy = self.num
                while copy > self.denom:
                        copy -= self.denom
                        coeff += 1
                if coeff == 0:
                        return MixedNumber(0, self.num, self.denom)
                return MixedNumber(coeff, self.num, self.denom)
        def __lt__(self, other):
                if self.__float__() < other.__float__():
                        return True
                return False
        def __lte__(self, other):
                if self.__float__() <= other.__float__():
                        return True
                return False
        def __eq__(self, other):
                if self.__float__() == other.__float__():
                        return True
                return False
        def __gt__(self, other):
                if self.__float__() > other.__float__():
                        return True
                return False
        def __gte__(self, other):
                if self.__float__() >= other.__float__():
                        return True
                return False
