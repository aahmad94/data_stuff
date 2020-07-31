import pandas as pd

file_to_load = "purchase_data.csv"
purchase_df = pd.read_csv(file_to_load)
purchase_df.set_index("Purchase ID")

item_ct_series = pd.DataFrame(purchase_df.groupby("Item ID")["Item ID"].count())
item_ct_series.columns = ["Item Ct"]

# Join new "Item Ct" column
purchase_df = purchase_df.join(item_ct_series, on="Item ID")

# Generate series for product of "Price" and "Item Ct" columns
total_purchase_value_series = pd.Series(purchase_df["Price"]*purchase_df["Item Ct"], name='Total Purchase Value')

# Drop duplicates of "Item ID" column
purchase_df = pd.concat([purchase_df, total_purchase_value_series], axis=1).drop_duplicates(subset=["Item ID"])

# Sort by "Total Purchase Value" descending and get only first  5 rows 
purchase_df = purchase_df.sort_values(["Total Purchase Value"], ascending=False).iloc[0:5]
print(purchase_df[["Item ID", "Item Name", "Item Ct", "Price", "Total Purchase Value"]])