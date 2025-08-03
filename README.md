# MCP Guard - Professional Security Scanner

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Security Scanner](https://img.shields.io/badge/Security-Scanner-red.svg)](https://github.com)
[![CVSS v4.0](https://img.shields.io/badge/CVSS-v4.0-green.svg)](https://www.first.org/cvss/)
[![AIVSS](https://img.shields.io/badge/AIVSS-Enabled-purple.svg)](https://github.com)

**MCP Guard** is the first comprehensive security scanner specifically designed for Model Context Protocol (MCP) servers. It performs both static and dynamic analysis to identify vulnerabilities in MCP implementations across multiple programming languages.

## 🚀 Features

- **🔍 Universal MCP Server Support**: Python, Node.js, Go, Docker-based servers
- **⚡ Comprehensive Analysis**: Static code analysis + Dynamic fuzzing
- **📊 Professional Scoring**: CVSS v4.0 and AIVSS (AI Vulnerability Scoring System)
- **🎯 MCP-Specific Vulnerabilities**: Detects protocol-specific security issues
- **🌐 No Authentication Required**: Downloads public repositories via HTTP
- **📋 Detailed Reports**: JSON output with complete vulnerability details
- **🔧 CI/CD Ready**: GitHub Actions integration included

## 🛡️ Supported MCP Servers

- **GitHub MCP Server** (Go) - `github.com/github/github-mcp-server`
- **Cloudflare MCP Server** (Node.js) - `github.com/cloudflare/mcp-server-cloudflare`
- **PostgreSQL MCP Server** (Python) - `github.com/crystaldba/postgres-mcp`
- **Docker MCP Server** (Go) - `github.com/docker/mcp-server`
- **Playwright MCP Server** (Node.js) - `github.com/microsoft/playwright-mcp`
- **Airbnb MCP Server** (Node.js) - `github.com/openbnb-org/mcp-server-airbnb`
- **Any public MCP server repository**

## 📦 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/mcp-guard.git
cd mcp-guard

# Install dependencies
pip install -r requirements.txt

# Verify installation
python mcp_scanner.py --help
```

### Basic Usage

```bash
# Scan any MCP server
python mcp_scanner.py <github_repo_url>

# Examples
python mcp_scanner.py https://github.com/github/github-mcp-server
python mcp_scanner.py https://github.com/openbnb-org/mcp-server-airbnb
python mcp_scanner.py https://github.com/cloudflare/mcp-server-cloudflare
```

## 📊 Sample Output

```
================================================================================
MCP GUARD SECURITY ASSESSMENT REPORT
================================================================================
Target: https://github.com/openbnb-org/mcp-server-airbnb
Scan Type: COMPREHENSIVE (STATIC + DYNAMIC)
Timestamp: 2025-08-01 23:36:50 UTC

--------------------------------------------------------------------------------
VULNERABILITY SUMMARY
--------------------------------------------------------------------------------
Total Vulnerabilities: 5
Overall Risk: MEDIUM
Business Impact: MODERATE

Severity Distribution:
  CRITICAL: 1
  HIGH: 2
  MEDIUM: 2

CVSS v4.0 METRICS
Highest CVSS Score: 8.5
Average CVSS Score: 6.2

AIVSS (AI VULNERABILITY SCORING SYSTEM) METRICS
AI-Specific Vulnerabilities: 5
Highest AIVSS Score: 7.2

MCP-SPECIFIC VULNERABILITY ANALYSIS
MCP Vulnerability Types Found:
  Command Injection: 1
  Path Traversal: 1
  Authorization Bypass: 1
  Information Disclosure: 1
```

## 🔧 Key Capabilities

### Static Analysis Engine
- **Pattern-based Detection**: Identifies dangerous code patterns
- **Dependency Scanning**: Checks for vulnerable dependencies (npm audit, pip-audit, gosec)
- **Configuration Analysis**: Reviews security configurations
- **MCP Protocol Validation**: Ensures proper MCP implementation
- **Hardcoded Secrets Detection**: Finds API keys, tokens, credentials

### Dynamic Analysis Engine
- **Live Server Testing**: Actually starts and tests MCP servers
- **Protocol Fuzzing**: Sends malicious JSON-RPC payloads
- **Input Validation Testing**: Tests parameter sanitization
- **Resource Exhaustion Testing**: DoS vulnerability detection
- **Authentication Bypass Testing**: Access control validation

### Vulnerability Types Detected
- **Command Injection** (CWE-78): Unsafe system command execution
- **Path Traversal** (CWE-22): Unauthorized file access
- **SQL Injection** (CWE-89): Database manipulation vulnerabilities
- **Code Injection** (CWE-94): Dynamic code execution risks
- **Authentication Bypass** (CWE-306): Missing access controls
- **Information Disclosure** (CWE-200): Sensitive data exposure
- **MCP Protocol Issues**: Protocol-specific vulnerabilities
- **Hardcoded Credentials** (CWE-798): Embedded secrets

## 📋 Professional Reporting

### Console Output
- Real-time scan progress
- Professional vulnerability summary
- Risk assessment with business impact
- CVSS v4.0 and AIVSS scoring
- Remediation recommendations

### JSON Reports
Detailed machine-readable reports saved as:
```
mcp_security_scan_[server-name]_[timestamp].json
```

Contains:
- Complete vulnerability details with line numbers
- Professional CVSS v4.0 and AIVSS scores
- Exploit payloads and proof-of-concept code
- Comprehensive remediation guidance
- Server metadata and scan configuration

## 🧪 Testing & Validation

```bash
# Run the test suite
python test_mcp_scanner.py

# Test download functionality
python test_download.py

# Test with dynamic fuzzing
python mcp_scanner.py --test-dynamic
```

## 🏗️ Architecture

```
MCP Guard Architecture
├── Static Analysis Engine
│   ├── Language-specific analyzers (Python, Node.js, Go)
│   ├── Dependency vulnerability scanning
│   ├── Pattern-based vulnerability detection
│   └── MCP protocol compliance checking
├── Dynamic Analysis Engine
│   ├── Live server startup and testing
│   ├── JSON-RPC protocol fuzzing
│   ├── Input validation testing
│   └── Resource exhaustion testing
├── Professional Scoring System
│   ├── CVSS v4.0 implementation
│   ├── AIVSS (AI Vulnerability Scoring)
│   └── Risk assessment engine
└── Reporting Engine
    ├── Console output formatting
    ├── JSON report generation
    └── Remediation recommendations
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
```bash
git clone https://github.com/your-username/mcp-guard.git
cd mcp-guard
pip install -r requirements.txt
python test_mcp_scanner.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔒 Security

If you discover a security vulnerability, please send an email to security@mcpguard.com. All security vulnerabilities will be promptly addressed.

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/mcp-guard/issues)
- **Documentation**: See the [docs/](docs/) folder
- **Discussions**: [GitHub Discussions](https://github.com/your-username/mcp-guard/discussions)

## 🏆 Recognition

MCP Guard is the **first open-source security scanner** specifically designed for Model Context Protocol servers, featuring:

- ✅ **Industry-standard CVSS v4.0 scoring**
- ✅ **Novel AIVSS (AI Vulnerability Scoring System)**
- ✅ **Comprehensive MCP protocol security testing**
- ✅ **Real vulnerability detection in production MCP servers**
- ✅ **Professional-grade reporting and remediation guidance**

## 📚 Research & Publications

This tool has been developed for academic research and is suitable for:
- Security research papers
- MCP protocol security analysis
- AI system security assessment
- Vulnerability disclosure programs

---

**Made with ❤️ for the MCP security community**

*Securing the future of AI agent communication protocols*