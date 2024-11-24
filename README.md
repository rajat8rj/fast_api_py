# fast_api_py

##Initial setup

1. Create virtual environemnt
   ```bash
   python3 -m venv venv
   ```
2. Activate virtual environment

   ```bash
   source venv/bin/activate
   ```
3. Install dependencies

   ```bash
   pip install fastapi uvicorn mysql-connector-python sqlalchemy
   ```

4. Setup mysql and create database

   ```bash
   CREATE DATABASE request_db;
   GRANT ALL PRIVILEGES ON request_db.* To 'user'@'localhost'; IDENTIFIED BY 'test123';
   GRANT ALL PRIVILEGES ON request_db.* To 'user'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. Run the app
   ```bash
   uvicorn main_api:app --reload
   ```

####Dockerising the APi

1. Build the api image
   ```bash
   docker-compose build
   ```
2. Deploy the app
   ```bash
   docker-compose up
   ```

####Deloying on minikube

Prerequisites:
- minikube
- kubectl

1. Start minikube with docker driver
   ```bash
   minikube start --driver=docker
   ```

2. Point docker cli to minikube's docker daemon
   ```bash
   eval $(minikube docker-env)
   ```
  
3. Build the image
   ```bash
   docker build -t fast_api_py_app:latest .
   ```
     
5. Deploy all manifest file with kubectl

6.  For ingress setup enbale nginx addon for minikube
   ```bash
   minikube addons enable ingress
   ```

7. Apply the ingress manifest and test api as:
   ```bash
   curl http://192.168.49.2.nip.io/count
   ```


