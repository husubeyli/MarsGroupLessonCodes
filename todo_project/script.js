$(document).ready(function (){
    // function onSubmit(){
    //     return false;
    // }
    
    $('form').submit(function( event ) {
        event.preventDefault();
        let input_value = $('input[name="task"]').val();
        if(input_value){
            console.log(input_value);
            $('#task_list').prepend(`<li>${input_value}</li>`);
            $('input[name="task"]').val('');
        }
      });
});

