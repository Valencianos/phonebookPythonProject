import text_fields as tf


def input_choice(size: int, message: str):
    while True:
        number = input(message)
        if number.isdigit() and 0 < int(number) < size + 1:
            return int(number)
        else:
            print(tf.wrong_choice(size))

def main_theme() -> int:
    print(*tf.menu, sep='\n')
    return input_choice(len(tf.menu) -1, tf.input_choice)

def show_contact(book: list[dict[str, str]], message: str):
    if book:
        print('\n' + '=' * 55)
        for i, contact in enumerate(book, 1):
            print(f'{i:<3} | {contact["name"]:<30} | {contact["phone"]:<15}')
        print('=' * 55 + '\n')
    else:
        print(message)

def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')

def input_contact(message: list[str]) -> dict[str, str]:
    contact = {}
    name = input(message[0])
    phone = input(message[1])
    if name:
        contact['name'] = name
    if phone:
        contact['phone'] = phone
    return contact

def input_index(message: str, pb: list) -> int:

    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(pb) + 1:
            return int(index)

def input_search(message) -> str:
    return input(message)