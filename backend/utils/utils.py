import aiofiles

from os.path import join
from time import time
from fastapi import UploadFile

from settings import MEDIA_ROOT


async def image_preprocessing(commons: dict):
    image: UploadFile = commons.get("image")
    if image:
        new_filename = image.filename.split(".")
        new_filename = f"{hash(new_filename[0]+str(time()))}.{new_filename[1]}" 
        image.filename = new_filename
        current_path = join(MEDIA_ROOT, image.filename)

        async with aiofiles.open(current_path, 'wb') as out_file:
            content = await image.read()
            await out_file.write(content)
        
        commons["image"] = str(new_filename)

    return commons