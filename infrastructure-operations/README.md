# Infrastructure operations

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-stakpak](01-stakpak/) | [stakpak/agent](https://github.com/stakpak/agent) | [760cd2b598](https://github.com/stakpak/agent/commit/760cd2b5984d29c2d513bb15ca33e995fae45f17) |
| 2 | [02-kubestellar-console](02-kubestellar-console/) | [kubestellar/console](https://github.com/kubestellar/console) | [f1a86ff9ec](https://github.com/kubestellar/console/commit/f1a86ff9ec0fa56d98bd53d9c1b70cb764e10cf4) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- infrastructure-operations/01-stakpak
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
