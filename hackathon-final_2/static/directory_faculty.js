const addButton = document.getElementById("add-faculty-button");
const table = document.querySelector("table");

const removeButtons = document.querySelectorAll('.remove-button');


removeButtons.forEach(button => {
  button.addEventListener('click', (event) => {

    const id = event.currentTarget.dataset.id;

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/remove-faculty');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = () => {

      location.reload();
    };
    xhr.send(JSON.stringify({ id: id }));
  });
});



addButton.addEventListener("click", () => {
  const formHtml = `
      <form id="add-faculty-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br>
        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone"><br>
        <label for="LAB">Lab:</label>
        <input type="text" id="LAB" name="LAB"><br>
        <label for="position">Position:</label>
        <input type="text" id="position" name="position"><br>
        <label for="office_hrs">Office Hours:</label>
        <input type="text" id="office_hrs" name="office_hrs"><br>
        <button type="submit" style="display: block; margin: 0 auto;">Add Faculty</button>
        <br><br><br><br><br><br><br><br><br><br>
      </form>
    `;
  const form = document.createRange().createContextualFragment(formHtml);
  table.parentNode.insertBefore(form, table);

  const addFacultyForm = document.getElementById("add-faculty-form");
  addFacultyForm.addEventListener("submit", (event) => {
    event.preventDefault();
    const formData = new FormData(addFacultyForm);
    fetch("/add_faculty", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          alert("Faculty added successfully");
          location.reload();
        } else {
          alert("Error adding faculty");
        }
      })
      .catch((error) => {
        console.error("Error adding faculty:", error);
        alert("Error adding faculty");
      });
  });
});
