# API Documentation

## 🔧 Core Classes and Functions

### MCPScanner Class

The main scanner class that orchestrates security analysis.

```python
class MCPScanner:
    """
    Main MCP security scanner class.
    
    Provides comprehensive security analysis for MCP servers including
    static analysis, dynamic analysis, and vulnerability reporting.
    """
    
    def __init__(self):
        """Initialize the MCP scanner with default configuration."""
        
    def scan_repository(self, repo_url: str) -> Dict[str, Any]:
        """
        Scan an MCP server repository for security vulnerabilities.
        
        Args:
            repo_url (str): GitHub repository URL to scan
            
        Returns:
            Dict[str, Any]: Comprehensive security report
            
        Raises:
            ValueError: If repository URL is invalid
            ConnectionError: If repository cannot be accessed
        """
```

#### Methods

##### `scan_repository(repo_url: str) -> Dict[str, Any]`

Performs comprehensive security analysis of an MCP server repository.

**Parameters:**
- `repo_url` (str): GitHub repository URL (e.g., "https://github.com/user/repo")

**Returns:**
- Dictionary containing complete security analysis results

**Example:**
```python
scanner = MCPScanner()
results = scanner.scan_repository("https://github.com/openbnb-org/mcp-server-airbnb")
print(f"Found {results['summary']['total']} vulnerabilities")
```

##### `static_analysis(repo_path: str) -> List[Dict[str, Any]]`

Performs static code analysis without executing the server.

**Parameters:**
- `repo_path` (str): Local path to repository

**Returns:**
- List of vulnerability dictionaries

##### `dynamic_analysis(repo_path: str, server_info: Dict) -> List[Dict[str, Any]]`

Performs dynamic analysis by running and testing the server.

**Parameters:**
- `repo_path` (str): Local path to repository
- `server_info` (Dict): Server configuration information

**Returns:**
- List of vulnerability dictionaries

### RepositoryHandler Class

Handles downloading and managing MCP server repositories.

```python
class RepositoryHandler:
    """
    Handles repository operations for MCP server analysis.
    
    Provides secure downloading, extraction, and cleanup of repositories
    for security analysis.
    """
    
    def download_repository(self, repo_url: str) -> str:
        """
        Download and extract a repository for analysis.
        
        Args:
            repo_url (str): GitHub repository URL
            
        Returns:
            str: Path to extracted repository
            
        Raises:
            ValueError: If URL is invalid
            ConnectionError: If download fails
        """
```

#### Methods

##### `download_repository(repo_url: str) -> str`

Downloads a GitHub repository for analysis.

**Parameters:**
- `repo_url` (str): GitHub repository URL

**Returns:**
- String path to downloaded repository

**Example:**
```python
handler = RepositoryHandler()
repo_path = handler.download_repository("https://github.com/user/repo")
print(f"Repository downloaded to: {repo_path}")
```

##### `cleanup_repository(repo_path: str) -> None`

Cleans up downloaded repository files.

**Parameters:**
- `repo_path` (str): Path to repository to clean up

### VulnerabilityScorer Class

Implements CVSS v4.0 and AIVSS scoring systems.

```python
class VulnerabilityScorer:
    """
    Implements vulnerability scoring systems for security assessment.
    
    Supports CVSS v4.0 and AIVSS (AI Vulnerability Scoring System)
    for comprehensive risk assessment.
    """
    
    def calculate_cvss_score(self, vulnerability: Dict[str, Any]) -> float:
        """
        Calculate CVSS v4.0 score for a vulnerability.
        
        Args:
            vulnerability (Dict): Vulnerability information
            
        Returns:
            float: CVSS score (0.0-10.0)
        """
        
    def calculate_aivss_score(self, vulnerability: Dict[str, Any]) -> float:
        """
        Calculate AIVSS score for AI-related vulnerabilities.
        
        Args:
            vulnerability (Dict): Vulnerability information
            
        Returns:
            float: AIVSS score (0.0-10.0)
        """
```

## 📊 Data Structures

### Vulnerability Dictionary

Standard structure for representing security vulnerabilities:

```python
vulnerability = {
    "id": "static-1722558410-1234",
    "type": "static",  # "static" or "dynamic"
    "severity": "high",  # "critical", "high", "medium", "low"
    "title": "Command Injection Vulnerability",
    "description": "Detailed description of the vulnerability...",
    "cwe_id": "CWE-78",
    "file_path": "src/server.js",
    "line_number": 45,
    "cvss_score": 8.5,
    "cvss_vector": "CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H",
    "cvss_severity": "HIGH",
    "aivss_score": 7.2,
    "aivss_vector": "AIVSS:1.0/AI:H/MI:P/DP:M/PI:H/TD:L/MT:L",
    "aivss_severity": "AI_HIGH",
    "remediation": "Use parameterized commands and validate all inputs...",
    "confidence": "high",  # "high", "medium", "low"
    "exploit_payload": "Optional payload used to discover vulnerability",
    "references": ["https://cwe.mitre.org/data/definitions/78.html"]
}
```

