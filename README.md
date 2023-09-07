# Leadboard App

The Leadboard App is a simple Flask application for managing a team leaderboard with their points. Administrators can update points and create new teams.

## Table of Contents

- [About the Project](#about-the-project)
  - [Features](#features)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## About the Project

The Leadboard App is designed to help you keep track of team points and rankings. It provides a user-friendly interface for administrators to manage teams and update their points.

### Features

- Create and manage teams.
- Update team points.
- User authentication for administrators.
- Simple and intuitive interface.

### Built With

- Python 3.8+
- Flask 2.0.1+
- Flask-Login 0.5.0+
- Flask-SQLAlchemy 3.0+
- Flask-Migrate 3.0+

## Getting Started

### Prerequisites

To run this application, you'll need the following:

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone this repository and set up the virtual environment:
   ```bash
   git clone https://github.com/YourUsername/leadboard-app.git
   cd leadboard-app
   python -m venv venv

2. Activate the virtual environment and install dependencies:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     pip install -r requirements.txt
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     pip install -r requirements.txt
     ```   

3. Set up the secret key in the `.env` file:
   Create a file named `.env` in the root directory of the project. Inside the `.env` file, set a secret key for your application.
   You can generate a random secret key using Python or any other secure method. For example:
   ```plaintext
   SECRET_KEY=mysecretkey123

## Usage

1. Run the application:

   ```bash
   flask run

1. Open a web browser and go to [http://localhost:5000](http://localhost:5000) to access the leaderboard.
2. Administrators can log in to update team points and create new teams

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.


