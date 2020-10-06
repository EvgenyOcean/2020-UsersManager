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