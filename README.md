# Professional REST API with Python, Flask, Docker, Flask-Smorest, and Flask-SQLAlchemy

## Overview

This project is a REST API built with Flask, using PostgreSQL as the database.
 
## Installation
 
1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```
 
2. Ensure you have Docker Desktop installed and running on your machine.
 
3. Install Insomnia:
   Download and install Insomnia from [Insomnia's official website](https://insomnia.rest/download).
 
## Local Development
 
1. Start the application:
   ```
   docker compose up
   ```
 
2. The API will be available at `http://localhost:5000`.
 
3. Use Insomnia to test the API endpoints.
 
## Deployment on Render
 
1. Set up a PostgreSQL database service on Render.
 
2. Create a new Web Service on Render:
   - Connect your GitHub repository
   - Select "Docker" as the environment
   - Set the environment variable `DATABASE_URL` to your Render PostgreSQL connection string
 
3. Deploy the service.
 
4. Once deployed, you can access your API at the URL provided by Render.
 
5. Update your Insomnia environment to use the Render URL instead of localhost.
