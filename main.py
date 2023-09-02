import datetime
import random
import time

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from crud import get_game1, get_game2, get_game3, add_game1, add_game2, add_game3
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Game1, Game2, Game3

from database import get_db

description = """

"""

tags_metadata = [
        {
                'name'       : '게임 점수',
                'description': "게임 점수 추가 또는 업데이트",
        },
        {
                'name'       : '세션 아이디 발급',
                'description': "세션 아이디를 발급합니다.",
        }
]

app = FastAPI(
        title="하나고등학교 인트라넷 게시판 요약 서비스",
        description=description,
        version="alpha",
        contact={
                "name" : "안호성",
                "url"  : "https://github.com/BetaTester772",
                "email": "hoseong8115.dev@gmail.com",
        },
        license_info={
                "name"      : "Apache 2.0",
                "identifier": "MIT",
        },
        docs_url="/docs", redoc_url="/redoc",
        openapi_tags=tags_metadata,
)

# middleware cors
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

index_html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Test</title>
    </head>
    <body>
        <div id='messages'>
        </div>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('p')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
                window.scrollBy(0, 1000000000000000000000000000)
            };
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(index_html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    index = 0
    while True:
        time.sleep(0.5)
        # raise ValueError(get_game1(db))
        await websocket.send_json(
                {
                        "game1": get_game1(db).to_dict(orient='records'),
                        "game2": get_game2(db).to_dict(orient='records'),
                        "game3": get_game3(db).to_dict(orient='records'),
                        "index": [index, str(datetime.datetime.now())],
                }
        )
        index += 1


@app.post("/upload_game1", status_code=204, tags=["게임 점수"])
async def upload_game1(session_id: int, name: str, student_id: int, score: int, db: Session = Depends(get_db)):
    add_game1(db, session_id, student_id, name, score)
    return


@app.post("/upload_game2", status_code=204, tags=["게임 점수"])
async def upload_game2(session_id: int, name: str, student_id: int, score: int, db: Session = Depends(get_db)):
    add_game2(db, session_id, student_id, name, score)
    return


@app.post("/upload_game3", status_code=204, tags=["게임 점수"])
async def upload_game3(session_id: int, name: str, student_id: int, score: int, db: Session = Depends(get_db)):
    add_game3(db, session_id, student_id, name, score)
    return


@app.get("/session_id", tags=["세션 아이디 발급"])
async def make_seesion_id(game: int, db: Session = Depends(get_db)):
    game_dict = {1: Game1, 2: Game2, 3: Game3}
    # return db.query(game_dict[game]).count() + 3
    session_id = random.randint(1000, 9999) * 1000000 + db.query(game_dict[game]).count()
    while True:
        if db.query(game_dict[game]).filter(game_dict[game].session_id == session_id).first():
            continue
        else:
            return session_id
