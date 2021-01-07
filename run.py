from app import create_app

app = create_app()

if __name__ == "__main__":
    debug = False

    if app.config.FLASK_ENV == "development":
        debug = True
    app.run(debug=debug)
