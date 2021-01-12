from post_service.config.extentions import ma
from flask_marshmallow.fields import AbsoluteURLFor
from marshmallow import validates, ValidationError

from post_service.models import Recipe, Category


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    image = AbsoluteURLFor(
        'uploaded_file',
        filename='<image>'
    )

    class Meta:
        model = Recipe
        include_fk = True
        load_instance = True

    @validates('category_id')
    def validate_category_id(self, category_id):
        """'value' is the datetime parsed from time_created by marshmallow"""
        category = Category.query.filter_by(id=category_id).first()
        print('category', category)
        if not category:
            raise ValidationError(f'Category with "{category_id}" pk not found')

