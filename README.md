# Trekking Management Application

## Overview
A Trekking Management Application built using Flask, Vue.js, SQLAlchemy, and SQLite.

### Roles
- Admin
- Trek Staff
- Trekker/User

## Features
- Authentication and Role-Based Access
- Trek Creation and Management
- Trek Booking System
- Trek Staff Dashboard
- Booking History
- Notifications and Reminders
- Scheduled Background Jobs (Celery)
- CSV and HTML Report Export

## Technology Stack
- Flask
- SQLAlchemy
- SQLite
- Vue.js
- Bootstrap
- JWT Authentication
- Celery
- Redis

## Running the Application

### Backend
```bash
pip install -r requirements.txt
flask run
```

### Frontend
```bash
npm install
npm run dev
```

## Project Structure

backend/
├── app/
├── models/
├── api/
├── tasks/
├── static/
└── templates/

frontend/
├── src/
├── components/
├── views/
└── services/

## Main Modules
- Authentication
- Admin Dashboard
- Trek Management
- Staff Operations
- Booking Management
- Notifications
- Reports & Exports

##Predefined email and Id
Admins:
1. email: 'admin@gmail.com', password: 'admin@123'

Staff:
1. email: sachin@tdm.com, password: 12345678
Trekker:
1. email: 'trekker@tdm.com', password: '12345678'
2. email: sanjit@gmail.com, password: 12345678