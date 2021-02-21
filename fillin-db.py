import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('users.db')
c = conn.cursor()

hs_users = [
    {
        'firstname': "Isac",
        'lastname': "Nguyen",
        'email': "isacnguyen@gmail.com",
        "username": "isacnguyen",
        'password': "test7890",
        'school': "Harold Brathwaite SS",
        "grade": "Grade 12"
    },

    {
        'firstname': "John",
        'lastname': "Hahm",
        'email': "johnhahm@gmail.com",
        "username": "johnhahm",
        'password': "test3344",
        'school': "Harold Brathwaite SS",
        "grade": "Grade 11"
    },

    {
        'firstname': "Lady",
        'lastname': "Gaga",
        'email': "ladygaga@gmail.com",
        "username": "ladygaga",
        'password': "test7733",
        'school': "Harold Brathwaite SS",
        "grade": "Grade 10"
    },

    {      
        'firstname': "Tana",
        'lastname': "Noel",
        'email': "tananoel@gmail.com",
        "username": "tananoel",
        'password': "test1023",
        'school': "Harold Brathwaite SS",
        "grade": "Grade 9"
    }
]

def database_add_hs_users(users):
    for user in users:
        hashed_pass = generate_password_hash(user["password"])
        c.execute("""INSERT INTO hs_user (first, last, email, username, password, school, grade)\
            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
            (
                user['firstname'],
                user['lastname'],
                user['email'],
                user['username'],
                hashed_pass, 
                user['school'],
                user['grade']
            )
        )
    conn.commit()

database_add_hs_users(hs_users)

uni_users = [
    {
        'firstname': "Bob",
        'lastname': "Smith",
        'email': "bobsmith@gmail.com",
        'university': 'University of Waterloo',
        'program': "Computer Science",
        'study': "Undergraduate",
        'username': 'bobsmith',
        'password': "test1234"
    },

    {
        'firstname': "Todd",
        'lastname': "Gurley",
        'email': "toddgurley@gmail.com",
        'university': 'University of Waterloo',
        'program': "Computer Science",
        'study': "Undergraduate",
        'username': 'toddgurley',
        'password': "test4567",
    },

    {
        'firstname': "Nancy",
        'lastname': "Drew",
        'email': "nancydrew@gmail.com",
        'university': 'University of Waterloo',
        'program': "Computer Science",
        'study': "Undergraduate",
        'username': 'nancydrew',
        'password': "test1122"
    },

    {
        'firstname': "Angel",
        'lastname': "Silva",
        'email': "angelsilva@gmail.com",
        'university': 'University of Waterloo',
        'program': "Computer Science",
        'study': "Undergraduate",
        'username': 'angelsilva',
        'password': "test4455"
    },

    {
        'firstname': "Soham",
        'lastname': "Shah",
        'email': "sohamshah@gmail.com",
        'university': 'University of Waterloo',
        'program': "Computer Science",
        'study': "Undergraduate",
        'username': 'sohamshah',
        'password': "test0606"
    }
]

def database_add_uni_users(users):
    for user in users:
        hashed_pass = generate_password_hash(user["password"])
        c.execute("""INSERT INTO uni_user (first, last, email, university, program, study_level, password, username)\
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
            (
                user['firstname'],
                user['lastname'],
                user['email'],
                user['university'],
                user['program'],
                user['study'],
                hashed_pass, 
                user['username']
            )
        )
    conn.commit()

database_add_uni_users(uni_users)
conn.close()

reviews = [
    {
        "name": "Guneet Bola",
        "university": "University of Waterloo",
        "program": "Computer Science",
        "message": """There are definitely sleepless nights and computer science assignments take forever to finish, but when you finish the program and the code works, the feeling is exhilarating and rewarding. Wonderful program for driven individuals who enjoy challenges.""",
        "rating": 3.5
    },

     {
        "name": "Richa Dalal",
        "university": "University of Waterloo",
        "program": "Computer Science",
        "message": """When I look at the first line on my math assignments I honestly feel lost. But, I realized in this program nothing comes easy, and I have developed a strong work ethic. Once I review lectures and get help from professors and teaching assistants, I am able to enhance my learning. Then, I can implement these skills into effectively solving the assignment questions.""",
        "rating": 4.0
    },

     {
        "name": "Dhir Patel",
        "university": "University of Waterloo",
        "program": "Computer Science",
        "message": """There are times when I feel like switching programs because things become really tough. However, I am glad I have a good group of peers to reach out to and talk to about my emotions because it is important to be able to express your feelings. We all feel the imposter-syndrome but honestly everyone is going through the same thing and we will get through this challenging time. """,
        "rating": 4.5
    },

     {
        "name": "Soham Shah",
        "university": "University of Waterloo",
        "program": "Computer Science",
        "message": """The close-knit community in computer science has allowed me to grow. There is a common stereotype that there is a lack of a community but the professors and peers are truly supportive. Even in a virtual setting I have been able to make good relationships and even met many life-long friends through this program.""",
        "rating": 5.0
    },

    {
        "name": "John Deo",
        "university": "University of Waterloo",
        "program": "Computer Science",
        "message": """Sometimes you may not be able to finish an assignment but, that's okay. Honestly, this program is rigorous and challenges you in every way, but there are endless opportunities in this field. From co-op opportunities and extracurricular activities, being a computer science student is exciting and rewarding!""",
        "rating": 4.0
    }
]

def add_ratings_to_db(reviews):
    conn = sqlite3.connect('reviews.db')
    c = conn.cursor()
    for review in reviews:
        c.execute("""INSERT INTO reviews (name, university, program, message, rating)\
            VALUES (?, ?, ?, ?, ?)""", 
            (
                review['name'],
                review['university'],
                review['program'],
                review['message'],
                review['rating'],       
            ))
    conn.commit()
    conn.close()

add_ratings_to_db(reviews)
