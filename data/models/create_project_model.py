from pydantic import BaseModel


class Resource(BaseModel):
    projectRoleId: int = 1
    userId: int = 2
    isProjectManager: bool = True


class CreateProject(BaseModel):
    code: str = 'ATP'
    name: str = 'AutoTestProject'
    startDate: str = '01.10.2022'
    endDate: str = '12.21.2029'
    status: str = 'ACTIVE'
    selfAdding: bool = True
    laborReasons: bool = False
    mandatoryAttachFiles: bool = False
    resources: list = [Resource().model_dump()]
    automaticLaborReports: bool = False
