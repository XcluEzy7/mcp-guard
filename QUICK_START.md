# MCP Guard - Quick Start Guide

## 🚀 Get Started in 3 Minutes

### Step 1: Download MCP Guard
```bash
git clone https://github.com/your-username/mcp-guard.git
cd mcp-guard
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run Your First Scan
```bash
python mcp_scanner.py https://github.com/openbnb-org/mcp-server-airbnb
```

That's it! 🎉

## What You'll See

```
================================================================================
MCP GUARD SECURITY ASSESSMENT REPORT
================================================================================
Target: https://github.com/openbnb-org/mcp-server-airbnb
Total Vulnerabilities: 5
Overall Risk: MEDIUM

CRITICAL SEVERITY (1 findings):
  [1] Command Injection Vulnerability
      CVSS Score: 8.5
      File: src/server.js
      Line: 45
```

## Try More Examples

```bash
# Scan different MCP servers
python mcp_scanner.py https://github.com/cloudflare/mcp-server-cloudflare
python mcp_scanner.py https://github.com/github/github-mcp-server

# Run interactive examples
python examples/basic_scan.py
```

## Need Help?

- **Problems?** Check [INSTALLATION.md](docs/INSTALLATION.md)
- **More features?** See [USAGE.md](docs/USAGE.md)
- **Examples?** Look at [EXAMPLES.md](docs/EXAMPLES.md)

## Requirements

- Python 3.8 or higher
- Internet connection
- That's it!

---

**Ready to secure your MCP servers!** 🛡️