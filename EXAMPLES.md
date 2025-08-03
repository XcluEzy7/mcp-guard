# Examples and Use Cases

## 📚 Overview

This document provides comprehensive examples of using MCP Guard in various scenarios, from basic security scanning to advanced enterprise integration.

## 🚀 Quick Start Examples

### Example 1: Basic Security Scan

The simplest way to scan an MCP server:

```bash
# Scan any MCP server repository
python mcp_scanner.py https://github.com/openbnb-org/mcp-server-airbnb

# Expected output:
# ================================================================================
# MCP GUARD SECURITY ASSESSMENT REPORT
# ================================================================================
# Target: https://github.com/openbnb-org/mcp-server-airbnb
# Total Vulnerabilities: 5
# Overall Risk: MEDIUM
```

### Example 2: Using the Basic Scan Script

```bash
# Run the interactive basic scan example
python examples/basic_scan.py

# Choose from menu:
# 1. Run basic scan example (Airbnb MCP Server)
# 2. Scan a custom repository
# 3. Exit
```

## 🔍 Advanced Analysis Examples

### Example 3: Comprehensive Security Analysis

```python
#!/usr/bin/env python3
from mcp_scanner import MCPScanner
import json

# Initialize scanner
scanner = MCPScanner()

# Scan repository with full analysis
results = scanner.scan_repository("https://github.com/cloudflare/mcp-server-cloudflare")

# Process results
print(f"Server Type: {results['server_info']['server_type']}")
print(f"Total Vulnerabilities: {results['summary']['total']}")

# Filter critical vulnerabilities
critical_vulns = [v for v in results['vulnerabilities'] if v['severity'] == 'critical']
print(f"Critical Issues: {len(critical_vulns)}")

# Save detailed report
with open('security_analysis.json', 'w') as f:
    json.dump(results, f, indent=2)
```

### Example 4: Advanced Analysis with Custom Filtering

```python
#!/usr/bin/env python3
from examples.advanced_analysis import AdvancedAnalyzer

# Initialize advanced analyzer
analyzer = AdvancedAnalyzer()

# Perform comprehensive analysis
results = analyzer.analyze_repository("https://github.com/github/github-mcp-server")

# Access advanced metrics
advanced = results['advanced_analysis']
print(f"Risk Level: {advanced['risk_assessment']['level']}")
print(f"Business Impact: {advanced['risk_assessment']['business_impact']}")

# Show vulnerability patterns
patterns = advanced['vulnerability_patterns']
for pattern, count in patterns.items():
    print(f"{pattern}: {count} occurrences")

# Generate executive summary
summary = analyzer.generate_executive_summary(results)
print(summary)
```

## 🏢 Enterprise Integration Examples

### Example 5: CI/CD Pipeline Integration

#### GitHub Actions Workflow

```yaml
# .github/workflows/security-scan.yml
name: MCP Security Scan

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install MCP Guard
      run: |
        git clone https://github.com/your-org/mcp-guard.git
        cd mcp-guard
        pip install -r requirements.txt
    
    - name: Run Security Scan
      run: |
        cd mcp-guard
        python examples/ci_cd_integration.py \
          --repo-url https://github.com/${{ github.repository }} \
          --max-critical 0 \
          --max-high 2 \
          --output-format junit
    
    - name: Upload Reports
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: security-reports
        path: mcp-guard/security_gate_*.json
```

#### Jenkins Pipeline

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    stages {
        stage('Security Scan') {
            steps {
                script {
                    sh '''
                        git clone https://github.com/your-org/mcp-guard.git
                        cd mcp-guard
                        pip install -r requirements.txt
                        python examples/ci_cd_integration.py \
                          --repo-url https://github.com/your-org/your-mcp-server \
                          --max-critical 0 \
                          --max-high 3
                    '''
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'mcp-guard/security_gate_*.json'
                    publishTestResults testResultsPattern: 'mcp-guard/security_gate_junit_*.xml'
                }
            }
        }
    }
}
```

### Example 6: Security Gate Implementation

```python
#!/usr/bin/env python3
from examples.ci_cd_integration import SecurityGate

