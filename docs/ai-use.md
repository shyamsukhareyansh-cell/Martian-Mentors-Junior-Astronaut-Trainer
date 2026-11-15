# AI, procedural media, and synthetic voice disclosure

- The interface, code, narrative scaffolding, and CSS-generated room environments were created with AI assistance and should be disclosed according to the current NASA Space Apps Challenge rules.
- The Earth-to-ASTRAL-9 opening is a procedural in-browser animation, not a pre-rendered video.
- ECHO and ZYRA dialogue is delivered by 25 locally bundled synthetic text-to-speech clips generated using the open-source eSpeak engine. These are not human recordings, not voice clones, and do not imitate named actors or copyrighted characters. The two voices use different pitch and pacing settings as original character direction.
- No external API, account, or network request is required for the game or voice playback.

Before submission, the team should confirm the current event rules for AI disclosure and asset licences, check all scientific claims against the cited NASA references, and ensure the team has permission to submit all material. Do not add film clips, actor voice recordings, or imitations of named performers/characters.


### Character voice update (build 1.0.1)
ECHO remains a synthetic, measured mission-intelligence voice. ZYRA dialogue is synthesized offline and post-processed with a subtle harmonic layer, chorus and short reflections to create an original otherworldly alien timbre. These are synthetic performances, not human recordings and not imitations or clones of actors or copyrighted characters.


### Character artwork and speech update (build 1.0.3)
- The ZYRA alien character and ECHO holographic-core artwork in `assets/images/` are included as project media and should be credited/disclosed by the team according to the origin/licence of the original image assets.
- The game now prefers the browser/device's built-in English speech synthesis for clearer playback, using separate rate and pitch direction for ECHO and ZYRA. The voice is generated locally by the browser and varies by operating system and installed voices. If speech synthesis is unavailable, the bundled eSpeak clips are used as fallback. Neither path is a human recording or a voice clone.
