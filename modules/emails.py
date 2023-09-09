# Osint a un email utilizando socialscan y dorking

import os
import time
from googlesearch import search
import random
import re

class Colores:
  red="\033[31;1m"
  verde="\033[92m"
  azul="\033[94m"
  magenta="\033[36m"
  amarillo="\033[33m"

def main():
    email = input(f'\n{Colores.azul}[~] Введите адрес электронной почты: ')
    if email == "" or email == " ":
        print(f'\n{Color.red}[!] Ошибка, вы должны ввести адрес электронной почты.')
        time.sleep(2)
        main()
    else:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if (re.fullmatch(regex, email)):
            print(f'\n{Colores.verde}[?] Действительный адрес электронной почты: ✔️')
        else:
            print(f'\n{Colores.red}[!] Неверный адрес электронной почты')
            exit()
    dom = ["com","com.tw","co.in","be","de","co.uk","co.ma","dz","ru","ca"]
    tld = random.choice(dom)
    command = f'intext:{email}'
    command2 = f"site:@ filetype:PDF intext:{email}"
    command3 = f"site:facebook.com intext:{email}"
    command4 = f"site:twitter.com intext:{email}"
    command5 = f"site:instagram.com intext:{email}"
    for j in search(command, tld, num=10, stop=10, pause=2):
        print(f'\nРезультаты найдены!: {j}')
    print(f'\n{Colores.azul}[~] Поиск электронной почты в файлах PDF...')
    time.sleep(3)
    for i in search(command2, tld, num=10, stop=10, pause=2):
        print(f'\nРезультаты найдены!: {i}')
    print(f'\n{Colores.amarillo}[~] Поиск почты в социальных сетях...')
    for a in search(command3, tld, num=10, stop=10, pause=2):
        print(f'\nРезультаты найдены!: {a}')
    for b in search(command4, tld, num=10, stop=10, pause=2):
      print(f'\nРезультаты найдены!: {b}')
    for c in search(command5, tld, num=10, stop=10, pause=2):
      print(f'\nРезультаты найдены!: {c}')
    print(f'\n{Colores.verde}[~] Запуск социального сканирования...')
    time.sleep(3)
    print('')
    os.system(f"socialscan {email}")
    print(f'\n{Colores.azul}[~] Сканирование завершено.')

main()
