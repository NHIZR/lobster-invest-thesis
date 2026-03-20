# Scripts

## setup.sh

First-time configuration script. Copies `config.example.json` to `config.json` and prints setup instructions.

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

If `config.json` already exists, the script exits without overwriting. Delete the existing config to re-run.

## fetch_data.py

Data fetcher wrapping free APIs (DeFiLlama, CoinGecko, Yahoo Finance). No dependencies beyond Python 3 standard library.

```bash
python scripts/fetch_data.py defi aave          # DeFiLlama protocol data
python scripts/fetch_data.py crypto bitcoin      # CoinGecko coin data
python scripts/fetch_data.py stock AAPL          # Yahoo Finance quote
python scripts/fetch_data.py fees aave           # DeFiLlama fees/revenue
python scripts/fetch_data.py yields aave         # DeFiLlama yield pools
```

## Adding Custom Scripts

Keep scripts self-contained and document dependencies.
