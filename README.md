# 🇪🇸 Pasito — AI Spanish Tutor

Pasito is an AI-powered Spanish learning assistant designed to help beginners practice Spanish through interactive conversations.

This project was built as a **hands-on project while learning LLM Engineering**, applying concepts from Ed Donner's LLM Engineering course to a real-world use case.

Pasito v1 started as a simple LLM-powered Spanish tutor. Building it helped me move beyond simply learning how LLMs work and start thinking about how to **design, structure, and build applications around LLMs**.

---

## 🎯 Project Overview

Learning a language requires consistent practice, but traditional learning resources can make it difficult to get immediate, interactive feedback.

Pasito explores how an LLM can be used as a conversational Spanish tutor for beginner learners.

The initial goal was intentionally simple:

> **Build a usable Spanish-learning application around an LLM while applying the LLM engineering concepts I was learning.**

Pasito v1 focuses on conversational practice rather than attempting to build a complete language-learning platform.

---

## ✨ Features

- 🇪🇸 AI-powered Spanish tutor
- 💬 Interactive conversation
- 🗣️ Spanish practice through dialogue
- 🎯 Designed with beginner learners in mind
- 🤖 LLM-generated responses
- 🖥️ Simple interactive web interface
- 🔄 Conversational context during a session

---

## 🏗️ Architecture

Pasito v1 uses a relatively simple architecture:

```text
                  ┌───────────────┐
                  │     User      │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   Streamlit   │
                  │      UI       │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ Prompt /      │
                  │ Application   │
                  │ Logic         │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │     LLM       │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │   Spanish     │
                  │   Response    │
                  └───────────────┘
```

The architecture was intentionally kept simple because the primary purpose of v1 was to **learn by building**.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LLM API**
- **Prompt Engineering**
- **Environment Variables**

---

## 📂 Project Structure

```text
pasito/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> The exact structure may vary depending on the version of the project.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Python 3.10+
- An API key for the LLM provider used by the application

### 1. Clone the repository

```bash
git clone <repository-url>
cd pasito
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add the required API credentials:

```env
OPENAI_API_KEY=your_api_key_here
```

> Never commit API keys or other secrets to the repository.

### 5. Run the application

```bash
streamlit run app.py
```

---

# 🧠 Learning Context

Pasito v1 was developed as a **learning-by-building project during my study of LLM Engineering with Ed Donner's course**.

The purpose was not simply to complete a tutorial or reproduce an example. Instead, I used the concepts I was learning as a starting point and applied them to a project based on a problem I personally cared about: **learning Spanish**.

This approach helped connect theoretical concepts with practical engineering decisions.

### Concepts explored through the project

- Working with LLM APIs
- Prompt engineering
- LLM application design
- Conversational interfaces
- Application state
- Environment and API-key management
- Building an interactive AI application
- Connecting an LLM to a user-facing application

---

# 💡 Why Pasito?

I was learning Spanish while simultaneously learning how to build LLM applications.

That made a Spanish tutor a natural project to experiment with.

Instead of building another generic chatbot, I wanted to answer a more practical question:

> **Can I use what I'm learning about LLM engineering to build something I would actually use?**

Pasito became the result of that experiment.

---

# 🔍 What I Learned

One of the biggest lessons from Pasito v1 was that **building an LLM application is different from simply calling an LLM API**.

The model itself is only one component.

The application also requires decisions around:

- User interaction
- Prompt design
- Context
- State management
- Application structure
- Error handling
- Secrets management
- User experience

Building Pasito helped me start thinking about LLMs from an **engineering perspective rather than only a model perspective**.

---

# ⚠️ Limitations of v1

Pasito v1 was intentionally simple, which also means it has several limitations.

### Knowledge

The tutor relies primarily on the LLM rather than a dedicated Spanish-learning knowledge base.

### Personalization

The system does not provide sophisticated long-term learner profiling or progress tracking.

### Retrieval

There is no dedicated retrieval pipeline for selecting relevant learning material.

### Evaluation

The application does not yet have a comprehensive evaluation framework for measuring tutoring quality.

### Learning Management

There is no structured curriculum, spaced repetition system, vocabulary database, or formal learner progression system.

These limitations became important when thinking about what Pasito could become in future versions.

---

# 🚀 Future Work

