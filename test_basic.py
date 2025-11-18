#!/usr/bin/env python3
# Quick test script
import sys
sys.path.insert(0, '.')

from agents import TrackingAgent

print("Testing Tracking Agent...")
tracker = TrackingAgent()

try:
    response = tracker.generate_content("Say 'Hello, the API is working!'")
    print(f"✅ API Response: {response[:100]}")
    
    report = tracker.get_usage_report()
    print(f"✅ Usage Report: {report}")
    
    print("\n✅ All basic tests passed!")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
