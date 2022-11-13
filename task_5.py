import random
import string

def get_random_password() -> str:
    ...  # TODO написать функцию генерации случайных паролей
    n = 8
    passw = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, n)
    password = "".join(passw)  # убираем соединительные символы
    return password

print(get_random_password())
