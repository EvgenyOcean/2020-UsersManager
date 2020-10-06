function createUser(e){
  e.preventDefault();
  let form = new FormData(formElement);
  let username = form.get('username');
  let firstName = form.get('firstName');
  let lastName = form.get('lastName');

  fetch('/api/create/', {
    method: "POST",
    headers: {
      'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
      'X-Requested-With': 'XMLHttpRequest',
      "Content-Type": "application/json",
    }, 
    body: JSON.stringify({username, firstName, lastName}),
  }).then(response => {
    if (response.ok){ 
      response.json().then(data => {
        if (data.message === 'Success'){
          formElement.reset();
          getUsers()
          return notifier({'message': "User was created! Hooray!"})
        } else {
          return notifier(data);
        }
      }).catch(err => {console.log(err)})
    } else {
      response.json().then(errData => { 
        console.log(errData);
      }).catch(err => {console.log(err)})
    }
  }).catch(err => {console.log('never here, but just in case!')});
}

function notifier({message}){
  let prevNotifier = document.querySelector('.notifier');
  if (prevNotifier){
    prevNotifier.remove();
  }
  let main = document.querySelector('main .container');
  let div = document.createElement('div');
  div.classList.add('alert', 'alert-info', 'notifier');
  div.textContent = message;
  main.insertAdjacentElement('afterbegin', div);
}

function getUsers(){
  fetch('/api/users/').then(response => {
    if (response.ok){
      response.json().then(data => {
        populateTable(data);
      })
    } else {
      response.json().then(errData => {
        console.log(errData);
      })
    }
  }).catch(err => {console.log('never here, but just in case!')});
}

function populateTable(users){
  let tbody = document.querySelector('tbody');
  tbody.innerHTML = '';
  users.forEach(user => {
    let tr = document.createElement('tr');
    let th = document.createElement('th');
    th.setAttribute('scope', 'row')
    th.textContent = user.id;
    tr.append(th);
    for (let i=0; i < 4; i++){
      let td = document.createElement('td');
      switch (i) {
        case 0:
          td.textContent = user.username;
          break;
        case 1:
          td.textContent = user.first_name;
          break;
        case 2:
          td.textContent = user.last_name;
          break;
        case 3:
          td.insertAdjacentHTML('afterbegin', '<button class="btn btn-small bg-danger text-white rm-btn">X</button>');
          break;
        default:
          break;
      }
      tr.append(td);
    }
    tbody.append(tr);
  })

  let btns = document.querySelectorAll('.rm-btn');
  btns.forEach(btn => btn.onclick = handleDelete);
}

function handleDelete(e){
  let tr = e.target.closest('tr');
  let id = tr.firstElementChild.textContent;
  fetch('/api/delete/', {
    method: "DELETE",
    headers: {
      'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest',
      'X-Requested-With': 'XMLHttpRequest',
      "Content-Type": "application/json",
    }, 
    body: JSON.stringify({id}),
  }).then(response => {
    if (response.ok){ 
      response.json().then(data => {
        if (data.message === 'Success'){
          tr.remove()
          return notifier({'message': "User was deleted!"});
        } else {
          return notifier(data);
        }
      }).catch(err => {console.log(err)})
    } else {
      response.json().then(errData => { 
        console.log(errData);
      }).catch(err => {console.log(err)})
    }
  }).catch(err => {console.log('never here, but just in case!')});
}
