document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('id_username').value;
    var password = document.getElementById('id_password').value;

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/login/', true); // replace '/login/' with the actual URL of your login view
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken')); // getCookie is a function to get the CSRF token, which is required by Django
    xhr.onload = function() {
        if (this.status == 200) {
            var response = JSON.parse(this.responseText);
            if (response.status == 'success') {
                alert('Logged in successfully');
                // redirect to another page or update the UI
            } else {
                alert(response.message);
            }
        } else {
            alert('An error occurred');
        }
    };
    xhr.send('username=' + encodeURIComponent(username) + '&password=' + encodeURIComponent(password));
});

function validateForm() {
    var username = document.getElementById("id_username").value;
    var password = document.getElementById("id_password").value;
    if (username == "" && password == "") {
      alert("Campos vacíos, por favor ingresar información");
    } else if (username != "fespinoza" || password != "fabo1234") {
      alert("Campos erróneos, por favor corrija la información");
    } else {
      alert("Usuario ha iniciado sesión satisfactoriamente");
    }
  }