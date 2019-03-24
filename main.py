from bokeh.plotting import figure, output_file, show, ColumnDataSource, save
import pandas as pd
# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]

## Read csv
df = pd.read_csv("cars.csv")

# Create a ColumnDataSource from the dataframe
source = ColumnDataSource(df)

# set the output_file
output_file("index.html")

# Car list
car_list = source.data['Car'].tolist()

# Add plot
p = figure(
    y_range = car_list,
    plot_height=600,
    title = 'Cars with Top Horsepower',
    x_axis_label = "Horsepower",
    tools="pan, box_select, zoom_in, zoom_out, save, reset"
)

# Let's render our glyph
p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    color='orange',
    fill_alpha=0.5,
    source=source
)

## let's go ahead and show our results
# show(p)

# to avoid opening new tabs everytime we run the show command
save(p)