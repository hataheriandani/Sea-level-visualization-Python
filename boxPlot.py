import pandas as pd
import lightningchart as lc
lc.set_license('my_license_key')
# Load the datasets
sea_level_data = pd.read_csv('/sealevel.csv')
# global_sea_level_data = pd.read_csv('C:/Users/Taheri/Desktop/darsi/m8.5/workplacement/project 3/sea-level.csv')

# Preprocess the data
sea_level_data['Year'] = pd.to_datetime(sea_level_data['Year'], format='%Y')
# Group data by year and prepare box plot data
grouped_data = sea_level_data.groupby(sea_level_data['Year'].dt.year)['GMSL_GIA'].apply(list).tolist()
years = sea_level_data['Year'].dt.year.unique().tolist()
# Create Box Plot
chart = lc.BoxPlot(
    data=grouped_data,
    theme=lc.Themes.White,
    title='Distribution of GMSL by Year',
    xlabel='Year',
    ylabel='GMSL (mm)'
)
# Set x-axis labels to years using custom ticks
x_axis = chart.get_default_x_axis()
# Assuming addCustomTick is the correct method
for i, year in enumerate(years):
    custom_tick = x_axis.add_custom_tick()
    custom_tick.set_value(i * 2)
    custom_tick.set_text(year)
    
chart.open()
