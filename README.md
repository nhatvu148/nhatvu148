### Hi, I'm Vu

Studied aerospace, ended up building software. These days I build developer tools in Rust — agentic coding assistants, MCP servers, AI code review — and a dictionary for a script almost nobody can read anymore.

### What I'm building

#### MCP servers

- **[video-transcriber-mcp-rs](https://github.com/nhatvu148/video-transcriber-mcp-rs)** [![crates.io](https://img.shields.io/crates/v/video-transcriber-mcp?style=flat-square&color=2F6F6F&label=)](https://crates.io/crates/video-transcriber-mcp)<br>Video → transcript on `whisper.cpp`. 1000+ platforms, fully offline, ~6x faster than Python Whisper.
- **[kagoni](https://github.com/nhatvu148/kagoni)** [![crates.io](https://img.shields.io/crates/v/kagoni?style=flat-square&color=2F6F6F&label=)](https://crates.io/crates/kagoni)<br>Docker MCP server built on token-bounded I/O. Logs come back as clustered digests — 13–80x fewer tokens.
- **[x402-mcp-proxy](https://github.com/nhatvu148/x402-mcp-proxy)** [![crates.io](https://img.shields.io/crates/v/x402-mcp-proxy?style=flat-square&color=2F6F6F&label=)](https://crates.io/crates/x402-mcp-proxy)<br>Lets a walletless MCP client *pay* for tools. Holds a Solana wallet, settles USDC per call, spend-capped.

#### AI code review

- **[pr-review-core](https://github.com/nhatvu148/pr-review-core)** [![crates.io](https://img.shields.io/crates/v/pr-review-core?style=flat-square&color=2F6F6F&label=)](https://crates.io/crates/pr-review-core)<br>Self-hosted reviewer. Line-anchored comments on GitHub / GitLab / Bitbucket, tree-sitter context, CVE scans.
- **[kaniscope-action](https://github.com/nhatvu148/kaniscope-action)**<br>The same engine as a GitHub Action, on the [Marketplace](https://github.com/marketplace/actions/kaniscope-ai-code-review) — with a [playground](https://kaniscope.nvnv.app).

#### Chữ Nôm

- **[Nôm Na Việt](https://nomnaviet.com)**<br>Hán Nôm dictionary: 27,900+ characters, handwriting recognition and manuscript OCR at 96.6% top-1. Native iOS + Android keyboards.
- **[rime-nom-viet](https://github.com/nomnaviet/rime-nom-viet)**<br>RIME input schema — type Telex, get Nôm. 100,000+ entries.

---

### Products

- **[Vexar](https://nhatvu148.dev/#projects)**<br>Agentic coding assistant in Rust. Autonomous multi-step tasks over a semantically indexed codebase; desktop and CLI share ~90% of the code.
- **[Whisgram](https://whisgram.nvnv.app)**<br>Video → study notes: summaries, concept diagrams, flashcards. Chrome extension + web app. Agents can pay for it directly over x402.
- **[SIMCEL](https://simcel.io)**<br>Day job: supply chain digital twin for Fortune 500s. Simulates promotions, disruptions, and market shifts.

More at **[nhatvu148.dev](https://nhatvu148.dev)**.

### Last 30 days

<img src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/stat.svg?v=20260812070047" alt="WakaTime Activity"/>

---

<p align="center">
  <a href="https://nhatvu148.dev">nhatvu148.dev</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/van-nhat-vu-nguyen/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://www.hackerrank.com/profile/nhatvu148">HackerRank</a>
</p>

<p align="center"><sub>Rust, full-stack, and AI tooling — remote.</sub></p>
