# Venture OS Workspace v0.1

A **private**, server-hosted Streamlit interface: Board, candidate Workspace,
experiments and SaaS Core dependency map. This is not a public SaaS frontend.

## Architecture

- Source of truth: Designeo OS Core records under \`scope=venture-factory\`.
- Reads use server-side \`GET /v1/system/state?scope=venture-factory\`.
- Only canonical \`designeo.venture.candidate.v0.1\` records are displayed.
- No second candidate database, no Core bearer exposed to browsers.
- Venture OS atomic revision API (Core PR #30) remains a **separate** integration.
- This v0.1 Core-state format is a temporary internal bridge, not the final
  Venture Record journal. A later controlled migration must preserve provenance.
- **Important:** \`venture-os\` is a public GitHub repo. Do not commit any Core
  token, real participant names, customer research notes or sensitive business data.

## Local demo (no Core requests)

Install Python 3.11+ and Streamlit, then:

\`\`\`bash
python -m pip install -r venture_workspace/requirements.txt
export VENTURE_WORKSPACE_ADMIN_PASSWORD='use-a-long-unique-secret'
export VENTURE_WORKSPACE_DEMO=1
streamlit run venture_workspace/app.py --server.address 127.0.0.1
\`\`\`

The demo displays a **synthetic** candidate. It cannot save changes.

## Private connection to existing Core

Configure these environment variables on a trusted machine, outside Git:

\`\`\`text
VENTURE_WORKSPACE_ADMIN_PASSWORD=(unique internal admin password)
DESIGNEO_CORE_URL=(HTTPS URL or loopback to private Core)
DESIGNEO_CORE_API_TOKEN=(server-only Core token)
VENTURE_WORKSPACE_DEMO=0
VENTURE_WORKSPACE_ENABLE_LEGACY_WRITES=0
\`\`\`

Start the app bound to \`127.0.0.1\`. If a web proxy is later used, require
HTTPS, a private access boundary and explicit deployment approval. The simple
internal password is **not** tenant-level authorization or an SSO substitute.

## Edit safety

- Default: read-only.
- A temporary flag \`VENTURE_WORKSPACE_ENABLE_LEGACY_WRITES=1\` enables only
  text edits (problem, value proposition, next action, notes) for one trusted
  admin. Do **not** enable it on a public service.
- The current Core system state PUT has **no atomic compare-and-swap**. The UI
  checks \`updated_at\` before saving but this check is not transactional.
- Stage changes, gates, customer evidence, validation claims, business approval
  and external actions are **not editable** through this UI.
- Before multi-editor or commercial usage, use reviewed Core Venture revisions
  with CAS, project-scoped identity, an audit trail, backups and tested rollback.
- No merge/deployment of Core PR #30 is part of this change.

## Verification

\`\`\`bash
python -m compileall -q venture_workspace
python -m unittest discover -s tests -v
\`\`\`

First candidates expected from existing Core state:
\`VF-LEARNING-01\` and \`VF-HORTA-01\`. They are read from the server, not
shipped in source or seeded again.

### Next milestones

1. Confirm private Core read connectivity and render both candidates.
2. Review UX on mobile and desktop.
3. Review/scoped-auth Core PR #30 integration and data migration contract.
4. Implement immutable experiment/evidence journals and safe edits.
5. Deploy only after backup/rollback and security checks, with human approval.
