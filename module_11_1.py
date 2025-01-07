# requests
# Библиотека для выполнения HTTP-запросов в Python. Она позволяет легко взаимодействовать с web-сервисами и получать данные из интернета.

# Основные возможности:
# Выполнение различных типов HTTP-запросов (GET, POST, PUT, DELETE и т.д.).
# Обработка ответов от серверов.
# Отправка данных и заголовков в запросах.

# Пример использования:
import requests

address = 'https://3dnews.ru/'
r = requests.get(address)
r.status_code

print(r)

print(r.status_code)

txt = r.text

iskomaya_fraza1 = 'Samsung'
iskomaya_fraza2 = 'Asus'
iskomaya_fraza3 = 'Horizon Zero Dawn'

if iskomaya_fraza1 or iskomaya_fraza2 or iskomaya_fraza3 in txt:
    print('Есть такие статьи')
else:
    print('Нет упоминаний')

if 'сиськи' in txt:
    print('Есть такие статьи')
else:
    print('Нет упоминаний')

# pandas
# Библиотека для анализа и обработки данных. Она предоставляет мощные инструменты для работы с табличными данными и временными рядами.

# Основные возможности:
# Чтение и запись данных в различных форматах (CSV, Excel, SQL и т.д.).
# Фильтрация, агрегация и группировка данных.
# Доступ к данным по меткам и индексам.

# Пример использования:
import pandas

csv_file = pandas.read_csv('homework.csv')

print(csv_file.head())

countsome = csv_file.count()
print(f'Подсчёт:{countsome}')

# pillow
# Обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат
# Пример использования:

from PIL import Image
img = Image.open('pic.png')

print(img.format, img.size, img.mode)

img.show()