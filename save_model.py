from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd

X = pd.DataFrame({
    'packet_size': [60, 500, 1500, 100, 2000],
    'is_tcp': [1, 1, 0, 0, 1],
    'is_udp': [0, 0, 1, 1, 0]
})

y = [0, 1, 1, 0, 1]

model = RandomForestClassifier()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
