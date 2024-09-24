from .. import app



@app.get("/calculate:{equ}")
def calculate(equ:str):
    if "+" in equ:
        num1, num2 = equ.split("+")
        return f"{num1} + {num2} = {int(num1) + int(num2)}"
    elif "-" in equ:
        num1, num2 = equ.split("-")
        return f"{num1} - {num2} = {int(num1) - int(num2)}"
    else:
        return {"error": "Invalid input/operation"}

    