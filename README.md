
---

# MongoDB Projects

This repository contains a collection of projects that use **MongoDB** as the database solution. These projects are built using **Flask** for the backend. Below are the details of the projects included in this repository:

---

## Projects

### 1. **Note_App**
- A simple note-taking application where users can create, update, and delete notes.
- Data is stored in a MongoDB database.
- Features include user authentication and CRUD operations for notes.

### 2. **Expense_Tracker**
- An application to track personal expenses, with features to add, update, and categorize expenses.
- Uses MongoDB to store expense data and tracks the total balance over time.
- Includes user authentication and expense categorization.

### 3. **Simple-Blog-App**
- A basic blogging application where users can write and publish blog posts.
- Users can create, read, update, and delete posts.
- MongoDB is used to store blog posts, comments, and user data.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MongoDB
- **Libraries/Frameworks**: Flask-PyMongo, Flask-Login (for authentication), Jinja2 (for templating), etc.

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mongodb-projects.git
   cd mongodb-projects
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your MongoDB instance (local or cloud):
   - For local MongoDB, ensure MongoDB is running on your machine.
   - For MongoDB Atlas, create a cluster and obtain the connection string.

5. Configure the MongoDB URI in the project (usually found in the `config.py` file or as an environment variable):
   ```python
   MONGO_URI = "your-mongo-db-connection-string-here"
   ```

6. Run the Flask application:
   ```bash
   flask run
   ```

The app will be accessible at [http://localhost:5000](http://localhost:5000).

---

## License

MIT License

---
