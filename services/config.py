from pydantic import BaseModel


class BaseResponseModel(BaseModel):
    code: int
    type: str
    message: str


class UserModel(BaseModel):
    id: int = None
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int


class Urls:
    URL_LOGIN = 'https://petstore.swagger.io/v2/user/login'
    URL_LOGOUT = 'https://petstore.swagger.io/v2/user/logout'
    BASE_URL = 'https://petstore.swagger.io/v2/user/'
    CREATE_WITH_LIST_URL = 'https://petstore.swagger.io/v2/user/createWithList'
    CREATE_WITH_ARRAY_URL = 'https://petstore.swagger.io/v2/user/createWithArray'

