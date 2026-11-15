# NASA data integration record — SPACEQUEST 1.0.9

**Challenge resource used:** RadLab (OSDR Radiation Dosimetry Database), supplied in the selected Junior Astronaut Mission Trainer challenge's Resources list.

## What is integrated
The Radiation Shelter's Shielding Panel includes an optional live request to the NASA OSDR RadLab API. It requests the documented ISS/DosTel sample interval from 2022-04-01 23:00 through 2022-04-02 01:05 UTC, filtered to absorbed dose-rate readings above 2 µGy/hour, and requests the `timestamp` and `absorbed_dose_rate` fields. The game displays up to five returned observations and their units. When at least two rows are returned, the player gets a short comparison activity that asks which of the first two actual readings is higher. The feedback explains what dose rate means.

## Scientific boundary
These are measurements from instruments aboard the International Space Station, in low Earth orbit. They are **not** Mars surface measurements and must not be presented as direct predictions of radiation exposure on Mars. The game's Shield Coverage Index remains a fictional gameplay abstraction, not a dose or engineering unit. The panel explains this distinction to the player.

## Sources
- NASA OSDR RadLab Data API documentation: https://visualization.osdr.nasa.gov/radlab/gui/data-api/
- NASA OSDR RadLab overview: https://visualization.osdr.nasa.gov/radlab/gui/overview/
- NASA OSDR absorbed dose rate definition: https://visualization.osdr.nasa.gov/radlab/gui/knowledgebase/absorbed_dose_rate
- Canadian Space Agency Food Production toolkit (Greenhouse contextual resource): https://www.asc-csa.gc.ca/eng/youth-educators/toolkits/food-production/

## Verification status
The code contains a graceful fallback if the API is unreachable or the browser blocks the request. **The live browser request has not yet been verified in a deployed browser.** Before submission, open the Radiation Shelter, click LOAD NASA RADLAB SAMPLE, and confirm that real rows appear. If not, use the direct NASA query link, inspect the API response, and adjust only against the actual returned schema. Do not invent readings or call the API integration verified until tested.
