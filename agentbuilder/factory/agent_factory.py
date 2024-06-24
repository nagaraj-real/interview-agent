from agentbuilder.agents.base_agent_builder import AgentBuilderParams, BaseAgentBuilder
from agentbuilder.agents.params import AgentParams
from agentbuilder.helper.env_helper import get_default_agent_type


def resume_vector_agent():
    return AgentParams(
            name="resume_vector_agent",
            preamble= """
            You are very powerful code assistant,with access to save skills tool.
            """,
            tools=  ["save_skill_tool"],
            agent_type= get_default_agent_type()
      )

def rating_agent():
    return AgentParams(
            name="rating_agent",
            preamble= """
            You are very powerful interview rating assistant,with access to save rating tools.
            """,
            tools=  ["save_rating_tool"],
            agent_type= get_default_agent_type()
      )

def interview_question_agent():
    return AgentParams(
            name="interview_question_agent",
            preamble= """
            You are very powerful interview assistant that can generate programming questions.
            """,
            tools=  [],
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
            interview_agent(),
            interview_question_agent()
    ]

def get_agent_builder(params:AgentBuilderParams):
    agent_name= params.name
    match agent_name:
        case "interview_agent":
            from agentbuilder.agents.interview.interview_agent import InterviewAgentBuilder
            return InterviewAgentBuilder(params)
        case "rating_agent":
            from agentbuilder.agents.interview.rating_agent import RatingAgentBuilder
            return RatingAgentBuilder(params)
        case "interview_question_agent":
            from agentbuilder.agents.interview.interview_question_agent import InterviewQuestionAgentBuilder
            return InterviewQuestionAgentBuilder(params)
        case "resume_vector_agent":
            from agentbuilder.agents.interview.resume_job_agent import ResumeJobAgentBuilder
            return ResumeJobAgentBuilder(params)
        case _:
            return BaseAgentBuilder(params)





