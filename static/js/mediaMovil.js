function validar(){

    var lista = document.getElementById("lista").value;
    dominio = document.getElementById("dominio").value;
    dominio2 = parseInt(dominio,10);
    numDatos = lista.split(",");
    num = numDatos.length+1;
    if (numDatos.length < dominio2){
        alert("el dominio solo puede ser menor que: "+num+" para los datos ingresados")
        document.getElementById("dominio").value = "";
    } 
}

