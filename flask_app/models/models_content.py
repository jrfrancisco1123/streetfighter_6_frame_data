from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Content:
    db = 'sf6'
    def __init__(self, data):
        self.id = data['id']
        self.subject = data['subject']
        self.message = data['message']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    # SAVE
    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO contents ( subject, message, user_id)
                VALUES ( %(subject)s, %(message)s, %(user_id)s )"""
        return connectToMySQL(cls.db).query_db(query, data)
    
    # UPDATE
    @classmethod
    def update(cls, data):
        query = """
                UPDATE contents
                SET subject = %(subject)s, message = %(message)s
                WHERE id = %(id)s"""
        return connectToMySQL(cls.db).query_db(query, data)
    
    # DELETE
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM contents WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)

    # GET ONE 
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM contents WHERE id = %(id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    # GET ALL
    @classmethod
    def content_with_users(cls):
        query = """
                SELECT * FROM contents
                JOIN users
                ON users.id = contents.user_id
                ORDER BY contents.updated_at DESC"""
        results = connectToMySQL(cls.db).query_db(query)
        all_posts = []
        for row in results:
            user_data = {
                'id': row['users.id'],
                'email': row['email'],
                'username': row['username'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            content_data = {
                'id': row['id'],
                'subject': row['subject'],
                'message': row['message'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'user_id': row['user_id'],
                'user': user_data
            }
            all_posts.append(content_data)
        return all_posts

# --------------------- VALIDATIONS ---------------------

    @staticmethod
    def validations(data):
        is_valid = True
        if len(data['subject']) == 0 or len(data['message']) == 0:
            flash("Fields Cannot Be Empty", 'content')
            is_valid = False
        return is_valid

