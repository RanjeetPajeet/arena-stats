import pandas as pd
import altair as alt




def plot_data(data: pd.DataFrame) -> alt.Chart:
    data = data.copy()
    data["matchNum"] = [i+1 for i in range(len(data))]
    min_rating = min(data["newTeamRating"])
    max_rating = max(data["newTeamRating"])
    ylims = (int(min_rating/1.1), int(max_rating*1.1))
    chart = alt.Chart(data).mark_line(
            color="#83c9ff",
            strokeWidth=2,
        ).encode(
            x=alt.X("matchNum", axis=alt.Axis(title="Match #")),
            y=alt.Y("newTeamRating", axis=alt.Axis(title="Rating"), scale=alt.Scale(domain=ylims))
    )
    return chart



def plot_data2(data: pd.DataFrame) -> alt.Chart:
    data = data.copy()
    data["matchNum"] = [i+1 for i in range(len(data))]
    min_rating = min(data["newTeamRating"])
    max_rating = max(data["newTeamRating"])
    ylims = (int(min_rating/1.1), int(max_rating*1.1))
    
    
    chart = alt.Chart(data).mark_area(
            color=alt.Gradient(
                gradient="linear",
                stops=[alt.GradientStop(color="#31333F", offset=0),     # bottom color
                       alt.GradientStop(color="#0068c9", offset=0.5)],  # top color
                x1=1, x2=1, y1=1, y2=0,
            ),
            opacity = 0.5,
            strokeWidth=2,
            interpolate="monotone",
            clip=True,
        ).encode(
            x=alt.X("matchNum", axis=alt.Axis(title="Match #"), scale=alt.Scale(domain=(min(data["matchNum"]), max(data["matchNum"])))),
            y=alt.Y("newTeamRating", axis=alt.Axis(title="Rating"), scale=alt.Scale(domain=ylims))
    )
    chart = chart.properties(height=600)
    chart = chart.properties(width =700)
    chart = chart.configure_axisY(
        grid=True,           gridOpacity=0.3,         tickCount=6,
        titleFont="Calibri", titleColor="#ffffff",    titlePadding=20,
        titleFontSize=22,    titleFontStyle="italic", titleFontWeight="bold",
        labelFont="Calibri", labelColor="#ffffff",    labelPadding=10,
        labelFontSize=14,    labelFontWeight="bold",
    )
    chart = chart.configure_axisX(
        grid=False,          titleOpacity=1,
        titleFont="Calibri", titleColor="#ffffff",    titlePadding=20,
        titleFontSize=22,    titleFontStyle="italic", titleFontWeight="bold",
        labelFont="Calibri", labelColor="#ffffff",   labelPadding=10,
        labelFontSize=14,    labelFontWeight="bold",
    )
    

    return chart
