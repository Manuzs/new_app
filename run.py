from flaskblog import app




data = [
    {"name": "Ranjit","age": 22,"emp":'TCS', "address": "Abad"},
    {"name": "asmf","age": 32, "emp": "AWS","address": "Abad"},
    {"name": "dsasit","age": 12, "emp": "Google", "address": "Abad"}
    ]





if __name__ == "__main__":
    app.run(debug = True)