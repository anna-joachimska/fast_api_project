import PIL
from PIL import Image, ImageOps
from fastapi import FastAPI, File, UploadFile
import io
from io import BytesIO

def invert(file: UploadFile = File(...)):
  file_content = file.file.read()
  img = Image.open(io.BytesIO(file_content))
  # img=img.filter(ImageFilter.BLUR)
  inverted_img = PIL.ImageOps.invert(img)
  inverted_img.save("inverted_img.jpg")
  buffor = BytesIO()
  inverted_img.save(buffor, "JPEG")
  buffor.seek(0);
  return buffor
