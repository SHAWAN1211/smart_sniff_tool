from scapy.all import sniff
from utils import extract_features, load_model, log_threat

model = load_model()

def analyze(packet):
    features = extract_features(packet)
    if features:
        result = model.predict([features])[0]
        if result == 1:
            print("⚠️ ALERT: Suspicious packet detected!")
            log_threat(features)

print("🔍 SmartSniff Started on Ubuntu... (press Ctrl+C to stop)")
sniff(prn=analyze, store=False)
