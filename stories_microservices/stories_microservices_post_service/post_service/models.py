from post_service.config.extentions import db
from sqlalchemy.sql import func
from slugify import slugify


class SaveMixin(object):
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class Tag(SaveMixin, db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    # recipes = db.relationship('Recipe', backref=db.backref('recipe', lazy=True))

    def __repr__(self):
        return self.title

    def __init__(self, title):
        self.title = title

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()



association_table = db.Table('association', db.Model.metadata,
    db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Category(SaveMixin, db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    recipes = db.relationship('Recipe', backref=db.backref('recipe', lazy=True))

    def __repr__(self):
        return self.title

    def __init__(self, title, image):
        self.title = title
        self.image = image

    # def save(self):
    #     db.session.add(self)
    #     db.session.commit()


class Recipe(SaveMixin, db.Model):
    # relation's
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    owner_id = db.Column(db.Integer)
    tags = db.relationship('Tag', secondary=association_table,
                           backref=db.backref('tags', lazy=True))
    slug = db.Column(db.String(120), nullable=False)

    # information's
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(255), nullable=False)

    is_published = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(),
                           server_onupdate=func.now(), nullable=False)

    def __repr__(self):
        return self.title

    def __init__(self, title, image, description, short_description, category_id, owner_id, is_published=True, **kwargs):
        self.slug = slugify(kwargs.get('title', ''))
        self.title = title
        self.image = image
        self.description = description
        self.short_description = short_description
        self.category_id = category_id
        self.owner_id = owner_id
        self.is_published = is_published

    def save(self):
        db.session.add(self)
        db.session.commit()
