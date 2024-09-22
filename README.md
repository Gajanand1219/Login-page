# Sign-Up Form with PHP Backend

This repository features a fully functional **Sign-Up Form** developed using **HTML**, **CSS**, and **JavaScript** for the frontend, paired with a **PHP** backend that handles form submissions and stores user data in a MySQL database. This project demonstrates basic web development skills, including form handling, validation, and database integration.

## Project Overview

The sign-up form is designed to allow users to create an account by entering their personal information. The form collects essential details such as name, email, phone number, city, and password. Upon submission, the data is processed and stored in a MySQL database, enabling easy management of user accounts.

## Key Features
- **User-Friendly Interface**: The form is intuitively designed with clear labels and input fields, ensuring a seamless user experience.
- **Responsive Design**: The layout adapts to various screen sizes, making it accessible on both desktop and mobile devices.
- **Form Validation**: Each input field is required, preventing incomplete submissions and ensuring data integrity.
- **Asynchronous Submission**: Utilizes AJAX for form submission, allowing users to send data without reloading the page, enhancing usability.
- **Database Integration**: The PHP backend connects to a MySQL database to store user information securely.

## Technologies Used
- **HTML5**: For structuring the form and its elements.
- **CSS3**: For styling the form, providing a clean and modern look.
- **JavaScript**: To handle the form submission asynchronously and provide dynamic user interactions.
- **PHP**: To process form data and interact with the MySQL database.
- **MySQL**: To store user data securely.

## API Endpoint
- **POST**: `save.php`
  - Receives the form data from the frontend and inserts it into the `loginform` table within the `camera` database.

## Database Setup
To use this application, you need to set up a MySQL database. Follow these steps:
1. **Create the Database**: Name it `camera`.
2. **Create the Table**: Run the following SQL command to create a `loginform` table:
   ```sql
   CREATE TABLE `loginform` (
       `id` INT AUTO_INCREMENT PRIMARY KEY,
       `name` VARCHAR(100),
       `email` VARCHAR(100),
       `phone` VARCHAR(15),
       `city` VARCHAR(100),
       `password` VARCHAR(100)
   );
   # Output
   #
   **Frant-page
![Screenshot 2024-09-22 191505](https://github.com/user-attachments/assets/de001466-f0f8-405c-8a92-a042da68bdf8)

# Backend -table

![Screenshot 2024-09-22 193126](https://github.com/user-attachments/assets/01009e6f-a9e6-4d1d-a9d9-12656b8f2c07)
