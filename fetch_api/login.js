var domain = 'http://localhost:8000/az';

async function login(e){
    e.preventDefault();
    let loginForm = document.querySelector('#loginForm');
    console.log(loginForm.username);
    console.log(loginForm.username.value);

    let postData = {
        username: loginForm.username.value,
        password: loginForm.password.value
    }

    let response = await fetch(`${domain}/accounts/api/v1.0/login/`, {
        headers: {
            'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify(postData)
    });

    let data = await response.json();
    console.log(data);
    
    if(data.token)
        localStorage.setItem('token', data.token);
}
