# Agent monitoring

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-ctop](01-ctop/) | [aakashadesara/ctop](https://github.com/aakashadesara/ctop) | [6e2265182f](https://github.com/aakashadesara/ctop/commit/6e2265182f9ec06ae35c73d4c10dfb773b21da39) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- agent-monitoring/01-ctop
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
