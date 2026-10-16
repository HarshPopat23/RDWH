# Autonomous development / issue fixing

Lower rank numbers come first in the supplied project order. Rankings are provisional and apply only within this category.

| Rank | Ranked source directory | Upstream repository | Pinned commit |
| ---: | --- | --- | --- |
| 1 | [01-swe-agent](01-swe-agent/) | [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | [3ea751c087](https://github.com/SWE-agent/SWE-agent/commit/3ea751c087f32b16e039a2233dd6eefecef325d5) |
| 2 | [02-openbitfun](02-openbitfun/) | [GCWing/OpenBitFun](https://github.com/GCWing/OpenBitFun) | [8211dd1c4c](https://github.com/GCWing/OpenBitFun/commit/8211dd1c4c9c22c1111c92c51c4e89c52d633f26) |
| 3 | [03-gpt-pilot](03-gpt-pilot/) | [Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) | [9b763fdaf0](https://github.com/Pythagora-io/gpt-pilot/commit/9b763fdaf0020c7d8abacc7b58b2b09e57494623) |
| 4 | [04-codel](04-codel/) | [semanser/codel](https://github.com/semanser/codel) | [fe1e846c9e](https://github.com/semanser/codel/commit/fe1e846c9e04f41209498ed0d88e92b15dcdfad2) |
| 5 | [05-devika](05-devika/) | [stitionai/devika](https://github.com/stitionai/devika) | [80bb343cbe](https://github.com/stitionai/devika/commit/80bb343cbe4a4e5f5a0ba08d2524920139baceb6) |
| 6 | [06-pycodeagi](06-pycodeagi/) | [chakkaradeep/pyCodeAGI](https://github.com/chakkaradeep/pyCodeAGI) | [13e02cf25f](https://github.com/chakkaradeep/pyCodeAGI/commit/13e02cf25fa64287531cb774e3cc74f53b6f79d0) |

## Get the source locally

From the RDWH root:

```bash
git submodule update --init -- autonomous-development-issue-fixing/01-swe-agent
```

Each ranked directory is a Git submodule. GitHub opens its pinned upstream source; a local submodule checkout contains the actual source tree. Initialize other entries by substituting their ranked path.

Submodules initially reference upstream repositories. Use the root [fork helper](../scripts/fork_repositories.py) to create personal forks and switch their URLs. The active source URL is recorded in [`.gitmodules`](../.gitmodules).

Each upstream retains its own license and notices; consult them before reusing code.
