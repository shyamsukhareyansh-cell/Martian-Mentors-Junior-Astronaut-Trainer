from pathlib import Path
import re, subprocess, tempfile
import tinycss2
root = Path(__file__).resolve().parents[1]
html = (root / 'index.html').read_text()
assert html.count("name:'") == 11, f'Expected 11 rooms, found {html.count("name:")} name fields'
assert 'function renderGame()' in html and 'game-hud' in html, 'Room-first gameplay renderer missing'
assert 'class="sidebar"' not in html, 'Dashboard sidebar should not be in rendered markup'
assert 'hub-portals' in html and 'hub-portal' in html, 'Immersive hub sector portals missing'
assert 'scene-power' in html and 'room-exit' in html, 'Power Station scene or room return control missing'
assert "['ops','MISSION OPERATIONS','open']" in html, 'Hub should expose Mission Operations portal'
riddles = html.split('const riddleBank=[', 1)[1].split('];', 1)[0]
equations = html.split('const equationBank=[', 1)[1].split('];', 1)[0]
assert len(re.findall(r"^\['", riddles, re.M)) == 25, 'Expected 25 riddles'
assert len(re.findall(r"^\['", equations, re.M)) == 15, 'Expected 15 equation puzzles'
assert 'SUBSURFACE04' in html and 'lab-equation' in html, 'Final progression locks missing'
assert 'function playCharacterVoice' in html and 'synth.speak(u)' in html, 'Speech playback missing'
assert 'resource2.heygen.ai/text_to_speech' in html and 'function startNarration()' in html, 'Dedicated cinematic opening narrator audio missing'
assert 'cinema-bars' in html and 'cataclysm-shot' in html and 'podReveal' in html, 'Cinematic opening treatment missing'
assert 'const voiceClips=' not in html, 'Mixed prerecorded character clips should be removed'
assert 'selectedVoices={ECHO:null,ZYRA:null,NARRATOR:null}' in html and 'voiceSelectionLocked=true' in html, 'Stable per-character voice selection missing'
assert 'riddlesSolved' in html and 'equationsSolved' in html, 'Per-question completion persistence missing'
assert 'ALREADY COMPLETED' in html and 'completionMap' in html, 'Room puzzle replay protection missing'
assert 'Math.min(25,Number(raw.riddleProgress)||0)' in html, 'Legacy riddle progress migration missing'
assert (root / 'SUBMISSION-READINESS.md').is_file(), 'Submission readiness notes missing'
assert (root / 'project-metadata.json').is_file(), 'Project metadata disclosure missing'
script = html.split('<script>', 1)[1].split('</script>', 1)[0]
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as f:
    f.write(script); name=f.name
subprocess.run(['node', '--check', name], check=True)
style = html.split('<style>', 1)[1].split('</style>', 1)[0]
css = tinycss2.parse_stylesheet(style, skip_whitespace=True, skip_comments=True)
errors = [x for x in css if x.type == 'error']
assert not errors, f'CSS parse errors: {errors}'
print('Static checks passed: 11 rooms, 25 riddles, 15 equations, progression locks, character speech, dedicated opening narrator, cinematic effects, JavaScript syntax, CSS syntax.')
