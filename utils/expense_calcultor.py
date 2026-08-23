

class Calcultor:
    @staticmethod 
    def multiply(a:int, b:int)->int:
        """
        Multiply two integer

        Args:
         a (int): The first integer 
         b (int) : The second integer

        Returns:
            int : The product  of a and b .
        
        
        """
        return a*b
    @staticmethod
    def calculate_total(*x:float) ->float:
        """
        Calculate sum of the given   list of numbers

        Args:
         x (list) :List of floating numbers

        Returns :
            float : The sum of numbers in the list x
        
        """
        return sum(x)