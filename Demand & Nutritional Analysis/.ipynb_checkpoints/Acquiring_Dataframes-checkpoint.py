import pandas as pd
import numpy as np

# 2005-06 Data
# Prices Dataframe
ugd1_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2005-06).csv')
ugd1_p0 = ugd1_p0[ugd1_p0["u"] == "Kg"]
ugd1_p = pd.pivot_table(ugd1_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures Dataframe
ugd1_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2005-06).csv')
ugd1_x0['i'] = ugd1_x0['i'].astype(str)
ugd1_x = pd.pivot_table(ugd1_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption Dataframe
ugd1_x_long = ugd1_x.stack().reset_index(name="Expenditure")
ugd1_p_long = ugd1_p0
ugd1_c = ugd1_x_long.merge(ugd1_p_long, on=["j", "t", "m"], how="left")
ugd1_c["Consumption"] = ugd1_c["Expenditure"] / ugd1_c["price"]
ugd1_c = ugd1_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics Dataframe
ugd_z0 = pd.read_csv("Data Files/Uganda - Household Characteristics.csv")
ugd1_z = ugd_z0[ugd_z0['t'] == '2005-06']
ugd1_z = ugd1_z.set_index(['i','t','m'])
ugd1_z.columns.name = 'k'
ugd1_z.fillna(0, inplace=True)

# 2009-10 Data
# Prices
ugd2_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2009-10).csv')
ugd2_p0 = ugd2_p0[ugd2_p0["u"] == "Kg"]
ugd2_p = pd.pivot_table(ugd2_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures
ugd2_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2009-10).csv')
ugd2_x0['i'] = ugd2_x0['i'].astype(str)
ugd2_x = pd.pivot_table(ugd2_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption
ugd2_x_long = ugd2_x.stack().reset_index(name="Expenditure")
ugd2_p_long = ugd2_p0
ugd2_c = ugd2_x_long.merge(ugd2_p_long, on=["j", "t", "m"], how="left")
ugd2_c["Consumption"] = ugd2_c["Expenditure"] / ugd2_c["price"]
ugd2_c = ugd2_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics
ugd2_z = ugd_z0[ugd_z0['t'] == '2009-10']
ugd2_z = ugd2_z.set_index(['i','t','m'])
ugd2_z.columns.name = 'k'
ugd2_z.fillna(0, inplace=True)

# 2010-11 Data
# Prices
ugd3_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2010-11).csv')
ugd3_p0 = ugd3_p0[ugd3_p0["u"] == "Kg"]
ugd3_p = pd.pivot_table(ugd3_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures
ugd3_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2010-11).csv')
ugd3_x0['i'] = ugd3_x0['i'].astype(str)
ugd3_x = pd.pivot_table(ugd3_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption
ugd3_x_long = ugd3_x.stack().reset_index(name="Expenditure")
ugd3_p_long = ugd3_p0
ugd3_c = ugd3_x_long.merge(ugd3_p_long, on=["j", "t", "m"], how="left")
ugd3_c["Consumption"] = ugd3_c["Expenditure"] / ugd3_c["price"]
ugd3_c = ugd3_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics
ugd3_z = ugd_z0[ugd_z0['t'] == '2010-11']
ugd3_z = ugd3_z.set_index(['i','t','m'])
ugd3_z.columns.name = 'k'
ugd3_z.fillna(0, inplace=True)

# 2011-12 Data
# Prices
ugd4_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2011-12).csv')
ugd4_p0 = ugd4_p0[ugd4_p0["u"] == "Kg"]
ugd4_p = pd.pivot_table(ugd4_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures
ugd4_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2011-12).csv')
ugd4_x0['i'] = ugd4_x0['i'].astype(str)
ugd4_x = pd.pivot_table(ugd4_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption
ugd4_x_long = ugd4_x.stack().reset_index(name="Expenditure")
ugd4_p_long = ugd4_p0
ugd4_c = ugd4_x_long.merge(ugd4_p_long, on=["j", "t", "m"], how="left")
ugd4_c["Consumption"] = ugd4_c["Expenditure"] / ugd4_c["price"]
ugd4_c = ugd4_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics
ugd4_z = ugd_z0[ugd_z0['t'] == '2011-12']
ugd4_z = ugd4_z.set_index(['i','t','m'])
ugd4_z.columns.name = 'k'
ugd4_z.fillna(0, inplace=True)

# 2013-14 Data
# Prices
ugd5_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2013-14).csv')
ugd5_p0 = ugd5_p0[ugd5_p0["u"] == "Kg"]
ugd5_p = pd.pivot_table(ugd5_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures
ugd5_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2013-14).csv')
ugd5_x0['i'] = ugd5_x0['i'].astype(str)
ugd5_x = pd.pivot_table(ugd5_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption
ugd5_x_long = ugd5_x.stack().reset_index(name="Expenditure")
ugd5_p_long = ugd5_p0
ugd5_c = ugd5_x_long.merge(ugd5_p_long, on=["j", "t", "m"], how="left")
ugd5_c["Consumption"] = ugd5_c["Expenditure"] / ugd5_c["price"]
ugd5_c = ugd5_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics
ugd5_z = ugd_z0[ugd_z0['t'] == '2013-14']
ugd5_z = ugd5_z.set_index(['i','t','m'])
ugd5_z.columns.name = 'k'
ugd5_z.fillna(0, inplace=True)

# 2015-16 Data
# Prices
ugd6_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2015-16).csv')
ugd6_p = pd.pivot_table(ugd6_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures
ugd6_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2015-16).csv')
ugd6_x = pd.pivot_table(ugd6_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption
ugd6_x_long = ugd6_x.stack().reset_index(name="Expenditure")
ugd6_p_long = ugd6_p0
ugd6_c = ugd6_x_long.merge(ugd6_p_long, on=["j", "t", "m"], how="left")
ugd6_c["Consumption"] = ugd6_c["Expenditure"] / ugd6_c["price"]
ugd6_c = ugd6_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics
ugd6_z = ugd_z0[ugd_z0['t'] == '2015-16']
ugd6_z = ugd6_z.set_index(['i','t','m'])
ugd6_z.fillna(0, inplace=True)
ugd6_z.columns.name = 'k'

# 2018-19 Data
# Prices
ugd7_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2018-19).csv')
ugd7_p0 = ugd7_p0[ugd7_p0["u"] == "Kg"]
ugd7_p = pd.pivot_table(ugd7_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures
ugd7_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2018-19).csv')
ugd7_x0['i'] = ugd7_x0['i'].astype(str)
ugd7_x = pd.pivot_table(ugd7_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption
ugd7_x_long = ugd7_x.stack().reset_index(name="Expenditure")
ugd7_p_long = ugd7_p0
ugd7_c = ugd7_x_long.merge(ugd7_p_long, on=["j", "t", "m"], how="left")
ugd7_c["Consumption"] = ugd7_c["Expenditure"] / ugd7_c["price"]
ugd7_c = ugd7_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics
ugd7_z = ugd_z0[ugd_z0['t'] == '2018-19']
ugd7_z = ugd7_z.set_index(['i','t','m'])
ugd7_z.columns.name = 'k'
ugd7_z.fillna(0, inplace=True)

# 2019-20 Data
# Prices
ugd8_p0 = pd.read_csv('Data Files/Uganda - Food Prices (2019-20).csv')
ugd8_p0 = ugd8_p0[ugd8_p0["u"] == "Kg"]
ugd8_p = pd.pivot_table(ugd8_p0, values="price", index=["j","u"], columns=["t","m"] , aggfunc="median")
# Food Expenditures
ugd8_x0 = pd.read_csv('Data Files/Uganda - Food Expenditures (2019-20).csv')
ugd8_x0['i'] = ugd8_x0['i'].astype(str)
ugd8_x = pd.pivot_table(ugd8_x0, values="Expenditure", index=["i","t","m"], columns="j" , aggfunc="median")
# Consumption
ugd8_x_long = ugd8_x.stack().reset_index(name="Expenditure")
ugd8_p_long = ugd8_p0
ugd8_c = ugd8_x_long.merge(ugd8_p_long, on=["j", "t", "m"], how="left")
ugd8_c["Consumption"] = ugd8_c["Expenditure"] / ugd8_c["price"]
ugd8_c = ugd8_c.pivot_table(values="Consumption", index=["i","t","m","u"], columns="j", aggfunc="sum")
# HH Characteristics
ugd8_z = ugd_z0[ugd_z0['t'] == '2019-20']
ugd8_z = ugd8_z.set_index(['i','t','m'])
ugd8_z.columns.name = 'k'
ugd8_z.fillna(0, inplace=True)

#FCT and RDI
#FCT
ugd_fct = pd.read_csv('Data Files/Uganda - FCT.csv')
ugd_fct = ugd_fct.rename(columns={"index":"j"}).set_index(["j"])
ugd_fct.columns.name = 'n'
#RDI
ugd_rdi = pd.read_csv('Data Files/Uganda - RDA.csv')
ugd_rdi = ugd_rdi.set_index(["n"])
ugd_rdi.columns.name = 'k'


