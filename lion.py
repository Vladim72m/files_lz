from collections import Counter
import docx
import pandas as pd
import matplotlib.pyplot as plt

doc = docx.Document('lion.docx')  # открываем документ Word
full_text = []
for i in doc.paragraphs:
    full_text.append(i.text)
text = ' '.join(full_text)

list = '.,!?;:"()[]{}«»—'  # список знаков препинания для удаления
for a in list:
    text = text.replace(a, '')  # удаляем каждый знак препинания из текста

s = text.split()  # разбиваем текст на слова
counter_word = Counter(s)  # считаем сколько раз встречается каждое слово
all_word = len(s)  # общее количество слов в тексте

list_word = [(word, amt, (amt / all_word) * 100) for word, amt in counter_word.items()]
pd.DataFrame(list_word, columns=['Слово', 'Количество', 'Частота (%)']).to_excel('s.xlsx', index=False)  # сохраняем в Excel

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # строка с алфавитом
b = [i for i in text if i in letters]  # отбираем только русские буквы
counter_letter = Counter(b)  # считаем частоту каждой буквы

plt.bar(counter_letter.keys(), counter_letter.values())  # создаем столбчатую диаграмму
plt.ylabel('Количество')  # подпись для  оси y
plt.xlabel('Буквы')  # подпись для горизонтальной оси x
plt.show()  # показываем график

for lett, amt in counter_letter.items():
    print(f"{lett}: {amt}")  # печатаем статистику по буквам
    
