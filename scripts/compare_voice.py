
from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np
import os
from pathlib import Path
import sys

def get_embedding(file_path):
    wav = preprocess_wav(Path(file_path))
    encoder = VoiceEncoder()
    embed = encoder.embed_utterance(wav)
    return embed

def compare_voices(file1, file2):
    emb1 = get_embedding(file1)
    emb2 = get_embedding(file2)
    similarity = np.inner(emb1, emb2)
    return similarity

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python compare_voice.py audio1.wav audio2.wav")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    similarity_score = compare_voices(file1, file2)
    print(f"Similaridad entre voces: {similarity_score:.4f}")
