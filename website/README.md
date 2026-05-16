# Nebuless.AGR

Static landing page for the Nebuless.AGR MCP Guard scanner-backed assessment product.

## Positioning

Nebuless.AGR is centered on MCP Guard: repository intake, MCP server detection, static analysis, dynamic testing, dependency checks, MCP protocol validation, CVSS v4.0, AIVSS, and CI-ready evidence outputs.

Nebuless.AGR is not the Nebuless.PRX product. PRX positioning, proxy/routing videos, and runtime proxy language should not drive this site.

## Launch offer

A fixed-scope $2,000, one-business-day MCP Guard Security Audit:

- Scan target MCP server repositories
- Flag command injection, path traversal, auth gaps, exposed secrets, vulnerable dependencies, and protocol issues
- Score findings with CVSS v4.0 and AIVSS
- Deliver JSON, SARIF, JUnit, executive summary, and remediation priorities
- Convert critical findings into CI pass or fail criteria

## Product path

- Week 1: paid MCP Guard audits and evidence reports
- Week 2: CI security gates from scanner output
- Month 1: richer reporting, owner assignment, and remediation workflow
- Month 2: scanner-backed registry exports for approved MCP servers

## Local development

```bash
npm run dev
```

The site serves on port 4173.
