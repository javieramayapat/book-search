from typing import Optional
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session

from . import models

def get_books(db: Session, title: Optional[str] = None, description: Optional[str] = None, author: Optional[str] = None):
    """Get all books using SQLAlchemy query with the operator or_

    Args:
        db (Session): database session/connection
        title (Optional[str], optional): book title sent as query parameter.  Defaults to None.
        description (Optional[str], optional): book description sent as query parameter. Defaults to None.
        author (Optional[str], optional): book author sent as query parameter. Defaults to None.

    Returns:
        The list of all books or an empty array if no book is registered
    """
        
    query_books = db.query(models.Book)
    
    if title:
        query_books = query_books.filter(
            and_(models.Book.title.ilike(f"%{title}%"))
        )
    if description:
        query_books = query_books.filter(
            and_(models.Book.description.ilike(f"%{description}%"))
        )
    if author:
        query_books = query_books.filter(
            and_(models.Book.author.ilike(f"%{author}%"))
        )
    
    return query_books.order_by(models.Book.id.desc()).all()