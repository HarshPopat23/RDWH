# Local-model coding

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-atomic-agent](01-atomic-agent/) | [AtomicBot-ai/atomic-agent](https://github.com/AtomicBot-ai/atomic-agent) | [7899d173e0](https://github.com/AtomicBot-ai/atomic-agent/commit/7899d173e0a07665f45cf014de065eb38f405127) |
| 2 | [02-claude-code-local](02-claude-code-local/) | [nicedreamzapp/claude-code-local](https://github.com/nicedreamzapp/claude-code-local) | [440cd68936](https://github.com/nicedreamzapp/claude-code-local/commit/440cd68936fe0fc6e33d2f90307b139ba33d777e) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- local-model-coding/01-atomic-agent
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
