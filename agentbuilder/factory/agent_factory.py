from agentbuilder.agents.BaseAgentBuilder import AgentBuilderParams, BaseAgentBuilder
from agentbuilder.agents.params import AgentParams
from agentbuilder.helper.env_helper import get_default_agent_type


def resume_vector_agent():
    return AgentParams(
            name="resume_vector_agent",
            preamble= """
            You are very powerful code assistant,with access to resume and job description tools.
            """,
            tools=  ["resume_search_tool","job_description_tool","save_skill_tool"],
            agent_type= get_default_agent_type()
      )

def rating_agent():
    return AgentParams(
            name="rating_agent",
            preamble= """
            You are very powerful interview rating assistant,with access to save rating tools.
            """,
            tools=  ["interview_answers_tool","save_rating_tool","save_evaluation_tool"],
            agent_type= get_default_agent_type()
      )

def interview_agent():
    return AgentParams(
            name="interview_agent",
            preamble= """
            You are very powerful interview preparation agent.
            """,
            tools=  [],
            agent_type= get_default_agent_type()
      )

def get_all_agents():
    return [
            resume_vector_agent(),
            rating_agent(),
            interview_agent()
    ]

def get_agent_builder(params:AgentBuilderParams):
    agent_name= params.name
    match agent_name:
        case "interview_agent":
            from agentbuilder.agents.interview_agent import InterviewAgentBuilder
            return InterviewAgentBuilder.InterviewAgentBuilder(params)
        case _:
            return BaseAgentBuilder(params)





