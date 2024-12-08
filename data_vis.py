import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input

# Load the dataset
df = pd.read_csv("housing.csv")

# Initialize the Dash app
app = Dash()

# Layout for the app
app.layout = html.Div([
    html.Div(children="Dashboard", style={"fontSize": 24, "fontWeight": "bold"}),

    dash_table.DataTable(
        id="data-table",
        data=df.to_dict("records"),
        page_size=20
    ),

    html.Div([
        html.Label("Select Feature:"),
        dcc.Dropdown(
            id="feature-dropdown",
            options=[{"label": col, "value": col} for col in df.columns],
            value=df.columns[0]
        )
    ]),

    dcc.Graph(id="histogram")
])

# Callback for updating the histogram
@app.callback(
    Output(component_id="histogram", component_property="figure"),
    Input(component_id="feature-dropdown", component_property="value")
)
def update_histogram(selected_feature):
    fig = px.histogram(df, x=selected_feature)
    fig.update_layout(
        title=f"Histogram of {selected_feature}",
        xaxis_title=selected_feature,
        yaxis_title="Frequency"
    )
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
