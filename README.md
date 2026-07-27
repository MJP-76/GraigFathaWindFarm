# Graig Fatha Wind Farm

[![Home Assistant][badge-home-assistant]][home-assistant]
[![HACS][badge-hacs]][hacs]
[![HACS Validation][badge-hacs-validation]][workflow-hacs-validation]
[![Hassfest][badge-hassfest]][workflow-hassfest]
[![CI][badge-ci]][workflow-ci]
[![Release][badge-release]][releases]
![Status][badge-status]
[![Built with AI][badge-ai]](https://openai.com)

Home Assistant custom component for Graig Fatha Wind Farm based on the JSON the dashboard returns.

> **Not affiliated with Graig Fatha Wind Farm.** This is a community integration that
> reads the JSON returned by the dashboard with your username and password.

## Support me

If you find this project useful, and would like to help support its continued development, you can do so here:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=000000)](https://www.buymeacoffee.com/mjp76)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=ffffff)](https://ko-fi.com/mjp76)
[![Octopus Energy — you get £50, I get £50](https://img.shields.io/badge/Octopus%20Energy-%E2%80%94%20you%20get%20%C2%A350%2C%20I%20get%20%C2%A350-14294A?style=for-the-badge&logo=octopus-energy&logoColor=ffffff)](https://share.octopus.energy/iron-moose-196)

## Included starter functionality

1. Basic config flow (username, password, dashboard URL, site name)
2. Core setup/unload integration wiring
3. One starter sensor confirming setup status

## Integration identity

- Name: Graig Fatha Wind Farm
- Domain: `graig_fatha_wind_farm`
- Platform: `sensor`

## Release notes

- `v1.0.4`: Moved the support section directly below the header content across the docs.

[badge-home-assistant]: https://img.shields.io/badge/Home%20Assistant-41BDF5?style=flat-square&logo=homeassistant&logoColor=white
[badge-hacs]: https://img.shields.io/badge/HACS-Custom-41BDF5.svg
[badge-hassfest]: https://img.shields.io/github/actions/workflow/status/MJP-76/GraigFathaWindFarm/hassfest.yml?branch=main&label=Hassfest
[badge-hacs-validation]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/validate.yml/badge.svg
[badge-ci]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/ci.yml/badge.svg
[badge-ai]: https://img.shields.io/badge/Built_with-AI-black?logo=openai&logoColor=white
[badge-release]: https://img.shields.io/badge/Release-v1.0.4-blue
[badge-status]: https://img.shields.io/badge/Status-stable-brightgreen
[home-assistant]: https://www.home-assistant.io/
[hacs]: https://github.com/hacs/integration
[workflow-hacs-validation]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/validate.yml
[workflow-hassfest]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/hassfest.yml
[workflow-ci]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/ci.yml
[releases]: https://github.com/MJP-76/GraigFathaWindFarm/releases
