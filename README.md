# Cloud-Based Student Registration System

A web-based student registration system built using **Python Flask, MySQL, Amazon S3, and Boto3**. The application collects student registration details, stores structured information in MySQL, and automatically uploads student documents and photographs to Amazon S3.

## Features

* Student registration form
* Stores student details in MySQL
* Uploads student documents to Amazon S3
* Uploads student photographs to Amazon S3
* Automatic S3 upload using Boto3
* Separate S3 folders for documents and photos
* Flask-based backend
* SQL database integration

## Technology Stack

* **Python**
* **Flask**
* **MySQL**
* **Amazon S3**
* **Boto3**
* **HTML/CSS**
* **SQL**

## System Architecture

```text
Student
   |
   v
Registration Form
   |
   v
Flask Application
   |
   +--------------------+
   |                    |
   v                    v
MySQL Database       Amazon S3
   |                    |
   v                    v
Student Details     Documents
                    Photos
```

## Database

The project uses a MySQL database named:

```text
student_registration
```

The `students` table stores:

* Student ID
* Name
* Class
* Section
* Gender
* Email
* Phone
* Document filename
* Photo filename
* Registration timestamp

## AWS S3 Storage

Uploaded files are stored in Amazon S3 using Boto3.

The bucket is organized as:

```text
student-registration-avantika-2026
|
+-- documents/
|     +-- student-document.pdf
|
+-- photos/
      +-- student-photo.jpg
```

## How It Works

1. Student fills out the registration form.
2. Flask receives the submitted information.
3. Student details are inserted into MySQL.
4. The uploaded document is sent to Amazon S3 using Boto3.
5. The uploaded photograph is sent to Amazon S3.
6. The filenames are stored along with the student's registration record in MySQL.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Configure your MySQL database and AWS credentials locally.

Run the Flask application:

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## Security

AWS credentials and other sensitive configuration values should **not be stored in the source code or committed to GitHub**.

## Project Purpose

This project demonstrates the integration of a web application with a relational database and cloud storage. It was developed as a practical project to understand **Flask, MySQL, AWS S3, Boto3, and cloud-based file management**.

## Author

**Avantika Doble**

Computer Science Engineering Student
