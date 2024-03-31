def decimal_to_olc20( num ):
    olc20_numerals = [ "23456789CFGHJMPQRVWX" ]
    
def convert_recursive( num, numerals ):
    if num == 0:
        return ""
    else:
        remainder = num % 20
        int_quotient = num // 20 
        return convert_recursive( int_quotient ) + olc20_numerals[ remainder ] 
    
    base20_string = convert_recursive(num)
    return base20_string

# Example usage:
decimal_num = 123456789
base20_string = decimal_to_olc20( decimal_num )
print( base20_string )