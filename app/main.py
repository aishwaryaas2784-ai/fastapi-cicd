from fastapi import FastAPI

app = FastAPI(title="Student CI/CD Demo", version="1.0.0")

students = ["Rahul", "Priya", "Aishwarya", "Arun", "Sneha"]

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!", "version": "v1"}

@app.get("/students")
def get_students():
    return {"students": students}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
