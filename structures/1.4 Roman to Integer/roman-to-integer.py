class Solution:
    def romanToInt(self, s: str) -> int:

        # Declare the essential arrays
        s_array = list(s)
        num_array = []

        # Convert roman letters to int
        for num in s_array:
            if num == "I":
                num_array.append(1)
            elif num == "V":
                num_array.append(5)
            elif num == "X":
                num_array.append(10)
            elif num == "L":
                num_array.append(50)
            elif num == "C":
                num_array.append(100)
            elif num == "D":
                num_array.append(500)
            elif num == "M":
                num_array.append(1000)
        
        # Essential algorithm variables
        previous = num_array[0] + 1
        result = 0
        index = 0

        # Identify the subtractions
        for fixed_num in num_array:
            if previous < fixed_num:
                num_array[index] = fixed_num - previous
                num_array[index - 1] = 0
            index += 1
            previous = fixed_num

        # Add the final result
        for add_num in num_array:
            result += add_num

        return result