Pasito v1 provides a foundation for building a more capable AI tutoring system.

The next iterations can focus on making the system more **knowledge-aware, personalized, measurable, and reliable**.

## 1. Retrieval-Augmented Generation

Introduce a RAG pipeline containing Spanish learning resources such as:

- Grammar explanations
- Vocabulary
- Example sentences
- Beginner dialogues
- Learning notes

The system could retrieve relevant material before generating an answer.

```text
User Question
      │
      ▼
   Retriever
      │
      ▼
Relevant Spanish Material
      │
      ▼
      LLM
      │
      ▼
Tutor Response
```

---

## 2. Semantic Search

Use embeddings and a vector database to retrieve learning material based on **semantic similarity** rather than simple keyword matching.

Potential technologies include:

- Sentence Transformers
- FAISS
- Vector databases

---

## 3. Personalized Learning

Future versions could maintain learner-specific information such as:

- Current Spanish level
- Vocabulary already learned
- Common mistakes
- Weak grammar topics
- Conversation history
- Learning goals

This could allow Pasito to adapt its responses to the learner.

---

## 4. Structured Learning Activities

Expand beyond free-form conversation with activities such as:

- Vocabulary exercises
- Grammar exercises
- Fill-in-the-blank questions
- Translation practice
- Conversation scenarios
- Reading comprehension
- Listening exercises

---

## 5. Evaluation

Introduce systematic evaluation to measure whether Pasito is actually helping the learner.

Possible evaluation dimensions include:

- Answer correctness
- Relevance
- Language difficulty
- Educational usefulness
- Retrieval quality
- Hallucination rate
- Response latency

This would move the project from:

```text
"It works"
```

toward:

```text
"We can measure how well it works."
```

---

## 6. Better RAG Architecture

A more advanced version could experiment with:

- Chunking strategies
- Embedding models
- Retrieval strategies
- Reranking
- Context compression
- Query transformation
- Retrieval evaluation

This would allow Pasito to become a practical environment for experimenting with modern RAG engineering techniques.

---

## 7. Agentic Learning Workflows

A future version could introduce specialized components for different tutoring tasks.

For example:

```text
                  ┌───────────────┐
                  │     User      │
                  └───────┬───────┘
                          │
                          ▼
                  ┌───────────────┐
                  │    Tutor      │
                  │   Orchestrator│
                  └───────┬───────┘
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        Vocabulary     Grammar     Conversation
          Module        Module        Module
             │            │            │
             └────────────┼────────────┘
                          ▼
                   Personalized
                      Response
```

---

# 🧪 From Prototype to Engineering Project

The evolution of Pasito can be viewed as:

```text
Pasito v1
   │
   │  LLM application fundamentals
   ▼
Pasito v2
   │
   │  RAG + embeddings + retrieval
   ▼
Pasito v3
   │
   │  Evaluation + personalization
   ▼
Future
   │
   │  Advanced RAG / agentic workflows
   ▼
Production-oriented AI Tutor
```

The purpose of this evolution is not simply to keep adding features.

Each version should address a specific limitation discovered in the previous version.

---

# 📚 Learning Philosophy

Pasito follows a simple **learn → build → identify limitations → improve** cycle.

```text
Learn a concept
      ↓
Apply it to Pasito
      ↓
Observe limitations
      ↓
Research the problem
      ↓
Build an improved version
      ↓
Measure the improvement
```

This makes Pasito more than a single application. It serves as a practical project through which I can explore different areas of **LLM engineering and AI systems**.

---

# 🗺️ Project Roadmap

| Stage | Focus | Status |
|---|---|---|
| v1 | Basic LLM-powered Spanish tutor | ✅ Completed |
| v2 | RAG + semantic retrieval | 🔜 Planned |
| v3 | Evaluation + personalization | 🔜 Planned |
| v4 | Advanced RAG / agentic workflows | 🔮 Future |

---

# 🙏 Acknowledgment

This project was developed while learning **LLM Engineering with Ed Donner**, using the course concepts as a foundation for hands-on experimentation and independent project development.

The project is intended primarily as a learning and engineering portfolio project.

---



**Ed Donner LLM Engineering → build Pasito v1 → discover limitations → study RAG → build Pasito v2/RAG → evaluate and improve.**

That also connects very naturally with the RAG work you've been doing afterward.
