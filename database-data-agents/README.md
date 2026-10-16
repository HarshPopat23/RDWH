# Database and data agents

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-db-gpt](01-db-gpt/) | [eosphoros-ai/DB-GPT](https://github.com/eosphoros-ai/DB-GPT) | [361eb34476](https://github.com/eosphoros-ai/DB-GPT/commit/361eb34476970ae4dba6d33454a45669ec6851bb) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- database-data-agents/01-db-gpt
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
