# Venture OS Workspace v0.1

A **private**, server-hosted Streamlit interface: Board, candidate Workspace,
experiments and SaaS Core dependency map. This is not a public SaaS frontend.

## Architecture

- Source of truth: Designeo OS Core records under `scope=venture-factory`.
- Reads use server-side `GET /v1/system/state?scope=venture-factory`.
- Only canonical `designeo.venture.candidate.v0.1` records are displayed.
- No second candidate database, no Core bearer exposed to browsers.
- Venture OS atomic revision API (Core PR #30) remains a **separate** integration.
- This v0.1 Core-state format is a temporary internal bridge, not the final
  Venture Record journal. A later controlled migration must preserve provenance.
- **Important:** `venture-os` is a public GitHub repo. Do not commit any Core
  token, real participant names, customer research notes or sensitive business data.

## Local demo (no Core requests)

Install Python 3.11+ and Streamlit, then:

```bash
python -m pip install -r venture_workspace/requirements.txt
export VENTURE_WORKSPACE_ADMIN_PASSWORD='use-a-long-unique-secret'
export VENTURE_WORKSPACE_DEMO=1
streamlit run venture_workspace/app.py --server.address 127.0.0.1
```

The demo displays a **synthetic** candidate. It cannot save changes.

## Private connection to existing Core

Configure these environment variables on a trusted machine, outside Git:

```text
VENTURE_WORKSPACE_ADMIN_PASSWORD=(unique internal admin password)
DESIGNEO_CORE_URL=(HTTPS URL or loopback to private Core)
DESIGNEO_CORE_API_TOKEN=(server-only Core token)
VENTURE_WORKSPACE_DEMO=0
VENTURE_WORKSPACE_ENABLE_LIVE_READ=1
```

Start the app bound to `127.0.0.1`. If a web proxy is later used, require
HTTPS, a private access boundary and explicit deployment approval. The simple
internal password is **not** tenant-level authorization or an SSO substitute.

## SaaS viability scenarios (new)

The **Viabilidade SaaS** page is a cross-candidate what-if calculator, not a
revenue tracker. It accepts user-defined, EUR-denominated, VAT-exclusive inputs
for paying accounts, price, AI call counts and input/output token sizes,
provider rates, other AI tools, storage, support, payment processing, hosting,
backups and additional fixed costs. It calculates monthly recurring revenue,
variable and fixed expenses, per-account contribution and break-even.

**Never** default provider pricing to a stale constant, misrepresent missing
cost inputs as free services, or combine USD price lists with EUR scenarios
without explicit conversion. At this stage there is no billing integration,
no recording of production usage, no automatic ROI prediction and no
commercial deployment approval. Comparisons should document evidence sources.

The Venture Factory distinguishes three product modes:
1. **Internal ChatGPT-assisted** — private/human-supervised pilot.
2. **Hybrid pilot** — independent, metered API only for high-value tasks.
3. **Public SaaS** — independently hosted operation, permissions, billing,
   support, privacy, backup and validated unit economics.

Learning OS remains an internal learning prototype until data isolation,
consent for minors, recovery and usability gates have been completed. Its
study-session and review functions should not require an AI call when a
deterministic application feature can do the job.

## Read-only safety and release boundary

- Default after login: synthetic demo if `VENTURE_WORKSPACE_DEMO=1`. Otherwise
  **fail closed** unless `VENTURE_WORKSPACE_ENABLE_LIVE_READ=1` is set.
- Live Core access is server-side and uses only `GET
  /v1/system/state?scope=venture-factory`; responses are bounded to 1 MB
  and malformed/duplicate records are rejected.
- The Core token remains **global admin** in the current deployed Core.
  Therefore enable live read only after independent review of private
  access controls; the Streamlit password alone does not create a security
  boundary suitable for Internet users.
- The entire candidate editor is **disabled**; no legacy Core state PUT
  is allowed. Core PR #30 atomic revisions are not yet in production.
- Validation claims are shown as *declared/unverified*, never converted
  automatically to proof of market demand.
- Do not put the token in a public container image, frontend code, Git,
  CI logs, or Streamlit user-visible state.
- Do not deploy, merge PR #30, or expose the Workspace to third parties
  until scoped identity, restore drills, audited configuration and explicit
  review/approval are complete.

## Verification

```bash
python -m compileall -q venture_workspace
python -m unittest discover -s tests -v
```

First candidates expected from existing Core state:
`VF-LEARNING-01` and `VF-HORTA-01`. They are read from the server, not
shipped in source or seeded again.

### Next milestones

1. Validate scoped private Core read with credentials issued for this service, then render both candidates.
2. Review UX on mobile and desktop.
3. Review/scoped-auth Core PR #30 integration and data migration contract.
4. Implement immutable experiment/evidence journals and safe edits.
5. Deploy only after backup/rollback and security checks, with human approval.
