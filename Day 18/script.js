document.getElementById("feedbackForm").addEventListener("submit", function(e){
    e.preventDefault(); 

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let feedback = document.getElementById("feedback").value;

    if(name === "" || email === "" || feedback === ""){
        alert("Please fill all fields");
        return;
    }
    

    let table = document.getElementById("feedbackTable");
    let row = table.insertRow();
    row.insertCell(0).innerText = name;
    row.insertCell(1).innerText = email;
    row.insertCell(2).innerText = feedback;

    document.getElementById("feedbackForm").reset();
});
