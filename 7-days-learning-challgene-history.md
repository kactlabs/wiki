/ [Home](index.md)

## 7 Days GenAI Learning Challenge Task History

### Season 1: Apr 2026

### Day 1 Task:

Python: Variables, Lists, and Dicts for AI data handling.

Learn the above topic from Claude and create multiple code-snippets in your pynotes. Create an article on personal blog (username.github.io).

Publish a post on LinkedIn.

Come and validate your learning with our mentors. They will help you get it done.

It will take you only 15-60 minutes.

Ref: [Python Fundamentals](https://csp.gitbook.io/python-learning/basics/ch02-python-fundamentals-)

### Day 2 Task:

FastAPI: Creating your first GET & POST endpoints.

Yesterday you handled data like a pro. Today you make it *live*. You're building a real HTTP server — the same kind that powers AI products and agent backends. FastAPI is what modern AI engineers actually use. And you're writing it today.

What you're doing:

- Build a `GET` endpoint — serve your Python data as JSON
- Build a `POST` endpoint — accept input, validate it, respond to it
- Open Swagger UI — test everything without touching a frontend

Your deliverables:

- Code snippets in your pynotes
- Article on your GitHub Pages blog
- LinkedIn post — share your win publicly
- Mentor validation session

15–60 minutes. That's it.

Ref: [FastAPI Basics](https://csp.gitbook.io/python-learning/fastapi-basics)

Drop your server screenshot below when it's running. Let's go!

-----

### Day 3 Task:

Goal: Build a complete end-to-end AI pipeline from scratch. Focus on stateful AI and efficient database storage. Teach your local AI to "read" your own private data. Build AI that can use tools and make independent decisions.

What you're doing:

- llama.cpp: Loading a GGUF model and generating text
- llama.cpp: Controlling temperature, top-p & max tokens
- MongoDB: Updating and deleting documents, field operators
- MongoDB: Storing entries by date, querying date ranges
- llama.cpp: Forcing output format — top text / bottom text JSON

Your deliverables:

- Code snippets in your pynotes
- Article on your GitHub Pages blog
- LinkedIn post — share your win publicly
- Mentor validation session

15–60 minutes. That's it.

-----

### Day 4 Task:

MongoDB Connection & Persistent Storage

Goal: Connect Python to a real MongoDB instance — Atlas or local — and build the persistence layer that all your future AI pipelines will rely on. By the end of this session, your app saves, retrieves, and manages data without losing it when the process dies.

What you're doing:

- MongoDB Atlas setup — Free tier cluster, IP whitelist, connection string
- PyMongo connection from Python — MongoClient, db/collection handles, ping check
- insert_one / insert_many — Save structured dicts, capture inserted_id
- find_one / find with filters — Query by field, equality, and projection
- Environment variable secrets — python-dotenv, .env file, never hardcode credentials
- Saving AI output to MongoDB — Persist llama.cpp response + prompt + timestamp as one document

Your deliverables:

- ☐ Code snippets in your pynotes
- ☐ Article on your GitHub Pages blog
- ☐ LinkedIn post — share your win publicly
- ☐ Mentor validation session

15–60 minutes. That's it.

-----

### ⚡ *Day 6 of 7 — GenAI Learning Challenge*

*Integration: Using FastAPI to trigger a llama.cpp response*

Day 2 you built endpoints. Day 5 you ran a local LLM. Today you wire them together — and everything clicks.

One POST request hits your FastAPI server. Your server calls llama.cpp. The model responds. You just built the backbone of a local AI product. No OpenAI. No cloud. Yours.

*What you're doing:*
→ Load your GGUF model once at FastAPI startup — not on every request
→ Define a Pydantic schema: `prompt`, `max_tokens`, `temperature`
→ Build `/generate` — prompt in, LLM response out as JSON
→ Test it from Swagger UI *and* `curl` — both must work

*The stack you've built this week:*
`Python → FastAPI → MongoDB → llama.cpp → /generate`

*Your deliverables:*
📓 Code snippets in your pynotes
✍️ Article on your GitHub Pages blog
💼 LinkedIn post — show the world your local AI API
🎓 Mentor validation session

⏱ *15–60 minutes. One day left after this.*

📖 Reference: https://csp.gitbook.io/python-learning/integration

Drop your `curl` output or Swagger screenshot below. Let's go! 👇


-----


### 🏁 *Day 7 of 7 — GenAI Learning Challenge*

*Project: A basic "AI Notes" app that saves chats to MongoDB*

This is it. The final day.

Day 1 you handled data. Day 2 you built endpoints. Day 3 you connected a database. Day 5 you ran a local LLM. Day 6 you wired it all together. Today you *ship a real product*.

The AI Notes app is everything you've learned — in one working application. Send a prompt to your local model, get a response, save it to MongoDB. Your app now has memory. Your week now has a proof of work.

*What you're building:*
→ `POST /chat` — prompt in, llama.cpp response out
→ Auto-save every chat to MongoDB with a timestamp
→ `GET /notes` — full conversation history across sessions
→ Push to GitHub with a clean README and screenshot

*The full stack — 7 days in one app:*
`Python → FastAPI → llama.cpp → MongoDB → AI Notes App`

*Your deliverables:*
📓 GitHub repo with README + screenshot
✍️ Blog article on your GitHub Pages
💼 LinkedIn post — you shipped an AI app this week
🎓 Live demo to your mentors (not just code — run it)

⏱ *30–90 minutes. Make it count.*

📖 Reference: https://csp.gitbook.io/python-learning/project

Drop your GitHub repo link below when it's live. You earned this. 👇

--

Tind:
30506a69-2441-4522-9f79-4c50631fdb95