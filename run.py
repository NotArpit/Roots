from routes import app

if (__name__ == "__main__"):
	app.run(port = 8082, debug = True, use_reloader = True)
