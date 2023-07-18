from pydantic import BaseModel
from typing import List, Optional
from .test_execution_base_schema import BaseTestExecutionResult

class PhpunitTestCase(BaseModel):
    name: str
    classname: str
    file: str
    line: int
    assertions: int
    time: str
    status: str
    exceptionProps: Optional[dict] = None

class PhpunitDetail(BaseModel):
    name: str
    tests: int
    assertions: int
    errors: int
    warnings: int
    failures: int
    skipped: int
    time: str
    testcases: List[PhpunitTestCase]

class PhpunitTestResult(BaseTestExecutionResult):
    name: str
    tests: int
    assertions: int
    errors: int
    warnings: int
    failures: int
    skipped: int
    time: str
    details: List[PhpunitDetails]