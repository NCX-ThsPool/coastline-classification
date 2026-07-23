# Security and privacy

The original scripts contained many absolute Windows paths and at least one
Earth Engine project identifier. The public refactoring follows these rules:

- No personal Windows directory is embedded in package code.
- No API key, token, cookie, password, e-mail address, or private endpoint is
  committed.
- Earth Engine project names are loaded from environment variables.
- Local paths live in ignored `*.local.yaml` files.
- Raw imagery, manually labelled samples, checkpoints, and third-party products
  are excluded.
- Generated logs should be reviewed before publication because software can
  echo local paths and environment details.
