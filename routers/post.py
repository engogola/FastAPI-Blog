from fastapi import APIRouter, Depends
from routers.schemas import PostBase, postDisplay
from sqlalchemy.orm import session
from database.database import get_db
from database import db_post

router=APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('')
def create(requests:PostBase ,db: session=Depends(get_db)):
    return db_post.create(db ,requests)

@router.post('/all')
def posts(db: session= Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}')
def delete(id: int, db: session=Depends(get_db)):
    return db_post.delete(id,db)
