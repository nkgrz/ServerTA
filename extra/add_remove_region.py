import sqlite3

# Классный полезный сайт
# Управление БД https://habr.com/ru/articles/754400/

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('regions.db')
cursor = connection.cursor()

# Добавляем нового региона
# cursor.execute('INSERT INTO regions (id, name, description, imageAsset, price) VALUES (?, ?, ?, ?, ?)', (9, 'Test region', 'test description', 'dagestan2.jpg', '0' ))
# # Удаляем регион "newuser"
# cursor.execute('DELETE FROM regions WHERE id = ?', ('9'))

# Выбираем все регионы
cursor.execute('SELECT id, name, imageAsset, price FROM regions')
regions = cursor.fetchall()

# Выводим результаты
for region in regions:
  print(region)

# Сохраняем изменения и закрываем соединение
# connection.commit()
connection.close()