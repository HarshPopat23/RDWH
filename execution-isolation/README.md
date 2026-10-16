# Execution isolation

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-greywall](01-greywall/) | [GreyhavenHQ/greywall](https://github.com/GreyhavenHQ/greywall) | [60ab1b5bfd](https://github.com/GreyhavenHQ/greywall/commit/60ab1b5bfd41c1683220435a85fc116dc29fd04f) |
| 2 | [02-agentrun](02-agentrun/) | [tjmlabs/AgentRun](https://github.com/tjmlabs/AgentRun) | [1997dd71d5](https://github.com/tjmlabs/AgentRun/commit/1997dd71d5350dd1e0c993cdd7060b3b9b765a8d) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- execution-isolation/01-greywall
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
