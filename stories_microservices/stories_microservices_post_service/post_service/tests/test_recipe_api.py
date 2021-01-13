

def test_get_recipes_status_code(app, client):
    response = client.get('/recipes/')
    assert response.status_code == 200


def test_post_recipe_valid_data_status_code(app, client):
    post_data = {
        "category_id": 1,
        "description": "sdfnsdjfndsfjnsdlsflsdkfnsksldn",
        "short_description": "23423423789",
        "slug": "345345",
        "title": "345353534"
    }
    response = client.post('/recipes/', json=post_data)
    assert response.status_code == 201


def test_post_recipe_valid_data(app, client):
    post_data = {
        "category_id": 1,
        "description": "sdfnsdjfndsfjnsdlsflsdkfnsksldn",
        "short_description": "23423423789",
        "slug": "345345",
        "title": "345353534"
    }
    response = client.post('/recipes/', json=post_data)
    res_data = response.json
    assert res_data['title'] == post_data['title']


def test_post_recipe_invalid_data_status_code(app, client):
    post_data = {
        "category_id": 1
    }
    response = client.post('/recipes/', json=post_data)
    assert response.status_code == 400


def test_post_recipe_invalid_data(app, client):
    post_data = {
        "category_id": 1
    }
    response = client.post('/recipes/', json=post_data)
    res_data = response.json
    assert "Missing data for required field." in res_data['description']
    assert "Missing data for required field." in res_data['short_description']
    assert "Missing data for required field." in res_data['slug']
    assert "Missing data for required field." in res_data['title']


def test_post_recipe_invalid_data_with_longer_title(app, client):
    post_data = {
        "title": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
                 "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type "
                 "and scrambled it to make a type specimen book. It has survived not only five centuries, "
                 "but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised "
                 "in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently "
                 "with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. "
    }
    response = client.post('/recipes/', json=post_data)
    res_data = response.json
    assert "Longer than maximum length 80." in res_data['title']


def test_post_recipe_with_not_valid_type(app, client):
    post_data = {
        "category_id": "sdkfsdn"
    }
    response = client.post('/recipes/', json=post_data)
    res_data = response.json
    assert "Not a valid integer." in res_data['category_id']


def test_get_recipe_with_wrong_id(app, client):
    recipe_id = 283274829342
    response = client.get(f'/recipes/{recipe_id}/')
    res_data = response.json
    print('res_data', res_data)
    assert "message" in res_data
    assert "Not found" in res_data['message']


def test_get_recipe_with_wrong_id_status_code(app, client):
    recipe_id = 283274829342
    response = client.get(f'/recipes/{recipe_id}/')
    assert response.status_code == 404
