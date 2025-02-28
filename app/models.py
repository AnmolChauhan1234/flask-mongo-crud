from mongoengine import Document, StringField, EmailField, signals
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(Document):
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6)

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email
        }

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        """Automatically hashes the password before saving."""
        document.password = bcrypt.generate_password_hash(document.password).decode('utf-8')

# Register signal to hash password before saving
signals.pre_save.connect(User.pre_save, sender=User)
