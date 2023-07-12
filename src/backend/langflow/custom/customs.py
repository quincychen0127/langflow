from langflow.template import frontend_node

# These should always be instantiated
CUSTOM_NODES = {
    "prompts": {
        "ZeroShotPrompt": frontend_node.prompts.ZeroShotPromptNode(),
    },
    "tools": {
        "PythonFunctionTool": frontend_node.tools.PythonFunctionToolNode(),
        "PythonFunction": frontend_node.tools.PythonFunctionNode(),
        "Tool": frontend_node.tools.ToolNode(),
        "GetMarketingObjectives": frontend_node.tools.GetMarketingObjectivesNode(),
        "GetCustomerPocAPI": frontend_node.tools.GetCustomerPocAPINode(),
        "OptOutCheckupToolAPI": frontend_node.tools.OptOutCheckupToolAPINode(),
        "ReportingAPI": frontend_node.tools.ReportingAPINode(),
        "GetTopPitchableCustomer": frontend_node.tools.GetTopPitchableCustomerNode(),
        "EmailAPI": frontend_node.tools.EmailAPINode(),
        "FetchNextBestAction": frontend_node.tools.FetchNextBestActionNode(),
        "GetAdsReportingData": frontend_node.tools.GetAdsReportingDataNode(),
        "PlannerAgent": frontend_node.tools.PlannerAgentNode(),
    },
    "agents": {
        "JsonAgent": frontend_node.agents.JsonAgentNode(),
        "CSVAgent": frontend_node.agents.CSVAgentNode(),
        "AgentInitializer": frontend_node.agents.InitializeAgentNode(),
        "VectorStoreAgent": frontend_node.agents.VectorStoreAgentNode(),
        "VectorStoreRouterAgent": frontend_node.agents.VectorStoreRouterAgentNode(),
        "SQLAgent": frontend_node.agents.SQLAgentNode(),
    },
    "utilities": {
        "SQLDatabase": frontend_node.agents.SQLDatabaseNode(),
    },
    "memories": {
        "PostgresChatMessageHistory": frontend_node.memories.PostgresChatMessageHistoryFrontendNode(),
    },
    "chains": {
        "SeriesCharacterChain": frontend_node.chains.SeriesCharacterChainNode(),
        "TimeTravelGuideChain": frontend_node.chains.TimeTravelGuideChainNode(),
        "MidJourneyPromptChain": frontend_node.chains.MidJourneyPromptChainNode(),
        "load_qa_chain": frontend_node.chains.CombineDocsChainNode(),
    },
}


def get_custom_nodes(node_type: str):
    """Get custom nodes."""
    return CUSTOM_NODES.get(node_type, {})
