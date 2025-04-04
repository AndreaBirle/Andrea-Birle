import hashlib

def get_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()

target_hash = "0e000d61c1735636f56154f30046be93b3d71f1abbac3cd9e3f80093fdb357ad"

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special_chars = "!@#$"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"

def backtrack(password, uppercase_count, digit_count, special_count, lowercase_count, recursive_calls):
    if len(password) == 6:
        if uppercase_count == 1 and digit_count == 1 and special_count == 1 and lowercase_count == 3:
            hashed_password = get_hash(password)
            if hashed_password == target_hash:
                print(f"Parola găsită: {password}")
                print(f"Număr apeluri recursive: {recursive_calls}")
                return True, recursive_calls
        return False, recursive_calls

    for char in uppercase_letters:
        if uppercase_count < 1:
            found, recursive_calls = backtrack(password + char, uppercase_count + 1, digit_count, special_count, lowercase_count, recursive_calls + 1)
            if found:
                return True, recursive_calls

    for char in digits:
        if digit_count < 1:
            found, recursive_calls = backtrack(password + char, uppercase_count, digit_count + 1, special_count, lowercase_count, recursive_calls + 1)
            if found:
                return True, recursive_calls

    for char in special_chars:
        if special_count < 1:
            found, recursive_calls = backtrack(password + char, uppercase_count, digit_count, special_count + 1, lowercase_count, recursive_calls + 1)
            if found:
                return True, recursive_calls

    for char in lowercase_letters:
        if lowercase_count < 3:
            found, recursive_calls = backtrack(password + char, uppercase_count, digit_count, special_count, lowercase_count + 1, recursive_calls + 1)
            if found:
                return True, recursive_calls

    return False, recursive_calls

def find_password():
    password = ""
    uppercase_count = 0
    digit_count = 0
    special_count = 0
    lowercase_count = 0
    recursive_calls = 0

    found, recursive_calls = backtrack(password, uppercase_count, digit_count, special_count, lowercase_count, recursive_calls)
    if not found:
        print("Parola nu a fost găsită.")

find_password()