
async function renderPost(post){
    // let post_comments = await getCommentData(post.id);
    let comments = post.comments;
    return `<div class="col-md-3">
                <div class="card p-4" >

                    <h5 class="card-title">${post.title}</h5>
                      <div class="card-body">
                        <ul>
                            ${ comments ? comments.map(comment => `<li>${comment.content} </li>`) : '' }
                        </ul>
                          <form id="createComment">
                              <label>Comment</label>
                              <input type="text" name="content"/>
                          </form>
                      </div>

                </div>
            </div>`
}

async function getPostData() {
    let response = await fetch('http://localhost:5002/posts/',)
    return await response.json();
}

// async function getCommentData(id) {
//     let response = await fetch(`http://localhost:5001/posts/${id}/comments/`,)
//     return await response.json();
// }


async function createPost(e){
    e.preventDefault();
    let form = e.target;
    let postData = {
        'title': form.title.value
    }
    let response = await fetch('http://localhost:5003/posts/',{
        headers: {
            'content-type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(postData),
    })
    let createPostData = await response.json();
    console.log(createPostData);
    let htmlContent =  await renderPost(createPostData);
    document.querySelector('#postList').innerHTML += htmlContent;
}


window.onload = async () => {

    let postList  = await getPostData();
    let htmlContent = ''
    for (post of postList){
        htmlContent += await renderPost(post)
    }
    document.querySelector('#postList').innerHTML += htmlContent;

}