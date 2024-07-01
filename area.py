import pandas as pd
import lightningchart as lc
# Place your license key here
lc.set_license('my_license_key')
# Read sea level data (replace with your dataset path)
sea_level_data = pd.read_csv('/sealevel.csv')


sea_level_data['Year'] = pd.to_datetime(sea_level_data['Year'], format='%Y')

average_data = sea_level_data.groupby(sea_level_data['Year'].dt.year)['GMSL_GIA'].mean().reset_index()

# Prepare data for the Area Chart
x_values = average_data['Year'].tolist()
y_values = average_data['GMSL_GIA'].tolist()
# Create the Area Chart
chart = lc.ChartXY(
    theme=lc.Themes.White,
    title='Global Mean Sea Level (GMSL) by Year'
)
# Add Area Series
area_series = chart.add_bipolar_area_series()
area_series.add(x_values, y_values)
area_series.set_name('GMSL')
# Customize x-axis to handle categorical data
x_axis = chart.get_default_x_axis()
x_axis.set_title('Year')
x_axis.set_interval(min(x_values), max(x_values))
x_axis.set_decimal_precision(0)
# Customize y-axis
y_axis = chart.get_default_y_axis()
y_axis.set_title('GMSL (mm)')
# Open the chart
chart.open()
