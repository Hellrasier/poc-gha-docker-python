from pydantic import BaseModel
from typing import List

class GithubProps(BaseModel):
    name: str
    commit: str
    branch: str
class BaseTestExecutionResult(BaseModel):
    application: str
    platform: str
    capabilities: str
    githubProps: GithubProps
    details: List[dict]