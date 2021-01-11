from post_service.config.extentions import ma
from flask_marshmallow.fields import AbsoluteURLFor

from post_service.models import Recipe


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    image = AbsoluteURLFor(
        'uploaded_file',
        filename='<image>'
    )

    class Meta:
        model = Recipe
        include_fk = True
        load_instance = True