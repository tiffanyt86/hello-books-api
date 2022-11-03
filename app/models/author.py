from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = db.relationship("Book", back_populates='author"')

    def to_dict(self):
        auth_as_dict = {}
        auth_as_dict["id"] = self.id
        auth_as_dict["name"] = self.name

        return auth_as_dict