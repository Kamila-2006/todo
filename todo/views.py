from django.shortcuts import HttpResponse

def html(view):
    html_response = """
        <!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vazifalar Ro'yxati</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <title>ToDo</title>
  <style>
    body {
      font-family: 'Roboto', sans-serif;
      background: linear-gradient(to right, #6a11cb, #2575fc);
      color: #ffffff;
      min-height: 100vh;
    }
    .container {
      margin-top: 50px;
    }
    .card {
      background: #ffffff;
      color: #333333;
      border-radius: 15px;
      box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .card h3 {
      font-weight: bold;
      color: #6a11cb;
    }
    .form-control, .form-select {
      border-radius: 10px;
    }
    .form-control:focus, .form-select:focus {
      box-shadow: 0 0 10px rgba(106, 17, 203, 0.5);
    }
    .btn-primary {
      background: #6a11cb;
      border: none;
      transition: all 0.3s ease;
    }
    .btn-primary:hover {
      background: #2575fc;
      transform: scale(1.05);
    }
    .table th {
      background: #2575fc;
      color: #ffffff;
    }
    .table tr:hover {
      background: rgba(106, 17, 203, 0.1);
    }
    .change-status {
      background: #17a2b8;
      border: none;
      color: #fff;
    }
    .edit-task {
      background: #ffc107;
      border: none;
      color: #fff;
    }
    .delete-task {
      background: #dc3545;
      border: none;
      color: #fff;
    }
    .btn-sm:hover {
      transform: scale(1.1);
      opacity: 0.9;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="text-center mb-4">Vazifalar Ro'yxati</h1>

    <div class="card p-4 mb-4">
      <h3 class="mb-3">Yangi vazifa qo'shish</h3>
      <form id="taskForm">
        <div class="mb-3">
          <label for="taskName" class="form-label">Vazifa nomi:</label>
          <input type="text" class="form-control" id="taskName" placeholder="Vazifa nomini kiriting" required>
        </div>
        <div class="mb-3">
          <label for="taskDescription" class="form-label">Tavsif:</label>
          <textarea class="form-control" id="taskDescription" rows="3" placeholder="Vazifa haqida qisqacha yozing" required></textarea>
        </div>
        <div class="row g-3">
          <div class="col-md-4">
            <label for="priority" class="form-label">Muhimlik darajasi:</label>
            <select class="form-select" id="priority" required>
              <option value="Past">Past</option>
              <option value="O'rta">O'rta</option>
              <option value="Yuqori">Yuqori</option>
            </select>
          </div>
          <div class="col-md-4">
            <label for="deadline" class="form-label">Muddat:</label>
            <input type="date" class="form-control" id="deadline" required>
          </div>
          <div class="col-md-4 d-flex align-items-end">
            <button type="submit" class="btn btn-primary w-100">Vazifani qo'shish</button>
          </div>
        </div>
      </form>
    </div>

    <div id="tasksTable" class="card p-4">
      <h3 class="mb-3">Mavjud vazifalar</h3>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th>Vazifa</th>
            <th>Tavsif</th>
            <th>Muhimlik</th>
            <th>Muddat</th>
            <th>Holat</th>
            <th>Amallar</th>
          </tr>
        </thead>
        <tbody id="tasksBody">
        </tbody>
      </table>
    </div>
  </div>

  <script>
    const taskForm = document.getElementById("taskForm");
    const tasksTable = document.getElementById("tasksTable");
    const tasksBody = document.getElementById("tasksBody");

    taskForm.addEventListener("submit", function (event) {
      event.preventDefault();

      const taskName = document.getElementById("taskName").value;
      const taskDescription = document.getElementById("taskDescription").value;
      const priority = document.getElementById("priority").value;
      const deadline = document.getElementById("deadline").value;

      const newRow = document.createElement("tr");
      newRow.innerHTML = `
        <td>${taskName}</td>
        <td>${taskDescription}</td>
        <td>${priority}</td>
        <td>${deadline}</td>
        <td class="task-status">Boshlanmagan</td>
        <td>
          <button class="btn btn-success btn-sm change-status">Holatni o'zgartirish</button>
          <button class="btn btn-warning btn-sm edit-task">Tahrirlash</button>
          <button class="btn btn-danger btn-sm delete-task">O'chirish</button>
        </td>
      `;
      tasksBody.appendChild(newRow);

      tasksTable.style.display = "block";

      taskForm.reset();

      attachTaskEvents(newRow);
    });

    function attachTaskEvents(row) {
      row.querySelector(".change-status").addEventListener("click", function () {
        const statusCell = row.querySelector(".task-status");
        statusCell.textContent =
          statusCell.textContent === "Boshlanmagan"
            ? "Bajarilmoqda"
            : "Bajarilgan";
      });

      row.querySelector(".edit-task").addEventListener("click", function () {
        const taskName = row.children[0].textContent;
        const taskDescription = row.children[1].textContent;
        const priority = row.children[2].textContent;
        const deadline = row.children[3].textContent;

        document.getElementById("taskName").value = taskName;
        document.getElementById("taskDescription").value = taskDescription;
        document.getElementById("priority").value = priority;
        document.getElementById("deadline").value = deadline;

        row.remove();
      });

      row.querySelector(".delete-task").addEventListener("click", function () {
        row.remove();
        if (tasksBody.children.length === 0) {
          tasksTable.style.display = "none";
        }
      });
    }
  </script>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

    """
    return HttpResponse(html_response)