### Server Information Dictionary

Structure for MCP server metadata:

```python
server_info = {
    "repo_url": "https://github.com/user/repo",
    "server_type": "nodejs",  # "python", "nodejs", "go", "docker"
    "name": "example-mcp-server",
    "package_manager": "npm",  # "npm", "pip", "go", "docker"
    "transport_type": "stdio",  # "stdio", "http", "websocket"
    "main_file": "src/index.js",
    "dependencies": ["express", "body-parser"],
    "mcp_version": "1.0.0"
}
```

### Scan Results Dictionary

Complete structure for scan results:

```python
scan_results = {
    "server_info": server_info,
    "scan_timestamp": "2025-08-01T23:36:50.123456",
    "scan_type": "both",  # "static", "dynamic", "both"
    "vulnerabilities": [vulnerability, ...],
    "summary": {
        "total": 5,
        "by_severity": {
            "critical": 1,
            "high": 2,
            "medium": 2,
            "low": 0
        },
        "by_type": {
            "static": 2,
            "dynamic": 3
        },
        "cvss_v4.0_metrics": {
            "highest_score": 8.5,
            "average_score": 6.2,
            "distribution": {
                "critical": 1,
                "high": 2,
                "medium": 2
            }
        },
        "aivss_metrics": {
            "highest_score": 7.2,
            "average_score": 5.8,
            "ai_specific_count": 5,
            "distribution": {
                "ai_critical": 0,
                "ai_high": 2,
                "ai_medium": 3
            }
        }
    },
    "recommendations": [
        "Implement input validation for all MCP tool parameters",
        "Use environment variables for sensitive configuration"
    ],
    "metadata": {
        "scan_duration": 45.2,
        "files_analyzed": 15,
        "lines_of_code": 1250,
        "analysis_engines": ["static", "dynamic", "dependency"]
    }
}
```

## 🔍 Analysis Engines

### Static Analysis Engine

Analyzes source code without execution:

```python
class StaticAnalysisEngine:
    """Static code analysis engine for MCP servers."""
    
    def analyze_patterns(self, file_path: str) -> List[Dict]:
        """Analyze code patterns for vulnerabilities."""
        
    def scan_dependencies(self, package_file: str) -> List[Dict]:
        """Scan dependencies for known vulnerabilities."""
        
    def detect_secrets(self, content: str) -> List[Dict]:
        """Detect hardcoded secrets and credentials."""
        
    def validate_mcp_protocol(self, file_path: str) -> List[Dict]:
        """Validate MCP protocol implementation."""
```

### Dynamic Analysis Engine

Tests running MCP servers:

```python
class DynamicAnalysisEngine:
    """Dynamic analysis engine for live MCP server testing."""
    
    def start_server(self, server_path: str, server_info: Dict) -> bool:
        """Start MCP server for testing."""
        
    def fuzz_json_rpc(self, server_process) -> List[Dict]:
        """Perform JSON-RPC protocol fuzzing."""
        
    def test_input_validation(self, server_process) -> List[Dict]:
        """Test input validation and sanitization."""
        
    def test_authentication(self, server_process) -> List[Dict]:
        """Test authentication and authorization."""
        
    def test_resource_limits(self, server_process) -> List[Dict]:
        """Test for resource exhaustion vulnerabilities."""
```

## 🛠️ Utility Functions

### Scoring Functions

```python
def calculate_overall_risk(vulnerabilities: List[Dict]) -> str:
    """
    Calculate overall risk level based on vulnerabilities.
    
    Args:
        vulnerabilities: List of vulnerability dictionaries
        
    Returns:
        str: Risk level ("CRITICAL", "HIGH", "MEDIUM", "LOW")
    """

def get_business_impact(vulnerabilities: List[Dict]) -> str:
    """
    Assess business impact of vulnerabilities.
    
    Args:
        vulnerabilities: List of vulnerability dictionaries
        
    Returns:
        str: Impact level ("SEVERE", "MODERATE", "MINOR", "MINIMAL")
    """
```

### Report Generation

```python
def generate_console_report(scan_results: Dict) -> str:
    """
    Generate formatted console report.
    
    Args:
        scan_results: Complete scan results dictionary
        
    Returns:
        str: Formatted console report
    """

def generate_json_report(scan_results: Dict, output_file: str) -> None:
    """
    Generate JSON report file.
    
    Args:
        scan_results: Complete scan results dictionary
        output_file: Path to output JSON file
    """
```

