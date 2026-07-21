## Set up Django backend database and update requirements.txt

1. Open terminal
2. Create and activate virtual environment (one-time):

   python -m venv env
   .venv/Scripts/activate  # Windows
   source .venv/bin/activate  # macOS/Linux

3. Install dependencies:
   
   pip install -r requirements.txt
   pip freeze  # Check that everything was installed
   pip freeze > requirements.txt  # Save dependencies

4. Create database:
   
   python manage.py migrate 

   Database has been created (db.sqlite3)
   
5. Start server:
   
   python manage.py runserver
   
   The server then runs at 'http://127.0.0.1:8000'.

## Set up frontend (Angular)
1. Open new terminal
2. Change into the `review_frontend` folder. ('cd review' then press Tab key)
3. Install dependencies:
   
   npm install

4. Rename local environment file:
   - Copy `src/environments/environment.example.ts`
   - Rename the copy to `src/environments/environment.ts`
   - Adjust `apiUrl` in it if needed, in case it's a different URL
5. Start server:
   ng serve
   The server then runs at 'localhost:4200'
