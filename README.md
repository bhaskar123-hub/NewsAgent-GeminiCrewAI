# NewsAgent — CrewAI ✕ Google Gemini

An experimental multi‑agent workflow that **researches a news topic and drafts a publishable markdown article** using [CrewAI](https://github.com/crewAIInc/crewAI) for orchestration and **Google Gemini** for language generation.


---

## 📌 What this project does

* Spins up a small **crew of specialized agents** (e.g., researcher, writer) defined in `agents.py`.
* Wires them to **tasks** in `tasks.py` and **external tools** (search/scrape, etc.) in `tools.py`.
* Orchestrates the flow in `crew.py` to produce a **news article** saved to `new-blog-post.md`.
* Uses **Gemini** as the LLM (via your Google API key) for reasoning and writing.

---

---

## 🚀 Quickstart

### 1) Prerequisites

* Python **3.10+** recommended
* A **Google API key** for Gemini (Model: 1.5‑Flash/Pro/2.0/2.5 depending on your setup)

### 2) Clone & set up

```bash
git clone https://github.com/bhaskar123-hub/NewsAgent-GeminiCrewAI.git
cd NewsAgent-GeminiCrewAI

# create & activate a virtual env (choose one)
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\Scripts\activate        # Windows PowerShell

# install
pip install -r requirements.txt
```

### 3) Configure secrets

Create a `.env` file in the project root (never commit real keys):

```dotenv
# Required for Gemini
GOOGLE_API_KEY=your_google_api_key_here

# Optional search providers (uncomment the one(s) you use)
# SERPER_API_KEY=your_serper_key
# TAVILY_API_KEY=your_tavily_key
# NEWSAPI_KEY=your_newsapi_key
```

If your code expects a different variable name (e.g., `GEMINI_API_KEY`), mirror the same value under that name as well.

### 4) Run

```bash
python crew.py
```

* The crew runs the research → writing pipeline.
* The final article is saved as **`new-blog-post.md`** by default.

> If your pipeline accepts CLI args or an interactive prompt (topic, style, length), use them here. Otherwise, set defaults inside `tasks.py`.

---

## 🧩 How it works (high‑level)

1. **Agents** (`agents.py`)

   * Define roles like *News Researcher* and *Article Writer* with clear goals and backstories.
   * Configure the LLM (Gemini) and attach capabilities (e.g., tools, context limits).

2. **Tools** (`tools.py`)

   * Wrap external capabilities such as **web search**, **page scraping**, RSS fetching, etc.
   * Expose them as callable tools to agents (CrewAI tool interface).

3. **Tasks** (`tasks.py`)

   * Map concrete objectives (e.g., “gather top 5 recent articles for a topic”, “draft a 800‑word post with citations”).
   * Provide input variables (topic, audience, tone) and expected output format (markdown, JSON, etc.).

4. **Orchestration** (`crew.py`)

   * Builds the crew (agents + tasks) and selects the **process** (commonly `sequential`).
   * Kicks off execution and writes the final artifact to `new-blog-post.md`.

A typical flow looks like:

```
[Research Task] → [Synthesis/Drafting Task] → [(Optional) Edit/Polish Task] → output.md
```

---

## ⚙️ Configuration knobs

* **Model**: In `agents.py`, switch Gemini variants (e.g., `gemini-1.5-flash`, `gemini-1.5-pro`, `gemini-2.0-flash`, `gemini-2.5-pro`) depending on latency/quality needs.
* **Topic/Prompt**: Centralize in `tasks.py` or read from CLI/env for reproducibility.
* **Safety/Filters**: Add basic guardrails in tools (e.g., domain allowlist, date filters).
* **Output Path**: Set the filename/path for generated content (default: `new-blog-post.md`).

---

## 🧪 Example: tweak the topic

Inside `tasks.py`, you’ll typically see a variable or input template for the topic. Adjust it, or make it dynamic:

```python
# tasks.py (illustrative snippet)
NEWS_TOPIC = os.getenv("NEWS_TOPIC", "AI regulation updates in India")
TARGET_AUDIENCE = "Tech‑savvy professionals"
```

Then run:

```bash
NEWS_TOPIC="NVIDIA Q3 earnings" python crew.py
```

---

## 🔧 Extending the project

* **Add more agents**: editor, fact‑checker, SEO specialist.
* **Add tools**: SERPer/Tavily search, RSS feeds, Archive.org, source credibility scoring.
* **Post‑processing**: Grammarly API, markdown linting, link checker, image generation.
* **Delivery**: auto‑publish to Medium/Hashnode/Dev.to, or push to a CMS/GitHub Pages.
* **Caching & evals**: local cache of fetched pages; add unit tests for prompts & tools.

---

## 🐛 Troubleshooting

* `google.generativeai` import errors → `pip install google-generativeai` and re‑check Python version.
* 401/403 from search providers → verify API keys and quota; ensure keys are loaded from `.env`.
* Tool HTTP errors → add retries, user‑agents, backoff in `tools.py`.
* Output not written → confirm the path in `crew.py` and that the process runs to completion.

---

## 📦 Requirements

All dependencies are pinned in `requirements.txt`. Install with:

```bash
pip install -r requirements.txt
```

> If you use a system Python that ships an older `protobuf`/`pydantic`, create a clean venv to avoid version conflicts.

---

## 📜 License

Add a LICENSE (MIT/Apache‑2.0 are common). Until then, treat this as **All Rights Reserved**.

---

## 🙏 Acknowledgments

* [CrewAI](https://github.com/crewAIInc/crewAI) for the multi‑agent framework
* Google **Gemini** API for LLM capabilities


