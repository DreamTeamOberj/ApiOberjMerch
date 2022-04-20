from bson.objectid import ObjectId
from motor import motor_asyncio

MONGO_URL = "mongodb+srv://groupe6:groupe6@bddoberjmerch.t2yjt.mongodb.net/oberjMerch?retryWrites=true&w=majority"

client = motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.oberj

oberj_collection = db.get_collection("oberjMerch")


# Helper
def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "description": product["description"],
        "img": product["img"],
        "is_offer": product["is_offer"],
    }


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "first_name": user["first_name"],
        "email": user["email"],
        "password": user["password"],
    }


# Operations
# User
async def retrieve_users():
    user = []
    async for user in oberj_collection.find():
        user.append(user_helper(user))
    return user


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    user = await oberj_collection.insert_one(user_data)
    new_user = await oberj_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: str) -> dict:
    user = await oberj_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await oberj_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await oberj_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: str):
    user = await oberj_collection.find_one({"_id": ObjectId(id)})
    if user:
        await oberj_collection.delete_one({"_id": ObjectId(id)})
        return True


# Product
async def retrieve_products():
    product = []
    async for product in oberj_collection.find():
        product.append(user_helper(product))
    return product


# Add a new product into to the database
async def add_product(product_data: dict) -> dict:
    product = await oberj_collection.insert_one(product_data)
    new_product = await oberj_collection.find_one({"_id": product.inserted_id})
    return user_helper(new_product)


# Retrieve a product with a matching ID
async def retrieve_product(id: str) -> dict:
    product = await oberj_collection.find_one({"_id": ObjectId(id)})
    if product:
        return user_helper(product)


# Update a product with a matching ID
async def update_product(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    product = await oberj_collection.find_one({"_id": ObjectId(id)})
    if product:
        updated_product = await oberj_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_product:
            return True
        return False


# Delete a product from the database
async def delete_product(id: str):
    product = await oberj_collection.find_one({"_id": ObjectId(id)})
    if product:
        await oberj_collection.delete_one({"_id": ObjectId(id)})
        return True