### Validation Functions

```python
def validate_github_url(url: str) -> bool:
    """
    Validate GitHub repository URL.
    
    Args:
        url: Repository URL to validate
        
    Returns:
        bool: True if valid GitHub URL
    """

def detect_server_type(repo_path: str) -> str:
    """
    Detect MCP server type from repository.
    
    Args:
        repo_path: Path to repository
        
    Returns:
        str: Server type ("python", "nodejs", "go", "docker")
    """
```

## 🔧 Configuration

### Environment Variables

```python
# Configuration environment variables
MCP_GUARD_MAX_TIME = 300  # Maximum analysis time in seconds
MCP_GUARD_MAX_MEMORY = 1073741824  # Maximum memory usage in bytes
MCP_GUARD_TEMP_DIR = "/tmp/mcp-guard"  # Temporary directory
MCP_GUARD_SANDBOX = True  # Enable sandboxing
MCP_GUARD_NETWORK_TIMEOUT = 30  # Network timeout in seconds
MCP_GUARD_DEBUG = False  # Enable debug logging
```

### Configuration Dictionary

```python
config = {
    "analysis": {
        "max_time": 300,
        "max_memory": 1073741824,
        "enable_static": True,
        "enable_dynamic": True,
        "enable_dependency_scan": True
    },
    "security": {
        "sandbox_mode": True,
        "network_isolation": True,
        "resource_limits": True,
        "temp_cleanup": True
    },
    "reporting": {
        "console_output": True,
        "json_output": True,
        "detailed_reports": True,
        "include_payloads": True
    },
    "scoring": {
        "cvss_version": "4.0",
        "enable_aivss": True,
        "risk_threshold": "medium"
    }
}
```

## 🚀 Usage Examples

### Basic Usage

```python
from mcp_scanner import MCPScanner

# Initialize scanner
scanner = MCPScanner()

# Scan repository
results = scanner.scan_repository("https://github.com/user/repo")

# Print summary
print(f"Total vulnerabilities: {results['summary']['total']}")
print(f"Risk level: {results['summary']['overall_risk']}")
```

### Advanced Usage

```python
from mcp_scanner import MCPScanner, VulnerabilityScorer
import json

# Initialize with custom configuration
scanner = MCPScanner()
scorer = VulnerabilityScorer()

# Scan repository
results = scanner.scan_repository("https://github.com/user/repo")

# Process vulnerabilities
for vuln in results['vulnerabilities']:
    if vuln['severity'] == 'critical':
        print(f"CRITICAL: {vuln['title']}")
        print(f"CVSS Score: {vuln['cvss_score']}")
        print(f"Remediation: {vuln['remediation']}")

# Save detailed report
with open('security_report.json', 'w') as f:
    json.dump(results, f, indent=2)
```

### Integration Example

```python
import sys
from mcp_scanner import MCPScanner

def security_gate(repo_url: str, max_critical: int = 0) -> bool:
    """
    Security gate function for CI/CD pipelines.
    
    Args:
        repo_url: Repository to scan
        max_critical: Maximum allowed critical vulnerabilities
        
    Returns:
        bool: True if security gate passes
    """
    scanner = MCPScanner()
    results = scanner.scan_repository(repo_url)
    
    critical_count = results['summary']['by_severity'].get('critical', 0)
    
    if critical_count > max_critical:
        print(f"Security gate FAILED: {critical_count} critical vulnerabilities found")
        return False
    
    print("Security gate PASSED")
    return True

# Usage in CI/CD
if __name__ == "__main__":
    repo_url = sys.argv[1]
    if not security_gate(repo_url):
        sys.exit(1)
```

## 🔍 Error Handling

### Exception Classes

```python
class MCPGuardError(Exception):
    """Base exception for MCP Guard errors."""
    pass

class RepositoryError(MCPGuardError):
    """Repository download or access errors."""
    pass

class AnalysisError(MCPGuardError):
    """Analysis engine errors."""
    pass

class ScoringError(MCPGuardError):
    """Vulnerability scoring errors."""
    pass
```

### Error Handling Example

```python
from mcp_scanner import MCPScanner, RepositoryError, AnalysisError

scanner = MCPScanner()

try:
    results = scanner.scan_repository("https://github.com/user/repo")
except RepositoryError as e:
    print(f"Repository error: {e}")
except AnalysisError as e:
    print(f"Analysis error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

This API documentation provides comprehensive information for developers who want to integrate MCP Guard into their applications or extend its functionality.