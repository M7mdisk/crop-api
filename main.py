from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from PIL import Image
import requests
import io
app = FastAPI()

@app.get("/crop")
async def crop(url: str,xmin: int ,ymin: int,xmax:int,ymax:int):
    try:
        im = Image.open(requests.get(url, stream=True).raw)
    except:
        return { "message" : "oops something went wrong"}
    area = (xmin,ymin,xmax,ymax)
    cropped = im.crop(area)
    img = io.BytesIO()
    cropped.save(img,format="PNG")
    img.seek(0)
    return StreamingResponse(img,media_type="image/jpeg")


# @app.get("/image/")
# async def crop(url: str):
#     try:
#         im = Image.open(requests.get(url, stream=True).raw)
#     except:
#         return { "message" : "oops something went wrong"}
#     img = io.BytesIO()
#     im.save(img,format="PNG")
#     img.seek(0)
#     return StreamingResponse(img,media_type="image/jpeg")
#     #return { "message" : f"returning the image at {url} "}


