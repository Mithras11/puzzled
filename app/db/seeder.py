from uuid import uuid4
from os.path import join, dirname

from app.db.database import engine
from app.db.models import Base, DifficultyLevel, Role

# file = join(dirname(__file__), "pic.jpg")
# file = join(dirname(__file__), "kitty.jpg")
# pic = open(file, "rb").read()

SOLUTION_CONTENT = """
def add_nums(a: int, b: int) -> int:
    return a + b
"""
MODEL_IDS = {
    "user_id": uuid4(),
    "task_id": uuid4(),
    "solution_id": uuid4(),
    "task_description_id": uuid4(),
    "solution_description_id": uuid4(),
}

INITIAL_DATA = {
    # "profile_images": [
    #     {
    #         "name": "Nemo",
    #         "content": pic,
    #     },
    # ],
    ##########
    "users": [
        {
            "id": MODEL_IDS["user_id"],
            "full_name": "Kumar Pandu",
            "nickname": "Djangolo",
            "email": "djangolo@mail.com",
            "about": "Happy coder",
            "task_stars_received": 0,
            "solution_stars_received": 0,
            "role": Role.user,
        },
    ],
    "tasks": [
        {
            "id": MODEL_IDS["task_id"],
            "name": "Add two numbers",
            "difficulty_level": DifficultyLevel.easy,
            "author_id": MODEL_IDS["user_id"],
        }
    ],
    "solutions": [
        {
            "id": MODEL_IDS["solution_id"],
            "name": "200 % faster implementation",  # TODO: remove property?
            "task_id": MODEL_IDS["task_id"],
            "author_id": MODEL_IDS["user_id"],
            "description": "Simply use + operator",
            "content": SOLUTION_CONTENT,
            "votes": 0,
        }
    ],
    "task_descriptions": [
        {
            "id": MODEL_IDS["task_description_id"],
            "task_id": MODEL_IDS["task_id"],
            "text": "Write a function that adds given arguments together",
            "links": [
                "https://en.wikipedia.org/wiki/Addition",
                "https://math.fandom.com/wiki/Addition",
            ],
        },
    ],
    "solution_descriptions": [
        {
            "id": MODEL_IDS["solution_description_id"],
            "solution_id": MODEL_IDS["solution_id"],
            "text": "Simply use the plus (+) sign",
        },
    ],
    # "task_description_images": [],
    # "solution_description_images": [],
    # "profile_images": [],
    # "test_data": [],
    # "test_cases": [],
    # "tags": [],
    # "tasks_tags": [],
    # "hints": [],
    # "task_votes": [],
    # "solution_votes": [],
}


async def initialize_table(target, target_data, connection):
    connection.execute(target.insert(), target_data)
    connection.commit()


async def initialize_database():
    connection = engine.connect()
    table_models = {cls.__tablename__: cls.__table__ for cls in Base.__subclasses__()}
    for table_name, table_data in INITIAL_DATA.items():
        model = table_models[table_name]
        await initialize_table(model, table_data, connection)
