# Flask MongoDB CRUD API

## 🚀 Overview

This is a **Flask** application that provides **CRUD operations** (Create, Read, Update, Delete) for a **User resource** using **MongoDB**. The application is containerized with **Docker** and exposes **RESTful API endpoints** for user management.

## 📌 Features

- **REST API with Flask**
- **MongoDB database connection**
- **User authentication with hashed passwords (bcrypt)**
- **Dockerized for easy deployment**
- **Testable via Postman**

---

## 🛠️ Tech Stack

- **Flask** (Python web framework)
- **MongoDB** (NoSQL database)
- **Flask-PyMongo** (MongoDB integration)
- **Flask-RESTful** (API framework)
- **bcrypt** (Password hashing)
- **Docker & Docker Compose**

---

## 🏗️ Project Structure

```
flask-mongo-crud/
│── app/
│   ├── __init__.py      # Initializes Flask App
│   ├── config.py        # App Configuration
│   ├── models.py        # Database Models
│   ├── routes.py        # API Routes
│── Dockerfile           # Docker Setup
│── requirements.txt     # Dependencies
│── docker-compose.yml   # Docker Compose File
│── run.py               # Entry Point
│── README.md            # Documentation
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone <your-repo-url>
cd flask-mongo-crud
```

### 2️⃣ Set Up Docker

Make sure Docker is installed and running.

Run the following command to build and start the containers:

```sh
docker-compose up --build
```

This will:

- Start **MongoDB** in a Docker container.
- Start **Flask API** in another container.
- Connect both services.

---

## 🛠️ API Endpoints

| Method     | Endpoint      | Description         |
| ---------- | ------------- | ------------------- |
| **GET**    | `/users`      | Retrieve all users  |
| **GET**    | `/users/<id>` | Get user by ID      |
| **POST**   | `/users`      | Create a new user   |
| **PUT**    | `/users/<id>` | Update user details |
| **DELETE** | `/users/<id>` | Delete user         |

---

## 📌 Testing with Postman

### 1️⃣ **Create a New User**

- **Endpoint:** `POST /users`
- **Body (JSON):**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "mypassword"
}
```

### 2️⃣ **Retrieve All Users**

- **Endpoint:** `GET /users`

### 3️⃣ **Retrieve a Specific User**

- **Endpoint:** `GET /users/<id>`

### 4️⃣ **Update a User**

- **Endpoint:** `PUT /users/<id>`
- **Body (JSON):**

```json
{
  "name": "Updated Name"
}
```

### 5️⃣ **Delete a User**

- **Endpoint:** `DELETE /users/<id>`

---

## 🛠️ Stopping & Removing Containers

To stop the containers, run:

```sh
docker-compose down
```

To remove all unused containers and images:

```sh
docker system prune -a
```

---

## 📌 Contributing

Feel free to fork this repository and submit a pull request if you have any improvements!

---

## 📜 License

This project is licensed under the MIT License.

---

## \\

## 📬 Contact

If you have any questions, feel free to reach out!

📧 Email: [your-email@example.com](mailto\:acanmolchauhan1234@gmail.com)\
🔗 GitHub: [Your GitHub Profile](https://github.com/AnmolChauhan1234)

---

## 📌 Next Steps

✅ Implement JWT authentication (optional)\
✅ Write unit tests with `pytest`\
✅ Deploy using **AWS/GCP/DigitalOcean**

