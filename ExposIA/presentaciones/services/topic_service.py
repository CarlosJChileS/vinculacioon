from ..models import Topic
from ..repositories.topic_repo import (
    create_topic, list_topics, get_topic, update_topic, delete_topic
)


def add_topic(data: Topic) -> Topic:
    return create_topic(data)


def get_topics():
    return list_topics()
