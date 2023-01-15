"""Selenium sensor platform"""
from datetime import timedelta
from typing import Any, Callable, Dict, Optional
import voluptuous as vol # <- for input validation

from homeassistant.components.sensor import PLATFORM_SCHEMA # <- for defining the config scheme (in configuration.yaml)
from homeassistant.const import (
    CONF_NAME,
) # <- consts from Home Assistant
# We can define our own consts in const.py file
# then -> from .const import (
#   CONST_NAMES
# )

import homeassistant.helpers.config_validation as cv # <- config validation
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.typing import (
    ConfigType,
    DiscoveryInfoType,
    HomeAssistantType,
)

DEFAULT_NAME = "Example Name"
SCAN_INTERVAL = timedelta(seconds=60)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})
# ^^^^^^^^^^^^
# The config in configuration.yaml will look like this:
# sensors:
#   - platform: selenium_sensors
#     name: "Test Sensor I"
#   - platform: selenium_sensors
#     name: "Test Sensor II"

# Entry function for updating the sensor value
async def async_setup_platform(
    hass: HomeAssistantType,
    config: ConfigType, # <- e.g. config.get(CONF_API_KEY)
    async_add_entities: Callable,
    discovery_info: Optional[DiscoveryInfoType] = None,
) -> None:
    """Set up the sensor platform."""
    sensors = [PolishPope(config)]
    async_add_entities(sensors, update_before_add=True)


class PolishPope(Entity):
    """First test sensor"""
    
    def __init__(self, config):
        super().__init__()
        self.ID = f"Jan Pawel II - {config.get(CONF_NAME)}"
        self._name = config.get(CONF_NAME)
        self._state = 2137
        self._available = True

    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return self._name

    @property
    def unique_id(self) -> str:
        """Return the unique ID of the sensor."""
        return self.ID

    @property
    def available(self) -> bool:
        """Return True if entity is available."""
        return self._available

    @property
    def state(self) -> Optional[str]:
        return self._state

    # This method updates the sensor with frequency set in SCAN_INTERVAL
    async def async_update(self):
        self._state += 1
