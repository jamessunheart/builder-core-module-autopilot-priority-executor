from meta_reflection_planner import MetaReflectionPlanner

class AutopilotPriorityExecutor:
    """
    Executes or routes high-confidence improvement actions automatically
    using plans from MetaReflectionPlanner.
    """

    def __init__(self):
        self.planner = MetaReflectionPlanner()
        self.execution_log = []

    def run_autopilot_cycle(self):
        plan = self.planner.auto_reflect()
        executed = []

        for action in plan["actions"]:
            if "update GitHub token" in action:
                executed.append("Notify admin to update token scope.")
            elif "Synchronize all API" in action:
                executed.append("Flag API schema alignment tool for sync.")
            elif "Add new routing rule" in action:
                executed.append("Inject keyword into task_intent_router.")
            else:
                executed.append(f"Logged for review: {action}")

        result = {
            "plan_time": plan["timestamp"],
            "executed": executed
        }
        self.execution_log.append(result)
        return result

    def get_execution_history(self):
        return self.execution_log