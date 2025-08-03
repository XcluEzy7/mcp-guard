#!/usr/bin/env python3
"""
Test script for MCP Guard download functionality
Tests repository download and extraction capabilities
"""

import sys
import os
import tempfile
import shutil
from datetime import datetime

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from mcp_scanner import MCPRepositoryHandler
    print("✅ Successfully imported MCPRepositoryHandler")
except ImportError as e:
    print(f"❌ Failed to import MCPRepositoryHandler: {e}")
    sys.exit(1)

def test_github_download():
    """Test GitHub repository download"""
    print("\n🌐 Testing GitHub Repository Download")
    print("-" * 45)
    
    test_repos = [
        {
            "url": "https://github.com/octocat/Hello-World",
            "description": "Simple test repository"
        },
        {
            "url": "https://github.com/modelcontextprotocol/servers",
            "description": "Official MCP servers collection"
        },
        {
            "url": "https://github.com/punkpeye/mcp-server-git",
            "description": "Git MCP server"
        }
    ]
    
    repo_handler = MCPRepositoryHandler()
    successful_downloads = 0
    
    for repo in test_repos:
        try:
            print(f"\n📥 Testing: {repo['description']}")
            print(f"URL: {repo['url']}")
            
            # Download repository
            local_path = repo_handler.download_repository(repo['url'])
            
            if os.path.exists(local_path):
                # Check contents
                files = os.listdir(local_path)
                print(f"✅ Downloaded successfully to: {local_path}")
                print(f"✅ Found {len(files)} items in repository")
                
                # Show some files
                if files:
                    print(f"✅ Sample files: {', '.join(files[:5])}")
                    if len(files) > 5:
                        print(f"   ... and {len(files) - 5} more")
                
                successful_downloads += 1
                
                # Test server type detection
                try:
                    server_info = repo_handler.detect_mcp_server_type(local_path)
                    print(f"✅ Detected server type: {server_info.server_type}")
                    print(f"✅ Server name: {server_info.name}")
                except Exception as e:
                    print(f"⚠️ Server detection failed: {e}")
                
            else:
                print(f"❌ Download failed - path doesn't exist")
                
        except Exception as e:
            print(f"❌ Download failed: {e}")
        
        finally:
            # Cleanup
            try:
                repo_handler.cleanup()
                print("✅ Cleanup completed")
            except Exception as e:
                print(f"⚠️ Cleanup warning: {e}")
    
    print(f"\n📊 Download Results: {successful_downloads}/{len(test_repos)} successful")
    return successful_downloads > 0

def test_branch_detection():
    """Test branch detection and fallback"""
    print("\n🌿 Testing Branch Detection")
    print("-" * 30)
    
    try:
        repo_handler = MCPRepositoryHandler()
        
        # Test with a repository that might have different branch names
        test_url = "https://github.com/octocat/Hello-World"
        print(f"Testing branch detection with: {test_url}")
        
        local_path = repo_handler.download_repository(test_url)
        
        if os.path.exists(local_path):
            print("✅ Branch detection and download successful")
            
            # Check if we got the right content
            files = os.listdir(local_path)
            if files:
                print(f"✅ Repository contains: {', '.join(files)}")
            
            repo_handler.cleanup()
            return True
        else:
            print("❌ Branch detection failed")
            return False
            
    except Exception as e:
        print(f"❌ Branch detection test failed: {e}")
        return False

def test_error_handling():
    """Test error handling for invalid repositories"""
    print("\n🚫 Testing Error Handling")
    print("-" * 25)
    
    invalid_repos = [
        "https://github.com/nonexistent/repository",
        "https://invalid-url",
        "not-a-url-at-all"
    ]
    
    repo_handler = MCPRepositoryHandler()
    handled_errors = 0
    
    for repo_url in invalid_repos:
        try:
            print(f"\n🧪 Testing invalid URL: {repo_url}")
            local_path = repo_handler.download_repository(repo_url)
            print(f"❌ Expected error but got path: {local_path}")
        except Exception as e:
            print(f"✅ Correctly handled error: {type(e).__name__}")
            handled_errors += 1
    
    print(f"\n📊 Error Handling: {handled_errors}/{len(invalid_repos)} errors handled correctly")
    return handled_errors == len(invalid_repos)

def test_cleanup():
    """Test cleanup functionality"""
    print("\n🧹 Testing Cleanup Functionality")
    print("-" * 30)
    
    try:
        repo_handler = MCPRepositoryHandler()
        
        # Download a repository
        test_url = "https://github.com/octocat/Hello-World"
        local_path = repo_handler.download_repository(test_url)
        
        if os.path.exists(local_path):
            print(f"✅ Repository downloaded to: {local_path}")
            
            # Test cleanup
            repo_handler.cleanup()
            
            # Check if cleaned up
            if not os.path.exists(local_path):
                print("✅ Cleanup successful - temporary files removed")
                return True
            else:
                print("⚠️ Cleanup incomplete - some files remain")
                return False
        else:
            print("❌ Could not test cleanup - download failed")
            return False
            
    except Exception as e:
        print(f"❌ Cleanup test failed: {e}")
        return False

def run_download_tests():
    """Run all download tests"""
    print("🚀 MCP Guard Download Test Suite")
    print("=" * 40)
    
    tests = [
        ("GitHub Download", test_github_download),
        ("Branch Detection", test_branch_detection),
        ("Error Handling", test_error_handling),
        ("Cleanup", test_cleanup),
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
    
    print("\n" + "=" * 40)
    print(f"📊 Download Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All download tests passed!")
        return True
    else:
        print("⚠️ Some download tests failed.")
        return False

if __name__ == "__main__":
    success = run_download_tests()
    sys.exit(0 if success else 1)