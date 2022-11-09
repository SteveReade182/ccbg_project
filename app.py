from application import app

# app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'  # needed for csrf when using forms, it's a known constant, can = anything

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')