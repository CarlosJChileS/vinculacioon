from fastapi import APIRouter
from ..models import Topic
from ..services.topic_service import add_topic, get_topics

router = APIRouter(prefix="/topics")

@router.post("/", response_model=Topic)
async def create_topic_route(topic: Topic):
    return add_topic(topic)

@router.get("/", response_model=list[Topic])
async def list_topics_route():
    return get_topics()
