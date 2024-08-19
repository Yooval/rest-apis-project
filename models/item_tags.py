from db import db


class ItemsTags(db.Model):
    __tablename__ = "items_tags"
    # Required fields for tables that maintains many-to-many relationships.
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))