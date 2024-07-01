import pandas as pd
import lightningchart as lc
# Place your license key here
lc.set_license('my_license_key')
# Read sea level data (replace with your dataset path)
sea_level_data = pd.read_csv('/sealevel.csv')
# Convert 'Year' column to datetime format
sea_level_data['Year'] = pd.to_datetime(sea_level_data['Year'], format='%Y')
# Calculate average sea level for each year
average_data = sea_level_data.groupby(sea_level_data['Year'].dt.year)['GMSL_GIA'].mean().reset_index()
# Prepare data for the Bar Chart
data = []
for index, row in average_data.iterrows():
    data.append({'category': str(int(row['Year'])), 'value': row['GMSL_GIA']})
# Create a Bar Chart
bar_chart = lc.BarChart(
    vertical=True,  # Vertical orientation of bars
    theme=lc.Themes.White,
    title='Average Global Mean Sea Level (GMSL) by Year'
)
# Disable sorting (optional)
bar_chart.set_sorting('disabled')
# Set data for the Bar Chart
bar_chart.set_data(data)
# Set the margin around each bar along category axis as percentage of bar thickness
bar_chart.set_bars_margin(0.1)  # Set margin to 10%
# Open the Bar Chart
bar_chart.open()
