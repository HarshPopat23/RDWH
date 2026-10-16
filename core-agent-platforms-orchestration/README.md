# Core agent platforms / orchestration

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-paperclip](01-paperclip/) | [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | [8f1cb11a03](https://github.com/paperclipai/paperclip/commit/8f1cb11a034b82e93fa414f8e77beeb702cc14e8) |
| 2 | [02-openhands](02-openhands/) | [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | [ccdb08783c](https://github.com/OpenHands/OpenHands/commit/ccdb08783cf83ffe4d72d8c41298c700fe7fda94) |
| 3 | [03-compozyos](03-compozyos/) | [compozy/compozy](https://github.com/compozy/compozy) | [2cf9f5fae8](https://github.com/compozy/compozy/commit/2cf9f5fae89db8c0e5ff1db61e108b7ea17464e0) |
| 4 | [04-typedai](04-typedai/) | [TrafficGuard/typedai](https://github.com/TrafficGuard/typedai) | [34139aec65](https://github.com/TrafficGuard/typedai/commit/34139aec65bb70f7062cf7f92667c11ffde4fcb1) |
| 5 | [05-metagpt](05-metagpt/) | [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | [11cdf466d0](https://github.com/FoundationAgents/MetaGPT/commit/11cdf466d042aece04fc6cfd13b28e1a70341b1f) |
| 6 | [06-superagi](06-superagi/) | [TransformerOptimus/SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | [c3c1982e7b](https://github.com/TransformerOptimus/SuperAGI/commit/c3c1982e7bd6a11cfed53c5a193ea502f924b1b6) |
| 7 | [07-agency](07-agency/) | [neurocult/agency](https://github.com/neurocult/agency) | [a1e4f35c5b](https://github.com/neurocult/agency/commit/a1e4f35c5bda985c4c8273dd674ad54ac5da1853) |
| 8 | [08-fractal](08-fractal/) | [plasma-ai/fractal](https://github.com/plasma-ai/fractal) | [e0cb09611c](https://github.com/plasma-ai/fractal/commit/e0cb09611c03bf0ea07eb671319714857385413b) |
| 9 | [09-microagent](09-microagent/) | [aymenfurter/microagents](https://github.com/aymenfurter/microagents) | [5d52c807de](https://github.com/aymenfurter/microagents/commit/5d52c807de0a607440dc52d1c71e789ca4132441) |
| 10 | [10-thinkgpt](10-thinkgpt/) | [jina-ai/thinkgpt](https://github.com/jina-ai/thinkgpt) | [59dd7e8a88](https://github.com/jina-ai/thinkgpt/commit/59dd7e8a881d7c6cf280c140344a72321bc289d6) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- core-agent-platforms-orchestration/01-paperclip
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
