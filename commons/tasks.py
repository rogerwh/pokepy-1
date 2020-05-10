import json
import time

from celery import shared_task

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage


@shared_task(bind=True)
def websocket_example_task(self):
    facility = self.request.id
    redis_publisher = RedisPublisher(
        facility=facility,
        broadcast=True
    )
    meta = {'mensaje': "Filtrando datos..", "status": "PROGRESS", "task_id": facility}
    publish_message_websocket(redis_publisher, meta)
    time.sleep(3)

    meta = {'mensaje': "Filtrando datos nuevamente..", "status": "PROGRESS", "task_id": facility}
    publish_message_websocket(redis_publisher, meta)
    time.sleep(3)

    meta = {'mensaje': "Obteniendo pokemon..", "status": "PROGRESS", "task_id": facility}
    publish_message_websocket(redis_publisher, meta)
    time.sleep(3)

    result_dic = {
        "cliente": "pedro",
        "consumo": "40GB"
    }
    meta = {'mensaje': json.dumps(result_dic), "status": "DONE", "task_id": facility}
    publish_message_websocket(redis_publisher, meta)

    return "Ejemplo"


def publish_message_websocket(redis_publisher, data):
    redis_publisher.publish_message(RedisMessage(
        json.dumps(data)
    ))
