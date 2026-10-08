# Venture OS v0.4 — Manual release and activation runbook

**Status:** READY FOR MANUAL CORE REVIEW — NOT DEPLOYED  
**Date:** 2026-10-08  
**Scope:** trusted internal, supervised Venture Discovery only. No customer-facing, trading or production actions.

## 0. Release identity and exact tested revisions

- **Venture OS:** [PR #1](https://github.com/Digitransarte/venture-os/pull/1) merged into `main`, squash commit `2bc04b71c7f108bd2ec62d0f1fa34c2ed607c5d0`.
- **Designeo Core:** [PR #30](https://github.com/Digitransarte/designeo-os/pull/30) is **not merged**, tested head `9dc564e8386766abb8ae00cc9c29d411ca2ec22d`.
- Final Core GitHub Actions [run #37776626041](https://github.com/Digitransarte/designeo-os/actions/runs/37776626041) completed **success**: unit tests, Docker build, isolated SQLite and PostgreSQL 17 E2E, using Venture OS squash commit above.
- The PR #30 merge was attempted through the connected GitHub tool but was blocked by its security check. **Do not bypass that block via a second automation path.** Review the PR and merge manually through the authorized GitHub UI if appropriate.
- Server target: Designeo Core production, `/opt/designeo-os` with Docker Compose; production deploy is controlled by the existing Builder, **not triggered by the repository CI**. This assumption must be checked against any external CD/webhooks at the time of release.
- Venture OS app registry entry exists but is inactive; no dedicated Venture runtime/website is deployed.

## Observed hold — 2026-10-08

**DO NOT DEPLOY:** Core PR #30 is still open and its merge via the connected tool was blocked by security checks. Current `main` gained three Illustration Agent/Control Surface commits since the Core PR fork. Last observed server checkout HEAD is `424b03903828cfa9a1f9843a27ed40e99b4f56ce`, not resolved by the GitHub compare endpoint. Core 0.7.2 health returned HTTP 200; no live changes were made. A verified PostgreSQL backup **and disposable restore test** have not yet been shown.

**Important rollback correction:** the restricted Builder checks out its registered branch and runs `git pull --ff-only` before rebuilding. It cannot select an older commit through the normal deployment request; do not represent redeploying `main` as rollback. Arrange an authorized rollback of application image/code, with an exact known-good reference, ahead of deployment.

See [predeploy readiness audit](PREDEPLOY_READINESS_2026-10-08.md) and [Core PR #30](https://github.com/Digitransarte/designeo-os/pull/30) review notes.

## 1. Hard prerequisites before any server rollout

1. Human reviewer examines PR #30 changes, access control, migration boundary, application impact and latest green CI against exact head. Check merge is performed from authorized GitHub UI; note merge SHA. No forced bypass.
2. Confirm current prod commit and availability of rollback revision. Inspect deployment target and automated builder configuration.
3. Obtain reliable timestamped backup of PostgreSQL **and prove that restore works in a disposable database** before updating production. Do not copy live data into GitHub Actions, user-facing chat or public artifacts.
4. Confirm time window and permission for an internal deployment; do not proceed if server connectivity/health or backup checks are incomplete.
5. Scope intended pilot to a separate internal Core project. Avoid reusing unrelated client projects.
6. Default `DESIGNEO_VENTURE_ACCESS_POLICY_JSON = []` deliberately **denies all Venture endpoints**. Do not deploy test tokens, fixture tokens or secrets in source control.
7. Review the legacy admin bearer: it is globally privileged on existing Core endpoints. The scoped Venture token model protects the new Venture routes only and is **not whole-Core multi-tenant RBAC**.

## 2. Safe release order

A. **Merge the reviewed Core PR** and verify main CI. This is a code operation only, not a deploy.

B. **Deploy Core with new Venture access policy EMPTY** via the existing authorized, reversible Builder deployment. Preserve deployment secrets and volumes; update only intended services and check health at `https://os.designeo.pt/health` plus existing API/MCP health. Confirm pre-existing Screenprint OS / DesignOS connections were not disrupted.

C. Confirm fail-closed behavior before provisioning scoped tokens: unknown/absent bearer and legacy Core admin token must be rejected at Venture endpoints; unchanged legacy Core workflows must still pass smoke tests.

D. Create the **Venture OS** Core project (`venture-os`) through authenticated admin API/MCP. Create `noetic-ink` as a separate Core project only after verifying no collision/existing project. Do not expose either to clients.

E. Provision a strong independent **service** token via secrets management; store only a SHA-256 digest of it in `DESIGNEO_VENTURE_ACCESS_POLICY_JSON`. Assign the minimum Core projects and permissions (e.g. `venture-os: read/write`, `noetic-ink: read/write` to a trusted internal service, separate identities if practical). Limit service network access. Configure and restart only necessary service(s) in controlled deployment; verify no raw secret enters logs or GitHub.

F. Perform smoke tests with a **new, harmless candidate** in the dedicated `venture-os` project. Verify `_access`, initial `rev1`, idempotency, readback, stale revision `409`, correct audit actor attribution, and `403` on cross-project scope. Confirm no launching/operating/gate approved is accepted from the candidate payload. No real customer data.

G. Migrate historical Noetic Ink candidate only after loading/verifying source memory ID `5330aff8-1b83-4360-aa63-7b5d77f75bf5`, validating rights and project context. Generate destination `rev1` with provenance, verify source remained unchanged, and link external refs. **No automatic or destructive migration.**

H. Only then exercise controlled Discovery Quick to create and read a real internal Venture Record. Keep specialist handoffs in `prepared_not_executed`. Any execution, outreach, production, payments or website publication requires a separate recorded CEO approval.

## 3. Stop / rollback criteria

Stop immediately if any of these occurs: unexpected production container restart/error; prior Core endpoint regression; authentication or project scope failure; test admin credentials accepted by Venture routes; unsupported schema; missing source record; a non-atomic writer; test writes targeting a real customer or wrong Core project; unverifiable backup/restore; any unapproved external action.

Rollback only via an explicitly documented, separately tested application-image/code recovery plan with an exact known-good reference; the existing Builder tracks the latest registered branch, **not an arbitrary historical SHA**. Do not drop or rewrite existing database tables. This release introduces no new tables, but candidate snapshots may persist if controlled smoke tests were performed; retain them for forensic audit or archive explicitly, **never delete historical memory automatically**. If Core schema is later changed independently, reassess rollback compatibility.

## 4. Post-activation sign-off

Required evidence:
- Exact production Core commit, deploy ID/time, health and rollback ref.
- Backup and restoration test evidence.
- Auth positive/negative tests for two scoped service identities and admin-token rejection on candidate endpoints.
- Venture Record rev/hash readback, audit actor, correct project and stale-write rejection.
- Successful prior workflow smoke tests for Screenprint OS, DesignOS and Project Agent.
- No customer-facing functionality and no autonomous external actions.
- Decision in Core marking the *internal-only* module active. **Venture OS must not be registered as externally available or customer-safe.**

## 5. Current checkpoint

The library is merged; Core source is not. The remote Linux device was last reported offline and the live Core API does not yet expose the candidate Venture endpoint. No production rollout or live Noetic Ink project creation was performed. This runbook is documentation, not an authorization to deploy.
