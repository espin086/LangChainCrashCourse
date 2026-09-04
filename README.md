# LangChainCrashCourse

Scripts written while following along with LangChain crash-course videos on YouTube. It is a
learning repo, not a library. Two small pieces: a function that asks an OpenAI chat model for
pet names, and a ReAct agent wired to a Wikipedia tool. A Streamlit page wraps the pet namer so
the prompt inputs become dropdowns and sliders.

## Contents

- `llm_helper.py`. the LangChain code. `pet_namer()` builds a `ChatPromptTemplate` with a system
  and user message, pipes it through `ChatOpenAI` and `StrOutputParser` using the LCEL `|` syntax,
  and invokes the chain with `animal`, `color`, and `num_names`. `agent_wikipedia()` pulls the
  `hwchase17/react` prompt from LangChain Hub, builds a ReAct agent over the `wikipedia` tool with
  `create_react_agent`, and runs it through an `AgentExecutor` with `verbose=True` so the
  reasoning steps print. Running the file directly calls `agent_wikipedia("What is the capital of
  France?")`; note the function prints its trace but returns `None`.
- `main.py`. Streamlit front end for `pet_namer()`. Sidebar controls pick the animal type, color,
  and number of names, and the result is written to the page. `load_dotenv()` reads the API key
  from `.env`.
- `__init__.py`. empty.
- `requirements.txt`. dependencies.

The file has a few unused imports left over from the videos (`initialize_agent`, `AgentType`,
`TavilySearchResults`, `OpenAI`). Nothing in the repo uses Tavily.

## Requirements

- Python 3
- An OpenAI API key
- Packages listed in `requirements.txt`: `openai`, `langchain`, `streamlit`, `python-dotenv`,
  `wikipedia`, `numexpr`

`llm_helper.py` imports from `langchain_openai`, `langchain_core`, and `langchain_community`,
which are not named in `requirements.txt`. Install them too if a plain `pip install -r` leaves
import errors.

## Installation

```bash
git clone https://github.com/espin086/LangChainCrashCourse.git
cd LangChainCrashCourse
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install langchain-openai langchain-community
```

Create a `.env` file in the repo root:

```
OPENAI_API_KEY=sk-...
```

`.env` is already in `.gitignore`.

## Usage

Streamlit pet namer:

```bash
streamlit run main.py
```

Pick an animal, type a color, set how many names you want, and the page shows the model output.

Wikipedia ReAct agent:

```bash
python llm_helper.py
```

That runs the hardcoded question about the capital of France and prints the agent's steps. Change
the string at the bottom of the file to ask something else.

The `hub.pull` call fetches the prompt from LangChain Hub over the network, so the agent needs
internet access on top of the API key.

## License

MIT. See [LICENSE](LICENSE).
