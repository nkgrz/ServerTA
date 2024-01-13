from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, send_from_directory


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///regions.db'
app.config['IMAGE_FOLDER'] = 'assets/images/'
app.config['AVATAR_FOLDER'] = 'assets/user_avatars/'
db = SQLAlchemy(app)


class Regions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.Text, nullable=False)
    imageAsset = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.String(130))  # Поле для хранения имени файла аватара

    def __init__(self, username, email, avatar=None):
        self.username = username
        self.email = email
        self.avatar = avatar


@app.route('/get_regions', methods=['GET'])
def get_regions():
    regions = Regions.query.all()
    region_list = []
    for region in regions:
        region_list.append({
            'id': region.id,
            'name': region.name,
            'description': region.description,
            'imageAsset': region.imageAsset,
            'price': region.price
        })
    return jsonify(region_list)


@app.route('/get_image/<image_name>', methods=['GET'])
def get_image(image_name):
    return send_from_directory(app.config['IMAGE_FOLDER'], image_name)
    # return send_from_directory(image_name)


@app.route('/create_region', methods=['POST'])
def create_region():
    data = request.get_json()
    new_region = Regions(
        name=data['name'],
        description=data['description'],
        imageAsset=data['imageAsset'],
        price=data['price']
    )
    db.session.add(new_region)
    db.session.commit()
    return jsonify({'message': 'Region created successfully'})


@app.route('/upload_regions', methods=['POST'])
def upload_regions():
    try:
        # Данные в формате JSON, добавляются в конце БД
        data = request.get_json()
        for region_data in data:
            region = Regions(
                name=region_data['name'],
                description=region_data['description'],
                imageAsset=region_data['imageAsset'],
                price=region_data['price']
            )
            db.session.add(region)

        db.session.commit()
        return jsonify({'message': 'Regions uploaded successfully'})
    except Exception as e:
        return jsonify({'error': str(e)})



@app.route('/get_user_avatar/<avatar_name>', methods=['GET'])
def get_user_avatar(avatar_name):
    return send_from_directory(app.config['AVATAR_FOLDER'], avatar_name)


@app.route('/api/upload_avatar', methods=['POST'])
def upload_avatar():
    try:
        avatar = request.files['avatar']
        if avatar:
            user_email = 'example@example.com'  # Получите адрес электронной почты пользователя из сессии или запроса
            avatar_filename = secure_filename(user_email + '_avatar.png')  # Создайте уникальное имя файла аватара
            avatar.save(os.path.join(app.config['AVATAR_FOLDER'], avatar_filename))

            # Сохраняем имя файла аватара в базе данных для текущего пользователя
            current_user.avatar = avatar_filename
            db.session.commit()

            return jsonify({'message': 'Avatar uploaded successfully'})
        else:
            # Если фото профиля не передано, используйте дефолтный аватар
            default_avatar_filename = 'default_avatar.png'
            current_user.avatar = default_avatar_filename
            db.session.commit()
            return jsonify({'message': 'Default avatar set'})
    except Exception as e:
        return jsonify({'error': str(e)})


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(port=8080)
