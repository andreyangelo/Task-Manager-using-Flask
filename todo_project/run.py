from todo_project import app
import os

if __name__ == '__main__':
    app.run(
        debug=os.getenv("FLASK_DEBUG", "False") == "True",
        host=os.getenv("FLASK_HOST", "127.0.0.1"),
        port=int(os.getenv("FLASK_PORT", "8080"))
    )
