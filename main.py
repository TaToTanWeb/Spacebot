from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from deta import Deta

from src.save_config import save_config
from src.handle_update import handle_update



class Data(BaseModel):
    # used to recieve JSON body of POST requests
    token: str
    patterns: dict


class App(FastAPI):
    def __init__(self):
        FastAPI.__init__(self)
        # automatically serving all files in the "public" folder
        self.mount('/public', StaticFiles(directory = 'public'), name = 'public')
        # base url for telegram bots api (https://core.telegram.org/bots/api)
        self.url = "https://api.telegram.org/bot{}/{}"
        # setting up the deta base sdk (https://deta.space/docs/en/reference/base/sdk)
        self.config = Deta().Base('config')

        # Routes
        # / — view the main app interface
        @self.get('/')
        def home():
            content = open('index.html', 'r').read()
            return HTMLResponse(content)
        
        # /save — store configuration and set the webhook
        @self.post('/save')
        def save(data: Data):
            return save_config(self, data)

        # /update (public) — handle telegram updates
        @self.post('/update/{bot_id:path}')
        async def update(request: Request, bot_id: str):
            return await handle_update(self, request, bot_id = bot_id)

        # /favicon.ico — returns the favicon for browsers
        @self.post('/favicon.ico')
        def favicon():
            return FileResponse('favicon.ico')



app = App()