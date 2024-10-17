from api.app.server import server_app
from api.app.config import HOST, PORT

if __name__ == "__main__":
    server_app.run(host=HOST, port=PORT)
