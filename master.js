  fetch('masterpage.html')
  .then(response => response.text())
  .then(data => {
    document.getElementById('importedContent').innerHTML = data;
  })
  .catch(error => console.error(error));