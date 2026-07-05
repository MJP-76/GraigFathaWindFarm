"""Sensor platform for Graig Fatha Wind Farm."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import CONF_DASHBOARD_URL, CONF_SITE_NAME


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up starter sensors for a config entry."""
    async_add_entities([GraigFathaIntegrationStatusSensor(entry)])


class GraigFathaIntegrationStatusSensor(SensorEntity):
    """Starter status sensor for a freshly scaffolded integration."""

    _attr_name = "Integration status"
    _attr_icon = "mdi:wind-turbine"

    def __init__(self, entry: ConfigEntry) -> None:
        self._entry = entry
        self._attr_unique_id = f"{entry.entry_id}_integration_status"

    @property
    def native_value(self) -> str:
        return "configured"

    @property
    def extra_state_attributes(self) -> dict[str, str]:
        return {
            "site_name": self._entry.data.get(CONF_SITE_NAME, ""),
            "dashboard_url": self._entry.data.get(CONF_DASHBOARD_URL, ""),
            "project_type": "wind_farm_json_starter",
        }
