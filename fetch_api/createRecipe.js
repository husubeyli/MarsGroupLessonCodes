var domain = 'http://localhost:8000/az';

if(!localStorage.getItem('token')){
    window.location = 'login.html'
}

window.onload = function() {
    getCategories();
    getTags();
}

async function getCategories(){
    let response = await fetch(`${domain}/api/v1.0/categories/`);

    let data = await response.json();
    options = '<option>Select category</option>';
    data.forEach(element => {
        options += `<option value="${element.id}">${element.title}</option>`
    });
    let select_tag = document.querySelector('#category');
    select_tag.innerHTML = options;
}

async function getTags(){
    let response = await fetch(`${domain}/api/v1.0/tags/`);

    let data = await response.json();
    options = '';
    data.forEach(element => {
        options += `<option value="${element.id}">${element.title}</option>`
    });
    let select_tag = document.querySelector('#tags');
    select_tag.innerHTML = options;
}


document.querySelector('#recipeForm').addEventListener('submit', async (e) =>{
    e.preventDefault();
    let token = localStorage.getItem('token')
    let form = e.target;
    let postData = new FormData(form);
    postData.append('title', form.title.value);
    postData.append('short_description', form.short_description.value);
    console.log(postData.entries());
    let response = await fetch(`${domain}/api/v1.0/recipes/`, {
        headers: {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryIn312MOjBWdkffIM',
            'Authorization': `Token ${token}`
        },
        method: "POST",
        body: new FormData(form)
    });

    data = await response.json();
    console.log(data);
})
// async function createRecipe(e, this){
   
    
// }
