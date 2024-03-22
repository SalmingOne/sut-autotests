from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, RootModel

from data import data


class ProjectModels:
    class CreateProjectResponseModel:
        class Project(BaseModel):
            id: int
            code: str
            name: str

        class SlotsTask(BaseModel):
            id: int
            startDate: str
            endDate: str
            employmentPercentage: int
            slotId: int
            taskId: int

        class Task(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            startDate: str
            endDate: str
            parentId: int
            slotsTasks: List[ProjectModels.CreateProjectResponseModel.SlotsTask]
            link: str

        class File(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            path: str
            size: int

        class LaborReport(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            hours: int
            date: str
            overtimeWork: int
            reason: str
            overtimeReason: str
            type: str
            userId: int
            projectId: int
            project: ProjectModels.CreateProjectResponseModel.Project
            taskId: int
            task: ProjectModels.CreateProjectResponseModel.Task
            stageId: int
            files: List[ProjectModels.CreateProjectResponseModel.File]
            rejectionReason: str
            approvalStatus: str

        class Role(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            attractionRateId: int
            salaryRate: int
            color: str
            leadership: bool

        class Assignment(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: Optional[str] = None
            projectRoleId: int
            projectId: int
            slotId: int
            userId: int
            role: Optional[ProjectModels.CreateProjectResponseModel.Role] = None
            isProjectManager: bool

        class Role1(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: Optional[str] = None
            name: str
            attractionRateId: int
            salaryRate: int
            color: Optional[str] = None
            leadership: bool

        class Slot(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: Optional[str] = None
            projectRoleId: int
            projectId: int
            assignments: List[ProjectModels.CreateProjectResponseModel.Assignment]
            role: ProjectModels.CreateProjectResponseModel.Role1
            attractionRateId: Optional[int] = None

        class Stage(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            parentId: int
            projectId: int
            link: str

        class Model(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: Optional[str] = None
            code: str
            name: str
            description: Optional[dict[str, Any]] = None
            consumer: Optional[str] = None
            status: str
            laborReasons: Optional[bool] = None
            laborReasonsStartDate: Optional[str] = None
            mandatoryAttachFiles: bool
            startDate: str
            endDate: str
            selfAdding: bool
            laborReports: Optional[List[ProjectModels.CreateProjectResponseModel.LaborReport]] = None
            slots: List[ProjectModels.CreateProjectResponseModel.Slot]
            stages: Optional[List[ProjectModels.CreateProjectResponseModel.Stage]] = None
            imageFileId: Optional[int] = None
            authorId: int
            possibleStatuses: List[str]
            fileDescription: Optional[Dict[str, Any]] = None
            automaticLaborReports: bool

    class GetAllProjectResponseModel:
        class Project(BaseModel):
            id: int
            code: str
            name: str

        class SlotsTask(BaseModel):
            id: int
            startDate: str
            endDate: str
            employmentPercentage: int
            slotId: int
            taskId: int

        class Task(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            startDate: str
            endDate: str
            parentId: int
            slotsTasks: List[ProjectModels.GetAllProjectResponseModel.SlotsTask]
            link: str

        class File(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            path: str
            size: int

        class LaborReport(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            hours: int
            date: str
            overtimeWork: int
            reason: str
            overtimeReason: str
            type: str
            userId: int
            projectId: int
            project: ProjectModels.GetAllProjectResponseModel.Project
            taskId: int
            task: ProjectModels.GetAllProjectResponseModel.Task
            stageId: int
            files: List[ProjectModels.GetAllProjectResponseModel.File]
            rejectionReason: str
            approvalStatus: str

        class Role(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            attractionRateId: int
            salaryRate: int
            color: str
            leadership: bool

        class Assignment(BaseModel):
            id: int
            createdAt: Optional[str] = None
            updatedAt: str
            deletedAt: Optional[str] = None
            projectRoleId: int
            projectId: int
            slotId: int
            userId: int
            role: Optional[ProjectModels.GetAllProjectResponseModel.Role] = None
            isProjectManager: bool

        class Role1(BaseModel):
            id: int
            createdAt: Optional[str] = None
            updatedAt: Optional[str] = None
            deletedAt: Optional[str] = None
            name: Optional[str] = None
            attractionRateId: Optional[int] = None
            salaryRate: Optional[int] = None
            color: Optional[str] = None
            leadership: bool

        class Slot(BaseModel):
            id: Optional[int] = None
            createdAt: Optional[str] = None
            updatedAt: Optional[str] = None
            deletedAt: Optional[str] = None
            projectRoleId: Optional[int] = None
            projectId: Optional[int] = None
            assignments: Optional[List[ProjectModels.GetAllProjectResponseModel.Assignment]] = None
            role: Optional[ProjectModels.GetAllProjectResponseModel.Role1] = None
            attractionRateId: Optional[int] = None

        class Stage(BaseModel):
            id: int
            createdAt: str
            updatedAt: str
            deletedAt: str
            name: str
            parentId: int
            projectId: int
            link: str

        class ModelItem(BaseModel):
            id: int
            createdAt: Optional[str] = None
            updatedAt: Optional[str] = None
            deletedAt: Optional[str] = None
            code: Optional[str] = None
            name: Optional[str] = None
            description: Optional[Dict[str, Any]] = None
            consumer: Optional[str] = None
            status: Optional[str] = None
            laborReasons: bool
            laborReasonsStartDate: Optional[str] = None
            mandatoryAttachFiles: bool
            startDate: str
            endDate: Optional[str] = None
            selfAdding: bool
            laborReports: Optional[List[ProjectModels.GetAllProjectResponseModel.LaborReport]] = None
            slots: Optional[List[ProjectModels.GetAllProjectResponseModel.Slot]] = None
            stages: Optional[List[ProjectModels.GetAllProjectResponseModel.Stage]] = None
            imageFileId: Optional[int] = None
            authorId: int
            possibleStatuses: Optional[List[str]] = None
            fileDescription: Optional[Dict[str, Any]] = None
            automaticLaborReports: Optional[bool] = None

        class Model(RootModel):
            root: List[ProjectModels.GetAllProjectResponseModel.ModelItem]
