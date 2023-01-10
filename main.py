from typing import List

from fastapi import FastAPI, Query, Path, Body
from schemas import Author, Book, BookOut


app = FastAPI()


@app.post('/book', response_model=BookOut)
def create_book(item: Book):
    # book = item.dict()
    # book['id'] = 3
    # return book
    return(BookOut(**item.dict(), id=5))

#
# @app.post('/author')
# def create_author(author: Author = Body(..., embed=True)):
#     return {"author": author}


# @app.get('/book')
# def get_book(q: List[str] = Query(["test", "test2"], description="Search book", deprecated=True)):
#     return q


# @app.get('/book/{pk}')
# def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
#     return {"pk": pk, "pages": pages}