# Configure security gate
config = {
    'max_critical': 0,      # Zero tolerance for critical issues
    'max_high': 2,          # Allow up to 2 high-severity issues
    'max_medium': 10,       # Allow up to 10 medium-severity issues
    'max_total': 15,        # Maximum total vulnerabilities
    'min_cvss_score': 8.0,  # Fail if CVSS score >= 8.0
    'fail_on_error': True   # Fail pipeline on scan errors
}

# Initialize security gate
gate = SecurityGate(config)

# Evaluate repository
repo_url = "https://github.com/your-org/mcp-server"
passed, results = gate.evaluate(repo_url)

if passed:
    print("✅ Security gate PASSED - Deployment approved")
    exit(0)
else:
    print("❌ Security gate FAILED - Deployment blocked")
    exit(1)
```

## 🔬 Research and Analysis Examples

### Example 7: Vulnerability Research

```python
#!/usr/bin/env python3
from mcp_scanner import MCPScanner
from collections import defaultdict
import matplotlib.pyplot as plt

# Research multiple MCP servers
repositories = [
    "https://github.com/openbnb-org/mcp-server-airbnb",
    "https://github.com/cloudflare/mcp-server-cloudflare",
    "https://github.com/github/github-mcp-server",
    "https://github.com/crystaldba/postgres-mcp"
]

scanner = MCPScanner()
research_data = []

# Scan all repositories
for repo_url in repositories:
    print(f"Scanning {repo_url}...")
    try:
        results = scanner.scan_repository(repo_url)
        research_data.append(results)
    except Exception as e:
        print(f"Error scanning {repo_url}: {e}")

# Analyze patterns across repositories
vulnerability_types = defaultdict(int)
server_types = defaultdict(int)
severity_distribution = defaultdict(int)

for results in research_data:
    # Count server types
    server_types[results['server_info']['server_type']] += 1
    
    # Count vulnerabilities by severity
    for severity, count in results['summary']['by_severity'].items():
        severity_distribution[severity] += count
    
    # Count vulnerability types
    for vuln in results['vulnerabilities']:
        if 'injection' in vuln['title'].lower():
            vulnerability_types['injection'] += 1
        elif 'authentication' in vuln['title'].lower():
            vulnerability_types['authentication'] += 1
        elif 'validation' in vuln['title'].lower():
            vulnerability_types['input_validation'] += 1

# Generate research report
print("\n📊 MCP Security Research Results")
print("=" * 40)
print(f"Repositories analyzed: {len(research_data)}")
print(f"Total vulnerabilities found: {sum(severity_distribution.values())}")

print("\nServer Type Distribution:")
for server_type, count in server_types.items():
    print(f"  {server_type}: {count}")

print("\nVulnerability Severity Distribution:")
for severity, count in severity_distribution.items():
    print(f"  {severity}: {count}")

print("\nCommon Vulnerability Types:")
for vuln_type, count in vulnerability_types.items():
    print(f"  {vuln_type}: {count}")
```

### Example 8: Comparative Analysis

```python
#!/usr/bin/env python3
from mcp_scanner import MCPScanner
import pandas as pd

def compare_mcp_servers(repo_urls):
    """Compare security posture of multiple MCP servers."""
    
    scanner = MCPScanner()
    comparison_data = []
    
    for repo_url in repo_urls:
        try:
            results = scanner.scan_repository(repo_url)
            
            # Extract comparison metrics
            data = {
                'repository': repo_url,
                'server_type': results['server_info']['server_type'],
                'total_vulnerabilities': results['summary']['total'],
                'critical': results['summary']['by_severity'].get('critical', 0),
                'high': results['summary']['by_severity'].get('high', 0),
                'medium': results['summary']['by_severity'].get('medium', 0),
                'low': results['summary']['by_severity'].get('low', 0),
                'highest_cvss': max([v.get('cvss_score', 0) for v in results['vulnerabilities']] + [0])
            }
            
            comparison_data.append(data)
            
        except Exception as e:
            print(f"Error analyzing {repo_url}: {e}")
    
    # Create comparison DataFrame
    df = pd.DataFrame(comparison_data)
    
    # Generate comparison report
    print("🔍 MCP Server Security Comparison")
    print("=" * 50)
    print(df.to_string(index=False))
    
    # Find most/least secure
    if not df.empty:
        most_secure = df.loc[df['total_vulnerabilities'].idxmin()]
        least_secure = df.loc[df['total_vulnerabilities'].idxmax()]
        
        print(f"\n✅ Most Secure: {most_secure['repository']}")
        print(f"   Total Vulnerabilities: {most_secure['total_vulnerabilities']}")
        
        print(f"\n⚠️  Least Secure: {least_secure['repository']}")
        print(f"   Total Vulnerabilities: {least_secure['total_vulnerabilities']}")
    
    return df

