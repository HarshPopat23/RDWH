# Coordinated coding and verification

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-zeroshot](01-zeroshot/) | [the-open-engine/zeroshot](https://github.com/the-open-engine/zeroshot) | [b62ee8afdd](https://github.com/the-open-engine/zeroshot/commit/b62ee8afdddcd3f48efe263d37f2688beeee6169) |
| 2 | [02-h5i](02-h5i/) | [h5i-dev/h5i](https://github.com/h5i-dev/h5i) | [5d03fc82d9](https://github.com/h5i-dev/h5i/commit/5d03fc82d9cbbf6a748b31a9797323c2bd7193d5) |
| 3 | [03-maestro-orchestrate](03-maestro-orchestrate/) | [josstei/maestro-orchestrate](https://github.com/josstei/maestro-orchestrate) | [e74aaad7bc](https://github.com/josstei/maestro-orchestrate/commit/e74aaad7bc6edc00d97b887bb9347a815c9c1058) |
| 4 | [04-orbi](04-orbi/) | [orbi-build/orbi](https://github.com/orbi-build/orbi) | [ce0d7dc09d](https://github.com/orbi-build/orbi/commit/ce0d7dc09d7c9c3511a4b05fa87b11e223aeb5dd) |
| 5 | [05-ouroboros-agent-os](05-ouroboros-agent-os/) | [Q00/ouroboros](https://github.com/Q00/ouroboros) | [26eaddacb9](https://github.com/Q00/ouroboros/commit/26eaddacb93ea79293193d09bc36485050cab7d1) |
| 6 | [06-ordewell](06-ordewell/) | [ordewell/ordewell](https://github.com/ordewell/ordewell) | [37b169b456](https://github.com/ordewell/ordewell/commit/37b169b4568ac047821ca57b14a5b22bf4030b8e) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- coordinated-coding-verification/01-zeroshot
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
