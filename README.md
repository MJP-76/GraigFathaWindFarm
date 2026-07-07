# Graig Fatha Wind Farm

[![Home Assistant][ha-badge]][home-assistant]
[![HACS][hacs-badge]][hacs]
[![Hassfest][hassfest-badge]][hassfest]
[![HACS Validation][validate-badge]][validate]
[![CI][ci-badge]][ci]
[![Built with GitHub Copilot][copilot-badge]][copilot]

## Support me

If you find this project useful, and would like to help support its continued development, you can do so here:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=000000)](https://www.buymeacoffee.com/mjp76)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-F16061?style=for-the-badge&logo=ko-fi&logoColor=ffffff)](https://ko-fi.com/mjp76)
[![Octopus Energy — you get £50, I get £50](https://img.shields.io/badge/Octopus%20Energy-%E2%80%94%20you%20get%20%C2%A350%2C%20I%20get%20%C2%A350-14294A?style=for-the-badge&logo=octopus-energy&logoColor=ffffff)](https://share.octopus.energy/iron-moose-196)

Home Assistant custom component for Graig Fatha Wind Farm based on the JSON the dashboard returns.

> **Not affiliated with Graig Fatha Wind Farm.** This is a community integration that
> reads the JSON returned by the dashboard with your username and password.

## Included starter functionality

1. Basic config flow (username, password, dashboard URL, site name)
2. Core setup/unload integration wiring
3. One starter sensor confirming setup status

## Integration identity

- Name: Graig Fatha Wind Farm
- Domain: `graig_fatha_wind_farm`
- Platform: `sensor`

## Release notes

- `v1.0.3`: Support section moved to the top of the docs and release metadata bumped.

[home-assistant]: https://www.home-assistant.io/
[ha-badge]: https://img.shields.io/badge/Home%20Assistant-41BDF5?style=flat-square&logo=homeassistant&logoColor=white
[hacs]: https://github.com/hacs/integration
[hacs-badge]: https://img.shields.io/badge/HACS-Custom-41BDF5.svg
[hassfest]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/hassfest.yml
[hassfest-badge]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/hassfest.yml/badge.svg
[validate]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/validate.yml
[validate-badge]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/validate.yml/badge.svg
[ci]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/ci.yml
[ci-badge]: https://github.com/MJP-76/GraigFathaWindFarm/actions/workflows/ci.yml/badge.svg
[copilot]: https://github.com/features/copilot
[copilot-badge]: https://img.shields.io/badge/Built%20with-GitHub%20Copilot-8A2BE2.svg
