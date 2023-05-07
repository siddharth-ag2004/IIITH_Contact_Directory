const addButton = document.getElementById("add-student-button");
const table = document.querySelector("table");

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
      <label for="phone">Phone Number:</label>
      <input type="text" id="phone" name="phone"><br>
      <button type="submit">Add Student</button>
    </form>
  `;
  const form = document.createRange().createContextualFragment(formHtml);
  table.parentNode.insertBefore(form, table);
});
