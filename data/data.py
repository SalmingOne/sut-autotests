

PROJECT_NAME: str = "AutoTestProject"
USER_NAME = "Администратор Администратор"
PROJECT_CODE = "ATP"
LOGIN = "admin"
PASSWORD = "password"

# http://10.7.2.3:43000/api/docs#:~:text=OutputPaginatedNotifications-,InputProject,-ProjectStats
VALID_PROJECT_DATA = {"code": "ATR",
                      "name": "AutoTest",
                      "startDate": "01.10.2022",
                      "status": "ACTIVE",
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
                      "resources": [{"projectRoleId": 1,
                                     "userId": 2,
                                     "isProjectManager": True}]}
