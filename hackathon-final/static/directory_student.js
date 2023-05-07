const addButton = document.getElementById("add-student-button");
const table = document.querySelector("table");

const removeButtons = document.querySelectorAll('.remove-button');

// Add click event listener to each remove button
removeButtons.forEach(button => {
  button.addEventListener('click', (event) => {
    // Get the rollno from the data-rollno attribute
    const rollno = event.currentTarget.dataset.rollno;

    // Send an AJAX request to remove the row with the given rollno
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/remove-student');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = () => {
      // Reload the page after removing the row
      location.reload();
    };
    xhr.send(JSON.stringify({ rollno: rollno }));
  });
});



addButton.addEventListener("click", () => {
  const formHtml = `
      <form id="add-student-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br>
        <label for="rollno">Roll Number:</label>
        <input type="text" id="rollno" name="rollno"><br>
        <label for="branch">Branch:</label>
        <input type="text" id="branch" name="branch"><br>
        <label for="batch">Batch:</label>
        <select id="batch" name="batch">
          <option value="UG1">UG1</option>
          <option value="UG2">UG2</option>
          <option value="UG3">UG3</option>
          <option value="UG4">UG4</option>
          <option value="MTECH">M.Tech</option>
          <option value="PHD">PhD</option>
        </select><br>
        <button type="submit">Add Student</button>
      </form>
    `;
  const form = document.createRange().createContextualFragment(formHtml);
  table.parentNode.insertBefore(form, table);

  const addStudentForm = document.getElementById("add-student-form");
  addStudentForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(addStudentForm);
    fetch("/add_student", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          alert("Student added successfully");
          location.reload();
        } else {
          alert("Error adding student");
        }
      })
      .catch((error) => {
        console.error("Error adding student:", error);
        alert("Error adding student");
      });
  });
});


//   const form = document.createRange().createContextualFragment(formHtml);
//   table.parentNode.insertBefore(form, table);
// });