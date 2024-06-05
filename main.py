from sys import path
from flask import Flask

path.append('app')

from app import app

if __name__ == '__main__':
	app.run(debug=True)