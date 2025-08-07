from scapy.layers.inet import IP, TCP, UDP
import pandas as pd
import os
import pickle

def extract_features(packet):
    if IP in packet:
        size = len(packet)
        is_tcp = 1 if TCP in packet else 0
        is_udp = 1 if UDP in packet else 0
        return [size, is_tcp, is_udp]
    return None

def load_model():
    with open('model.pkl', 'rb') as f:
        return pickle.load(f)

def log_threat(features):
    columns = ['packet_size', 'is_tcp', 'is_udp']
    df = pd.DataFrame([features], columns=columns)
    os.makedirs('logs', exist_ok=True)
    path = 'logs/threat_log.csv'
    df.to_csv(path, mode='a', header=not os.path.exists(path), index=False)
