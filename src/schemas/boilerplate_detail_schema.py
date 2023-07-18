from pydantic import BaseModel
from typing import List, Optional
from .test_execution_base_schema import BaseTestExecutionResult

class Capability(BaseModel):
    browser: str
    browserVersion: str
    os: str
    osVersion: str
    deviceName: str
    deviceType: str
    bsRunMode: str
    isDeviceTesting: bool

class ExceptionProps(BaseModel):
    name: str
    stepName: str
    stackTrace: str
    exceptionOccuredAt: str
    reason: Optional[str] = None
class BoilerplateDetails(BaseModel):
    environment: Capability
    scenario: str
    defect: Optional[str] = None
    tags: list
    bsUrls: dict
    feature: str
    featureFileName: str
    status: str
    duration: int
    jiraProps: dict
    exceptionProps: Optional[ExceptionProps] = None

class BoilerplateTestResult(BaseTestExecutionResult):
    details: List[BoilerplateDetails]