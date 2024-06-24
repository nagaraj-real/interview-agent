# Interview Agent

## 🚀 Quick Start

1. Set up a Python virtualenv and install dependencies

```sh
   python -m venv --prompt interview-agent venv
   source venv/bin/activate
   # venv/Scripts/activate (Windows)
   pip install .
```

2. Set the model name and API key in **.env** file

```sh
   export OPENAI_API_KEY=""
   export NVIDIA_API_KEY=""
```

3. Start Gradio UI at http://localhost:7860

```sh
   gradio ./agentbuilder/ui/app.py
```

#### [Alternate] Start using Poetry

1. Follow the [Offical Instruction Guide](https://python-poetry.org/docs/#installation) to install Poetry.

2. Install dependencies.

```sh
   poetry install
```

3. Update API keys in the environment

```sh
   export OPENAI_API_KEY=""
   export NVIDIA_API_KEY=""
```

4. Start Gradio UI at http://localhost:7860

```sh
   gradio ./agentbuilder/ui/app.py
```

## Usage

Interview Agent uses the power of AI to help users prepare for their programming interviews.

**Skills Recommendation**: Using RAG, the Agent can ingest the candidate's resume, and job description and recommend skills.

**Programming Interview**: Based on the programming language selected, the agent will ask questions to evaluate the candidate.

**Evaluation Report**: At the end of the Interview, the Agent generates an Evaluation report in markdown format with a rating and explanation for each answer.

## Architecture

The Agents are executed using [Langchain](https://www.langchain.com/) and [Nemo Guard Rails](https://docs.nvidia.com/nemo/guardrails/index.html) framework.

**interview_agent**: The primary agent that interacts with the user. It uses other agents to complete the workflow.

**resume_vector_agent**: The agent uses RAG (retrieval augmented generation) to read the candidate's resume, and job description and produces a list of recommended skills.

**interview_question_agent**: The agent uses a job summary, and selected programming language as inputs to generate an interview question.

**rating_agent**: Evaluation Agent that provides rating and explanation based on the provided questions and answers.


## Guardrails

Using Nemo Guardrails, the Interview Agent is designed to follow a fixed workflow updating the global **Interview State**.
This also prohibits the AI agent from responding on its own thereby avoiding hallucination and unpredictable AI responses.
As an additional guard, Input Rails are configured to invoke refusal from agents when responding to user messages that contain harmful intentions.

## Interview State

The entire state of the conversation is updated live. The candidate at any time during the conversation can track the global state in UI and update it.


## Agents in Depth

![interview_agent drawio](https://github.com/nagaraj-real/interview-agent/assets/17967313/a5097b4b-dd53-4701-a1bf-46026a170928)

### Resume Vector Agent

The Agent uses the NV-Embed-QA model by integrating NIM endpoints and Langchain. The workflow is designed using Langraph.
The following sequence of steps is executed:
- Skills are extracted from the job description and resume using RAG retriever.
- Job summary is captured using RAG summarization and stored in state.
- Finally, the recommended skills are captured from LLM and stored in state.

![image](https://github.com/nagaraj-real/interview-agent/assets/17967313/5803cc75-a6cf-4af8-bcd2-332aaa519bf5)

### Interview Question Agent

The agent executes in a loop asking interview questions and capturing both the question and answer in state.
The number of questions for the interview is made configurable using state.

![image](https://github.com/nagaraj-real/interview-agent/assets/17967313/9e73b502-f1d9-4c29-9635-5fb35cfacc22)

### Rating Agent

The agent loops through the answers provided by the user and gives a rating with an explanation. 
Finally, the evaluation is rendered as a markdown.

![image](https://github.com/nagaraj-real/interview-agent/assets/17967313/e14e5a0d-fb07-43a2-ad7d-7c54405f8997)
















