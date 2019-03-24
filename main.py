from bokeh.plotting import figure, output_file, show, ColumnDataSource, save

# module for our tooltips
from bokeh.models.tools import HoverTool

# adding some color palette, and using the car list as the factor
from bokeh.transform import factor_cmap

# color palettes from bokeh
from bokeh.palettes import Blues8

# say, you want to embed the graph into a file
from bokeh.embed import components


import pandas as pd
# x = [1, 2, 3, 4, 5]
# y = [4, 6, 2, 4, 3]

# Read csv
df = pd.read_csv("cars.csv")

# Create a ColumnDataSource from the dataframe
source = ColumnDataSource(df)

# set the output_file
output_file("index.html")

# Car list
car_list = source.data['Car'].tolist()

# Add plot
p = figure(
    y_range=car_list,
    plot_height=600,
    title='Cars with Top Horsepower',
    x_axis_label="Horsepower",
    tools="pan, box_select, zoom_in, zoom_out, save, reset"
)

# Let's render our glyph
p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        "Car",
        palette=Blues8,
        factors=car_list
    ),
    fill_alpha=0.9,
    source=source,
    legend='Car'
)

# Add legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
<div>
    <h3>@Car</h3>
    <div><strong>Price: </strong>@Price</div>
    <div><strong>HP: </strong>@Horsepower</div>
    <div><img src="@Image" alt="" width="200"/></div>
</div>
"""

p.add_tools(hover)
# let's go ahead and show our results
# show(p)

# to avoid opening new tabs everytime we run the show command
save(p)


# Print out div and script
# script, div = components(p)
# print(script)
# print(div)
