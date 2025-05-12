# OpenAI Responses API vs Chat Completions API – Hands-on Playground 🚀

Watch the step-by-step walkthrough for each script (with timestamps):

## 🎬 Demo video playlist

<p align="center">
  <a href="https://www.youtube.com/playlist?list=PLxa63PV1cn7AGqToKbLVMcBoDGx48ocaL" target="_blank">
    <img src="docs/demo-playlist.png" alt="Click to watch the Responses-API demo playlist on YouTube" width="720">
  </a>
</p>

[![Watch the demo playlist](https://img.youtube.com/vi/VIDEO_ID/hqdefault.jpg)](https://www.youtube.com/playlist?list=PLxa63PV1cn7AGqToKbLVMcBoDGx48ocaL)


*Click the image to open the full playlist on YouTube (9 × short episodes, ~5 min each).*


The **Responses API** is OpenAI’s next-gen interface for building agent-style applications.  
It keeps everything you already know from `chat.completions.create()` **and** layers on:

|           | Chat Completions | Responses API |
|-----------|-----------------|---------------|
| Built-in tools (`web_search`, `file_search`, `computer_use`) | ✖ | ✔ |
| Automatic state via `previous_response_id` | ✖ | ✔ |
| JSON / Pydantic structured output helper | ✖ | ✔ |
| `reasoning.effort = low \| medium \| high` | ✖ | ✔ |
| Developer-only prompt channel | ✔ | ✔ (simplified) |

*(The Responses API will replace the Assistants API; Completions will remain supported.)* :contentReference[oaicite:1]{index=1}

---

## Repository contents

| Script | What it shows | TL;DR |
|--------|---------------|-------|
| `01.simple_query.py` | **Hello Responses** – one-liner text prompt | No more `choices[0].message.content` 💜 |
| `02.image_query.py` | Native multimodal input/output | Pass bytes or URLs directly |
| `03.stream_query.py` | Server-sent streaming | Identical pattern, new event objects |
| `04.web_search.py` | 🔍 `web_search` tool | Real-time citations from the public web |
| `05.file_search.py` | 📄 `file_search` tool + vector stores | Zero-setup RAG over your PDFs |
| `06.function_calling.py` | Custom function calling | Structured calls just like before |
| `07.state_management.py` | `previous_response_id` | Forget chat-history juggling |
| `08.structured_output.py` | JSON / Pydantic parsing | Hallucination-free data contracts |
| `09.developer_role.py` | Developer role & `instructions` param | Keep the system prompt slim |
| `10.reasoning.py` | Controllable chain-of-thought | Trade latency for deeper reasoning |

*(All scripts are ≤ 100 LOC and independent.)*

## Watch the demo videos series on YouTube https://www.youtube.com/playlist?list=PLxa63PV1cn7AGqToKbLVMcBoDGx48ocaL 


---

## Quick start

```bash
# Clone the repo
git clone https://github.com/lararachidi/responses-api.git
cd responses-api
```

Create a .env at the project root:
```OPENAI_API_KEY=sk-...```

Run any example:
```python 04.web_search.py```


## How the built-in tools work
web_search – retrieves and cites fresh public-web content (same engine as ChatGPT browse).

file_search – upload files ► chunk & embed ► query with similarity search.

computer_use – (preview) drive a virtual desktop with mouse/keyboard events. 

The model decides when to invoke a tool; your code only needs to list the tools in the tools=[...] array.

## Further Reading 

Blog: New tools for building agents: https://openai.com/index/new-tools-for-building-agents/

Docs:
* https://platform.openai.com/docs/guides/text?api-mode=responses
* https://platform.openai.com/docs/guides/tools-web-search
* https://platform.openai.com/docs/guides/tools-file-search

## Contributing
Issues and PRs are welcome – especially for additional examples (audio, code-interpreter once released).


