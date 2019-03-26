#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть зашифрованное сообщение

secret_message = [
    '56муп7ы1ьу4и5ечту2цьчдп98влтмк',
    '36дхлкалхсемииф5няцум7иыгтчярсмс2ямепфг',
    'ншбвянляснзепкк9еср52д79м9с2мк',
    'с2ноопроктятидщв6охки3пшш8щьра',
    'и4мяобявььелроч3з6сааялруг8гзе8еаббр2'
]

# ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 14, через одну
#   четвертое слово - буквы с 8 по 14, в обратном порядке
#   пятое слово - буквы с 11 по 35, через две, в обратном порядке
#
# Требуется задать конкретные индексы, например secret_message[3][12:23:4]
# Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

word_1 = secret_message[0][3]
word_2 = secret_message[1][9:13]
word_3 = secret_message[2][5:14:2]
word_4 = secret_message[3][-17:-24:-1]
word_5 = secret_message[4][-3:-30:-3]

unsecret_message = word_1 + ' ' + word_2 + ' ' + word_3 + ' ' + word_4 + ' ' + ' ' + word_5

print(unsecret_message)

# зачет!