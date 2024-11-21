import sqlite3
import os
import time
db_path = os.path.join(os.path.dirname(__file__), 'cipher_db.sqlite')
def get_cipher_dict_from_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cipher")
    rows = cursor.fetchall()
    cipher_dict = {}
    for row in rows:
        letter, phrase_1, phrase_2, phrase_3 = row
        phrases = [phrase_1]
        if phrase_2:
            phrases.append(phrase_2)
        if phrase_3:
            phrases.append(phrase_3)
        cipher_dict[letter] = phrases

    conn.close()
    return cipher_dict
def encrypt(message, cipher_dict):
    encrypted_message = []
    for char in message:
        if char.upper() in cipher_dict:
            encrypted_message.append(cipher_dict[char.upper()])
        else:
            encrypted_message.append([char])
    return encrypted_message
def decrypt(encrypted_message, cipher_dict):
    decrypted_message = []
    for word_list in encrypted_message:
        if len(word_list) == 1 and word_list[0].isalpha():
            decrypted_message.append(word_list[0])
        else:
            if word_list:
                for key, value in cipher_dict.items():
                    if word_list[0] in value:
                        decrypted_message.append(key)
                        break
                else:
                    decrypted_message.append('?')
            else:
                decrypted_message.append(' ')
    return ''.join(decrypted_message)

def main():
    cipher_dict = get_cipher_dict_from_db()
    print("введите текст")
    message = input()
    encrypted_message = encrypt(message, cipher_dict)
    data_str = '|'.join(' '.join(sublist) for sublist in encrypted_message)
    data_back = [sublist.split() for sublist in data_str.split('|')]
    decrypted_message = decrypt(data_back, cipher_dict)
    print("Исходное сообщение:", message)
    print("Зашифрованное сообщение:", data_str)
    print("Дешифрованное сообщение:", decrypted_message)
    print("Программа приостановлена. Нажмите Enter для выхода")
    try:
        input_timeout = input(">")
    except TimeoutError:
        time.sleep(10000)

if __name__ == "__main__":
    main()
