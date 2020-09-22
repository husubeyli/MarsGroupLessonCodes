function  CreateQuestion(question, answer){
    return {
        'question': question,
        'answer': answer
    }
}

var questions = [];

var question1 = CreateQuestion('Bayraqda nece reng movcuddur?', '3',);

var question2 = CreateQuestion('Everest daginin hundurluyu ne qederdi?', '8848');
var question3 = CreateQuestion('Elifbada nece herf var?', '32');

questions.push(question1);
questions.push(question2);
questions.push(question3);

var count = 0;
var mistage_count = 0;
var max_mistage_count = 2;

for(var i=0; i<questions.length; i++){
    var question = questions[i];
    var user_answer =  prompt(question['question']);
    if (user_answer===question['answer']){
        alert('Cavab dogrudur!');
        count++;
    }else{
        alert('Cavab yalnisdir!');
        max_mistage_count--;
        mistage_count++;
        if ((max_mistage_count === 0) &&  (i!==questions.length-1)){
            alert('Siz artiq 2 sehv etdiyiniz ucun istirak haqqinizi itirdiz!')
            break;
        }
    }
}

alert('Duzgun cavablarin sayi: ' +  count + ' Sehv cavablarin sayi: ' + mistage_count );