from config import create_app

app = create_app()

# setup db


if __name__ == "__main__":
    # print(app.config["MONGO_URI"])
    app.run(host='0.0.0.0', debug=True)

