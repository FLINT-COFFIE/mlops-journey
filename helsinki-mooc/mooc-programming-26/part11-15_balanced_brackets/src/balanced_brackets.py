
def balanced_brackets(my_string: str):
    filtered = "".join([bracket for bracket in my_string if bracket in "()[]"])
    
    def checks(char: str):
        if len(char) == 0:
            return True
        
        round = char[0] == "(" and char [-1] == ")"
        square = char[0] == "[" and char [-1] == "]"
        
        if not round or square:
            return False
        
        return checks(s[1:-1])
    return checks(filtered)
        