from flask import request, jsonify, send_from_directory
from flasgger import swag_from
from http import HTTPStatus
from post_service.app import app
from marshmallow.exceptions import ValidationError

from post_service.schemas.schmas import RecipeSchema
from post_service.config.base import MEDIA_ROOT

from post_service.utils.common import save_file
from post_service.models import Recipe


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(MEDIA_ROOT, filename)


@app.route('/recipes/', methods=['GET', 'POST'])
@swag_from('docs/all_recipes.yml', methods=['GET',])
@swag_from('docs/create_recipe.yml', methods=['POST',])
def recipes():
    if request.method == 'POST':
        try:
            data = request.json or request.form
            # print(data)
            image = request.files.get('image')
            serializer = RecipeSchema()
            recipe = serializer.load(data)
            recipe.owner_id = 1
            recipe.image = save_file(image)
            recipe.save()
            return RecipeSchema().jsonify(recipe), HTTPStatus.CREATED
        except ValidationError as err:
            return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    recipes = Recipe.query.filter_by(is_published=True)
    return RecipeSchema(many=True).jsonify(recipes), HTTPStatus.OK


@app.route('/recipes/<int:recipe_id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@swag_from('docs/create_recipe.yml', methods=['PUT', 'PATCH'])
@swag_from('docs/all_recipes.yml', methods=['GET',])
def recipe(recipe_id):
    recipe = Recipe.query.filter_by(id=recipe_id).first()
    if not recipe:
        return jsonify({'message': 'Not found'}), HTTPStatus.NOT_FOUND
    if request.method == 'DELETE':
        recipe.delete()
        return jsonify({}), HTTPStatus.NO_CONTENT
    if request.method == 'GET':
        return RecipeSchema().jsonify(recipe), HTTPStatus.OK
    try:
        data = request.json or request.form
        image = request.files.get('image')
        serializer = RecipeSchema()
        if request.method == 'PUT':
            recipe_serializer = serializer.load(data, instance=recipe)
        elif request.method == 'PATCH':
            recipe_serializer = serializer.load(data, instance=recipe, partial=True)
        recipe.owner_id = 1
        if image:
            recipe.image = save_file(image)
        recipe_serializer.save()
        return RecipeSchema().jsonify(recipe), HTTPStatus.OK
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST
