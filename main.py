from fastapi import FastAPI

app = FastAPI()  # created an object from FastAPI class


# is an endpoint that we say after each /. for example blabla.com/showcourses
# showcourses is an endpoint

@app.get("/hello")  # if you write "/hello", in 127.0.0.1:8000 you will see Not Found! message
# but in 127.0.0.1.800/hello, you will see {"message": "Hello World"} message
async def hello_world():  # we need to work asynchronous with web application
    # but via FastAPI, without "async" word, it will run without any problem
    return {"message": "Hello World"}  # dictionary

# at console, run: uvicorn main:app --reload
# uvicorn: run the server via unicorn
# reload: if we make any changes in the code, it is re-starting (no need to run new command)
# if you get any error, run "pip install uvicorn" in terminal
# you can see all libraries that you are using with running "pip freeze" command in terminal
# if it didn't fix your problem, try running this in terminal: pip install "fastapi[standard]"
# run: uvicorn main:app --reload or run: fastapi run main.py
# then, open 127.0.0.1:8000 in the browser, check 127.0.0.1:8000/hell
