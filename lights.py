import asyncio
import logging

from phue import Bridge
from pywizlight import wizlight, PilotBuilder

logger = logging.getLogger(__name__)


# Philips Hue Bridge control
bridge_ip = "insert ip"
b = Bridge(bridge_ip)

# Connect to the bridge (this is a blocking call)
b.connect()

# Toggle Philips Hue lights
lights = b.lights
for light in lights:
    light.on = not light.on

async def control_lights():
    # WizLight control
    wiz_ip = "insert ip"
    wiz_light = wizlight(wiz_ip)
    # Turn on WizLight (async operation)
    logger.info("Attempting to control WizLight at {wiz_ip}")
    await asyncio.wait_for(wiz_light.lightSwitch(), timeout=5.0)
    logger.info("WizLight successfully turned on")


async def main():
    await control_lights()

if __name__ == "__main__":
    asyncio.run(main())