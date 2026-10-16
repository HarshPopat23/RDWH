# RDWH

A ranked source workspace for 56 agent projects across 16 categories, supporting research toward a combined-agent system.

## Ranking

The numeric prefix is the rank **within its category**: `01` is first. The order preserves the supplied project shortlist; it is provisional and is not a benchmark or a universal quality score. A single-entry category has rank `01`.

## Categories

| Category | Projects | First-ranked entry |
| --- | ---: | --- |
| [Core agent platforms / orchestration](core-agent-platforms-orchestration/) | 10 | Paperclip |
| [Managing multiple coding agents](managing-multiple-coding-agents/) | 9 | Maestro |
| [General coding assistants](general-coding-assistants/) | 10 | OpenCode |
| [Autonomous development / issue fixing](autonomous-development-issue-fixing/) | 6 | SWE Agent |
| [Coordinated coding and verification](coordinated-coding-verification/) | 6 | zeroshot |
| [Code review](code-review/) | 2 | OpenCodeReview |
| [Execution isolation](execution-isolation/) | 2 | Greywall |
| [Local-model coding](local-model-coding/) | 2 | Atomic Agent |
| [Infrastructure operations](infrastructure-operations/) | 2 | Stakpak |
| [Repository understanding / documentation](repository-understanding-documentation/) | 1 | RepoAgent |
| [Database and data agents](database-data-agents/) | 1 | DB GPT |
| [Computer-vision development](computer-vision-development/) | 1 | Vision agent |
| [Frontend development](frontend-development/) | 1 | Frontman |
| [LLM workflow optimization](llm-workflow-optimization/) | 1 | DSPy |
| [Agent governance](agent-governance/) | 1 | Bernstein |
| [Agent monitoring](agent-monitoring/) | 1 | ctop |

## Source layout

For example: `core-agent-platforms-orchestration/01-paperclip` and `general-coding-assistants/01-opencode`.

The 56 ranked entries are real Git submodules pinned to verified source commits. They initially reference upstream repositories. **Personal GitHub forks have not been created by this change.** Forks are independent repositories under a GitHub account; they cannot live inside another repository folder.

[catalog.json](catalog.json) records each project, rank, source URL, default branch, and pinned commit. [`.gitmodules`](.gitmodules) records the active clone URLs.

## Clone and load selected source trees

```bash
git clone https://github.com/HarshPopat23/RDWH.git
cd RDWH
git submodule update --init -- core-agent-platforms-orchestration/01-paperclip
```

To download all 56 source trees, use `git submodule update --init --jobs 4`. This only downloads source; it does not install dependencies or run agents. Nested upstream submodules can be initialized separately when a selected project requires them.

## Create personal forks and switch the links

Requires Python 3, Git, GitHub CLI, and a GitHub login that can create repositories. Run as HarshPopat23:

```bash
gh auth login
python3 scripts/fork_repositories.py --apply
```

The helper creates or reuses forks in the matching upstream fork network, verifies that each pinned commit is available, and changes the corresponding `.gitmodules` URL. New fork names use `rdwh-<upstream-owner>-<repository>` to avoid collisions. Existing forks may retain their existing names. A local ignored `forks.local.json` records successful fork links. The helper does not clone or execute project code and never commits or pushes automatically.

Without `--apply`, the helper prints its plan without network calls or changes. To process one category, append `--category general-coding-assistants`. Partial failures are reported, successful changes are retained, and the command can be rerun.

After successful fork setup:

```bash
git diff -- .gitmodules
git add .gitmodules
git commit -m "Point ranked submodules to personal forks"
git push
```

## Scope and licensing

This is a categorized source workspace, not an integrated agent runtime. Each project has separate setup, model, hardware, and API requirements. Upstream licenses and notices remain in their source repositories and apply independently.
