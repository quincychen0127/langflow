from typing import Callable, Optional
from langflow.interface.importing.utils import get_function

from pydantic import BaseModel, validator

from langflow.utils import validate
from langchain.agents.tools import Tool


class Function(BaseModel):
    code: str
    function: Optional[Callable] = None
    imports: Optional[str] = None

    # Eval code and store the function
    def __init__(self, **data):
        super().__init__(**data)

    # Validate the function
    @validator("code")
    def validate_func(cls, v):
        try:
            validate.eval_function(v)
        except Exception as e:
            raise e

        return v

    def get_function(self):
        """Get the function"""
        function_name = validate.extract_function_name(self.code)

        return validate.create_function(self.code, function_name)


class PythonFunctionTool(Function, Tool):
    """Python function"""

    name: str = "Custom Tool"
    description: str
    code: str

    def ___init__(self, name: str, description: str, code: str):
        self.name = name
        self.description = description
        self.code = code
        self.func = get_function(self.code)
        super().__init__(name=name, description=description, func=self.func)

class GetMarketingObjectives(PythonFunctionTool):
    pass

class GetCustomerPocAPI(PythonFunctionTool):
    pass

class OptOutCheckupToolAPI(PythonFunctionTool):
    pass

class ReportingAPI(PythonFunctionTool):
    pass

class GetTopPitchableCustomer(PythonFunctionTool):
    pass

class EmailAPI(PythonFunctionTool):
    pass

class FetchNextBestAction(PythonFunctionTool):
    pass

class GetAdsReportingData(PythonFunctionTool):
    pass

class PlannerAgent(PythonFunctionTool):
    pass

class SalesOutreachAgent(PythonFunctionTool):
    pass

class SalesContextAgent(PythonFunctionTool):
    pass

class AdwordsPerformanceAgent(PythonFunctionTool):
    pass

class PythonFunction(Function):
    """Python function"""

    code: str
