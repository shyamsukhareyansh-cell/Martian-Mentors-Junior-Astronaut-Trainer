# Original character voice assets

This build includes 25 offline-generated synthetic speech clips in `lines/`, selected by the game from `voice-index.json` (also embedded in `index.html`). They are generated with the open-source eSpeak text-to-speech engine, not recorded human performances and not AI voice clones.

- **ECHO:** lower-pitched, measured, deliberate masculine-presenting synthetic voice.
- **ZYRA:** brighter, quicker, expressive feminine-presenting synthetic voice.

These are original broad voice directions. They do not imitate James Spader, Ultron, FRIDAY, or any other actor or copyrighted character. The sound is intentionally a synthetic prototype performance; the team may replace it with original recorded performances if desired and if every speaker grants permission.

The audio is bundled locally and requires no network connection. The in-game VOICE toggle can disable playback, and each dialogue panel has a replay control.


## Playback behavior in voice-fix build

The game prioritizes bundled MP3 clips before browser speech synthesis. This prevents the same installed browser voice from overriding both character identities. ECHO and ZYRA opening lines play automatically in sequence. Manual Play/Replay voice buttons have been removed; the global VOICE toggle remains available.


## Earth opening ambience

`earth-intro-ambience.mp3` is an original 48-second atmospheric instrumental loop. It begins when the player starts the Earth cinematic and stops when the sequence ends or is skipped. The soundtrack is intentionally restrained beneath any future narration.

## Voice quality note

The bundled character dialogue in this build is still synthetic eSpeak audio. ECHO and ZYRA use separate voice profiles, but these clips can sound robotic. Do not describe them as natural or human-like. Replacing them with convincingly natural performances requires licensed human recordings or neural TTS-generated audio, then replacing the corresponding MP3 assets.


## Proposed Earth-cinematic narrator script (not yet recorded)

Voice direction: original deep masculine documentary narrator; warm low register, calm and grave, cinematic pacing, clear diction. This is an original direction, not an imitation of a named actor or character.

“Earth. Our only home. For generations, we believed the blue horizon would always be there. Then the signals began to fail. The atmosphere changed. Cities went dark. One by one, the evacuation ships departed. There was no return window. Earth was lost. The survivors carried the future into deep space. Aboard ASTRAL-9, one final mission continued.”

This script is a proposed voice-over and is not embedded as audio in this build. The Earth soundtrack currently plays on its own beneath the on-screen cinematic captions.


## Earth soundtrack playback reliability

The 54-second original cinematic instrumental has a stronger audible mix than the previous ambience version. It starts at 62% volume when Start Mission is clicked. If browser autoplay policy blocks playback, an ENABLE SOUND control appears in the Earth cinematic. The music stops when the cinematic is skipped or transitions to ASTRAL-9.
