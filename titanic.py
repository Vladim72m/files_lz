import matplotlib.pyplot as plt
import pandas as pd 
data = pd.read_parquet('titanic.parquet')
data.to_csv('titanic.csv', index=False)  # конвертация в csv
table = data.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0) # группируем данные для анализа
table_procent = table.div(table.sum(axis=1), axis=0) * 100 # перевод в проценты
table_procent.plot(kind='bar', stacked=True)  # делается столбчатая диаграмма в процентах 
plt.title('Выживаемость пассажиров Титаника')   #Подписи вывод графика
plt.xlabel('Класс билета')
plt.ylabel('% людей')
plt.legend(['Не выжил', 'Выжил'])
plt.show()  # показываем  график
