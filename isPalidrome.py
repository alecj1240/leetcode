class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        arr = [int(d) for d in str(x)]
        pointer1 = 0
        pointer2 = len(arr) - 1
        
        while pointer1 < pointer2:            
            if arr[pointer1] == arr[pointer2]:
                pointer1 += 1
                pointer2 -= 1
            else:
                return False
            
        return True
