#!/usr/bin/env python3
"""
Test script for MCP Guard Scanner
Tests the scanner with real MCP server repositories
"""

import sys
import os
import json
import tempfile
import shutil
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from mcp_scanner import UniversalMCPScanner, MCPRepositoryHandler
    print("✅ Successfully imported MCP Guard modules")
except ImportError as e:
    print(f"❌ Failed to import MCP Guard modules: {e}")
    sys.exit(1)

def test_basic_functionality():
    """Test basic scanner functionality"""
    print("\n🧪 Testing Basic Functionality")
    print("-" * 40)
    
    try:
        # Test scanner initialization
        scanner = UniversalMCPScanner()
        print("✅ Scanner initialized successfully")
        
        # Test repository handler
        repo_handler = MCPRepositoryHandler()
        print("✅ Repository handler initialized successfully")
        
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def test_repository_download():
    """Test repository download functionality"""
    print("\n🌐 Testing Repository Download")
    print("-" * 40)
    
    try:
        repo_handler = MCPRepositoryHandler()
        
        # Test with a small, reliable repository
        test_repo = "https://github.com/octocat/Hello-World"
        print(f"Testing download: {test_repo}")
        
        local_path = repo_handler.download_repository(test_repo)
        
        if os.path.exists(local_path):
            print(f"✅ Repository downloaded to: {local_path}")
            
            # Check if files exist
            files = os.listdir(local_path)
            print(f"✅ Found {len(files)} files in repository")
            
            # Cleanup
            repo_handler.cleanup()
            print("✅ Cleanup completed")
            
            return True
        else:
            print("❌ Repository download failed - path doesn't exist")
            return False
            
    except Exception as e:
        print(f"❌ Repository download test failed: {e}")
        return False

def test_mcp_server_detection():
    """Test MCP server type detection"""
    print("\n🔍 Testing MCP Server Detection")
    print("-" * 40)
    
    try:
        repo_handler = MCPRepositoryHandler()
        
        # Test with a known MCP server
        test_repos = [
            "https://github.com/modelcontextprotocol/servers",
            "https://github.com/punkpeye/mcp-server-git",
        ]
        
        for repo_url in test_repos:
            try:
                print(f"\nTesting: {repo_url}")
                local_path = repo_handler.download_repository(repo_url)
                server_info = repo_handler.detect_mcp_server_type(local_path)
                
                print(f"✅ Detected server type: {server_info.server_type}")
                print(f"✅ Server name: {server_info.name}")
                print(f"✅ Package manager: {server_info.package_manager}")
                print(f"✅ Entry points: {len(server_info.entry_points)}")
                
                repo_handler.cleanup()
                return True
                
            except Exception as e:
                print(f"⚠️ Failed to test {repo_url}: {e}")
                continue
        
        print("❌ All MCP server detection tests failed")
        return False
        
    except Exception as e:
        print(f"❌ MCP server detection test failed: {e}")
        return False

def test_static_analysis():
    """Test static analysis functionality"""
    print("\n🔬 Testing Static Analysis")
    print("-" * 40)
    
    try:
        scanner = UniversalMCPScanner()
        
        # Test with a small repository
        test_repo = "https://github.com/punkpeye/mcp-server-git"
        print(f"Running static analysis on: {test_repo}")
        
        results = scanner.scan_mcp_server(test_repo, 'static')
        
        if 'error' in results:
            print(f"⚠️ Scan completed with error: {results['error']}")
            return False
        
        print(f"✅ Static analysis completed successfully")
        print(f"✅ Server type: {results['server_info']['server_type']}")
        print(f"✅ Total vulnerabilities: {results['summary']['total']}")
        
        # Show severity breakdown
        severity_counts = results['summary']['by_severity']
        for severity, count in severity_counts.items():
            if count > 0:
                print(f"✅ {severity.upper()}: {count}")
        
        # Save test results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"test_results_static_{timestamp}.json"
        
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"✅ Results saved to: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Static analysis test failed: {e}")
        return False

def test_vulnerability_scoring():
    """Test vulnerability scoring system"""
    print("\n📊 Testing Vulnerability Scoring")
    print("-" * 40)
    
    try:
        from simple_vulnerability_scoring import VulnerabilityScorer
        
        scorer = VulnerabilityScorer()
        print("✅ Vulnerability scorer initialized")
        
        # Test scoring
        test_context = {
            'server_type': 'nodejs',
            'server_name': 'test-mcp-server',
            'confidence': 'high'
        }
        
        score = scorer.score_vulnerability('command_injection', 'CWE-78', test_context)
        
        print(f"✅ CVSS Score: {score.cvss.base_score}")
        print(f"✅ CVSS Severity: {score.cvss.severity}")
        print(f"✅ AIVSS Score: {score.aivss.base_score}")
        print(f"✅ AIVSS Severity: {score.aivss.severity}")
        print(f"✅ Overall Risk: {score.overall_risk}")
        
        return True
        
    except Exception as e:
        print(f"❌ Vulnerability scoring test failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("🚀 MCP Guard Test Suite")
    print("=" * 50)
    
    tests = [
        ("Basic Functionality", test_basic_functionality),
        ("Repository Download", test_repository_download),
        ("MCP Server Detection", test_mcp_server_detection),
        ("Static Analysis", test_static_analysis),
        ("Vulnerability Scoring", test_vulnerability_scoring),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name}: PASSED")
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! MCP Guard is working correctly.")
        return True
    else:
        print("⚠️ Some tests failed. Please check the output above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)