class Boolean:
    @staticmethod
    def bool2int(b):
        if(b) : return -1
        else : return 0
    
    @staticmethod
    def int2bool(i):
        if(i == 0) : return False
        elif(i == -1) : return True
        else :
            raise Exception("Error: operand no booleà (-1 o 0)")
    
    @staticmethod
    def _and(a,b):
        return Boolean.bool2int(Boolean.int2bool(a) and Boolean.int2bool(b))
    
    @staticmethod
    def _or(a,b):
        return Boolean.bool2int(Boolean.int2bool(a) or Boolean.int2bool(b))
    
    @staticmethod
    def _not(a):
        return Boolean.bool2int(not(Boolean.int2bool(a)))
    
    
        
    
    