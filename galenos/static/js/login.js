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
