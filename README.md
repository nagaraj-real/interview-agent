# Interview Agent

## 🚀 Quick Start

1. Set up a Python virtualenv and install dependencies

```sh
   python -m venv --prompt interview-agent venv
   source venv/bin/activate
   # venv/Scripts/activate (Windows)
   pip install -r requirements.txt
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

**resume_vector_agent**: The agent uses RAG (retrieval augmented generation) to read candidate's resume, job description and produces a list of recommended skills.

**interview_question_agent**: The agent uses job summary, user selected programming language as inputs to generate an interview question.

**rating_agent**: Evaluation Agent that provides rating and explanation based on the provided questions and answers.


## Guardrails

Using Nemo Guardrails, the Interview Agent is designed to follow a fixed workflow updating the global **Interview State**.
Using Input Rails, the agent refuses to respond to user messages that contain harmful intentions.
This also prohibits the AI agent from responding on its own thereby avoiding hallucination and unpredictable AI responses.

## Interview State

The entire state of the conversation is updated live. The candidate at any time during the conversation can track the global state in UI and update it.


## Agents in Depth

### Interview Agent




