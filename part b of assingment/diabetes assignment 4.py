import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
diabetes_data = pd.read_csv("diabetes.csv")

# a) Random sample of 25 observations
np.random.seed(123)  # setting seed for reproducibility
sample = diabetes_data.sample(n=25)
sample_mean_glucose = sample['Glucose'].mean()
sample_max_glucose = sample['Glucose'].max()

# Population statistics
population_mean_glucose = diabetes_data['Glucose'].mean()
population_max_glucose = diabetes_data['Glucose'].max()

# Comparison using charts
plt.bar(['Sample Mean', 'Population Mean'], [sample_mean_glucose, population_mean_glucose], color=['blue', 'green'])
plt.title('Mean Glucose Comparison')
plt.ylabel('Glucose')
plt.show()

plt.bar(['Sample Max', 'Population Max'], [sample_max_glucose, population_max_glucose], color=['blue', 'green'])
plt.title('Max Glucose Comparison')
plt.ylabel('Glucose')
plt.show()

# b) 98th percentile of BMI
sample_98th_percentile_bmi = np.percentile(sample['BMI'], 98)
population_98th_percentile_bmi = np.percentile(diabetes_data['BMI'], 98)

# Comparison using charts
plt.bar(['Sample 98th Percentile', 'Population 98th Percentile'], [sample_98th_percentile_bmi, population_98th_percentile_bmi], color=['blue', 'green'])
plt.title('98th Percentile BMI Comparison')
plt.ylabel('BMI')
plt.show()

# c) Bootstrap samples
bootstrap_means = []
bootstrap_stds = []
bootstrap_percentiles = []

for _ in range(500):
    bootstrap_sample = diabetes_data.sample(n=150, replace=True)
    bootstrap_means.append(bootstrap_sample['BloodPressure'].mean())
    bootstrap_stds.append(bootstrap_sample['BloodPressure'].std())
    bootstrap_percentiles.append(np.percentile(bootstrap_sample['BloodPressure'], 95))

# Population statistics
population_mean_bp = diabetes_data['BloodPressure'].mean()
population_std_bp = diabetes_data['BloodPressure'].std()
population_percentile_bp = np.percentile(diabetes_data['BloodPressure'], 95)

# Comparison using charts
plt.hist(bootstrap_means, bins=30, alpha=0.5, color='blue', label='Bootstrap Samples')
plt.axvline(x=population_mean_bp, color='green', linestyle='dashed', linewidth=2, label='Population Mean')
plt.title('Bootstrap Sample Means vs Population Mean')
plt.xlabel('Blood Pressure')
plt.legend()
plt.show()

plt.hist(bootstrap_stds, bins=30, alpha=0.5, color='blue', label='Bootstrap Samples')
plt.axvline(x=population_std_bp, color='green', linestyle='dashed', linewidth=2, label='Population STD')
plt.title('Bootstrap Sample STDs vs Population STD')
plt.xlabel('Blood Pressure')
plt.legend()
plt.show()

plt.hist(bootstrap_percentiles, bins=30, alpha=0.5, color='blue', label='Bootstrap Samples')
plt.axvline(x=population_percentile_bp, color='green', linestyle='dashed', linewidth=2, label='Population 95th Percentile')
plt.title('Bootstrap Sample 95th Percentiles vs Population 95th Percentile')
plt.xlabel('Blood Pressure')
plt.legend()
plt.show()
