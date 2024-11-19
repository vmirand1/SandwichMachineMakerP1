from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .models import models, schemas
from .controllers import orders, sandwiches, resources, recipes, orderdetails
from .dependencies.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------- Orders ------------------ #
@app.post("/orders/", response_model=schemas.Order, tags=["Orders"])
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return orders.create(db=db, order=order)


@app.get("/orders/", response_model=list[schemas.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders.read_all(db)


@app.get("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def read_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return order

@app.put("/orders/{order_id}", response_model=schemas.Order, tags=["Orders"])
def update_one_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    order_db = orders.read_one(db, order_id=order_id)
    if order_db is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.update(db=db, order=order, order_id=order_id)


@app.delete("/orders/{order_id}", tags=["Orders"])
def delete_one_order(order_id: int, db: Session = Depends(get_db)):
    order = orders.read_one(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="User not found")
    return orders.delete(db=db, order_id=order_id)

# ---------------- Sandwiches ------------------ #
@app.post("/sandwiches/", response_model=schemas.Sandwich, tags=["Sandwiches"])
def create_sandwich(sandwich: schemas.SandwichCreate, db: Session = Depends(get_db)):
    return sandwiches.create(db=db, sandwich=sandwich)

@app.get("/sandwiches/", response_model=list[schemas.Sandwich], tags=["Sandwiches"])
def read_sandwiches(db: Session = Depends(get_db)):
    return sandwiches.read_all(db)

@app.get("/sandwiches/{order_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def read_one_sandwich(order_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, order_id=order_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwich

@app.put("/sandwiches/{order_id}", response_model=schemas.Sandwich, tags=["Sandwiches"])
def update_one_sandwich(order_id: int, sandwich: schemas.SandwichUpdate, db: Session = Depends(get_db)):
    sandwich_db = sandwiches.read_one(db, order_id=order_id)
    if sandwich_db is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.update(db=db, sandwich=sandwich, order_id=order_id)

@app.delete("/sandwiches/{order_id}", tags=["Sandwiches"])
def delete_one_sandwich(order_id: int, db: Session = Depends(get_db)):
    sandwich = sandwiches.read_one(db, order_id=order_id)
    if sandwich is None:
        raise HTTPException(status_code=404, detail="Sandwich not found")
    return sandwiches.delete(db=db, order_id=order_id)


#-------------------- Resources -------------------- #
@app.post("/resources/", response_model=schemas.Resource, tags=["Resources"])
def create_resource(resource: schemas.ResourceCreate, db: Session = Depends(get_db)):
    return resources.create(db=db, resource=resource)

@app.get("/resources/", response_model=list[schemas.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources.read_all(db)

@app.get("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def read_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resource

@app.put("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def update_one_resource(resource_id: int, resource: schemas.ResourceUpdate, db: Session = Depends(get_db)):
    resource_db = resources.read_one(db, resource_id=resource_id)
    if resource_db is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.update(db=db, resource=resource, resource_id=resource_id)

@app.delete("/resources/{resource_id}", response_model=schemas.Resource, tags=["Resources"])
def delete_one_resource(resource_id: int, db: Session = Depends(get_db)):
    resource = resources.read_one(db, resource_id=resource_id)
    if resource is None:
        raise HTTPException(status_code=404, detail="Resource not found")
    return resources.delete(db=db, resource_id=resource_id)

# --------------------- Recipes --------------------- #

@app.post("/recipes/", response_model=schemas.Recipe, tags=["Recipes"])
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipes.create(db=db, recipe=recipe)

@app.get("/recipes/", response_model=list[schemas.Resource], tags=["Recipes"])
def read_recipes(db: Session = Depends(get_db)):
    return recipes.read_all(db)

@app.get("/recipes/{resource_id}", response_model=schemas.Recipe, tags=["Recipes"])
def read_one_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, recipe_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.put("/recipes/{resource_id}", response_model=schemas.Recipe, tags=["Recipes"])
def update_one_recipe(resource_id: int, recipe: schemas.RecipeUpdate, db: Session = Depends(get_db)):
    recipe_db = recipes.read_one(db, resource_id=resource_id)
    if recipe_db is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.update(db=db, recipe=recipe, resource_id=resource_id)

@app.delete("/recipes/{resource_id}", response_model=schemas.Recipe, tags=["Recipes"])
def delete_one_recipe(resource_id: int, db: Session = Depends(get_db)):
    recipe = recipes.read_one(db, resource_id=resource_id)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipes.delete(db=db, resource_id=resource_id)

# --------------OrderDetails----------------- #

@app.post("/orderdetails/", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def create_orderdetail(orderdetail: schemas.OrderDetailCreate, db: Session = Depends(get_db)):
    return orderdetails.create(db=db, orderdetail=orderdetail)

@app.get("/orderdetails/", response_model=list[schemas.OrderDetail], tags=["OrderDetails"])
def read_orderdetails(db: Session = Depends(get_db)):
    return orderdetails.read_all(db)

@app.get("/orderdetails/{order_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def read_one_orderdetail(order_id: int, db: Session = Depends(get_db)):
    orderdetail = orderdetails.read_one(db, order_id)
    if orderdetail is None:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return orderdetail

@app.put("/orderdetails/{order_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def update_one_orderdetail(order_id: int, orderdetail: schemas.OrderDetailUpdate, db: Session = Depends(get_db)):
    orderdetail_db = orderdetails.read_one(db, order_id=order_id)
    if orderdetail_db is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return orderdetails.update(db=db, orderdetail=orderdetail, order_id=order_id)

@app.delete("/orderdetails/{order_id}", response_model=schemas.OrderDetail, tags=["OrderDetails"])
def delete_one_orderdetail(order_id: int, db: Session = Depends(get_db)):
    orderdetail = orderdetails.read_one(db, order_id=order_id)
    if orderdetail is None:
        raise HTTPException(status_code=404, detail="Order Detail not found")
    return orderdetails.delete(db=db, order_id=order_id)

