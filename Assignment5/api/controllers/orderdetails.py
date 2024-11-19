from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, orderdetail: schemas.OrderDetailCreate):
    db_orderdetail = models.OrderDetail(
        order_id=orderdetail.order_id,
        sandwich_id=orderdetail.sandwich_id,
        amount=orderdetail.amount
    )
    db.add(db_orderdetail)
    db.commit()
    db.refresh(db_orderdetail)
    return db_orderdetail


def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, order_id):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == order_id).first()

def update(db: Session, order_id, orderdetail):
    # Query the database for the specific order to update
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_id)
    # Extract the update data from the provided 'order' object
    update_data = orderdetail.model_dump(exclude_unset=True)
    # Update the database record with the new data, without synchronizing the session
    db_orderdetail.update(update_data, synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return the updated order record
    return db_orderdetail.first()

def delete(db: Session, order_id):
    # Query the database for the specific order to delete
    db_orderdetail = db.query(models.OrderDetail).filter(models.OrderDetail.id == order_id)
    # Delete the database record without synchronizing the session
    db_orderdetail.delete(synchronize_session=False)
    # Commit the changes to the database
    db.commit()
    # Return a response with a status code indicating success (204 No Content)
    return Response(status_code=status.HTTP_204_NO_CONTENT)