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
#         'Men (%)': [62, 86, 33],
#         'Women (%)': [55, 31, 12],
#         'Other (%)': [25, 11, 32],
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
# props.GridProp(dataset, ["Men (%)","Women (%)","Other (%)"], labels=True, title="Country", description="Capital")