# Example usage
repositories = [
    "https://github.com/openbnb-org/mcp-server-airbnb",
    "https://github.com/cloudflare/mcp-server-cloudflare"
]

comparison_df = compare_mcp_servers(repositories)
```

## 🛠️ Custom Integration Examples

### Example 9: Custom Vulnerability Filter

```python
#!/usr/bin/env python3
from mcp_scanner import MCPScanner

class CustomVulnerabilityFilter:
    """Custom vulnerability filtering and processing."""
    
    def __init__(self):
        self.scanner = MCPScanner()
    
    def scan_with_custom_filters(self, repo_url, filters):
        """Scan repository with custom vulnerability filters."""
        
        # Perform standard scan
        results = self.scanner.scan_repository(repo_url)
        
        # Apply custom filters
        filtered_vulnerabilities = []
        
        for vuln in results['vulnerabilities']:
            if self._matches_filters(vuln, filters):
                filtered_vulnerabilities.append(vuln)
        
        # Update results
        results['vulnerabilities'] = filtered_vulnerabilities
        results['summary']['total'] = len(filtered_vulnerabilities)
        
        # Recalculate severity distribution
        severity_counts = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
        for vuln in filtered_vulnerabilities:
            severity_counts[vuln['severity']] += 1
        
        results['summary']['by_severity'] = severity_counts
        
        return results
    
    def _matches_filters(self, vulnerability, filters):
        """Check if vulnerability matches custom filters."""
        
        # Filter by severity
        if 'min_severity' in filters:
            severity_order = {'low': 1, 'medium': 2, 'high': 3, 'critical': 4}
            min_level = severity_order.get(filters['min_severity'], 1)
            vuln_level = severity_order.get(vulnerability['severity'], 1)
            if vuln_level < min_level:
                return False
        
        # Filter by CWE
        if 'cwe_include' in filters:
            if vulnerability.get('cwe_id') not in filters['cwe_include']:
                return False
        
        # Filter by file pattern
        if 'file_pattern' in filters:
            file_path = vulnerability.get('file_path', '')
            if filters['file_pattern'] not in file_path:
                return False
        
        # Filter by CVSS score
        if 'min_cvss' in filters:
            cvss_score = vulnerability.get('cvss_score', 0)
            if cvss_score < filters['min_cvss']:
                return False
        
        return True

# Example usage
filter_config = {
    'min_severity': 'medium',           # Only medium and above
    'cwe_include': ['CWE-78', 'CWE-89'], # Only specific CWEs
    'min_cvss': 5.0                     # CVSS score >= 5.0
}

custom_filter = CustomVulnerabilityFilter()
results = custom_filter.scan_with_custom_filters(
    "https://github.com/openbnb-org/mcp-server-airbnb",
    filter_config
)

print(f"Filtered results: {results['summary']['total']} vulnerabilities")
```

### Example 10: Integration with Security Platforms

```python
#!/usr/bin/env python3
from mcp_scanner import MCPScanner
import requests
import json

