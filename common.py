import pandas as pd
from collections import defaultdict
from typing import TypedDict, List, Dict, Optional

client_state_id = "client-state"

Config = TypedDict(
    "Config",
    {
        "avengers_paths": Dict[str, str],
        "esa_paths": Dict[str, str],
        "start": str,  # pd.to_datetime()
        "stop": str,  # pd.to_datetime()
    },
)

ClientState = TypedDict(
    "ClientState",
    {
        "session_id": str,
        "config_path": Optional[str],
        "config": Optional[Config],
    },
)


class SessionState:  # server-side client state
    def __init__(self):
        self.avengers_dfs: Optional[List[pd.DataFrame]] = None
        self.esa_dfs: Optional[List[pd.DataFrame]] = None


server_state: Dict[str, SessionState] = defaultdict(SessionState)


def remove_class(class_name: str, to_remove: str) -> str:
    sep = " "
    return sep.join([c for c in class_name.split(sep) if c != to_remove])
