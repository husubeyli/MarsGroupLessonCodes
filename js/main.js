
var array = ['rock', 'scissors', 'paper',];

var user_choice = prompt('Enter rock or scissors or paper!');

if (array.indexOf(user_choice) === -1){
    user_choice = prompt('Enter rock or scissors or paper!');
}

comp_choice = array[parseInt(Math.random() * array.length)]; // [0,1,2]

console.log(comp_choice);

if(user_choice === 'rock'){
    if(comp_choice === 'scissors' ){
        alert('You win');
    }else if (comp_choice === 'paper'){
        alert('You lost');
    }else{
        alert('Draw');
    }
}else if (user_choice === 'scissors'){
    if(comp_choice === 'rock' ){
        alert('You lost');
    }else if (comp_choice === 'paper'){
        alert('You win');
    }else{
        alert('Draw');
    }
}else if (user_choice === 'paper'){
    if(comp_choice === 'rock' ){
        alert('You win');
    }else if (comp_choice === 'scissors'){
        alert('You lost');
    }else{
        alert('Draw');
    }
}

alert('Computer choise is ' + comp_choice);