class SecurityPlatformIntegration:
    """Integration with external security platforms."""
    
    def __init__(self, platform_config):
        self.scanner = MCPScanner()
        self.config = platform_config
    
    def scan_and_upload(self, repo_url):
        """Scan repository and upload results to security platform."""
        
        # Perform security scan
        results = self.scanner.scan_repository(repo_url)
        
        # Transform results for platform
        platform_data = self._transform_for_platform(results)
        
        # Upload to security platform
        self._upload_to_platform(platform_data)
        
        return results
    
    def _transform_for_platform(self, results):
        """Transform MCP Guard results for security platform format."""
        
        # Example transformation for SARIF format
        sarif_report = {
            "version": "2.1.0",
            "runs": [{
                "tool": {
                    "driver": {
                        "name": "MCP Guard",
                        "version": "1.0.0",
                        "informationUri": "https://github.com/your-org/mcp-guard"
                    }
                },
                "results": []
            }]
        }
        
        # Convert vulnerabilities to SARIF format
        for vuln in results['vulnerabilities']:
            sarif_result = {
                "ruleId": vuln.get('cwe_id', 'unknown'),
                "message": {"text": vuln['description']},
                "level": self._map_severity_to_sarif(vuln['severity']),
                "locations": [{
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": vuln.get('file_path', 'unknown')
                        },
                        "region": {
                            "startLine": vuln.get('line_number', 1)
                        }
                    }
                }]
            }
            
            sarif_report["runs"][0]["results"].append(sarif_result)
        
        return sarif_report
    
    def _map_severity_to_sarif(self, severity):
        """Map MCP Guard severity to SARIF levels."""
        mapping = {
            'critical': 'error',
            'high': 'error',
            'medium': 'warning',
            'low': 'note'
        }
        return mapping.get(severity, 'note')
    
    def _upload_to_platform(self, data):
        """Upload results to security platform."""
        
        # Example: Upload to GitHub Security tab
        if self.config['platform'] == 'github':
            self._upload_to_github_security(data)
        
        # Example: Upload to custom security platform
        elif self.config['platform'] == 'custom':
            self._upload_to_custom_platform(data)
    
    def _upload_to_github_security(self, sarif_data):
        """Upload SARIF results to GitHub Security tab."""
        
        # This would use GitHub's SARIF upload API
        # Requires authentication and proper permissions
        print("📤 Uploading to GitHub Security tab...")
        print(f"SARIF results: {len(sarif_data['runs'][0]['results'])} findings")
    
    def _upload_to_custom_platform(self, data):
        """Upload to custom security platform."""
        
        try:
            response = requests.post(
                self.config['endpoint'],
                headers={
                    'Authorization': f"Bearer {self.config['api_key']}",
                    'Content-Type': 'application/json'
                },
                json=data
            )
            
            if response.status_code == 200:
                print("✅ Successfully uploaded to security platform")
            else:
                print(f"❌ Upload failed: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Upload error: {e}")

# Example usage
platform_config = {
    'platform': 'custom',
    'endpoint': 'https://security-platform.company.com/api/upload',
    'api_key': 'your-api-key-here'
}

integration = SecurityPlatformIntegration(platform_config)
results = integration.scan_and_upload("https://github.com/openbnb-org/mcp-server-airbnb")
```

## 📊 Reporting Examples

### Example 11: Custom Report Generation

```python
#!/usr/bin/env python3
from mcp_scanner import MCPScanner
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

