<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/banner-dark.svg?v=4">
  <img src="images/banner-light.svg?v=4" alt="Developer tools in Rust — agentic coding assistants, MCP servers, AI code review, and a dictionary for a script almost nobody can read anymore" width="100%">
</picture>

### Hi, I'm Vu

Studied aerospace, ended up building software.

### What I'm building

#### MCP servers

- **[video-transcriber-mcp-rs](https://github.com/nhatvu148/video-transcriber-mcp-rs)**<br>Video → transcript on `whisper.cpp`. 1000+ platforms, fully offline, ~6x faster than Python Whisper. [crates.io](https://crates.io/crates/video-transcriber-mcp)
- **[kagoni](https://github.com/nhatvu148/kagoni)**<br>Docker MCP server built on token-bounded I/O. Logs come back as clustered digests — 13–80x fewer tokens. [crates.io](https://crates.io/crates/kagoni)
- **[x402-mcp-proxy](https://github.com/nhatvu148/x402-mcp-proxy)**<br>Lets a walletless MCP client *pay* for tools. Holds a Solana wallet, settles USDC per call, spend-capped. [crates.io](https://crates.io/crates/x402-mcp-proxy)
- **[wincrust](https://github.com/nhatvu148/wincrust)**<br>Drives a Windows desktop over UI Automation, not screenshots. One 7 MB binary running elevated, where the Python equivalent loads 200 modules. [crates.io](https://crates.io/crates/wincrust)

#### AI code review

- **[pr-review-core](https://github.com/nhatvu148/pr-review-core)**<br>Self-hosted reviewer. Line-anchored comments on GitHub / GitLab / Bitbucket, tree-sitter context, CVE scans. [crates.io](https://crates.io/crates/pr-review-core)
- **[kaniscope-action](https://github.com/nhatvu148/kaniscope-action)**<br>The same engine as a GitHub Action, on the [Marketplace](https://github.com/marketplace/actions/kaniscope-ai-code-review) — with a [playground](https://kaniscope.nvnv.app).

#### Chữ Nôm

- **[Nôm Na Việt](https://nomnaviet.com)**<br>Hán Nôm dictionary: 27,900+ characters, handwriting recognition and manuscript OCR at 96.6% top-1. Native iOS + Android keyboards.
- **[rime-nom-viet](https://github.com/nomnaviet/rime-nom-viet)**<br>RIME input schema — type Telex, get Nôm. 100,000+ entries.

---

### Products

- **[Vexar](https://vexar.nvnv.app)**<br>Multi-agent cockpit in Rust. Run `claude`, `gemini` or `codex` in parallel, each isolated in its own git worktree, and review and merge from one screen. Download for Apple Silicon.
- **[Whisgram](https://whisgram.nvnv.app)**<br>Video → study notes: summaries, concept diagrams, flashcards. Chrome extension + web app. Agents can pay for it directly over x402.
- **[SIMCEL](https://simcel.io)**<br>Day job: supply chain digital twin for Fortune 500s. Simulates promotions, disruptions, and market shifts.

More at **[nhatvu148.dev](https://nhatvu148.dev)**.

### Where the time goes

<img src="https://raw.githubusercontent.com/nhatvu148/nhatvu148/master/images/stat.svg?v=20260902152356" alt="WakaTime Activity"/>

### And what comes out of it

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="images/shipping-dark.svg?v=20260902152356">
  <img src="images/shipping-light.svg?v=20260902152356" alt="65 releases and 1,614 downloads across 6 repositories in the last 12 months" width="100%">
</picture>

---

<p align="center">
  <a href="https://nhatvu148.dev">nhatvu148.dev</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/van-nhat-vu-nguyen/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://www.hackerrank.com/profile/nhatvu148">HackerRank</a>
</p>

<p align="center"><sub>Rust, full-stack, and AI tooling — remote.</sub></p>
