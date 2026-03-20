#!/bin/bash
# Lobster Investment Research — First-time setup
# Creates config.json from the example template

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
CONFIG_FILE="$SKILL_DIR/config.json"
EXAMPLE_FILE="$SKILL_DIR/config.example.json"

if [ -f "$CONFIG_FILE" ]; then
    echo "config.json already exists at: $CONFIG_FILE"
    echo "Edit it directly or delete it to re-run setup."
    exit 0
fi

if [ ! -f "$EXAMPLE_FILE" ]; then
    echo "Error: config.example.json not found at: $EXAMPLE_FILE"
    exit 1
fi

echo "=== Lobster Investment Research Setup ==="
echo ""
echo "Creating config.json from template..."
cp "$EXAMPLE_FILE" "$CONFIG_FILE"
echo ""
echo "Config created at: $CONFIG_FILE"
echo ""
echo "Next steps:"
echo "  1. Edit config.json with your preferences:"
echo "     - preferred_lenses: your 2-3 most-used investment lenses"
echo "     - edge_definitions: what gives you an advantage (see references/edge-framework.md)"
echo "     - report_path: where to save completed reports"
echo "     - watchlist: tickers/tokens you track"
echo "     - data_sources: API keys (most are free tier)"
echo ""
echo "  2. Test with: 'Analyze AAPL — current valuation vs growth'"
echo ""
echo "Done."
