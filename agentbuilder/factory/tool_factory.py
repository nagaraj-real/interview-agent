
from typing import Sequence
from langchain.tools import BaseTool
from agentbuilder.tools.interview_tools.interview_toolkit import interview_tools


def get_all_tools()->Sequence[BaseTool]:
    return  interview_tools