class CustomReportGenerator:
    """Generate custom security reports with visualizations."""
    
    def __init__(self):
        self.scanner = MCPScanner()
    
    def generate_executive_dashboard(self, repo_urls):
        """Generate executive dashboard with multiple repositories."""
        
        dashboard_data = []
        
        # Scan all repositories
        for repo_url in repo_urls:
            try:
                results = self.scanner.scan_repository(repo_url)
                dashboard_data.append(results)
            except Exception as e:
                print(f"Error scanning {repo_url}: {e}")
        
        # Generate visualizations
        self._create_severity_chart(dashboard_data)
        self._create_trend_analysis(dashboard_data)
        self._create_risk_matrix(dashboard_data)
        
        # Generate executive summary
        summary = self._generate_executive_summary(dashboard_data)
        
        return summary
    
    def _create_severity_chart(self, data):
        """Create severity distribution chart."""
        
        severity_totals = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
        
        for results in data:
            for severity, count in results['summary']['by_severity'].items():
                severity_totals[severity] += count
        
        # Create pie chart
        plt.figure(figsize=(10, 6))
        plt.pie(severity_totals.values(), labels=severity_totals.keys(), autopct='%1.1f%%')
        plt.title('Vulnerability Severity Distribution')
        plt.savefig('severity_distribution.png')
        plt.close()
        
        print("📊 Severity distribution chart saved: severity_distribution.png")
    
    def _create_trend_analysis(self, data):
        """Create trend analysis chart."""
        
        # Simulate trend data (in real implementation, you'd track over time)
        dates = [datetime.now().strftime('%Y-%m-%d') for _ in range(len(data))]
        total_vulns = [results['summary']['total'] for results in data]
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, total_vulns, marker='o')
        plt.title('Vulnerability Trend Analysis')
        plt.xlabel('Date')
        plt.ylabel('Total Vulnerabilities')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('trend_analysis.png')
        plt.close()
        
        print("📈 Trend analysis chart saved: trend_analysis.png")
    
    def _create_risk_matrix(self, data):
        """Create risk assessment matrix."""
        
        risk_data = []
        
        for results in data:
            repo_name = results['server_info']['name']
            total_vulns = results['summary']['total']
            critical_count = results['summary']['by_severity'].get('critical', 0)
            
            # Calculate risk score
            risk_score = (critical_count * 10) + (total_vulns * 2)
            
            risk_data.append({
                'repository': repo_name,
                'total_vulnerabilities': total_vulns,
                'critical_vulnerabilities': critical_count,
                'risk_score': risk_score
            })
        
        # Create risk matrix visualization
        plt.figure(figsize=(10, 8))
        
        x = [item['total_vulnerabilities'] for item in risk_data]
        y = [item['critical_vulnerabilities'] for item in risk_data]
        sizes = [item['risk_score'] * 10 for item in risk_data]
        
        plt.scatter(x, y, s=sizes, alpha=0.6)
        plt.xlabel('Total Vulnerabilities')
        plt.ylabel('Critical Vulnerabilities')
        plt.title('Security Risk Matrix')
        
        # Add repository labels
        for item in risk_data:
            plt.annotate(item['repository'], 
                        (item['total_vulnerabilities'], item['critical_vulnerabilities']))
        
        plt.savefig('risk_matrix.png')
        plt.close()
        
        print("🎯 Risk matrix chart saved: risk_matrix.png")
    
    def _generate_executive_summary(self, data):
        """Generate executive summary report."""
        
        total_repos = len(data)
        total_vulns = sum(results['summary']['total'] for results in data)
        total_critical = sum(results['summary']['by_severity'].get('critical', 0) for results in data)
        
        summary = f"""
🏢 EXECUTIVE SECURITY DASHBOARD
{'=' * 50}

📊 PORTFOLIO OVERVIEW
Repositories Analyzed: {total_repos}
Total Vulnerabilities: {total_vulns}
Critical Issues: {total_critical}
Average Vulnerabilities per Repository: {total_vulns / total_repos if total_repos > 0 else 0:.1f}

🚨 HIGH-RISK REPOSITORIES
"""
        
        # Identify high-risk repositories
        high_risk_repos = []
        for results in data:
            critical_count = results['summary']['by_severity'].get('critical', 0)
            if critical_count > 0:
                high_risk_repos.append({
                    'name': results['server_info']['name'],
                    'critical': critical_count,
                    'total': results['summary']['total']
                })
        
        high_risk_repos.sort(key=lambda x: x['critical'], reverse=True)
        
        for repo in high_risk_repos[:5]:  # Top 5 high-risk
            summary += f"  • {repo['name']}: {repo['critical']} critical, {repo['total']} total\n"
        
        summary += f"""
💡 RECOMMENDATIONS
1. Immediately address {total_critical} critical vulnerabilities
2. Implement automated security scanning in CI/CD pipelines
3. Establish security training program for development teams
4. Create incident response procedures for security issues
5. Schedule regular security assessments

📈 VISUALIZATIONS GENERATED
• severity_distribution.png - Vulnerability severity breakdown
• trend_analysis.png - Security trend over time
• risk_matrix.png - Repository risk assessment matrix
"""
        
        return summary

# Example usage
report_generator = CustomReportGenerator()

repositories = [
    "https://github.com/openbnb-org/mcp-server-airbnb",
    "https://github.com/cloudflare/mcp-server-cloudflare"
]

executive_summary = report_generator.generate_executive_dashboard(repositories)
print(executive_summary)

# Save executive summary
with open('executive_dashboard.txt', 'w') as f:
    f.write(executive_summary)

