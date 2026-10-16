# Code review

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-opencodereview](01-opencodereview/) | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | [8eb83340a4](https://github.com/alibaba/open-code-review/commit/8eb83340a487b1150af00701b94f01af97e4b4d6) |
| 2 | [02-reviewcerberus](02-reviewcerberus/) | [Kirill89/reviewcerberus](https://github.com/Kirill89/reviewcerberus) | [0bfd89f8d1](https://github.com/Kirill89/reviewcerberus/commit/0bfd89f8d1c18295154b42aa533da55bc02edc7b) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- code-review/01-opencodereview
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
