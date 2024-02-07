from .app import app as application


if __name__ == "__main__":
    from werkzeug.serving import run_with_reloader
    run_with_reloader(application)
