import shutil
from typing import List

from fastapi import APIRouter, File, Form, UploadFile

from schemas import UploadVideo, GetVideo
from models import Video, User


video_router = APIRouter()


@video_router.post('/')
async def create_video(
    title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)
):
    info = UploadVideo(title=title, description=description)
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    user = await User.objects.first()
    print(type(user))
    return await Video.objects.create(user=user,
                                      **info.dict(),
                                      file=file.filename)

@video_router.get('/video/{video_pk}', response_model=GetVideo, response_model_exclude={"user__users"})
async def get_video(video_pk: int):
    return await Video.objects.select_related('user').get(pk=video_pk)
