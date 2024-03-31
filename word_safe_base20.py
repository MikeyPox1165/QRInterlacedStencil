def decimal_to_word_safe_base20(num):
    base20_words = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    
    def convert_recursive(num):
        if num == 0:
            return ""
        else:
            remainder = num % 20
            return convert_recursive(num // 20) + base20_words[remainder] + " "
    
    base20_string = convert_recursive(num)
    return base20_string.strip()

# Example usage:
decimal_num = 123456789
base20_string = decimal_to_word_safe_base20(decimal_num)
print(base20_string)