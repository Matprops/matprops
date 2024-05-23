# # Pandas - DataFrame Support
# import pandas as pd
#
# # Matprops
# from matprops import props
#
# # Creating a dataframe with the help of pandas
# dataset = pd.DataFrame(
#     {
#         'Country': ['France', 'Germany', 'United Arab Emirates'],
#         'Men (%)': [60, 80, 30],
#         'Women (%)': [50, 30, 80],
#         'Other (%)': [20, 60, 100],
#         'Capital': ['Paris', 'Berlin', 'Mecca']
#     }
# )
#
# # Changing the limits
# # Limit : 0 -> 1
# dataset["Men (%)"] = dataset["Men (%)"]/100
# dataset["Women (%)"] = dataset["Women (%)"]/100
# dataset["Other (%)"] = dataset["Other (%)"]/100
#
# props.AreaProp(dataset, ["Men (%)","Women (%)","Other (%)"], labels=True, title="Country", description="Capital")