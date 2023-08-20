# Authentication and Authorization System

This Python-based project demonstrates the implementation of a mock Authentication and Authorization System using Flask and JWT (JSON Web Tokens). The project consists of three components: Authorization Server, Resource API, and a Client interacting with both.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Testing](#testing)


## Features

- **Authorization Server:** Handles user authentication, generates JWT tokens, and issues them to clients.
- **Resource API:** Provides protected resources and verifies JWT tokens before granting access.
- **Client:** Simulates a client application that interacts with the Authorization Server and accesses protected resources.

## Getting Started

### Prerequisites

- Python (3.x)
- `pip` package manager

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/Amit-Kumar19/mock-authorization-assignment.git
   cd mock-authorization-assignment

2. Create and activate a virtual environment

   ```bash
    python3 -m venv venv
    source venv/bin/activate

3. Install project dependencies
 
   ```bash
   pip install -r requirements.txt

## Project Structure

   ```bash
├── README.md
├── authorization_server
│   ├── auth.py
│   ├── mock_users/py
│   ├── utils.py
├── client
│   ├── main.py
├── resource_api
│   ├── main.py
│   ├── sample_data.py
├── tests
├   ├── test_authorization_server.py
├   ├── test_client.py
├   ├── test_resource_api.py
├── requirements.txt
├── .gitignore
├── venv_screenshot
```

## Usage

  ```bash
   1. # Start Authorization Server:
      python -m authorization_server.auth

   2. # Start Resource API:
      python -m resource_api.main

   3. # Run Client:
      python -m client.main --username user1 --password password
  ```

## Testing

  ```bash
  1. # Authorization Server tests
     python -m unittest tests.test_authorization_server.TestAuthorizationServer

  2. # Resource API tests
     python -m unittest tests.test_resource_api.TestResourceAPI

  3. # Client tests
     python -m unittest tests.test_client.TestClient