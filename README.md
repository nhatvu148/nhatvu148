[![wakatime](https://wakatime.com/badge/user/37f85803-060b-4faf-950b-e8a7c3f4d7e7.svg)](https://wakatime.com/@37f85803-060b-4faf-950b-e8a7c3f4d7e7)

### Hi, I'm Vu

Studied aerospace, ended up building software. Now working on AI agents, 3D visualization, and desktop apps.

```rust
use ai::{agents, mcp, rag};
use graphics::{threejs, webgl, ceetron};

#[derive(Debug, Clone, CoffeePowered)]
pub struct Vu {
    langs: Vec<&'static str>,
    building: Vec<&'static str>,
}

impl Vu {
    pub fn init() -> Self {
        Self {
            langs: vec!["TypeScript", "Python", "Rust", "C++"],
            building: vec![
                "Full-stack apps",
                "AI Agents & RAG",
                "3D/CAE visualization",
                "Tauri desktop apps",
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

### Things I play with

<div align="center">
<img title="TypeScript" alt="TypeScript" width="26px" src="images/Typescript_logo_2020.svg" />&nbsp;&nbsp;
<img title="Python" alt="Python" width="26px" src="images/Python-logo-notext.svg" />&nbsp;&nbsp;
<img title="Rust" alt="Rust" width="40px" src="images/rustacean-flat-happy.svg" />&nbsp;&nbsp;
<img title="C++" alt="C++" width="26px" src="images/ISO_C++_Logo.svg" />&nbsp;&nbsp;
<img title="React" alt="React" width="28px" src="images/react-svgrepo-com.svg" />&nbsp;&nbsp;
<img title="Angular" alt="Angular" width="28px" src="images/angular-svgrepo-com.svg" />&nbsp;&nbsp;
<img title="PostgreSQL" alt="PostgreSQL" width="27px" src="images/postgresql-icon.svg" />&nbsp;&nbsp;
<img title="MongoDB" alt="MongoDB" width="27px" src="images/mongo-svgrepo-com.svg" />&nbsp;&nbsp;
<img title="Redis" alt="Redis" width="35px" src="images/redis-logo.png" />&nbsp;&nbsp;
<img title="Docker" alt="Docker" width="35px" src="images/4844483.png" />&nbsp;&nbsp;
</div>

### This week

<img src="images/stat.svg" alt="WakaTime Activity"/>

---

<p align="center">
  <a href="https://nhatvu148.dev">nhatvu148.dev</a>
</p>
