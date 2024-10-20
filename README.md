# Project_6 - Curation App

This project is a **backend** curation logic application. The app allows users to curate questions by providing options like "Correct," "Not Correct," and "Not Sure." The app is designed to be easily deployable using Docker for containerization, making setup and running simple.

## Features
- Curate questions with three choices: "Correct," "Not Correct," and "Not Sure."
- API-based backend powered by Flask.
- Database management using MongoDB.
- Containerized with Docker for simple deployment.

## Technologies Used
- **Flask** (with Flask-RESTx for API design)
- **MongoDB** (as the database)
- **Python 3.10**
- **Docker** (for containerization)

## Prerequisites

Make sure you have the following installed:
- **Docker**: [Get Docker here](https://www.docker.com/get-started)
- **Docker Compose** (bundled with Docker Desktop)

## Setup & Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yoftil7/project_6.git
    cd project_6
    ```

2. **Build and Run with Docker:**
    Simply run the following command to build the Docker image and start the services:
    ```bash
    docker-compose up --build
    ```

3. The backend will be available on [http://localhost:5000](http://localhost:5000).

## Usage

Once the app is running, you can interact with the API to curate questions. The available options are:
- **Correct**
- **Not Correct**
- **Not Sure**

You can customize and extend the app by editing the Flask routes and MongoDB models.

## API Documentation

The API documentation will be auto-generated using **Flask-RESTx** and available at:
```
http://localhost:5000/docs
```


## How to Contribute

Feel free to fork this repository, make any improvements, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
