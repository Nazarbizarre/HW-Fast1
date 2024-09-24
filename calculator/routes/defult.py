from .. import app

@app.get("/")
def index():
    return "Welcome, to calculate write 'calculate:yournumber+/-yournumber in the link'"