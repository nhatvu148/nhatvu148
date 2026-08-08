### Hi, I'm Vu

Studied aerospace, ended up building software. These days I build developer tools in Rust — agentic coding assistants, MCP servers, AI code review — and a dictionary for a script almost nobody can read anymore.

### What I'm building

**Open source**

| Project | What it does |
| --- | --- |
| [video-transcriber-mcp-rs](https://github.com/nhatvu148/video-transcriber-mcp-rs) | MCP server on `whisper.cpp` — transcribes video from 1000+ platforms, 90+ languages, fully offline. ~6x faster than Python Whisper. [`crates.io`](https://crates.io/crates/video-transcriber-mcp) |
| [pr-review-core](https://github.com/nhatvu148/pr-review-core) | Self-hosted AI PR reviewer. Line-anchored inline comments on GitHub / GitLab / Bitbucket, tree-sitter structural context, OSV.dev CVE scans. [`crates.io`](https://crates.io/crates/pr-review-core) |
| [kagoni](https://github.com/nhatvu148/kagoni) | Docker MCP server built around token-bounded I/O — logs come back as clustered digests (13x fewer tokens on a fleet check, 80x on repetitive logs), destructive writes are gated, and `--read-only` removes write tools rather than refusing them. Drives Docker, OrbStack, Podman or Colima. [`crates.io`](https://crates.io/crates/kagoni) |
| [rime-nom-viet](https://github.com/nomnaviet/rime-nom-viet) | RIME input schema for Vietnamese Chữ Nôm — type Telex, get Nôm. 100,000+ entries, works on desktop and mobile. |
| [agent-loop-core](https://github.com/nhatvu148/agent-loop-core) | A hand-rolled LLM agent loop for Rust: resilient transport, typed tools, streaming events, two-model cost split. Provider-agnostic. |
| [llm-harness-starter](https://github.com/nhatvu148/llm-harness-starter) | Clone-and-go scaffold for a grounded LLM agent — model + MCP tools + RAG + curated procedures, each swappable. |
| [kaniscope-action](https://github.com/nhatvu148/kaniscope-action) | AI code review as a GitHub Action, powered by `pr-review-core` — on the [GitHub Marketplace](https://github.com/marketplace/actions/kaniscope-ai-code-review) (`uses: nhatvu148/kaniscope-action@v1`), with a [playground](https://kaniscope.nvnv.app). |

**Products**

| Project | What it does |
| --- | --- |
| [Vexar](https://nhatvu148.dev/#projects) | Agentic coding assistant in Rust — autonomous multi-step tasks over a semantically indexed codebase. Tauri desktop + CLI sharing ~90% of the code. |
| [Nôm Na Việt](https://nomnaviet.com) | Hán Nôm dictionary: 27,900+ characters across 31 classical texts, eight lookup methods including handwriting recognition and manuscript OCR — in-house PyTorch models at 96.6% top-1 on real woodblock crops. Ships native **iOS and Android system keyboards**: type Telex → Chữ Nôm in any app, offline. |
| [Whisgram](https://whisgram.nvnv.app) | Turns video into study notes — summaries, concept diagrams, flashcards, timestamped transcripts. Chrome extension + web app. |
| [SIMCEL](https://simcel.io) | Day job: supply chain digital twin for Fortune 500s. Simulates promotions, disruptions, and market shifts. |

More at **[nhatvu148.dev](https://nhatvu148.dev)**.

### Last 30 days

<img src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/stat.svg?v=20260808062754" alt="WakaTime Activity"/>

---

<p align="center">
  <a href="https://nhatvu148.dev">nhatvu148.dev</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/van-nhat-vu-nguyen/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://www.hackerrank.com/profile/nhatvu148">HackerRank</a>
</p>

<p align="center"><sub>Rust, full-stack, and AI tooling — remote.</sub></p>
