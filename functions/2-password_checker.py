#check whether password is strong or not

def is_strong_password(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*+_' for char in password):
        return False
    return True
#function calling
print(is_strong_password('Manasa@renu'))
print(is_strong_password('Manasa@617'))
