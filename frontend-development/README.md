# Frontend development

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-frontman](01-frontman/) | [frontman-ai/frontman](https://github.com/frontman-ai/frontman) | [0bfca4ed2e](https://github.com/frontman-ai/frontman/commit/0bfca4ed2e7cc8bcf7e3bb87e51b277322d000a8) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- frontend-development/01-frontman
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
