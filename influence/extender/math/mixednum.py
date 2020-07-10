class MixedNumber:
        def __init__(self, coeff, num, denom):
                self.coeff = coeff
                self.num = num
                self.denom = denom
                self.fraction = Fraction(num, denom)
        def simplify(self):
                current_value = 1
                while (current_value <= self.denom):
                        if self.num % current_value == 0 and self.denom % current_value == 0:
                                self.num /= current_value
                                self.denom /= current_value
                        curent_value += 1
                while self.num >= self.denom:
                        self.num -= self.denom
                        self.coeff += 1
                self.fraction = Fraction(self.num, self.denom)
                self.fraction.simplify()
        def __float__(self):
                return float(self.coeff * self.denom + self.num) / float(self.denom)
        def __int__(self):
                return int((self.coeff * self.denom + self.num) / self.denom)
        def __str__(self):
                return f'{self.coeff} {self.num}/{self.denom}'
        def equals(self, other):
                if (self.coeff == other.coeff and self.num == other.num and self.denom == other.denom) or (self.float() == other.float()):
                        return True
                return False
        def compare_to(self, other):
                return self.int() - other.int()
        def to_fraction(self):
                new_num = self.coeff * self.denom + num
                return Fraction(new_num, self.denom)
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
