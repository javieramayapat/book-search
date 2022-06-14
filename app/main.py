from fastapi import FastAPI, Query, status, Depends

from typing import List, Optional
from sqlalchemy.orm import Session

# import crud.py file
from . import crud, schemas, models

# In a very simplistic way create the database tables:
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Now use the SessionLocal class we created in the sql_app/database.py file to create a dependency.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(path="/")
def index():
    return {"Hello": "World"}


@app.get(path="/books", response_model=List[schemas.BookOut] , status_code=status.HTTP_200_OK, tags=['Books'])
def get_books(
    db: Session = Depends(get_db),
    title: Optional[str] = Query(None, min_length=1, max_length=150),
    description: Optional[str] = Query(None, min_length=1, max_length=250),
    author: Optional[str] = Query(None, min_length=1, max_length=150),
):
    books = crud.get_books(db=db, title=title, description=description, author=author)
    return books