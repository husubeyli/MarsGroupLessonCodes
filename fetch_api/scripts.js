var domain = 'http://localhost:8000/az';



async function getRecipes(){
    let response = await fetch(`${domain}/api/v1.0/recipes/`);

    let data = await response.json();

    console.log(data);

    let recipeSection = document.querySelector('#recipes');

    let addedHTMLDATA = '';
    data.forEach(recipe => {
        addedHTMLDATA +=  `<div class="col-md-3">
        <div class="card">
            <img class="card-img-top" src="${recipe.image}" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">${recipe.title}</h5>
              <p class="card-text">${recipe.short_description}</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>`
    });
    recipeSection.innerHTML = addedHTMLDATA;
}


getRecipes();