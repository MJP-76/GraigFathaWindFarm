# Sensors

The starter integration exposes a single sensor that confirms setup completed
successfully.

| Name | State | Attributes |
|---|---|---|
| Integration status | `configured` | `site_name`, `dashboard_url`, `project_type` |

- **State** — always reports `configured` while the integration is set up.
- **Attributes** — `site_name` (the name entered during configuration),
  `dashboard_url`, and `project_type` (`wind_farm_json_starter`).

This is a starter scaffold — sensor coverage will grow as the dashboard JSON
is mapped into dedicated entities. The integration identity is:

- Domain: `graig_fatha_wind_farm`
- Platform: `sensor`