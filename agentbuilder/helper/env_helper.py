import os


def get_log_level():
    try:
        return os.environ["LOG_LEVEL"] or "info"
    except:
        return "info"
    

def get_default_agent_type():
    try:
        return os.environ["DEFAULT_AGENT_TYPE"] or "tool_calling"
    except:
        return "tool_calling"
    
    