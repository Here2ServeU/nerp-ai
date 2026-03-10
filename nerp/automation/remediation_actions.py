def scale_cluster() -> None:
    print("Scaling Kubernetes cluster")
    print("kubectl scale deployment api --replicas=6")


def investigate_anomaly() -> None:
    print("Opening anomaly investigation workflow")
    print("Collect logs, traces, and recent deploy information")


def no_action() -> None:
    print("No scaling needed")


def execute_action(action: str) -> None:
    if action == "Scale infrastructure and investigate anomaly":
        scale_cluster()
        investigate_anomaly()
        return
    if action == "Scale infrastructure":
        scale_cluster()
        return
    if action == "Investigate anomaly":
        investigate_anomaly()
        return
    no_action()