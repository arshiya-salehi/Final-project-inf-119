#!/bin/bash
# Script to run the generated verb conjugator application
# Author: [Your Name] - [Student ID]

echo "================================"
echo "Running Generated Application"
echo "================================"

# Check if generated files exist
if [ ! -f "generated/conjugator/verb_conjugator.py" ]; then
    echo "Error: Generated code not found!"
    echo "Please run the factory first to generate the application."
    exit 1
fi

echo ""
echo "Installing dependencies..."
pip install -q mlconjug3 gradio pytest

echo ""
echo "Running tests..."
cd generated/tests
pytest test_conjugator.py -v
TEST_RESULT=$?

echo ""
echo "================================"
if [ $TEST_RESULT -eq 0 ]; then
    echo "✅ All tests passed!"
else
    echo "⚠️  Some tests failed (this is expected if pass rate is ~80%)"
fi
echo "================================"

echo ""
echo "Starting Gradio UI..."
cd ../conjugator
python gradio_ui.py
