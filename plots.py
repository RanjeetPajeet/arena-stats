import pandas as pd
import altair as alt




def plot_data(data: pd.DataFrame, is3v3: bool = False) -> alt.Chart:
    data = data.copy()
    if is3v3: data = data[11:]
    data["matchNum"] = [i+1 for i in range(len(data))]
    data["Match"] = data["matchNum"]        # added for better tooltip
    data["Rating"] = data["newTeamRating"]  # added for better tooltip
    min_rating = min(data["newTeamRating"])
    max_rating = max(data["newTeamRating"])
    ylims = (int(min_rating/1.01), int(max_rating*1.05))
    
    data["maxRating"] = [max_rating for i in range(len(data))]
    
    chart = alt.Chart(data).mark_area(
            color=alt.Gradient(
                gradient="linear",
                stops=[alt.GradientStop(color="#0054a3", offset=0),     # bottom color
                       alt.GradientStop(color="#60b4ff", offset=1)],  # top color
                x1=1, x2=1, y1=1, y2=0,
            ),
            opacity = 0.25,
            strokeWidth=2,
            interpolate="monotone",
            clip=True,
            line=True,
        ).encode(
            x=alt.X("matchNum", axis=alt.Axis(title="Match #"), scale=alt.Scale(domain=(min(data["matchNum"]), max(data["matchNum"])))),
            y=alt.Y("newTeamRating", axis=alt.Axis(title="Rating"), scale=alt.Scale(domain=ylims)),
            tooltip=["Match", "Rating"]
    ) + alt.Chart(data).mark_line(color = "#ffffff",opacity = 0.05,strokeWidth = 2).encode(
        x=alt.X("matchNum", axis=alt.Axis(title="Match #")),
        y=alt.Y("maxRating", axis=alt.Axis(title="Rating"), scale=alt.Scale(domain=ylims))
    )
    chart = chart.properties(height=600)
    chart = chart.properties(width =700)
    chart = chart.configure_axisY(
        grid=True,           gridOpacity=0.3,         tickCount=6,
        titleFont="Calibri", titleColor="#ffffff",    titlePadding=20,
        titleFontSize=22,    titleFontStyle="italic", titleFontWeight="bold",
        labelFont="Calibri", labelColor="#ffffff",    labelPadding=10,
        labelFontSize=16,    labelFontWeight="bold",
    )
    chart = chart.configure_axisX(
        grid=False,          titleOpacity=1,
        titleFont="Calibri", titleColor="#ffffff",    titlePadding=20,
        titleFontSize=22,    titleFontStyle="italic", titleFontWeight="bold",
        labelFont="Calibri", labelColor="#ffffff",   labelPadding=10,
        labelFontSize=14,    labelFontWeight="bold",
    )
    
    return chart




def plot_data2(data: pd.DataFrame) -> alt.Chart:
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
