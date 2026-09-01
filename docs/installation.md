# Installation

## HACS (recommended)

1. In HACS, add this repository as a custom repository (category: **Integration**):
   `https://github.com/MJP-76/GraigFathaWindFarm`
2. Search for "Graig Fatha Wind Farm" in HACS and install it.
3. Restart Home Assistant.
4. Go to **Settings > Devices & Services > Add Integration**, search for
   "Graig Fatha Wind Farm", and enter your dashboard username and password.

## Manual

1. Copy `custom_components/graig_fatha_wind_farm/` into your Home Assistant
   `config/custom_components/` directory.
2. Restart Home Assistant.
3. Go to **Settings > Devices & Services > Add Integration**, search for
   "Graig Fatha Wind Farm", and enter your dashboard credentials.

## Configuration flow

The config flow asks for:

- **Username** — your Graig Fatha Wind Farm dashboard username.
- **Password** — your Graig Fatha Wind Farm dashboard password.
- **Dashboard URL** — the base URL of the dashboard the JSON is read from.
- **Site name** — a label for the site, used in your entities.