function   CreateQuestion(question, answer){
    return {
        'question': question,
        'answer': answer
    }
}

var questions = [];

// var question1 = CreateQuestion('Salam', 'Aleykum salam',);

// var question2 = CreateQuestion('Necesen?', 'Yaxsiyam!');

// questions.push(question1);
// questions.push(question2);

console.log(questions);

while(true){
    var user_question = prompt(`Sualinizi daxil edin. 
Ve ya Q daxil etmekle proqrami dayandirin!`);
    if(user_question === 'Q'){
        alert('Tesekkur edirik');
        break;
    }
    var question_founded = false;
    for(var question of questions){
        if(user_question.toLowerCase() === question['question'].toLowerCase()){
            alert(question['answer']);
            question_founded = true;
        }
    }
    if(question_founded===false){
        alert('Cavab tapilmadi!');
        if (confirm('Sualin cavabini daxil etmek isteyirsinizmi?')){
            var user_answer = prompt('Cavabi daxil edin: ');
            var new_question = CreateQuestion(user_question, user_answer);
            questions.push(new_question);
            alert('Yeni sualiniz elave edildi. Yeniden ceht edin!')
        }
    }
}