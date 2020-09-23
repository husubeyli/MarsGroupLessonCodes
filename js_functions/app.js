var firstValue = 0;
var secondValue = 0;
var operator = '';

function sum(){
    console.log(firstValue + secondValue);
}
function subtraction(){
    console.log(firstValue - secondValue);
}

function divide(){
    console.log(firstValue / secondValue);
}

function multiplate(){
    console.log(firstValue * secondValue);
}


function getValue(value){
    if (operator === ''){
        firstValue = firstValue*10 + value;
    }else{
        secondValue = secondValue*10 + value;
    }
}

function getOperator(newOperator){
    if (newOperator === '='){
        if(operator == '+'){
            sum();
        }
        else if (operator == '-'){
            subtraction();
        }
        else if (operator == '/'){
            divide();
        }
        else if (operator == '*'){
            multiplate();
        }
    }
    operator = newOperator;
}