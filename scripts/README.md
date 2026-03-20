# Scripts

## setup.sh

First-time configuration script. Copies `config.example.json` to `config.json` and prints setup instructions.

```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```

If `config.json` already exists, the script exits without overwriting. Delete the existing config to re-run.

## Adding Custom Scripts

This directory is a good place for:
- Data fetching scripts (custom API wrappers)
- Report formatting tools
- Watchlist monitoring automations

Keep scripts self-contained and document dependencies.
