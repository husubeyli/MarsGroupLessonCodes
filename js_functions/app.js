var firstValue = 0;
var secondValue = 0;
var operator = '';

function writeToPage(){
    if (secondValue !== 0)
        document.querySelector('#screen').value = firstValue + operator + secondValue;
    else
        document.querySelector('#screen').value = firstValue + operator;
}

function sum(){
    firstValue = firstValue + secondValue;
}
function subtraction(){
    firstValue = firstValue - secondValue
}

function divide(){
    firstValue = firstValue / secondValue;
}

function multiplate(){
    firstValue = firstValue * secondValue;
}

function getValue(value){
    if (operator === ''){
        firstValue = firstValue*10 + value;
    }else{
        secondValue = secondValue*10 + value;
    }
    writeToPage();
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
    writeToPage();
}