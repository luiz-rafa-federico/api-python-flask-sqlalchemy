from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
   from app.models.leads_model import LeadModel
   from app.models.users_model import UserModel
   from app.models.categories_model import CategoryModel

   Migrate(app, app.db)
