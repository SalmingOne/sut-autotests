from __future__ import annotations

from pydantic import BaseModel
from typing import List, Optional

from data.data import LOGIN, PASSWORD


class AuthModels:
    class AuthRequestModel:
        class Model(BaseModel):
            login: str = LOGIN
            password: str = PASSWORD

    class AuthResponseModel:
        class Model(BaseModel):
            accessToken: str
            refreshToken: str
            abilityToken: str

    class NotCorrectAuthResponseModel:
        class Context(BaseModel):
            systemError: str
            duplicateKeys: List[str]

        class Model(BaseModel):
            status: int
            message: str
            timestamp: str
            context: AuthModels.NotCorrectAuthResponseModel.Context
