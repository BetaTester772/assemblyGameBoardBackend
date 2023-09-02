import http

from passlib.context import CryptContext
from sqlalchemy.orm import Session
import pandas as pd
from fastapi import HTTPException

from models import Game1, Game2, Game3

d_game1_score_max = 1
d_game2_score_max = 1
d_game3_score_max = 1


def get_game1(db: Session):
    df = pd.read_sql_table('game1', con=db.bind).sort_values(by='score', ascending=False).head(10)
    return df


def get_game2(db: Session):
    df = pd.read_sql_table('game2', con=db.bind).sort_values(by='score', ascending=False).head(10)
    return df


def get_game3(db: Session):
    df = pd.read_sql_table('game3', con=db.bind).sort_values(by='score', ascending=False).head(10)
    return df


def add_game1(db: Session, session_id: int, student_id: int, name: str, score: int):
    game = db.query(Game1).filter(Game1.session_id == session_id).first()
    if game:
        if game.score - score > d_game1_score_max:
            raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST, detail="점수가 너무 많이 차이납니다.")
        game.score = score
    else:
        db_game1 = Game1(session_id=session_id, student_id=student_id, name=name, score=0)
        db.add(db_game1)
    db.commit()


def add_game2(db: Session, session_id: int, student_id: int, name: str, score: int):
    game = db.query(Game2).filter(Game2.session_id == session_id).first()
    if game:
        if game.score - score > d_game2_score_max:
            raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST, detail="점수가 너무 많이 차이납니다.")
        game.score = score
    else:
        db_game2 = Game2(session_id=session_id, student_id=student_id, name=name, score=0)
        db.add(db_game2)
    db.commit()


def add_game3(db: Session, session_id: int, student_id: int, name: str, score: int):
    game = db.query(Game3).filter(Game3.session_id == session_id).first()
    if game:
        if game.score - score > d_game3_score_max:
            raise HTTPException(status_code=http.HTTPStatus.BAD_REQUEST, detail="점수가 너무 많이 차이납니다.")
        game.score = score
    else:
        db_game3 = Game3(session_id=session_id, student_id=student_id, name=name, score=0)
        db.add(db_game3)
    db.commit()
