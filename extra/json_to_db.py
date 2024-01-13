import requests
import json

# # Чтение данных из regions.json
# with open('regions.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# # Отправка данных на сервер Flask
# url = 'https://b8ac-162-19-247-254.ngrok-free.app/upload_regions'
# response = requests.post(url, json=data)

# if response.status_code == 200:
#     print('Regions uploaded successfully')
# else:
#     print('Error:', response.text)


# Очистка БД!
# from flask_sqlalchemy import SQLAlchemy
# from app import Regions, db
# from flask import Flask

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///regions.db'

# db = SQLAlchemy(app)  # Регистрация SQLAlchemy с приложением

# # Создайте контекст приложения
# with app.app_context():
#     # Очистка таблицы "regions"
#     db.session.query(Regions).delete()
#     db.session.commit()
