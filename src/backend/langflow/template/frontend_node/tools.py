from langflow.template.field.base import TemplateField
from langflow.template.frontend_node.base import FrontendNode
from langflow.template.template.base import Template
from langflow.utils.constants import DEFAULT_PYTHON_FUNCTION, EMAIL_FUNCTION


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
    
class GetMarketingObjectivesNode(PythonFunctionToolNode):
    name: str = "GetMarketingObjectives"
    description: str = "MarketingObjective API. Use this when you to find the marketing objective of a customer. You should pass the customer_name as the parameter to this tool."
    code: str = """def marketing_objective_api(customer_name: str) -> str:
    return "increase customer leads"
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

PLAN = "Here are steps to make a low hanging fruit pitch to a Google ads customer. \
Step 1. Identify the top pitchable customer company, find its POC.\
Step 2. Check the customer's campaign performance metrics and product recommendations from the Next Best Action engine. Do any Google ads product help them better achieve their objectives? \
Step 3. Draft a short email (no more than 50 words) to the customer company to recommend a Google ads product.\
Step 4. Give TL;DR for each step."

PLAN2 = "Here are steps to make a recommendation. \
Step 1. Check the  Adwords Performance for the client. \
Step 2. Check the Sales Context for the client and relevant recommendation \
Step 3. Get Sales Outreach information including the name of point of contact and the email adress \
Step 4. Draft an email to the point of contact with relevant recommendaton."

class PlannerAgentNode(PythonFunctionToolNode):
    name: str = "PlannerAgent"
    description: str = "Useful to make a plan to solve a problem. Pass the problem as the parameter."
    code: str = f"def make_plans(problem: str) -> str: return \"{PLAN2}\""
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
    description: str = "Reporting API. Use this when you need to find the low hanging fruit customers. You should pass the number of customers to return as parameter to this tool."
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

class GetAdsReportingDataNode(PythonFunctionToolNode):
    name: str = "GetAdsReportingData"
    description: str = "Useful to find the campaign performance of a customer. Pass the customer_name as the parameter to this tool."
    code: str = """def adwords_campaign_performance(customer_name: str) -> str:
    return "customer_name: Netally, cpc: 0.5 USD"
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

class FetchNextBestActionNode(PythonFunctionToolNode):
    name: str = "FetchNextBestAction"
    description: str = "Useful to find an ads product to suggest to the customer. Pass the customer_name as the parameter to this tool."
    code: str = """def next_best_action(customer_name: str) -> str:
    return "customer_name: Netally, ads_product: PMax, rationale: cpc is too high due to incorrect manual config. PMax will help you optimize your ads spend."
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

class GetTopPitchableCustomerNode(PythonFunctionToolNode):
    name: str = "GetTopPitchableCustomer"
    description: str = "Useful to find the pitchable low hanging fruit customers. Pass the number of customers to return as parameter to this tool."
    code: str = """def pitchable_low_hanging_fruit_workflow(count: str) -> str:
    return "customer_name: Netally, spending: 10 million, POC: hejinming, email: hejinming@gmail.com, phone: 1234567890"
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


class EmailAPINode(PythonFunctionToolNode):
    name: str = "EmailAPI"
    description: str = "Email API. Use this to send an email to a customer."
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
                value="EmailAPI",
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
                value="Email API. Use this to send an email to a customer.",
                name="description",
                advanced=False,
            ),
            TemplateField(
                field_type="code",
                required=False,
                placeholder="",
                is_list=False,
                show=False,
                value=EMAIL_FUNCTION,
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

class SalesOutreachAgentNode(PythonFunctionToolNode):
    name: str = "SalesOutreachAgent"
    description: str = "SalesOutreachAgent that can give you the information about customer name, spending, and poc information."
    code: str = """def sales_outreach(count: str) -> str:
    return "customer_name: Netally, spending: 10 million, POC: hejinming, email: hejinming@gmail.com, phone: 1234567890"
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

class SalesContextAgentNode(PythonFunctionToolNode):
    name: str = "SalesContextAgent"
    description: str = "SalesContextAgent that can help you get the sales context about a customer like marketing objective and recommendation."
    code: str = """def get_sales_context(customer_name: str) -> str:
    return "The customer is Netally, and their marketing objective is to maximize conversions. Currently they have conversion tracking enabled and is manually setting CPC. Combining with high CPC, one recommendation is they could Adopt Smart Bidding (specifically “maximize conversions” bid strategy) to maximize conversions on relevant queries."
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

class AdwordsPerformanceAgentNode(PythonFunctionToolNode):
    name: str = "AdwordsPerformanceAgent"
    description: str = "AdwordsPerformanceAgent that can help you get information about their customer's performance."
    code: str = """def get_adwords_perf(customer_name: str) -> str:
    return "The customer is Netally, and their CPC looks to be high compared to peers in vertical. And all their spend is on search campaigns with broad match enabled."
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
