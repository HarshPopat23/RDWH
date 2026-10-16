# Agent governance

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-bernstein](01-bernstein/) | [sipyourdrink-ltd/bernstein](https://github.com/sipyourdrink-ltd/bernstein) | [88c9857dee](https://github.com/sipyourdrink-ltd/bernstein/commit/88c9857deeba255d25a34f6a9a9081e2fa508aad) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- agent-governance/01-bernstein
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
