import random
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

messages = ["Erro ao conectar", "Usuario autenticado", "Requisicao recebida"]

while True:
    logging.info(random.choice(messages))
    time.sleep(2)
