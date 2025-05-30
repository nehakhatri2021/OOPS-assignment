# -*- coding: utf-8 -*-
"""Statistics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZR2GriRX7trDWK3B-g9o-qDK7McDMUqX

### **1. Types of Data: Qualitative vs Quantitative**

* **Qualitative Data**: Descriptive and categorical.

  * *Examples*: Eye color, gender, car brand.
  * **Scales**:

    * **Nominal**: Categories with no order (e.g., gender, city).
    * **Ordinal**: Categories with an order (e.g., rankings, satisfaction levels).

* **Quantitative Data**: Numerical and measurable.

  * *Examples*: Age, height, income.
  * **Scales**:

    * **Interval**: Numeric data without a true zero (e.g., temperature in °C).
    * **Ratio**: Numeric data with a true zero (e.g., weight, distance).

---

### **2. Measures of Central Tendency**

* **Mean**: Average of all values.

  * *Use when*: Data is normally distributed.
  * *Example*: Average marks in a test.
* **Median**: Middle value in sorted data.

  * *Use when*: Data is skewed or has outliers.
  * *Example*: Median income in a city.
* **Mode**: Most frequently occurring value.

  * *Use when*: You want to know the most common category.
  * *Example*: Most popular car color sold.

---

### **3. Dispersion: Variance and Standard Deviation**

* **Dispersion**: Describes how spread out the data is.
* **Variance**: Average of squared differences from the mean.
* **Standard Deviation (SD)**: Square root of variance; more interpretable since it’s in the same unit as the data.

  * *Higher SD = more spread out data*.

---

### **4. Box Plot**

* **Box Plot**: A graphical summary of data distribution.

  * Shows:

    * Median (line in box)
    * Quartiles (box edges)
    * Whiskers (spread)
    * Outliers (dots)
  * *Helps identify*: Skewness, spread, and outliers.

---

### **5. Random Sampling**

* **Random Sampling**: Selecting a subset from a population where each individual has an equal chance.

  * *Importance*: Reduces bias, ensures results are generalizable.
  * *Used in*: Surveys, experiments, hypothesis testing.

---

### **6. Skewness and Its Types**

* **Skewness**: Measure of asymmetry in data.

  * **Positive Skew**: Tail on right; mean > median.
  * **Negative Skew**: Tail on left; mean < median.
  * **Effect**: Impacts which measure of central tendency to use and statistical test validity.

---

### **7. Interquartile Range (IQR) and Outliers**

* **IQR = Q3 - Q1**: Middle 50% of data.
* **Outlier Rule**: Any value below Q1 − 1.5×IQR or above Q3 + 1.5×IQR is an outlier.

  * *Used in*: Box plots, data cleaning.

---

### **8. Binomial Distribution Conditions**

* Fixed number of trials (**n**).
* Each trial has 2 outcomes (success/failure).
* Probability of success (**p**) is constant.
* Trials are independent.

  * *Example*: Flipping a coin 10 times.

---

### **9. Normal Distribution & Empirical Rule**

* **Normal Distribution**: Symmetric bell curve.
* **Empirical Rule**:

  * 68% of data within 1 SD of mean.
  * 95% within 2 SD.
  * 99.7% within 3 SD.
  * *Used in*: Z-scores, quality control.

---

### **10. Poisson Process Example**

* **Poisson Distribution**: Models number of events in a fixed time/space.

  * *Example*: Number of customer arrivals per hour.
  * *Formula*:

    $$
    P(x; \lambda) = \frac{e^{-\lambda} \lambda^x}{x!}
    $$
  * *If* λ = 4 (avg 4 customers/hour), *find P(2)*:

    $$
    P(2) = \frac{e^{-4} \cdot 4^2}{2!} ≈ 0.1465
    $$

---

### **11. Random Variables**

* **Random Variable**: Numeric outcome of a random process.

  * **Discrete**: Countable (e.g., number of calls).
  * **Continuous**: Measurable (e.g., height, weight).

---

### **12. Covariance vs Correlation**

```python
import pandas as pd

data = {'x': [2, 4, 6, 8], 'y': [1, 3, 5, 7]}
df = pd.DataFrame(data)

cov = df.cov().iloc[0, 1]
corr = df.corr().iloc[0, 1]

print("Covariance:", cov)
print("Correlation:", corr)
```

* **Covariance**: Indicates direction of relationship.
* **Correlation**: Normalized value (-1 to 1), shows strength and direction.
"""