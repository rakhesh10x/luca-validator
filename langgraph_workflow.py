import sys
import os

# ✅ Fix import paths
sys.path.insert(0, os.path.abspath("."))
os.environ["PYTHONPATH"] = "."

print("🔥 Workflow loaded correctly")

from langgraph.graph import StateGraph, END
from typing import TypedDict, Dict, List

# ✅ Import agents
from agents.access_validator import AccessValidatorAgent
from agents.drive_fetch import DriveFetchAgent
from agents.file_classifier import FileClassifierAgent
from agents.rule_matcher import RuleMatcherAgent
from agents.code_generator import CodeGeneratorAgent
from agents.execution_agent import ExecutionAgent
from agents.analysis_agent import AnalysisAgent
from agents.report_generator import ReportGeneratorAgent

# ✅ STATE STRUCTURE (IMPORTANT)
class ValidationState(TypedDict):
    drive_link: str
    rule_sets: Dict
    files: List[Dict]
    access_status: str
    matched_rules: Dict
    results: List[Dict]
    final_report: Dict

# ✅ MAIN FUNCTION
async def run_validation_pipeline(drive_link: str, rule_sets: Dict):

    graph = StateGraph(ValidationState)

    # ✅ ADD ALL NODES
    graph.add_node("access_validator", AccessValidatorAgent().run)
    graph.add_node("drive_fetch", DriveFetchAgent().run)
    graph.add_node("file_classifier", FileClassifierAgent().run)
    graph.add_node("rule_matcher", RuleMatcherAgent().run)
    graph.add_node("code_generator", CodeGeneratorAgent().run)
    graph.add_node("execution", ExecutionAgent().run)
    graph.add_node("analysis", AnalysisAgent().run)
    graph.add_node("report_generator", ReportGeneratorAgent().run)

    # ✅ ENTRY POINT
    graph.set_entry_point("access_validator")

    # ✅ PIPELINE FLOW (VERY IMPORTANT)
    graph.add_edge("access_validator", "drive_fetch")
    graph.add_edge("drive_fetch", "file_classifier")
    graph.add_edge("file_classifier", "rule_matcher")
    graph.add_edge("rule_matcher", "code_generator")
    graph.add_edge("code_generator", "execution")

    # 🔥 FIXED FLOW (IMPORTANT CHANGE)
    graph.add_edge("execution", "analysis")
    graph.add_edge("analysis", "report_generator")

    # ✅ END
    graph.add_edge("report_generator", END)

    # ✅ COMPILE GRAPH
    app = graph.compile()

    # ✅ INITIAL STATE
    initial_state = {
        "drive_link": drive_link,
        "rule_sets": rule_sets
    }

    print("🚀 Running validation pipeline...")

    result = await app.ainvoke(initial_state)

    return result["final_report"]