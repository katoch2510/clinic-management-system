Clinic Management System
This is a simple web-based Clinic Management System built using Flask (Python web framework). It allows you to manage patients, appointments, billing, and medical reports with a user-friendly interface and data stored in JSON files.

🚀 Features
👨‍⚕️ Patient Management: Add and view patient details.

📅 Appointment Booking: Schedule and cancel appointments.

💵 Billing System: Generate and view patient bills.

📋 Medical Reports: Create and manage patient reports.

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML (Jinja2 templating)

Storage: JSON files

📁 Project Structure
pgsql
Copy
Edit
clinic-management-system/
│
├── app.py                    # Main Flask application
├── data/                     # Folder to store JSON data files
│   ├── patients.json
│   ├── appointments.json
│   ├── bills.json
│   └── reports.json
├── templates/                # HTML templates
│   ├── index.html
│   ├── patients.html
│   ├── appointments.html
│   ├── billing.html
│   └── report.html
🏁 Getting Started
Prerequisites
Make sure you have Python installed. You can install Flask using:

bash
Copy
Edit
pip install flask
Running the App
Save the code in app.py.

Create a folder named templates and add the required HTML files.

Run the application:

bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000/.

📝 Usage
Visit /patients to add and view patients.

Visit /appointments to book or cancel appointments.

Visit /billing to generate bills.

Visit /report to manage patient reports.

📌 Notes
All data is stored in the data/ folder as JSON files.

This project is suitable for small clinics or educational/demo purposes.

For production, consider replacing JSON with a database like SQLite or PostgreSQL.

📄 License
This project is open-source and free to use for learning and non-commercial purposes.
