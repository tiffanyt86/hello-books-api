from app import db

class Author(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String)
  books = db.relationship("Book", back_populates = "author")

  @classmethod
  def from_dict(cls, req_body):
    return cls(
      name=req_body['name']
    )