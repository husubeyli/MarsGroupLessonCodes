let createItemBtn = document.getElementById('createItem');

let input = document.getElementById('itemInput');

var itemListElement = document.querySelector('.item-list')

createItemBtn.addEventListener('click', function(){
    var inputValue = input.value;
    itemListElement.innerHTML += `
    <div class="item my-3">
        <h5 class="item-name text-capitalize">${inputValue}</h5>
        <div class="item-icons">
        <a href="#" class="complete-item mx-2 item-icon"><i class="far fa-check-circle"></i></a>
        <a href="#" class="edit-item mx-2 item-icon"><i class="far fa-edit"></i></a>
        <a href="#" class="delete-item item-icon"><i class="far fa-times-circle"></i></a>
        </div>
     </div>
    `;

});