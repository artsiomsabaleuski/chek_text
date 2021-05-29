
import pymorphy2 as pymorphy2



def pos(word, morth=pymorphy2.MorphAnalyzer()):

    return morth.parse(word)[0].tag.POS
words, words_1 = input(), input()
functors_pos = {'PREP'}  # функция для удаления предлогов
text_words = "".join(word for word in words if pos(word) not in functors_pos) # удалили предлоги и пробелы для первого input(). Цифры оставляем.
text_1 = "".join(i for i in text_words if i.isalnum())  # удалили любые символы кроме текста и буквы в первом inpute()
text_words_1 = "".join(word for word in words_1 if pos(word) not in functors_pos)  # удалили предлоги и пробелы для второго input(). Цифры оставляем.
text_2 = "".join(i for i in text_words_1 if i.isalnum()) # удалили любые символы кроме текста и буквы в втором inpute()
if len(text_1) == len(text_2):  # сравниваем длину
    if text_1 == text_2:  # сравниваем символы
        print("Да, строки одиноковы")
else:
    print("Нет, строки разные")