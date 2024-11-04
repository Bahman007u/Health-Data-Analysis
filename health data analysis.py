import numpy as np
import matplotlib.pyplot as plt

# 1. Data Collection and Preparation
num_patients = 100
np.random.seed(0)

# Simulate health data: [Patient ID, Age, Gender, Blood Pressure, Cholesterol Level, Heart Rate]
# Gender: 0 for Male, 1 for Female
patient_ids = np.arange(1, num_patients + 1)
ages = np.random.randint(20, 80, num_patients)
genders = np.random.randint(0, 2, num_patients)
blood_pressures = np.random.randint(110, 180, num_patients)
cholesterol_levels = np.random.randint(150, 300, num_patients)
heart_rates = np.random.randint(60, 100, num_patients)

# Combine data into a single array
data = np.column_stack((patient_ids, ages, genders, blood_pressures, cholesterol_levels, heart_rates))

# 2. Data Manipulation and Cleaning
# Remove entries where blood pressure is outside a normal range (e.g., 110-180)
filtered_data = data[(data[:, 3] >= 110) & (data[:, 3] <= 180)]

# 3. Analyzing and Visualizing Patient Demographics

# Age Distribution - Histogram
ages = filtered_data[:, 1]  # Extract ages
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.title('Age Distribution of Patients')
plt.show()

# Gender Distribution - Bar Plot
genders = filtered_data[:, 2]  # Extract genders
male_count = np.sum(genders == 0)
female_count = np.sum(genders == 1)

plt.bar(['Male', 'Female'], [male_count, female_count], color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Number of Patients')
plt.title('Gender Distribution')
plt.show()

# 4. Scatter Plots for Correlation Analysis

# Scatter Plot: Age vs. Blood Pressure
ages = filtered_data[:, 1]
blood_pressures = filtered_data[:, 3]

plt.scatter(ages, blood_pressures, color='purple', alpha=0.6)
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.title('Age vs. Blood Pressure')
plt.show()

# Scatter Plot: Cholesterol Level vs. Blood Pressure
cholesterol_levels = filtered_data[:, 4]

plt.scatter(cholesterol_levels, blood_pressures, color='green', alpha=0.6)
plt.xlabel('Cholesterol Level')
plt.ylabel('Blood Pressure')
plt.title('Cholesterol Level vs. Blood Pressure')
plt.show()