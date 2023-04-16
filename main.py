from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from deta import Deta

from src.save_config import save_config
from src.handle_update import handle_update



class Data(BaseModel):
    token: str
    patterns: dict


class App(FastAPI):
    def __init__(self):
        FastAPI.__init__(self)
        self.mount('/public', StaticFiles(directory = 'public'), name = 'public')
        self.url = "https://api.telegram.org/bot{}/{}"
        self.config = Deta().Base('config')

        @self.get('/')
        def home():
            content = open('index.html', 'r').read()
            return HTMLResponse(content)
        
        @self.post('/save')
        def save(data: Data):
            return save_config(self, data)

        @self.post('/update/{bot_id:path}')
        async def update(request: Request, bot_id: str):
            return await handle_update(self, request, bot_id = bot_id)

        @self.post('/favicon.ico')
        def favicon():
            return FileResponse('favicon.ico')



app = App()