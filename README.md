# Sunstone-Ace-Academy-Backend-Certification
This is the project for backend certification provided by Sunstone Ace Academy


# Management Systems Project

## Table of Contents
- Project Description
- Features
- Technologies Used
- Project Structure
- Setup Instructions
- Usage
- Contributing
- Contact

## Project Description
This project includes three management systems: Library Management System, Student Management System, and Bank Management System. Each system is built using Flask for the backend, SQLAlchemy with SQLite3 for the database, and Bootstrap for designing the front end.



### Library Management System
- **Pages:**
  - `parent.html`
  - `add_book.html`
  - `updatebook.html`
  - `table.html`

### Student Management System
- **Pages:**
  - `parent.html`
  - `add_student.html`
  - `updatestudent.html`
  - `table.html`

### Bank Management System
- **Pages:**
  - `parent.html`
  - `add_account.html`
  - `updateaccount.html`
  - `table.html`

## Backend Technology
- **Flask:** Used for handling server-side logic and routing.
- **SQLAlchemy:** An ORM (Object Relational Mapper) used for database operations.

## Database
- **SQLite3:** A lightweight disk-based database.

## Designing
- **Bootstrap:** Used for creating responsive and visually appealing web pages.

## Getting Started

### Prerequisites
- Python 3.x
- Flask
- SQLAlchemy
- SQLite3
- Bootstrap (included in templates)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/thedead101/Sunstone-Ace-Academy-Backend-Certification
2. **Change to the project directory:**
   ```bash
   cd management-systems-project
3. **Create a virtual environment:**
```bash
    python -m venv venv
```
4. **Activate the virtual environment:**
On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
5. **Install the required packages:**
```bash
pip install -r requirements.txt    
```
## Running the Application
1. **Run the Application:**
    ```bash
    python app.py
    ```

2. **Access the Application:**
    - Open your web browser and navigate to `http://127.0.0.1:5000/`

## Project Structure
``` plain 
management-systems-project/
│
├── templates/
│   ├── library_management/
│   │   ├── parent.html
│   │   ├── add_book.html
│   │   ├── updatebook.html
│   │   └── table.html
│   │
│   ├── student_management/
│   │   ├── parent.html
│   │   ├── add_student.html
│   │   ├── updatestudent.html
│   │   └── table.html
│   │
│   └── bank_management/
│       ├── parent.html
│       ├── add_account.html
│       ├── updateaccount.html
│       └── table.html
│
├── app.py
├── extension.py
├── model.py
├── requirements.txt
└── README.md
```  
## Features
### Library Management System
- Add, update, and view books.
- Responsive design using Bootstrap.

### Student Management System
- Add, update, and view students.
- Responsive design using Bootstrap.

### Bank Management System
- Add, update, and view bank accounts.
- Responsive design using Bootstrap.

## Contributing
Contributions are welcome! Please create a pull request or submit an issue for any bugs or feature requests.

## License
This project is licensed under the MIT License.
