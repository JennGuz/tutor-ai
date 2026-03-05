from ninja import NinjaAPI
import random

api = NinjaAPI()

@api.get("/hello-world")
def hello(request):
    saludos = ["Hola!", "Hello world!", "Bienvenido!", "Welcome!", "Hallo!", "こんにちは!", "안녕하세요!", "Bonjour!", "Ciao!", "Hallo!"]
    return {"message": random.choice(saludos)}