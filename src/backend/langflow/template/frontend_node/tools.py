from langflow.template.field.base import TemplateField
from langflow.template.frontend_node.base import FrontendNode
from langflow.template.template.base import Template
from langflow.utils.constants import DEFAULT_PYTHON_FUNCTION


class ToolNode(FrontendNode):
    name: str = "Tool"
    template: Template = Template(
        type_name="Tool",
        fields=[
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value="",
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=True,
                value="",
                name="description",
                advanced=False,
            ),
            TemplateField(
                name="func",
                field_type="function",
                required=True,
                is_list=False,
                show=True,
                multiline=True,
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    )
    description: str = "Converts a chain, agent or function into a tool."
    base_classes: list[str] = ["Tool"]

    def to_dict(self):
        return super().to_dict()


class PythonFunctionToolNode(FrontendNode):
    name: str = "PythonFunctionTool"
    template: Template = Template(
        type_name="PythonFunctionTool",
        fields=[
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=False,
                value="",
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=False,
                value="",
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                value=DEFAULT_PYTHON_FUNCTION,
                name="code",
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    )
    description: str = "Python function to be executed."
    base_classes: list[str] = ["Tool"]

    def to_dict(self):
        return super().to_dict()
    
def create_fields(name, description, code):
    return [
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=name,
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=description,
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                value=code,
                name="code",
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    
class ShareOfWalletAPINode(PythonFunctionToolNode):
    name: str = "ShareOfWalletAPI"
    description: str = "Share of Wallet API. Use this when you need information about a customer's ads budget distribution."
    code: str = """def share_of_wallet_api(customer: str) -> str:
    return "Google: 40 million, Facebook: 60 million"
"""
    template: Template = Template(
        type_name="PythonFunctionTool",
        fields=[
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=name,
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=description,
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                value=code,
                name="code",
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    )

class ReportingAPINode(PythonFunctionToolNode):
    name: str = "ReportingAPI"
    description: str = "Reporting API. Use this when you need to find the low hanging fruit customers."
    code: str = """def reporting_api(count: str) -> str:
    return "customer_name: Netally, spending: 10 million"
"""
    template: Template = Template(
        type_name="PythonFunctionTool",
        fields=[
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=name,
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=description,
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                value=code,
                name="code",
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    )

class GetPitchableLowHangingFruitWorkflowNode(PythonFunctionToolNode):
    name: str = "GetPitchableLowHangingFruitWorkflow"
    description: str = "GetPitchableLowHangingFruitWorkflow API. Use this when you need to find the pitchable low hanging fruit customers."
    code: str = """def pitchable_low_hanging_fruit_workflow(count: str) -> str:
    return "customer_name: Netally, spending: 10 million, POC: hejinming, email: hejinming@google.com, phone: 1234567890"
"""
    template: Template = Template(
        type_name="PythonFunctionTool",
        fields=[
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=name,
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=description,
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                value=code,
                name="code",
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    )


class GetCustomerPocAPINode(PythonFunctionToolNode):
    name: str = "GetCustomerPocAPI"
    description: str = "GetCustomerPoc API. Use this when you need to find a customer's POC."
    code: str = """def get_customer_poc(customer: str) -> str:
    return "email_address:hejinming@google.com, phone_number:123456789"
"""
    template: Template = Template(
        type_name="PythonFunctionTool",
        fields=[
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=name,
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=description,
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                value=code,
                name="code",
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    )

class OptOutCheckupToolAPINode(PythonFunctionToolNode):
    name: str = "OptOutCheckupToolAPI"
    description: str = "OptOutCheckupTool API. Use this when you need to check if a phone number is in the Opt-out registry."
    code: str = """def check_do_not_call_registry(phone_number: str) -> str:
    return "can_call=True"
"""
    template: Template = Template(
        type_name="PythonFunctionTool",
        fields=[
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=name,
                name="name",
                advanced=False,
            ),
            TemplateField(
                field_type="str",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=description,
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                value=code,
                name="code",
                advanced=False,
            ),
            TemplateField(
                field_type="bool",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                multiline=False,
                value=False,
                name="return_direct",
            ),
        ],
    )

class PythonFunctionNode(FrontendNode):
    name: str = "PythonFunction"
    template: Template = Template(
        type_name="PythonFunction",
        fields=[
            TemplateField(
                field_type="code",
                required=True,
                placeholder="",
                is_list=False,
                show=True,
                value=DEFAULT_PYTHON_FUNCTION,
                name="code",
                advanced=False,
            )
        ],
    )
    description: str = "Python function to be executed."
    base_classes: list[str] = ["function"]

    def to_dict(self):
        return super().to_dict()
