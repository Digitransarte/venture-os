# Designeo Core / Venture OS — reconciliation checkpoint, 2026-10-10

**Scope:** source-code review only. **No deploy, no PR merge and no operational Venture activation.**

## Verified code references

- **Production-server local Core `main` snapshot:** `b81916e365a48a22ef069452398ed24cc18c2084`.
- **Published Core GitHub `main` at inspection:** `5b55fad6a2ce464971b2152178f703eb37f275ca`; the server had **45 additional local commits**. The source server received concurrent Control Board/Illustration updates over the preceding days. Do not overwrite them or assume remote `main` contains all deployed changes.
- **Core Venture PR:** [#30](https://github.com/Digitransarte/designeo-os/pull/30), updated review head `6c1239f2a5e2454aba1eac99ad7d87ee62645925`, **not merged**.
- **Venture OS:** [PR #1](https://github.com/Digitransarte/venture-os/pull/1) already merged into its own `main`.
- **CI for Core PR after gate hardening:** [run #38051738205](https://github.com/Digitransarte/designeo-os/actions/runs/38051738205), **success** (Python suite, Docker image, SQLite HTTP E2E, PostgreSQL concurrency test). This CI tests the PR checkout, **not the unpublished server changes after conflict resolution**.

## Safety checkpoint of local source history

A Git bundle for the observed server `main` was created on the server and successfully passed `git bundle verify`. It is stored in `/root/designeo-core-secure-backups/core_main_pre_venture_b81916e365a4.bundle` (root, mode 600; **329,036 bytes**; SHA-256 `ad867faf46045b854d3dbd362289a704a98731f5218080e82bbf86a606580700`).

This preserves the committed source for review even if the current server branch advances. It is **not an offsite backup** and it contains Git source history, **not database rows or uncommitted work**. It should not be copied into a public repository.

## Merge-tree review

Using an isolated Git clone under `/tmp/venture-core-review-20261010` and **read-only** `git merge-tree --write-tree`, the server checkpoint and PR head yielded merge-tree `20a5e649ab2dadb12f9df3f7e0f610f9fddd8711`.

Two conflicting source files were identified:

1. `app/main.py`: import and register both the existing `agents` router and new `venture_records` router.
2. `tests/test_mcp_discovery.py`: retain the existing Project Agent MCP tool names and add `create_project`.

`app/config.py` and `app/mcp_server.py` were auto-combined by Git but still need human semantic review.

An **untracked, non-Git preview** was prepared under `/tmp/venture-core-reconciled-preview-20261010`. Only the two conflict hunks were resolved. `python3 -m compileall` for `app/` and `tests/` passed; static checks confirmed required routes, MCP methods and gate controls, with **61 Python files parseable**. This is **not a deployed or tested integration build**.

For exact reproduction, a 1,631-byte patch with SHA-256 `6da868ef911bb3587194f88ebd93368fead653f3ef7f71451641d25e1afdbf63` and a manifest are stored **only on the server** under `/root/designeo-core-secure-backups/venture_pr30_conflict_resolutions_b81916e_6c1239f.patch` and `venture_pr30_review_manifest_b81916e_6c1239f.json`. These patch the conflict-marked preview, **not arbitrary `main` files**.

## Gate validation improvements submitted to Core PR #30

The candidate Venture API now uses allowlisted *non-authorizing* gate/experiment statuses and rejects a forged CEO decision/action reference, arbitrary approval aliases, claims of independently validated market evidence from a mere source string, and claimed validated revenue/profit numbers. Regression tests cover these cases. Approval and economic verification require a separate authenticated process.

## Release constraints

- The previous GitHub PR merge attempt was **blocked by tool security checks**. Do **not** bypass it via another programmatic route. Core PR #30 requires authorized manual review and integration through GitHub's approved path.
- No reconciled-runtime tests were performed: the earlier local container TestClient command was blocked by tool security and **was not retried by an alternate route**. After the private commits are reviewed, a human-authorized branch should run CI against the complete reconciled tree.
- The PostgreSQL snapshot/restore test on 2026-10-08 passed on the server, but **encrypted off-host backup and an application rollback independent of Builder's branch pull have not been verified**. These remain release blockers.
- The Venture OS app remains inactive; no new live `noetic-ink` Project, migration, agent execution or commercial actions occurred.

**Next human gate:** review and publish the local Core history through the team's normal source-control process, approve a reconciled integration candidate, run tests on that actual candidate, then consider manual Core PR merge and a separate reversible internal release.
