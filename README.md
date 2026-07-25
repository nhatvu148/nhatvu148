[![wakatime](https://wakatime.com/badge/user/37f85803-060b-4faf-950b-e8a7c3f4d7e7.svg)](https://wakatime.com/@37f85803-060b-4faf-950b-e8a7c3f4d7e7)

### Hi, I'm Vu

Studied aerospace, ended up building software. These days I build developer tools in Rust — and a dictionary for a script almost nobody can read anymore.

```rust
use ai::{agents, mcp, rag};
use rust::{axum, tauri, tokio};

#[derive(Debug, Clone, CoffeePowered)]
pub struct Vu {
    langs: Vec<&'static str>,
    building: Vec<&'static str>,
}

impl Vu {
    pub fn init() -> Self {
        Self {
            langs: vec!["Rust", "TypeScript", "Python", "Go"],
            building: vec![
                "Agentic dev tools",
                "MCP servers & RAG",
                "Tauri desktop apps",
                "A Hán Nôm dictionary",
            ],
        }
    }

    pub fn run(&self) -> Result<(), Burnout> {
        for project in &self.building {
            self.build(project)?;
            self.learn()?;
            self.coffee()?;
        }
        Ok(())
    }
}

fn main() -> Result<(), Burnout> {
    Vu::init().run()
}
```

### What I'm building

**Open source**

| Project | What it does |
| --- | --- |
| [video-transcriber-mcp-rs](https://github.com/nhatvu148/video-transcriber-mcp-rs) | MCP server on `whisper.cpp` — transcribes video from 1000+ platforms, 90+ languages, fully offline. ~6x faster than Python Whisper. [`crates.io`](https://crates.io/crates/video-transcriber-mcp) |
| [pr-review-core](https://github.com/nhatvu148/pr-review-core) | Self-hosted AI PR reviewer. Line-anchored inline comments on GitHub / GitLab / Bitbucket, tree-sitter structural context, OSV.dev CVE scans. [`crates.io`](https://crates.io/crates/pr-review-core) |
| [rime-nom-viet](https://github.com/nhatvu148/rime-nom-viet) | RIME input schema for Vietnamese Chữ Nôm — type Telex, get Nôm. 100,000+ entries, works on desktop and mobile. |
| [agent-loop-core](https://github.com/nhatvu148/agent-loop-core) | A hand-rolled LLM agent loop for Rust: resilient transport, typed tools, streaming events, two-model cost split. Provider-agnostic. |
| [llm-harness-starter](https://github.com/nhatvu148/llm-harness-starter) | Clone-and-go scaffold for a grounded LLM agent — model + MCP tools + RAG + curated procedures, each swappable. |
| [kaniscope-action](https://github.com/nhatvu148/kaniscope-action) | AI code review as a GitHub Action, powered by `pr-review-core`. |

**Products**

| Project | What it does |
| --- | --- |
| [Vexar](https://nhatvu148.dev/#projects) | Agentic coding assistant in Rust — autonomous multi-step tasks over a semantically indexed codebase. Tauri desktop + CLI sharing ~90% of the code. |
| [Nôm Na Việt](https://nomnaviet.com) | Hán Nôm dictionary: 27,900+ characters across 30+ texts, eight lookup methods including handwriting recognition and manuscript OCR (in-house PyTorch models). |
| [Whisgram](https://whisgram.nvnv.app) | Turns video into study notes — summaries, concept diagrams, flashcards, timestamped transcripts. Chrome extension + web app. |
| [SIMCEL](https://simcel.io) | Day job: supply chain digital twin for Fortune 500s. Simulates promotions, disruptions, and market shifts. |

More at **[nhatvu148.dev](https://nhatvu148.dev)**.

### Things I play with

<div align="center">
<img title="Rust" alt="Rust" width="40px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/rustacean-flat-happy.svg" />&nbsp;&nbsp;
<img title="TypeScript" alt="TypeScript" width="26px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/Typescript_logo_2020.svg" />&nbsp;&nbsp;
<img title="Python" alt="Python" width="26px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/Python-logo-notext.svg" />&nbsp;&nbsp;
<img title="Go" alt="Go" width="30px" src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/go.svg" />&nbsp;&nbsp;
<img title="React" alt="React" width="28px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/react-svgrepo-com.svg" />&nbsp;&nbsp;
<picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/nextjs-dark.svg" /><img title="Next.js" alt="Next.js" width="25px" src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/nextjs-light.svg" /></picture>&nbsp;&nbsp;
<img title="Angular" alt="Angular" width="28px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/angular-svgrepo-com.svg" />&nbsp;&nbsp;
<img title="Node.js" alt="Node.js" width="27px" src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/nodejs.svg" />&nbsp;&nbsp;
<img title="Tauri" alt="Tauri" width="26px" src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/tauri.svg" />&nbsp;&nbsp;
<img title="PostgreSQL" alt="PostgreSQL" width="27px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/postgresql-icon.svg" />&nbsp;&nbsp;
<img title="MongoDB" alt="MongoDB" width="27px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/mongo-svgrepo-com.svg" />&nbsp;&nbsp;
<img title="Redis" alt="Redis" width="35px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/redis-logo.png" />&nbsp;&nbsp;
<img title="Docker" alt="Docker" width="35px" src="https://cdn.jsdelivr.net/gh/nhatvu148/nhatvu148@master/images/4844483.png" />&nbsp;&nbsp;
</div>

### Last 30 days

<img src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/stat.svg?v=20260725121434" alt="WakaTime Activity"/>

---

<p align="center">
  <a href="https://nhatvu148.dev">nhatvu148.dev</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/van-nhat-vu-nguyen/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://leetcode.com/nhatvu148">LeetCode</a>
</p>

<p align="center"><sub>Open to full-stack, Rust, and AI tooling work — remote.</sub></p>
