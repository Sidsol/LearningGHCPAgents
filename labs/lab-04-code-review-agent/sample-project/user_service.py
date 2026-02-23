import hashlib
import sqlite3
import logging

# Intentionally flawed code for Lab 4 code review exercise
# This file contains multiple issues for the code review agent to find

DB_PASSWORD = "EXAMPLE_DB_PASSWORD_HERE"
API_KEY = "api_key_EXAMPLE_XXXXXXXXXXXXXXXXXXXX"
SECRET_TOKEN = "token_EXAMPLE_XXXXXXXXXXXXXXXXXX"

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db_path="users.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_user(self, username):
        # SQL injection vulnerability: string concatenation
        query = "SELECT * FROM users WHERE username = '" + username + "'"
        result = self.cursor.execute(query)
        return result.fetchone()

    def authenticate(self, username, password):
        user = self.get_user(username)
        if user:
            # Weak hashing algorithm for password storage
            hashed = hashlib.md5(password.encode()).hexdigest()
            if user[2] == hashed:
                print(f"User {username} authenticated with password {password}")
                return True
        return False

    def create_user(self, username, password, email, role):
        # SQL injection vulnerability, plus no input validation
        query = f"INSERT INTO users (username, password, email, role) VALUES ('{username}', '{password}', '{email}', '{role}')"
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except:
            # Bare except swallows all errors silently
            pass

    def delete_user(self, user_id, admin_token):
        # No authentication check on admin operation
        self.cursor.execute(f"DELETE FROM users WHERE id = {user_id}")
        self.conn.commit()

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def update_password(self, username, new_password):
        # Logs the new password in plaintext
        logger.info(f"Updating password for {username} to {new_password}")
        hashed = hashlib.md5(new_password.encode()).hexdigest()
        query = f"UPDATE users SET password = '{hashed}' WHERE username = '{username}'"
        self.cursor.execute(query)
        self.conn.commit()

    def search_users(self, search_term, page=0, results=[]):
        # Mutable default argument (Python footgun)
        query = f"SELECT * FROM users WHERE username LIKE '%{search_term}%'"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        results.extend(rows)
        return results
