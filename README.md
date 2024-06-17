# Interview Agent

## 🚀 Quick Start

1. Set up a Python virtualenv and install dependencies

```sh
   python -m venv --prompt interview-agent venv
   source venv/bin/activate
   # venv/Scripts/activate (Windows)
   pip install -r requirements.txt
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

#### [Optional] Start using Poetry

For fine-grained dependency management, use [Poetry](https://python-poetry.org/) to pick and choose dependency packs based on your LLM model provider and tool features.

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

Interview Agent uses the power of AI to help users prepare for their interview.

**Skills Recommendation**: Using RAG, the Agent can ingest the candidate's resume, and job description and recommend skills.

**Programming Interview**: Based on the programming language selected, the agent will ask questions to evaluate the candidate.

**Evaluation Report**: At the end of the Interview, the Agent generates an Evaluation report in markdown format with a rating and explanation for each answer.

## Architecture

The Agents are executed using [Langchain](https://www.langchain.com/) and [Nemo Guard Rails](https://docs.nvidia.com/nemo/guardrails/index.html) framework.

**interview_agent**: The primary agent that interacts with the user. It uses other agents to complete the workflow.

- _Model_: **meta/llama3-70b-instruct** using [NVIDIA NIM APIs](https://build.nvidia.com/explore/discover#llama3-70b)

**resume_vector_agent**: A vector DB retrieval Agent that suggests programming skills using tool calling based on the provided resume,job description.

- _Model_: **openai/gpt-3.5-turbo**

**rating_agent**: Evaluation Agent that provides rating and explanation based on the provided questions and answers.

- _Model_: **openai/gpt-3.5-turbo**

## Guardrails

Using Nemo Guardrails, the Interview Agent is designed to follow a fixed workflow updating the global **Interview State**.
This also prohibits the AI agent from responding on its own thereby avoiding hallucination and unpredictable AI responses.

## Interview State

The entire state of the conversation is updated live. The candidate at any time during the conversation can track the global state in UI and update it.
