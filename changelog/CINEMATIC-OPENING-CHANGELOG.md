# SPACEQUEST 1.0.17 — Synchronized cinematic opening

This update preserves the existing opening story and sequence. It addresses the reported mismatch between narration and subtitles and strengthens the destruction sound/visual treatment.

## Changes
- Subtitle cues are now driven by the narrator audio playback position rather than independent 3.3-second timers.
- Narrator playback rate is set to 0.82 for more deliberate pacing.
- Caption wording is aligned to the spoken narration.
- Added synthesized layered sound design using Web Audio: low-frequency impact booms, filtered debris/noise bursts, warning alarm tones, and rumble.
- Added expanding shockwave, bright blast bloom, and stronger camera shake on major destruction beats.
- The opening still transitions to the same ASTRAL-9 scene and preserves the same story order and mission flow.

## QA
- JavaScript syntax check passed.
- Existing static project checks passed.
- Existing navigation/progression smoke test passed (9 operational rooms reachable; Archive and Annex remain gated as designed).
- Browser playback and subjective audio mix still require a real-device listening test.
