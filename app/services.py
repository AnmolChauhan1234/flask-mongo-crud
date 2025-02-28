from app.models import User

class UserService:
    @staticmethod
    def get_all_users():
        return [user.to_json() for user in User.objects()]

    @staticmethod
    def get_user_by_id(user_id):
        user = User.objects(id=user_id).first()
        return user.to_json() if user else None

    @staticmethod
    def create_user(data):
        if User.objects(email=data["email"]).first():
            return {"error": "Email already exists"}, 400
        user = User(**data)
        user.save()
        return {"message": "User created", "id": str(user.id)}, 201

    @staticmethod
    def update_user(user_id, data):
        user = User.objects(id=user_id).first()
        if not user:
            return {"error": "User not found"}, 404
        user.update(**data)
        return {"message": "User updated"}, 200

    @staticmethod
    def delete_user(user_id):
        user = User.objects(id=user_id).first()
        if not user:
            return {"error": "User not found"}, 404
        user.delete()
        return {"message": "User deleted"}, 200
