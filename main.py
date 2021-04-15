from app import app  # noqa: F401

# app.config.from_pyfile("app.config.py")

if __name__ == "__main__":
    app.run(debug=True)