print("📄 Executive dashboard saved: executive_dashboard.txt")
```

## 🎯 Best Practices Examples

### Example 12: Security Scanning Best Practices

```python
#!/usr/bin/env python3
"""
Security Scanning Best Practices Example

This example demonstrates best practices for using MCP Guard
in production environments.
"""

from mcp_scanner import MCPScanner
import logging
import time
from contextlib import contextmanager

class ProductionScanner:
    """Production-ready MCP security scanner with best practices."""
    
    def __init__(self):
        self.scanner = MCPScanner()
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup comprehensive logging."""
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('mcp_guard.log'),
                logging.StreamHandler()
            ]
        )
        
        self.logger = logging.getLogger('MCPGuard')
    
    @contextmanager
    def _scan_context(self, repo_url):
        """Context manager for safe scanning."""
        
        self.logger.info(f"Starting scan of {repo_url}")
        start_time = time.time()
        
        try:
            yield
        except Exception as e:
            self.logger.error(f"Scan failed for {repo_url}: {e}")
            raise
        finally:
            duration = time.time() - start_time
            self.logger.info(f"Scan completed in {duration:.2f} seconds")
    
    def secure_scan(self, repo_url, max_retries=3):
        """Perform secure scan with error handling and retries."""
        
        for attempt in range(max_retries):
            try:
                with self._scan_context(repo_url):
                    # Validate repository URL
                    if not self._validate_repo_url(repo_url):
                        raise ValueError(f"Invalid repository URL: {repo_url}")
                    
                    # Perform scan
                    results = self.scanner.scan_repository(repo_url)
                    
                    # Validate results
                    if not self._validate_results(results):
                        raise ValueError("Invalid scan results")
                    
                    # Log success
                    self.logger.info(f"Scan successful: {results['summary']['total']} vulnerabilities found")
                    
                    return results
                    
            except Exception as e:
                self.logger.warning(f"Scan attempt {attempt + 1} failed: {e}")
                if attempt == max_retries - 1:
                    self.logger.error(f"All scan attempts failed for {repo_url}")
                    raise
                
                # Wait before retry
                time.sleep(2 ** attempt)  # Exponential backoff
        
        return None
    
    def _validate_repo_url(self, repo_url):
        """Validate repository URL for security."""
        
        # Check for valid GitHub URL
        if not repo_url.startswith("https://github.com/"):
            return False
        
        # Check for suspicious patterns
        suspicious_patterns = ['..', '<script>', 'javascript:', 'data:']
        for pattern in suspicious_patterns:
            if pattern in repo_url.lower():
                return False
        
        return True
    
    def _validate_results(self, results):
        """Validate scan results structure."""
        
        required_keys = ['server_info', 'vulnerabilities', 'summary']
        
        for key in required_keys:
            if key not in results:
                return False
        
        # Validate summary structure
        if 'total' not in results['summary']:
            return False
        
        return True

# Example usage with best practices
def main():
    """Demonstrate production scanning best practices."""
    
    scanner = ProductionScanner()
    
    # List of repositories to scan
    repositories = [
        "https://github.com/openbnb-org/mcp-server-airbnb",
        "https://github.com/cloudflare/mcp-server-cloudflare"
    ]
    
    successful_scans = []
    failed_scans = []
    
    for repo_url in repositories:
        try:
            results = scanner.secure_scan(repo_url)
            if results:
                successful_scans.append(results)
        except Exception as e:
            failed_scans.append({'repo_url': repo_url, 'error': str(e)})
    
    # Report results
    print(f"✅ Successful scans: {len(successful_scans)}")
    print(f"❌ Failed scans: {len(failed_scans)}")
    
    # Process successful scans
    for results in successful_scans:
        repo_name = results['server_info']['name']
        total_vulns = results['summary']['total']
        print(f"  {repo_name}: {total_vulns} vulnerabilities")
    
    # Report failures
    for failure in failed_scans:
        print(f"  Failed: {failure['repo_url']} - {failure['error']}")

if __name__ == "__main__":
    main()
```

---

These examples demonstrate the full range of MCP Guard capabilities, from basic security scanning to advanced enterprise integration. Each example includes complete, runnable code that you can adapt for your specific use case.