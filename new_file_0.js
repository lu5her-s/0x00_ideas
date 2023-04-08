document.querySelector('form').addEventListener('submit', (event) => {
  event.preventDefault();
  let counter = 5;
  const countdown = setInterval(() => {
    console.log(counter);
    counter--;
    if (counter < 0) {
      clearInterval(countdown);
      console.log('Submit form');
      event.target.submit();
    }
  }, 1000);
});
