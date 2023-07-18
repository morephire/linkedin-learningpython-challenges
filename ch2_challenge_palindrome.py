def is_palindrome(str) -> bool:
    if str == str[::-1]:
        return True
    return False

def string_sanitizer(str) -> str:
    # string is sanitized: no spaces or special char
    return ''.join(e for e in str if e.isalnum()).lower()

while True:
    str = input("Enter a string to test or 'exit':")

    if str == 'exit':
        break

    cmp = string_sanitizer(str.lower())   
    print("Palindrome test:", is_palindrome(cmp))
    