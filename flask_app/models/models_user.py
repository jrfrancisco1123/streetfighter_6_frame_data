from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') # Email format

class User:
    db = 'sf6'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.username = data['username']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # SAVE
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO users ( email, username, password )
                VALUES ( %(email)s, %(username)s, %(password)s )"""
        return connectToMySQL(cls.db).query_db(query, data)
    
    # GET EMAIL
    @classmethod
    def get_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    # GET ID
    @classmethod
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
# --------------------- VALIDATIONS ---------------------

    @staticmethod
    def validations(data):
        is_valid = True

        # Email Validations
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('sf6').query_db(query, data)
        if len(results) >= 1 and len(data['email']) > 0:
            flash("Invalid Email", 'registration')
            is_valid = False
        if not EMAIL_REGEX.match(data['email']) and len(data['email']) > 0:
            flash("Invalid Email", 'registration')
            is_valid = False
        if len(data['email']) == 0:
            flash("Email Required", 'registration')
            is_valid = False
        
        # Username Validations
        query = "SELECT * FROM users WHERE username = %(username)s"
        results = connectToMySQL('sf6').query_db(query, data)
        if len(results) >= 1 and len(data['username']) > 0:
            flash("Username is Already Being Used", 'registration')
            is_valid = False
        if len(data['username']) == 0:
            flash("Username Required", 'registration')
            is_valid = False
        if len(data['username']) < 3:
            flash("Username Requires at Least 3 Characters", 'registration')
            is_valid = False

        # Password Validations
        if len(data['password']) == 0 or len(data['confirm_password']) == 0:
            flash("Password Required", 'registration')
            is_valid = False
        if len(data['password']) < 8:
            flash("Password Requires at Least 8 Characters", 'registration')
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Password/Confirm Password Do Not Match", 'registration')
            is_valid = False
        return is_valid