def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            negative = True
        string = str(abs(x))
        outputString = string[::-1]
        if negative:
            outputString = '-' + outputString
        output = int(outputString)
        
        if output < (-2**31) or output > ((2**31)-1):
            return 0
        
        return output