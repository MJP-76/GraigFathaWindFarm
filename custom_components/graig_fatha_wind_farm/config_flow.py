"""Config flow for the Graig Fatha Wind Farm integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.helpers.selector import (
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)

from .const import (
    CONF_DASHBOARD_URL,
    CONF_PASSWORD,
    CONF_SITE_NAME,
    CONF_USERNAME,
    DEFAULT_DASHBOARD_URL,
    DEFAULT_NAME,
    DOMAIN,
)


class GraigFathaWindFarmConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Graig Fatha Wind Farm."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial setup step."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            return self.async_create_entry(
                title=user_input.get(CONF_SITE_NAME, DEFAULT_NAME),
                data={
                    CONF_USERNAME: user_input[CONF_USERNAME],
                    CONF_PASSWORD: user_input[CONF_PASSWORD],
                    CONF_DASHBOARD_URL: user_input[CONF_DASHBOARD_URL],
                    CONF_SITE_NAME: user_input.get(CONF_SITE_NAME, DEFAULT_NAME),
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_USERNAME): str,
                    vol.Required(CONF_PASSWORD): TextSelector(
                        TextSelectorConfig(type=TextSelectorType.PASSWORD)
                    ),
                    vol.Required(
                        CONF_DASHBOARD_URL, default=DEFAULT_DASHBOARD_URL
                    ): str,
                    vol.Optional(CONF_SITE_NAME, default=DEFAULT_NAME): str,
                }
            ),
        )
