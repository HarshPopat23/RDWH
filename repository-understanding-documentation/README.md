# Repository understanding / documentation

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-repoagent](01-repoagent/) | [OpenBMB/RepoAgent](https://github.com/OpenBMB/RepoAgent) | [825d988127](https://github.com/OpenBMB/RepoAgent/commit/825d988127d7bfd757237d9c4e8678d9104030f0) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- repository-understanding-documentation/01-repoagent
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
