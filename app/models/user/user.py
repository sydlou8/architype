from sqlmodel import SQLModel, Field
from pydantic import EmailStr
from datetime import datetime
from uuid import UUID, uuid4


class User(SQLModel, table=True):
    """User model representing a user in the system. This is for Authentication and Account/System data"""
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    username: str = Field(index=True, unique=True)
    email: EmailStr = Field(index=True, unique=True)
    hashed_password: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserCreate(SQLModel):
    """Schema for user registration"""
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)


class UserLogin(SQLModel):
    """Schema for user login"""
    username: str
    password: str


class UserResponse(SQLModel):
    """Schema for user response (no password)"""
    id: UUID
    username: str
    email: str
    is_active: bool
    created_at: datetime


class Token(SQLModel):
    """Schema for JWT token response"""
    access_token: str
    token_type: str = "bearer"


class TokenData(SQLModel):
    """Schema for data stored in JWT token"""
    username: str | None = None

