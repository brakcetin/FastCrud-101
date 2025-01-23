from fastapi import FastAPI, Body

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
# Code: 500's mean is there is an error in the code
# these Codes are HTTP codes

# PATH
@app.get("/courses/{course_title}")  # creating dynamic titles
async def get_course(course_title: str):
    for course in courses_db:
        if course.get('title').casefold() == course_title.casefold():  # casefold(): handling case sensitivity
            return course


# 127.0.0.1:800/courses/java = working
# 127.0.0.1:800/courses/scala = null

# this function is not used
@app.get("/courses/{course_id}")  # creating dynamic titles
async def get_course_by_id(course_id: str):  # functions' names can be same
    for course in courses_db:
        if course.get('id') == course_id:  # you cannot use casefold() for int
            return course


# 127.0.0.1:800/courses/1 = null
# 127.0.0.1:800/courses/3 = null => because of same paths for get_course and get_course_by_id
# Whichever one is written first, it will accept it (get_course is written first)
# you can add another path
# 127.0.0.1:800/courses/java = working
# 127.0.0.1:800/courses/scala = null

@app.get("/courses/byid/{course_id}")  # creating dynamic titles
async def get_course_by_id(course_id: int):  # functions' names can be same
    for course in courses_db:
        if course.get('id') == course_id:  # you cannot use casefold() for int
            return course


# 127.0.0.1:800/courses/1 = working
# 127.0.0.1:800/courses/3 = working
# 127.0.0.1:800/courses/java = null
# 127.0.0.1:800/courses/scala = null

# QUERY
@app.get("/courses/")
async def get_category_by_query(category: str):
    courses_to_return = []
    for course in courses_db:
        if course.get('category').casefold() == category.casefold():
            courses_to_return.append(course)
    return courses_to_return


# try on browser: http://127.0.0.1:8000/courses/?category=Development

# PATH AND QUERY
@app.get("/courses/{course_instructor}/")
async def get_instructor_category_by_query(course_instructor: str, category: str):
    courses_to_return = []
    for course in courses_db:
        if (course.get('instructor').casefold() == course_instructor.casefold()
                and course.get('category').casefold() == category.casefold()):
            courses_to_return.append(course)
    return courses_to_return


# try on web: http://127.0.0.1:8000/courses/burak/?category=development
# try on web: http://127.0.0.1:8000/courses/burak/?category=ai
# try on web: http://127.0.0.1:8000/courses/burak/?category=devops

# POST
@app.post("/courses/create_course")
async def create_course(new_course=Body()):
    courses_db.append(new_course)


# step 1: open on web -> http://127.0.0.1:8000/docs
# step 2: expand /courses/create_courses
# step 3: click "Try it out"
# step 4: write below of Request body: {'id': 7, 'instructor': 'Ayse', 'title': 'Docker', 'category': 'DevOps'}
# step 5: click "Execute" button
# !: Propably you took this error: "422 Error: Unprocessable Entity"
# step 6: change ' with " (write: {"id": 7, "instructor": "Ayse", "title": "Docker", "category": "DevOps"})
# step 7: expand /courses Get All Courses
# step 8: click "Try it out"
# step 9: click "Execute" button

# UPDATE with PUT
@app.put("/courses/update_course")
async def update_course(updated_course=Body()):
    for index in range(len(courses_db)): # this time, we used index to find correct element
        if courses_db[index].get("id") == updated_course.get("id"):
            courses_db[index] = updated_course


# step 1: open on web -> http://127.0.0.1:8000/docs
# step 2: expand /courses/update_course
# step 3: click "Try it out"
# step 4: write below of Request body: {'id': 5, 'instructor': 'Cem', 'title': 'ML', 'category': 'AI'}
# step 5: click "Execute" button
# !: Propably you took this error: "422 Error: Unprocessable Entity"
# step 6: change ' with " (write: {"id": 5, "instructor": "Cem", "title": "ML", "category": "AI"})
# step 7: expand /courses Get All Courses
# step 8: click "Try it out"
# step 9: click "Execute" button

# DELETE using PATH
@app.delete("/courses/delete_course/{course_id}")
async def delete_course(course_id: int):  # we are using id to delete specific item
    for index in range(len(courses_db)):
        if courses_db[index].get("id") == course_id:
            courses_db.pop(index)
            break  # we dont need to continue for loop anymore if we found the item


# step 1: open on web -> http://127.0.0.1:8000/docs
# step 2: expand /courses/delete_course
# step 3: click "Try it out"
# step 4: write beside of course_id: 2
# step 5: click "Execute" button
# step 6: expand /courses Get All Courses
# step 7: click "Try it out"
# step 8: click "Execute" button
