import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from detector.analyzer import extract_features
df = pd.read_csv('dataset_phishing.csv')
print(df.shape)
print(df.columns)
print(df['status'].value_counts())
features_list = []
labels = []
for index, row in df.iterrows():
    features = extract_features(row['url'])
    features_list.append(list(features.values()))
    labels.append(1 if row['status'] == 'phishing' else 0)
X_train, X_test, y_train, y_test = train_test_split(features_list, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print('done')