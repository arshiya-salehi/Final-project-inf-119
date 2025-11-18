#!/usr/bin/env python3
# Main entry point for the Verb Conjugator Factory
# Author: [Your Name] - [Student ID]

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.gradio_app import VerbConjugatorFactoryUI

def main():
    """Main entry point"""
    print("=" * 60)
    print("🏭 Language Verb Conjugator Factory")
    print("=" * 60)
    print("\nInitializing multi-agent system...")
    print("Starting Gradio interface...\n")
    
    # Create and launch UI
    app = VerbConjugatorFactoryUI()
    app.launch()

if __name__ == "__main__":
    main()
