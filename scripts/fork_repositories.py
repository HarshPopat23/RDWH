#!/usr/bin/env python3
"""Create personal forks and point RDWH submodules at them; never push automatically."""

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True, check=True).stdout


def api(endpoint, *args):
    return json.loads(run('gh', 'api', endpoint, *args))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Create forks and update .gitmodules; otherwise print the plan.')
    parser.add_argument('--category', help='Process just one catalog category slug.')
    args = parser.parse_args()
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    categories = catalog['categories']
    if args.category:
        categories = [g for g in categories if g['slug'] == args.category]
        if not categories:
            parser.error('Unknown category slug')
    entries = [e for g in categories for e in g['repositories']]
    if not args.apply:
        for e in entries:
            print(f"{e['path']} <- fork {e['upstream']} into HarshPopat23")
        print(f'{len(entries)} forks planned. Add --apply to execute.')
        return 0
    if not shutil.which('gh') or not shutil.which('git'):
        parser.error('Install Git and GitHub CLI, then run gh auth login.')
    if api('user')['login'].lower() != 'harshpopat23':
        parser.error('Authenticate GitHub CLI as HarshPopat23 before creating these forks.')
    if run('git', 'rev-parse', '--show-toplevel').strip() != str(ROOT):
        parser.error('Run this script from a clone of RDWH.')
    changes = run('git', 'status', '--porcelain', '--untracked-files=no').splitlines()
    if any(line[3:] != '.gitmodules' for line in changes):
        parser.error('Commit or stash tracked changes other than .gitmodules before continuing.')
    report_path = ROOT / 'forks.local.json'
    report = json.loads(report_path.read_text()) if report_path.exists() else {}
    failures = []
    for index, entry in enumerate(entries, 1):
        upstream = entry['upstream']
        print(f'[{index}/{len(entries)}] {upstream}', flush=True)
        try:
            source = api(f'repos/{upstream}')
            source_root = source.get('source', source)['full_name'].lower()
            fork_name = 'rdwh-' + upstream.replace('/', '-').lower()
            # GitHub may return an existing fork in the same network, even with a different name.
            fork = api(f'repos/{upstream}/forks', '--method', 'POST', '-f', f'name={fork_name}', '-F', 'default_branch_only=false')
            fork_repo = fork['full_name']
            verified = None
            for _ in range(12):
                try:
                    info = api(f'repos/{fork_repo}')
                    if (info.get('fork') and info['owner']['login'].lower() == 'harshpopat23'
                            and info.get('source', info.get('parent', {})).get('full_name', '').lower() == source_root):
                        # Check the pinned source commit exists before changing its URL.
                        api(f"repos/{fork_repo}/commits/{entry['pinned_commit']}")
                        verified = info
                        break
                except subprocess.CalledProcessError:
                    pass
                time.sleep(5)
            if verified is None:
                raise RuntimeError(f'Fork {fork_repo} not ready or not in the expected source network; rerun later.')
            url = verified['clone_url']
            run('git', 'config', '--file', '.gitmodules', f"submodule.{entry['path']}.url", url)
            run('git', 'submodule', 'sync', '--', entry['path'])
            report[entry['path']] = {'upstream': upstream, 'fork': verified['html_url'], 'pinned_commit': entry['pinned_commit']}
            report_path.write_text(json.dumps(report, indent=2) + '\n')
            print(f"  Linked {verified['html_url']}", flush=True)
            time.sleep(2)
        except (subprocess.CalledProcessError, KeyError, RuntimeError) as exc:
            detail = exc.stderr.strip() if isinstance(exc, subprocess.CalledProcessError) else str(exc)
            failures.append(upstream)
            print(f'  Failed: {detail}', file=sys.stderr)
    print(f'Linked {len(entries) - len(failures)}/{len(entries)} selected repositories.')
    print('Review git diff -- .gitmodules, then commit and push it to retain the fork links.')
    if failures:
        print('Retry the command for: ' + ', '.join(failures), file=sys.stderr)
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
