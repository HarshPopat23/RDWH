# LLM workflow optimization

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-dspy](01-dspy/) | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | [8698747677](https://github.com/stanfordnlp/dspy/commit/869874767729866f96f77e757a685ee72fb663a5) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- llm-workflow-optimization/01-dspy
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
