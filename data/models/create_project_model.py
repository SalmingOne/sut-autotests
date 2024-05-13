from pydantic import BaseModel

from data.data import USER_ID, PROJECT_NAME


class Resource(BaseModel):
    projectRoleId: int = 1
    userId: int = USER_ID
    isProjectManager: bool = True


class CreateProject(BaseModel):
    code: str = 'ATP'
    name: str = PROJECT_NAME
    startDate: str = '01.10.2022'
    endDate: str = '12.21.2029'
    status: str = 'ACTIVE'
    selfAdding: bool = True
    laborReasons: bool = False
    mandatoryAttachFiles: bool = False
    resources: list = [Resource().model_dump()]
    automaticLaborReports: bool = False
