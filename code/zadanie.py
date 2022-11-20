from fastapi import FastAPI, File, UploadFile, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from code.primes.primes_functions import is_prime as is_prime_function
from code.picture.picture_functions import invert as invert_function
from fastapi.responses import StreamingResponse
from code.authentification.authentification_functions import login_for_access_token, oauth2_scheme, get_current_time
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="code/templates")

@app.get("/prime/{number}")
def is_prime(number: int):
   return is_prime_function(number)

@app.get("/uploadpicture",  response_class=HTMLResponse)
def uploadpic(request: Request):
    return templates.TemplateResponse("picture_page.html",
                                      {"request": request})

@app.post("/picture")
async def invert(file : UploadFile = File(...)):
    return StreamingResponse(invert_function(file), media_type="image/jpeg")

@app.get("/time")
def get_time(token: str = Depends(oauth2_scheme)):
    return get_current_time(token)

@app.post("/token")
def access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return login_for_access_token(form_data)