from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# File paths
PATIENTS_FILE = 'data/patients.json'
APPOINTMENTS_FILE = 'data/appointments.json'
BILLS_FILE = 'data/bills.json'

# Helper functions to load/save JSON data
def load_data(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as f:
        return json.load(f)

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

# Patients
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    patients = load_data(PATIENTS_FILE)
    if request.method == 'POST':
        new_patient = {
            'id': len(patients) + 1,
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender']
        }
        patients.append(new_patient)
        save_data(PATIENTS_FILE, patients)
        return redirect(url_for('patients'))
    return render_template('patients.html', patients=patients)

# Appointments
@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    appointments = load_data(APPOINTMENTS_FILE)
    if request.method == 'POST':
        new_appointment = {
            'id': len(appointments) + 1,
            'patient_name': request.form['patient_name'],
            'date': request.form['date'],
            'time': request.form['time']
        }
        appointments.append(new_appointment)
        save_data(APPOINTMENTS_FILE, appointments)
        return redirect(url_for('appointments'))
    return render_template('appointments.html', appointments=appointments)

@app.route('/cancel_appointment/<int:id>')
def cancel_appointment(id):
    appointments = load_data(APPOINTMENTS_FILE)
    appointments = [a for a in appointments if a['id'] != id]
    save_data(APPOINTMENTS_FILE, appointments)
    return redirect(url_for('appointments'))

# Billing
@app.route('/billing', methods=['GET', 'POST'])
def billing():
    bills = load_data(BILLS_FILE)
    if request.method == 'POST':
        new_bill = {
            'id': len(bills) + 1,
            'patient_name': request.form['patient_name'],
            'service': request.form['service'],
            'amount': request.form['amount'],
            'status': request.form['status']
        }
        bills.append(new_bill)
        save_data(BILLS_FILE, bills)
        return redirect(url_for('billing'))
    return render_template('billing.html', bills=bills)

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    for file in [PATIENTS_FILE, APPOINTMENTS_FILE, BILLS_FILE]:
        if not os.path.exists(file):
            save_data(file, [])
    app.run(debug=True)
