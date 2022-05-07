import math as m

class complex_number():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'{self.real} + {self.imag}i'

    @staticmethod # This is the staticmethod decorator, which transforms the method into a static one.
    def conj(c):
        '''Returns the conjugate of the complex number c'''
        return complex_number(c.real, -c.imag)

    @staticmethod
    def mod(c):
        '''Returns the modulos of the complex number c'''
        return m.sqrt((c.real)**2 + (c.imag)**2)

    @staticmethod
    def csum(c1,c2):
        '''Returns the sum/subtraction of two complex numbers (c1 and c2)'''
        return complex_number(c1.real + c2.real, c1.imag + c2.imag)
    
    @staticmethod
    def cmult(c1,c2):
        '''Returns the multiplication of two complex numbers (c1 and c2)'''
        return complex_number(c1.real*c2.real - c1.imag*c2.imag, c1.real*c2.imag + c1.imag*c2.real)

    @staticmethod
    def cdiv(c1,c2):
        '''Returns the division of two complex numbers: c1/c2'''
        num = complex_number.cmult(c1, complex_number.conj(c2))
        return complex_number(num.real/(complex_number.mod(c2))**2 , num.imag/((complex_number.mod(c2))**2))

    @staticmethod
    def carg(c):
        '''Returns the argument (angle) of the complex number c'''
        return m.atan(c.imag/c.real)

    @staticmethod
    def print_cis(c):
        '''Prints the complex number in its p*cis form: mod*(cos(arg) + i*sin(arg))'''
        print(f"{complex_number.mod(c)}*(cos({complex_number.carg(c)}) + i*sin({complex_number.carg(c)}))")