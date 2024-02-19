

PROJECT_NAME: str = "AutoTestProject"
USER_NAME = "Администратор Администратор"
PROJECT_CODE = "ATP"
LOGIN = "admin"
PASSWORD = "admin"

# http://10.7.2.3:43000/api/docs#:~:text=OutputPaginatedNotifications-,InputProject,-ProjectStats
VALID_PROJECT_DATA = {"code": "ATP",
                      "name": "AutoTestProject",
                      "startDate": "01.10.2022",
                      "status": "ACTIVE",
                      "selfAdding": True,
                      "laborReasons": False,
                      "mandatoryAttachFiles": False,
                      "description": {"blocks": [{"key": "46l7i",
                                                  "text": "ProjectDescription",
                                                  "type": "unstyled",
                                                  "depth": 0,
                                                  "inlineStyleRanges": [],
                                                  "entityRanges": [],
                                                  "data": {}}],
                                      "entityMap": {}},
                      "endDate": "01.10.2025",
                      "fileDescription": {"blocks": [{"key": "46l7i",
                                                      "text": "AttachFileDescription",
                                                      "type": "unstyled",
                                                      "depth": 0,
                                                      "inlineStyleRanges": [],
                                                      "entityRanges": [],
                                                      "data": {}}],
                                          "entityMap": {}},
                      "automaticLaborReports": False,
                      "resources": [{"projectRoleId": 1,
                                     "userId": 2,
                                     "isProjectManager": True}]}
