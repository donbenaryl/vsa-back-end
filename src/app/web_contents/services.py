from src.app.web_contents.schemas import IBasicDetailUpdateData, IPageDetails
from src.config.db import get_db
from src.app.web_contents.models import BasicDetails, PageDetails

from flask import jsonify, make_response

USER_KEY = "0x66dFA4b56678B6EdE0ab2765804EeB009dc0EE47"
SECRET_KEY = "12da3c99a9c42c33347b67e452af5e8b9bad81bc4fbfb777af9749cbc6e5399d"

def get_basic_details():
    db = next(get_db())
    contents = db.query(BasicDetails).order_by(BasicDetails.order.asc()).all()
    
    # EMAIL NOT FOUND
    if len(contents) == 0:
        return make_response(jsonify({
            "msg": "No data found"
        }), 404) 

    contentsArr = []
    for content in contents:
        contentsArr.append(content.toDict()) 

    return contentsArr

def get_page_details(page_module: int):
    db = next(get_db())
    goals = db.query(PageDetails).filter(PageDetails.page_module == page_module).all()
    
    # EMAIL NOT FOUND
    if len(goals) == 0:
        return make_response(jsonify({
            "msg": "No data found"
        }), 404) 

    goalsArr = []
    for content in goals:
        goalsArr.append(content.toDict()) 

    return goalsArr

def get_page_detail(id):
    db = next(get_db())
    data = db.query(PageDetails).filter(PageDetails.id == id).first()
    
    # EMAIL NOT FOUND
    if data == None:
        return make_response(jsonify({
            "msg": "No data found"
        }), 404) 

    return data.toDict()


def data_to_add(data: IPageDetails):
    if (data.id == 0):
        return True
    else:
        return False


def data_to_update(data: IPageDetails):
    if (data.id > 0):
        return True
    else:
        return False

def update_page_details(body: list[IPageDetails], page_module: int):
    print(body)
    to_update = filter(lambda row: row["id"] > 0, body)
    to_add = filter(lambda row: row["id"] == 0, body)
    ids = list(map(lambda row: row["id"], body))

    # DELETE
    db = next(get_db())
    (
        db.query(PageDetails)
            .filter(
                PageDetails.id.not_in(ids),
                PageDetails.page_module == page_module
            )
            .delete()
    )
    db.commit()

    # INSERT NEW DATA
    for row in list(to_add):
        # print("insert", row["ttl"])
        db = next(get_db())
        to_save = {
            "title": row["title"],
            "description": row["description"],
            "img": row["img"] if "img" in row else "",
            "location": row["location"] if "location" in row else "",
            "page_module": page_module
        }
        
        db.add(PageDetails(**dict(to_save)))
        db.commit()

    # UPDATE DATA
    for row in list(to_update):
        # print("update", row)
        db = next(get_db())
        (
            db.query(PageDetails)
                .filter(
                    PageDetails.id == row["id"],
                    PageDetails.page_module == page_module
                )
                .update({
                    "title": row["title"],
                    "description": row["description"],
                    "img": row["img"] if "img" in row else "",
                    "location": row["location"] if "location" in row else "",
                })
        )
        db.commit()

    return ('', 204)

def update_basic_details(body: IBasicDetailUpdateData):
    db = next(get_db())
    (
        db.query(BasicDetails)
            .filter(BasicDetails.col_name == body.col_name)
            .update({
                "content": body.content
            })
    )
    db.commit()

    return ('', 204)
