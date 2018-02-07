//<span onclick="newToDo()" class="addBtn">Add To-Do</span>
//<input type="text" id="input" placeholder="New task...">

function addToDo(){
  var toDoList = document.getElementById("toDoUL");
  var newItem = document.createElement("li");
  var userInput = document.getElementById("input").value;
  if(userInput != ''){
    var inputTxtNode = document.createTextNode(userInput);
    newItem.appendChild(userInput);
    toDoList.appendChild(newItem);
    clearInput(userInput);
  } else{
      alert("Invalid response: Field cannot be blank!");
  }
}


function clearInput(currInput){
  currInput.value = null;
}
