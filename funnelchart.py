import pandas as pd
import lightningchart as lc
# Place your license key here
lc.set_license('my_license_key')

# Read sea level data
sea_level_data = pd.read_csv('/sealevel.csv')

# Convert 'Year' column to datetime format
sea_level_data['Year'] = pd.to_datetime(sea_level_data['Year'], format='%Y')
# Specific years of interest
years_of_interest = [2005, 2009, 2013, 2017, 2021]
# Filter data for specific years and calculate average sea level
filtered_data = sea_level_data[sea_level_data['Year'].dt.year.isin(years_of_interest)]
average_data = filtered_data.groupby(filtered_data['Year'].dt.year)['GMSL_GIA'].mean().reset_index()
# Sort data by 'value' (GMSL_GIA) in descending order
average_data_sorted = average_data.sort_values(by='GMSL_GIA', ascending=False)
# Prepare data for the Funnel Chart
data = []
for index, row in average_data_sorted.iterrows():
    data.append({'name': str(int(row['Year'])), 'value': row['GMSL_GIA']})
# Create a Funnel Chart
funnel_chart = lc.FunnelChart(
    slice_mode='height',  # Adjust slice_mode as per your data characteristics
    theme=lc.Themes.White,
    title='Average Global Mean Sea Level (GMSL) Funnel Chart for Specific Years'
)
# Add slices to the Funnel Chart
funnel_chart.add_slices(data)
# Add legend
funnel_chart.add_legend().add(funnel_chart).set_title('Yearly Average Sea Level Changes')
# Open the Funnel Chart
funnel_chart.open()
