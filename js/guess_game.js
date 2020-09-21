
function compare(comp_choice, guess){
    if (guess < comp_choice){
        return parseInt(prompt('Daha boyuk eded daxil edin!'));
    }else if(guess > comp_choice){
        return parseInt(prompt('Daha kicik eded daxil edin!'));
    }else{
        alert('Texmin dogrudur!');
        return false;
    }
}

var guess = prompt('Enter the value between 0,6 ');

var comp_choice = 3 //parseInt(Math.random() * 7);

if (isNaN(guess) || parseInt(guess) < 0 || parseInt(guess) > 6){
    alert('Daxil olunan deyer 0-6 arasinda reqem olmalidir!');
    guess = prompt('Enter the value between 0,6 ');
}

condition = compare(comp_choice, guess );
while (condition){
    guess = condition;
    condition = compare(comp_choice, guess);
    // if (condition){
    //     guess = condition;
    //     condition = compare(comp_choice, guess );
    //     if (condition){
    //         guess = condition;
    //         if(condition){
    //             alert('Siz meglub oldunuz!');
    //         }
    //     }
    // }
}


