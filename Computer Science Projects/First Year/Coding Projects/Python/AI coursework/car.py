import pandas as pd #Imports
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

df_read = pd.read_csv("car.data", header=None) #Load dataset
df_columns = ["Buying", "Maint", "Doors", "Persons", "Lug Boot", "Safety", "Class"]
df_read.columns = df_columns #Define the columns and set them as dataFrame columns
df = pd.DataFrame(data=df_read)

#check the dataset for missing data, duplicates, categorical columns,... etc.
'''
print(df.info())
print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())
categorical_cols = df.select_dtypes(include=['object']).columns
print("Categorical Columns:", categorical_cols)
'''

#Change all of the categorical data to numerical data
df['Buying'] = df['Buying'].map({'low': 0, 'med': 1, 'high': 2, 'vhigh': 3})
df['Maint'] = df['Maint'].map({'low': 0, 'med': 1, 'high': 2, 'vhigh': 3})
df['Doors'] = df['Doors'].map({'2': 0, '3': 1, '4': 2, '5more': 3})
df['Persons'] = df['Persons'].map({'2': 0, '4': 1, 'more': 2})
df['Lug Boot'] = df['Lug Boot'].map({'small': 0, 'med': 1, 'big': 2})
df['Safety'] = df['Safety'].map({'low': 0, 'med': 1, 'high': 2})
df['Class'] = df['Class'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3})

#Check data again, make sure data is clean
'''
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
'''
print(df.head())

#Training 67%, Testing 33%
X = df.drop('Class', axis=1)
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

#Verify the training/testing splits shape
'''
print("X_train Shape:", X_train.shape)
print("X_test Shape:", X_test.shape)
print("y_train Shape:", y_train.shape)
print("y_test Shape:", y_test.shape)
'''

#Graphs to figure out hardest and easiest class to recognize
sns.countplot(x=df['Class'])
sns.pairplot(df, hue="Class")
plt.show()
#Same as previous comment
#Do not have both running
'''
corr = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.show()
print(corr["Class"].abs().sort_values(ascending=False))
'''

#Entropy computation
def compute_entropy(target):
    unique, counts = np.unique(target, return_counts=True)
    samples = len(target)
    probs = counts/samples
    entropy_value = -np.sum(p * np.log2(p) for p in probs if p > 0)
    return entropy_value

#Information Gain computation
def compute_information_gain(feature_column, target):
    total_entropy = compute_entropy(target)
    unique_values = np.unique(feature_column)
    best_gain = -1
    best_threshold = None
    for i in range(len(unique_values) - 1):
        threshold = (unique_values[i] + unique_values[i + 1]) / 2
        left_split = target[feature_column <= threshold]
        right_split = target[feature_column > threshold]
        weighted_entropy = (len(left_split) / len(target)) * compute_entropy(left_split) + \
                            (len(right_split) / len(target)) * compute_entropy(right_split)
        gain = total_entropy - weighted_entropy
        if gain > best_gain:
            best_gain = gain
            best_threshold = threshold
    return best_gain, best_threshold

#Computation of the information gain for display
info_gains = []
for feature in X_train.columns:
    unique_values = np.unique(X_train[feature])
    if len(unique_values) > 1:
        gain, threshold = compute_information_gain(X_train[feature], y_train)
        info_gains.append((feature, gain, threshold))

#Sort features by Information Gain (highest first)
info_gains.sort(key=lambda x: x[1], reverse=True)

#Print results in a table format
print("\n=== Information Gain per Feature ===")
print(f"{'Feature':<12} {'Information Gain':<20} {'Best Threshold'}")
print("=" * 50)
for feature, gain, threshold in info_gains:
    print(f"{feature:<12} {gain:<20.4f} {threshold if threshold is not None else 'N/A'}")

#Sorted features, thresholds and prints for display
sorted_features = [feature for feature, _, _ in info_gains]
best_thresholds = {feature: threshold for feature, _, threshold in info_gains}
best_feature = sorted_features[0]
best_threshold = best_thresholds[best_feature]
second_best_feature = sorted_features[1]
second_best_threshold = best_thresholds[second_best_feature]
third_best_feature = sorted_features[2]
third_best_threshold = best_thresholds[third_best_feature]
print(sorted_features)
print("Best Feature for First Split:", best_feature, "at threshold", best_threshold)
print("Second Best Feature:", second_best_feature, "at threshold", second_best_threshold)
print("Third Best Feature:", third_best_feature, "at threshold", third_best_threshold)

#Classifcation to implement decision tree
def classify(instance):
    if (instance["Safety"] == 2 and instance["Persons"] >= 1 and instance["Buying"] <= 1 \
        and instance["Lug Boot"] >= 1 and instance["Maint"] <= 2):
        return "vgood"
    if (instance["Safety"] >= 1 and instance["Persons"] >= 2 and instance["Maint"] <= 1):
        return "good"
    if instance[best_feature] <= best_threshold:
        return "unacc"
    if instance[second_best_feature] <= second_best_threshold:
        return "unacc"
    if instance["Lug Boot"] >= 1:
        return "acc"
    if instance[third_best_feature] <= third_best_threshold:
        if instance["Doors"] <= 1:
            return "unacc"
        return "acc"
    return "unacc"

#Maps to change categorical to numerical and vice-versa
cat_map = {0: "unacc", 1: "acc", 2: "good", 3: "vgood"}
num_map = {"unacc": 0, "acc": 1, "good": 2, "vgood": 3}
y_test_cat = y_test.map(cat_map)

#Predictions and accuracy calculation
predictions = X_test.apply(classify, axis=1)
accuracy = np.mean(predictions == y_test_cat)
print("\nDecision Tree Accuracy:", accuracy)
