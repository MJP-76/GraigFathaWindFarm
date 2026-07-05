"""Constants for Graig Fatha Wind Farm."""

from homeassistant.const import Platform

DOMAIN = "graig_fatha_wind_farm"
DEFAULT_NAME = "Graig Fatha Wind Farm"

CONF_USERNAME = "username"
CONF_PASSWORD = "password"
CONF_DASHBOARD_URL = "dashboard_url"
CONF_SITE_NAME = "site_name"

DEFAULT_DASHBOARD_URL = "https://example.com/dashboard/api"

PLATFORMS = [Platform.SENSOR]
