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
   uvicorn test2:app --reload
   ```
