# Managing multiple coding agents

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-maestro](01-maestro/) | [RunMaestro/Maestro](https://github.com/RunMaestro/Maestro) | [d17490464a](https://github.com/RunMaestro/Maestro/commit/d17490464a24e577fd71aa4c221331ed6865c9d5) |
| 2 | [02-agentsmesh](02-agentsmesh/) | [AgentsMesh/AgentsMesh](https://github.com/AgentsMesh/AgentsMesh) | [d38e3932df](https://github.com/AgentsMesh/AgentsMesh/commit/d38e3932df436fadd814a8871b8c6b7be52281d5) |
| 3 | [03-dorothy](03-dorothy/) | [Charlie85270/Dorothy](https://github.com/Charlie85270/Dorothy) | [470b8ac71c](https://github.com/Charlie85270/Dorothy/commit/470b8ac71c51a5f1634672d5b430f190cfb65646) |
| 4 | [04-agent-teams-ai](04-agent-teams-ai/) | [777genius/agent-teams-ai](https://github.com/777genius/agent-teams-ai) | [5aa0a03b6e](https://github.com/777genius/agent-teams-ai/commit/5aa0a03b6e87e48cfce6060cde0341c73d7cfa57) |
| 5 | [05-reevesagents](05-reevesagents/) | [mertkayacs/reevesagents](https://github.com/mertkayacs/reevesagents) | [7a5d37721e](https://github.com/mertkayacs/reevesagents/commit/7a5d37721ed1df20608a640cf7ce8411b2880ec5) |
| 6 | [06-amux](06-amux/) | [mixpeek/amux](https://github.com/mixpeek/amux) | [6f19279726](https://github.com/mixpeek/amux/commit/6f192797264dd6701603aaef01bbdde3ce8580f0) |
| 7 | [07-wmux](07-wmux/) | [openwong2kim/wmux](https://github.com/openwong2kim/wmux) | [6abc7ef205](https://github.com/openwong2kim/wmux/commit/6abc7ef205fbc170ecefcee2f8a2e069efe103a8) |
| 8 | [08-agent-manager](08-agent-manager/) | [YoanWai/agent-manager](https://github.com/YoanWai/agent-manager) | [258117120a](https://github.com/YoanWai/agent-manager/commit/258117120aee1534c9437421c07d9902f00daab2) |
| 9 | [09-cate](09-cate/) | [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | [cd54943572](https://github.com/0-AI-UG/cate/commit/cd5494357270fd6412e08d0f7574ed5cbcdd0782) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- managing-multiple-coding-agents/01-maestro
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
