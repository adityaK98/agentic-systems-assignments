from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    username: str = Field(min_length=5, description="Provide name of the user")
    email: EmailStr = Field(description="Provide valid email address", examples="abc@domain.com")
    age: int = Field(ge=18, description="Provide age of the user")




userDetails = {'username':'Aditya', 'email':'test@gmail.com', 'age':26}

userObj = UserRegister(**userDetails)
print(userObj.username)
