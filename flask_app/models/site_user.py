from flask_app.config.mysqlconnection import connectToMySQL

class Site_User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * from site_users"

        results = connectToMySQL('User_CR').query_db(query)
        site_users = []

        for user in results:
            site_users.append(cls(user))
        return site_users
    
    @classmethod
    def save(cls, data):
        query = """INSERT INTO site_users(first_name, last_name, email, created_at, updated_at)
                VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW(), NOW());
                """
        return connectToMySQL('User_CR').query_db(query, data)
    
    @classmethod
    def get_one(cls, user_id):
        query = """SELECT * from site_users
                WHERE id = %(id)s;
                """
        data = {'id' : user_id}
        result = connectToMySQL('User_CR').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_one_new(cls, data):
        query = """SELECT * from site_users
                WHERE first_name = %(first_name)s AND last_name = %(last_name)s AND email = %(email)s;
                """
        result = connectToMySQL('User_CR').query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = """UPDATE site_users
                SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW()
                WHERE id = %(id)s;
                """
        return connectToMySQL('User_CR').query_db(query, data)
    
    @classmethod
    def delete(cls, user_id):
        query = """DELETE from site_users
                WHERE id = %(id)s;
                """
        data = {'id': user_id}
        return connectToMySQL('User_CR').query_db(query, data)
        
        