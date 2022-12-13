"""
Holds functions used by Users Sample API
"""

import requests
import os
from fastapi import APIRouter, status
from fastapi_versioning import version
from app.models.users import UserModel
from app.core import common_handlers

router = APIRouter(
  prefix="/users",
  tags=["Users"],
  responses={404: {"description": "Not found"}}
)

def get_system_env():
  api_sys_env = os.getenv("BEAVER_API_SYS_ENV", "DEVELOPMENT")
  if api_sys_env == "PRODUCTION":
    return production
  elif api_sys_env == "STAGE":
    return stage
  else:
    return development

@router.get("/", status_code=status.HTTP_200_OK)
@version(1)
async def get_users():
  """
  Return sample response
  """
  configs = common_handlers.get_system_env()
  print(configs)
  print()

  response = requests.get(f"{configs.JSON_PLACE_HOLDER}/users", timeout=10)
  if response.status_code == status.HTTP_200_OK:
    return response.json()
  return None

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
@version(1)
async def get_user(user_id: int):
  """
  Return sample response
  """
  response = requests.get(f"{configs.JSON_PLACE_HOLDER}/users/{user_id}", timeout=10)
  if response.status_code == status.HTTP_200_OK:
    return response.json()
  return None

@router.post("/user", status_code=status.HTTP_200_OK)
@version(1)
async def add_user(user: UserModel):
  """
  Return sample response
  """
  return {
    "user_id": user.user_id,
    "first_name": user.first_name,
    "last_name": user.last_name,
    "email": user.email
  }
