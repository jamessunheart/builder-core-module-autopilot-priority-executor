from meta_reflection_planner import MetaReflectionPlanner
from self_diagnostic_engine import SelfDiagnosticEngine
from core_memory_hub import CoreMemoryHub

class AutopilotPriorityExecutor:
    def __init__(self):
        self.planner = MetaReflectionPlanner()
        self.diagnostics = SelfDiagnosticEngine()
        self.memory = CoreMemoryHub()
        self.execution_log = []

    def run_autopilot_cycle(self):
        diagnostics_report = self.diagnostics.run_diagnostics()
        plan = self.planner.generate_improvement_plan(diagnostics_report)
        executed = []

        for action in plan["actions"]:
            executed.append(f"Executed: {action}")

        result = {
            "plan_time": plan["timestamp"],
            "executed": executed
        }
        self.execution_log.append(result)

        self.memory.remember(f"Autopilot executed plan at {plan['timestamp']}: {executed}", tags=["autopilot", "execution"])
        return result

    def get_execution_history(self):
        return self.execution_log