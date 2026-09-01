# Graig Fatha Wind Farm

[![Home Assistant][badge-home-assistant]][home-assistant]
[![HACS][badge-hacs]][hacs]
[![HACS Validation][badge-hacs-validation]][workflow-hacs-validation]
[![Hassfest][badge-hassfest]][workflow-hassfest]
[![CI][badge-ci]][workflow-ci]
[![Release][badge-release]][releases]
[![Built with AI][badge-built-with-ai]][built-with-ai]

A Home Assistant custom component for **Graig Fatha Wind Farm**, based on the
JSON the dashboard returns.

!!! warning "Not affiliated"

    This is a community integration. It is not affiliated with Graig Fatha
    Wind Farm — it reads the JSON returned by the dashboard using your
    username and password.

## What this integration does

- Basic config flow (username, password, dashboard URL, site name)
- Core setup/unload integration wiring
- One starter sensor confirming setup status

## Integration identity

- Name: Graig Fatha Wind Farm
- Domain: `graig_fatha_wind_farm`
- Platform: `sensor`

## Where to go next

| Topic | Page |
|---|---|
| Install and configure | [Installation](installation.md) |
| What sensors are available | [Sensors](sensors.md) |
| Release history | [Changelog](changelog.md) |

[badge-home-assistant]: https://img.shields.io/badge/Home%20Assistant-41BDF5?style=flat-square&logo=homeassistant&logoColor=white
[home-assistant]: https://www.home-assistant.io/
[badge-hacs]: https://img.shields.io/badge/HACS-Custom-41BDF5.svg
[hacs]: https://github.com/hacs/integration
[badge-hacs-validation]: https://img.shields.io/badge/HACS%20Validation-passing-brightgreen
[workflow-hacs-validation]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/validate.yml
[badge-hassfest]: https://img.shields.io/github/actions/workflow/status/MJP-76/GraigFathaWindFarm/hassfest.yml?branch=main&label=Hassfest
[workflow-hassfest]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/hassfest.yml
[badge-ci]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/ci.yml/badge.svg
[workflow-ci]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/ci.yml
[badge-release]: https://img.shields.io/github/v/release/MJP-76/GraigFathaWindFarm?style=flat&label=Release
[releases]: https://github.com/MJP-76/GraigFathaWindFarm/releases
[badge-built-with-ai]: https://img.shields.io/badge/Built%20with-AI-black?logo=openai&logoColor=white
[built-with-ai]: https://openai.com