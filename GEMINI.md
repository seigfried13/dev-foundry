# Hephaestus: A Semi-Structured Agentic Framework

## Project Overview

Hephaestus is a Python-based, semi-structured agentic framework designed to allow AI agents to collaboratively solve complex software engineering tasks. The system is architected around a phased approach, enabling agents to dynamically create and delegate tasks, adapting the workflow in real-time based on their discoveries.

The core of Hephaestus is a `fastapi` server that orchestrates the work of multiple AI agents. These agents operate in isolated `tmux` sessions and interact with various services, including a Qdrant vector store for memory and a database for task management. The system is designed to be highly configurable, with a central `hephaestus_config.yaml` file controlling everything from LLM providers to agent behavior.

### Key Technologies

- **Backend:** Python, FastAPI, SQLAlchemy
- **Vector Store:** Qdrant
- **LLM Integration:** OpenAI, Anthropic, OpenRouter, Groq, Google AI
- **Agent Execution:** tmux
- **Frontend:** Node.js, npm (for UI)
- **Containerization:** Docker

## Building and Running

The primary way to run Hephaestus is through Docker Compose, which orchestrates the necessary services.

### Prerequisites

- Python 3.10+
- Docker
- Node.js & npm
- `tmux`

### Running the Application

1.  **Set up the environment:**
    -   Create a `.env` file from the `.env.example` and populate it with your API keys for the desired LLM providers.

2.  **Start the services:**
    ```bash
    docker-compose up -d
    ```
    This command will start the Qdrant vector store, the Hephaestus server, and the monitoring service in the background.

3.  **Running a workflow:**
    -   Workflows are defined as Python scripts that interact with the Hephaestus server. The `run_example.py` script provides a starting point for executing a workflow.
    ```bash
    python run_example.py
    ```

### Testing

The project includes a `tests` directory with a suite of tests that can be run using `pytest`:

```bash
pytest
```

## Development Conventions

-   **Configuration:** The primary configuration for the project is in `hephaestus_config.yaml`. This file should be used to configure all aspects of the system.
-   **Dependencies:** Python dependencies are managed with Poetry and are listed in `pyproject.toml`. Additional dependencies are listed in `requirements.txt`.
-   **Workflows:** Workflows are defined in the `example_workflows` directory. These serve as examples of how to structure and execute tasks within the Hephaestus framework.
-   **Agents:** Agent logic and prompts are located in the `src/agents` and `src/prompts` directories, respectively.
-   **Phases:** The different phases of a workflow are defined in the `src/phases` directory.
