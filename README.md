It's an online portal for booking appointments with available doctors, enhanced by an AI assistant.

# easy_health

**An online portal to book appointments with available doctors, enhanced by an AI assistant.**

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Overview
**easy_health** is designed to streamline the process of booking medical appointments. Integrated with an AI assistant, it helps users find available doctors quickly and efficiently.

## Features
- 🔘 Browse and search for available doctors
- 🗓 Schedule and manage appointments
- 🤖 Interact with an AI assistant for guidance and recommendations
-  Responsive, user-friendly interface

## Technologies
Built using:
- **Python** – backend logic, AI integration, scheduling
- **HTML**, **CSS**, **JavaScript** – frontend UI
- **SQLite** – lightweight database via `db.sqlite3`
- Framework: Django

## Demo
You can visit a live link : `https://mafuzur22.pythonanywhere.com/`
## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mafuzur22/easy_health.git
   cd easy_health
   ```

2. **Set up a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Database setup**
   If using Django:

   ```bash
   python manage.py migrate
   ```
5. **Run the application**

   ```bash
   python manage.py runserver
   ```

   Then open `http://127.0.0.1:8000/` in your browser.

## Usage

Describe how a user interacts with the app:

* Navigate to the homepage, search for doctors
* Use the AI assistant by clicking/interacting with \[assistant interface]
* Book appointments, view confirmations, manage bookings

## Project Structure

```
easy_health/
├── assistant/        # AI assistant functionality (conversations, logic)
├── main_site/        # Main application logic and views
├── templates/        # HTML templates (UI views)
├── static/           # Static assets (CSS, JS, images)
├── db.sqlite3        # SQLite database
├── manage.py         # Django (or similar) project manager
└── requirements.txt  # Python dependencies
```

## Contributing

Contributions are welcome! Here’s how to help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to your branch (`git push origin feature/my-feature`)
5. Open a pull request and describe your changes

Feel free to open issues for bugs or enhancements!

## Contact

For questions or collaboration, reach out to mafuzur22 at mfrahaman22@gmail.com
