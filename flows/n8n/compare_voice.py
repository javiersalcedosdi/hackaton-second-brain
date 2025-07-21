from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import os
import sys
from scipy.spatial.distance import cosine
import json

reference_dir = "reference_voices/"
encoder = VoiceEncoder()
references = {}

for file in os.listdir(reference_dir):
    if file.endswith(".wav"):
        wav = preprocess_wav(os.path.join(reference_dir, file))
        embed = encoder.embed_utterance(wav)
        references[file.replace(".wav", "")] = embed

target_wav = preprocess_wav(sys.argv[1])
target_embed = encoder.embed_utterance(target_wav)

results = {name: float(1 - cosine(ref, target_embed)) for name, ref in references.items()}
print(json.dumps(results, indent=2))