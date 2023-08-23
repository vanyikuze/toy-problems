def Constant(s):
    def constant_value(substring):
        return sum(ord(c) - ord('a') + 1 for c in substring)

    constant_substrings = []
    latest_substring = ''

    for latest in s:
        if latest not in "aeiou":
            latest_substring += latest
        else:
            if latest_substring:
                constant_substrings.append(latest_substring)
                latest_substring = ''
    if latest_substring:
        constant_substrings.append(latest_substring)
    
    max_value = 0
    for substring in constant_substrings:
        substring_value = constant_value(substring)
        if substring_value > max_value:
            max_value = substring_value

            return max_value
        
print(Constant("vany"))        