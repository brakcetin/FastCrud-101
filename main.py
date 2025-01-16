from fastapi import FastAPI

app = FastAPI()  # created an object from FastAPI class

# is an endpoint that we say after each /. for example blabla.com/showcourses
# showcourses is an endpoint

courses_db = [  # create a manuel temporary database
    {'id': 1, 'instructor': 'Burak', 'title': 'Python', 'category': 'Development'},
    {'id': 2, 'instructor': 'Buket', 'title': 'Java', 'category': 'Development'},
    {'id': 3, 'instructor': 'Mahmut', 'title': 'Jenkins', 'category': 'DevOps'},
    {'id': 4, 'instructor': 'Burak', 'title': 'Kubernetes', 'category': 'DevOps'},
    {'id': 5, 'instructor': 'Cem', 'title': 'Machine Learning', 'category': 'AI'},
    {'id': 6, 'instructor': 'Lale', 'title': 'Deep Learning', 'category': 'AI'},
]


@app.get("/hello")  # if you write "/hello", in 127.0.0.1:8000 you will see Not Found! message
# but in 127.0.0.1.800/hello, you will see {"message": "Hello World"} message
async def hello_world():  # we need to work asynchronous with web application
    # but via FastAPI, without "async" word, it will run without any problem
    return {"message": "Hello World"}  # dictionary => key, value => good for JSON format


# JSON -> JavaScript Object Notation

# at console, run: uvicorn main:app --reload
# uvicorn: run the server via unicorn
# reload: if we make any changes in the code, it is re-starting (no need to run new command)
# if you get any error, run "pip install uvicorn" in terminal
# you can see all libraries that you are using with running "pip freeze" command in terminal
# if it didn't fix your problem, try running this in terminal: pip install "fastapi[standard]"
# run: uvicorn main:app --reload or run: fastapi run main.py
# then, open 127.0.0.1:8000 in the browser, check 127.0.0.1:8000/hello

'''
CRUD: Create (POST), Read (GET), Update (PUT), Delete (DELETE)
GET :   the query string (name/value pairs) is sent in the URL of a GET request
        requests can remain in browser history
        read from the server
POST:   The data sent to the server with POST is stored in the request body of the HTTP request
        requests do not remain in browser history
        better and reliable for bigger datas
        send to the server
'''


@app.get("/courses")  # you can also check on 127.0.0.1:800/docs
async def get_all_courses():
    return courses_db


# in 127.0.0.1:800/docs, Code: 200's mean is there is not any problem, Code: 404 is error
# these Codes are HTTP codes

# PATH
@app.get("/courses/{course_title}")  # creating dynamic titles
async def get_course(course_title: str):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold():  # casefold(): handling case sensitivity
            return course
# 127.0.0.1:800/courses/java = working
# 127.0.0.1:800/courses/scala = null
