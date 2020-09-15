function validarListasIguales(){

    var listaX = document.getElementById("listaX").value;
    var listaY = document.getElementById("listaY").value;

    liX = listaX.split(",");
    liY = listaY.split(",");
    
    if (liX.length != liY.length){
        alert("el numero de datos ingresados tiene que ser igual para ambas listas\n La lista X tiene: "+liX.length+" datos\n La lista Y tiene: "+liY.length+" datos")
    } 
}

function validateMyForm(){

   var listaX = document.getElementById("listaX").value;
   var listaY = document.getElementById("listaY").value;

   liX = listaX.split(",");
   liY = listaY.split(",");

   if (liX.length != liY.length){
    return false;
   }else{
    return true;
   }
}
