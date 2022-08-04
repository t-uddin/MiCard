from setup_app import create_app

app = create_app()

# setup db


if __name__ == "__main__":
    # print(app.config["MONGO_URI"])
    app.run(debug=True)

