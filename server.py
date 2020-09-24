from src import app
import os

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=os.getenv('PORT', 5000))