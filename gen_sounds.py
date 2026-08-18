# Generates the 5 new WAV sounds for HORER 2: VFRIEND.
# Uses only the Python standard library (wave, struct, math, random).
import wave, struct, math, random, os

SR = 22050  # sample rate
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")
os.makedirs(OUT, exist_ok=True)

def write_wav(name, samples):
    path = os.path.join(OUT, name)
    with wave.open(path, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        frames = b"".join(struct.pack("<h", max(-32767, min(32767, int(s * 32767)))) for s in samples)
        w.writeframes(frames)
    print("wrote", path, "(", len(samples), "samples )")

def sine(freq, t):
    return math.sin(2 * math.pi * freq * t)

# 1. alarm.wav  - rising/falling XP-style siren, loopable ~2s
alarm = []
for i in range(SR * 2):
    t = i / SR
    # sweep 600Hz <-> 1300Hz over 0.6s
    ph = (t % 1.2) / 1.2
    freq = 600 + 700 * (0.5 - 0.5 * math.cos(2 * math.pi * ph))
    s = 0.45 * math.sin(2 * math.pi * freq * t)
    # add a little square edge for harshness
    s += 0.15 * (1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0)
    alarm.append(s)
write_wav("alarm.wav", alarm)

# 2. phone_ring.wav  - classic old telephone ring (two tones, bursts), ~2s
phone = []
ring_dur = 2.0
for i in range(int(SR * ring_dur)):
    t = i / SR
    # ring burst pattern: 0.4s on, 0.2s off, repeated
    cycle = t % 0.6
    on = cycle < 0.4
    if on:
        # classic ring = 440Hz + 480Hz
        s = 0.35 * (math.sin(2 * math.pi * 440 * t) + math.sin(2 * math.pi * 480 * t)) / 2
    else:
        s = 0.0
    phone.append(s)
write_wav("phone_ring.wav", phone)

# 3. beep_xp.wav  - the friendly XP "ding" (two soft sine tones), short
beep = []
dur = 0.9
for i in range(int(SR * dur)):
    t = i / SR
    env = math.exp(-3.0 * t)  # decay
    s = 0.5 * env * (math.sin(2 * math.pi * 1318 * t) + 0.6 * math.sin(2 * math.pi * 1760 * t)) / 1.6
    beep.append(s)
write_wav("beep_xp.wav", beep)

# 4. broken_voice.wav  - glitchy distorted drone bed, loopable ~3s
random.seed(7)
broken = []
dur = 3.0
for i in range(int(SR * dur)):
    t = i / sr if False else i / SR
    # low drone
    s = 0.25 * math.sin(2 * math.pi * 70 * t)
    s += 0.15 * math.sin(2 * math.pi * 53 * t)
    # glitchy bitcrush crackle
    if random.random() < 0.06:
        s += random.uniform(-0.5, 0.5)
    # wobbly amplitude to feel "broken"
    s *= 0.6 + 0.4 * math.sin(2 * math.pi * 7 * t)
    # harsh clipping
    if s > 0.5: s = 0.5
    if s < -0.5: s = -0.5
    broken.append(s)
write_wav("broken_voice.wav", broken)

# 5. dial_up.wav  - creepy modem handshake-ish, ~3.5s
random.seed(3)
dial = []
dur = 3.5
for i in range(int(SR * dur)):
    t = i / sr if False else i / SR
    seg = t
    s = 0.0
    if t < 0.5:
        # initial handshake tone
        s = 0.25 * math.sin(2 * math.pi * 1100 * t)
    elif t < 1.2:
        # rising chirp
        f = 800 + (t - 0.5) * 3000
        s = 0.25 * math.sin(2 * math.pi * f * t)
    elif t < 2.0:
        # weird warble
        f = 1600 + 400 * math.sin(2 * math.pi * 18 * t)
        s = 0.22 * math.sin(2 * math.pi * f * t)
    else:
        # static + whine tail
        s = 0.15 * math.sin(2 * math.pi * 2200 * t) + random.uniform(-0.25, 0.25)
    dial.append(s)
write_wav("dial_up.wav", dial)

print("DONE")
