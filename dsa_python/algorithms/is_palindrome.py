def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def is_palindrome_two_ptr(s: str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] == s[right]:
            left, right = left + 1, right - 1
        else:
            return False
    return True

if __name__ == '__main__':
    print('REVERSE STRING APPROACH')
        
    print(is_palindrome('abba'))
    print(is_palindrome('racecar'))
    print(is_palindrome('truck'))
    
    print('TWO POINTER APPROACH')
    
    print(is_palindrome_two_ptr('abba'))
    print(is_palindrome_two_ptr('racecar'))
    print(is_palindrome_two_ptr('truck'))