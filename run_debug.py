#!/usr/bin/env python3

import app

app = app.create_app()

if __name__ == "__main__":
	app.run(debug=True)
