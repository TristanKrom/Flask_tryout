from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():    
    return "<p>Huiswerk les 11!</p>"