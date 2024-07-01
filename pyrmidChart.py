import pandas as pd
import lightningchart as lc
# Place your license key here
lc.set_license('my_license_key')
# Read sea level data
sea_level_data = pd.read_csv('/sealevel.csv')
sea_level_data['Year'] = sea_level_data['Year'].astype(int)
# Convert 'Year' column to datetime format
sea_level_data['Year'] = pd.to_datetime(sea_level_data['Year'], format='%Y')
# Calculate average sea level for the last 5 years
last_six_years = sea_level_data['Year'].dt.year.max() - 4
filtered_data = sea_level_data[sea_level_data['Year'].dt.year >= last_six_years]
average_data = filtered_data.groupby(filtered_data['Year'].dt.year)['GMSL_GIA'].mean().reset_index()
# Prepare data for the Pyramid Chart
data = []
for index, row in average_data.iterrows():
    data.append({'name': str(int(row['Year'])), 'value': row['GMSL_GIA']})
print(data)
# Create a Pyramid Chart
chart = lc.PyramidChart(
    slice_mode='height',  # Adjust slice_mode as per your data characteristics
    theme=lc.Themes.White,
    title='Average Global Mean Sea Level (GMSL) for Last 5 Years'
)
# Add slices to the Pyramid Chart
chart.add_slices(data)
# Add legend
chart.add_legend().add(chart).set_title('Yearly Average Sea Level Changes')
# Open the chart
chart.open()