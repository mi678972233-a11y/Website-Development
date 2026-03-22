function clearScreen() {
    document.getElementById("result").value = "";
}
//Append's the clicked button's value to the input field
function setScreen(value) {
   const r = document.getElementById("result");
   if (r.value === "Enter An Expression" || r.value === "Invalid Expression") r.value = "";  
    r.value += value; 
}
//Calculates And Displays The Result
function calculateResult() {
    const resultElement = document.getElementById("result");
    const expression = resultElement.value.trim();
    //Check For Empty Inputs
    if (expression === "") {
        resultElement.value = "Enter An Expression";
        return;
    }
        //Evaluate The Expression And Handle Errors
       try {
        resultElement.value = eval(expression);
    }   catch (error) { 
        resultElement.value = "Invalid Expression";  
    }
}   
