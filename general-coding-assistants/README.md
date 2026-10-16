# General coding assistants

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-opencode](01-opencode/) | [anomalyco/opencode](https://github.com/anomalyco/opencode) | [50d4280dbd](https://github.com/anomalyco/opencode/commit/50d4280dbdb2a8e5d9c89eb6c893d12c7a37f69f) |
| 2 | [02-aider](02-aider/) | [Aider-AI/aider](https://github.com/Aider-AI/aider) | [5dc9490bb3](https://github.com/Aider-AI/aider/commit/5dc9490bb35f9729ef2c95d00a19ccd30c26339c) |
| 3 | [03-cline](03-cline/) | [cline/cline](https://github.com/cline/cline) | [01b8a9724d](https://github.com/cline/cline/commit/01b8a9724da905423e636396d7fb4acdf47796bb) |
| 4 | [04-plandex](04-plandex/) | [plandex-ai/plandex](https://github.com/plandex-ai/plandex) | [e2d772072e](https://github.com/plandex-ai/plandex/commit/e2d772072efadbe41d2946d97d79be55532dbab5) |
| 5 | [05-keen-code](05-keen-code/) | [mochow13/keen-code](https://github.com/mochow13/keen-code) | [725e44f054](https://github.com/mochow13/keen-code/commit/725e44f0548d0b8e5f437cf5aec28fb2d7b13bc9) |
| 6 | [06-nanocoder](06-nanocoder/) | [Nano-Collective/nanocoder](https://github.com/Nano-Collective/nanocoder) | [3945ef797b](https://github.com/Nano-Collective/nanocoder/commit/3945ef797b38085c551ae7c7e11be59f167f6bc0) |
| 7 | [07-orca](07-orca/) | [echoVic/orca-agent](https://github.com/echoVic/orca-agent) | [a7631c5c5e](https://github.com/echoVic/orca-agent/commit/a7631c5c5e6d40ce7d4db3eef3f3ad3e0163f228) |
| 8 | [08-tura](08-tura/) | [Tura-AI/tura](https://github.com/Tura-AI/tura) | [a6d1364f08](https://github.com/Tura-AI/tura/commit/a6d1364f0876fd564efee9503c0be8d7cd7a926d) |
| 9 | [09-mu](09-mu/) | [qybaihe/mu](https://github.com/qybaihe/mu) | [6c8126d3a4](https://github.com/qybaihe/mu/commit/6c8126d3a4dfef5a5c8bbf175885de7ed394c901) |
| 10 | [10-claude-engineer](10-claude-engineer/) | [Doriandarko/claude-engineer](https://github.com/Doriandarko/claude-engineer) | [0a9e4b309b](https://github.com/Doriandarko/claude-engineer/commit/0a9e4b309bf6b2eda05dcf073cf5094beb08e0c8) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- general-coding-assistants/01-opencode
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
