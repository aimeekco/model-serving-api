from flask import url_for

class PredictionModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    description = db.Column(db.String(256), index=True)
    version = db.Column(db.String(64), index=True)
    url = db.Column(db.String(256), index=True)

    def __repr__(self):
        return f'<Model {self.name}>'