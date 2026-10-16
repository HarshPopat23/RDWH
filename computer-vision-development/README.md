# Computer-vision development

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-vision-agent](01-vision-agent/) | [landing-ai/vision-agent](https://github.com/landing-ai/vision-agent) | [545651c889](https://github.com/landing-ai/vision-agent/commit/545651c8899a81f49fbfa2fac797111e5f0a6be3) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- computer-vision-development/01-vision-agent
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
