class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        x_array = list(str(x))
        print(x_array)

        flipped_array = []
        flipped_index = -1
        print(flipped_array)
        
        for i in range(len(x_array)):
            flipped_array.append(x_array[flipped_index])
            flipped_index -= 1
        

        print(flipped_array)

        if x_array == flipped_array:
            return True
        else:
            return False
