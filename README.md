# **Project 4: Team Jennifer Doudna**

### **Objective**  
Analyze the nutrition and cost - demand of current system in Uganda from 2019-2020. Explore how agricultural subsidies and fortification can help meet nutritional needs.

---

### **Group Members**
- Celeste Basken cbasken@berkeley.edu github: celestebasken
- Carmen Vega carmenvega@berkeley.edu github: carmen4vega
- Emily Wu wuemily@berkeley.edu github: wuemilyy
- Xiaolong Wang justinwx@berkeley.edu github: Justinwxl 
- Leona Katibah leonakatibah@berkeley.edu github: leonakatibah
- Junsu Yi yijunsu@berkeley.edu github: jjjunsu

---

### **Project Structure**

#### 📁 **Data Files**  
Contains all CSV files used in our analysis, including raw and cleaned datasets from various Uganda surveys.

#### 📁 **Nutrient Data**  
Includes saved nutrient dataframes generated from our analysis for each year of data. These were used to assess dietary quality and nutritional trends over time.

#### 📁 **RGSN Files**  
Stores regression-ready data for each year, used in our statistical modeling and demand estimation analyses.

#### 📄 **Nutritional_Analysis_19_20.ipynb**  
Contains analysis for
- Determining the Most Consumed Foods
- Nutritional Adequacy of Diet: Determining Which Nutrients Are Lacking 
- Nutritional Analysis: Looking at the Most-Deficient Nutrients
- How can we increase these most limited nutrients by increasing the consumption of existing foods?
- Which food items are available to subsidize?
- Determining Subsidies for Vitamin E and Vitamin K-rich foods, and associated demand curves

#### 📄 **Acquiring Dataframes.py**  
Contains code for acquiring prices, food expenditures, consumption, household characteristics, recommended daily intakes, and a food conversion table.

#### 📄 **Cost Analysis.ipynb**  
Analysis of Marshallian and Hicksian demand curves, compensating variation, and deadweight loss for subsidized goods (specifically tomatoes).

#### 📄 **Estimate Demand Systems.ipynb**
Includes code for defining a regression to define our data, followed by an estimate demand system analysis. Our demand system focuses on the following parameters: (Relative) Income Elasticity, Demand and Household Composition, and Welfare. It also analyzes demand and utility.                                                                                        
                                                                                        
#### 📄 **Nutrient Demands.ipynb**  
Code to determine and visualize the nutrient demands for our population: analyzing the nutritional needs of households, and how nutritional adequacy of a deficient nutrient and price of a good interact.                                                                                                                                                                                           

#### 📄 **Unit Tests.ipynb**  
File containing unit tests, in the form of assert statements, to enforce the integrity of functions defined and used in cost analysis.                                                                                                                                        