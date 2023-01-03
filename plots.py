import pandas as pd
import altair as alt




def plot_data(data: pd.DataFrame) -> alt.Chart:
    data = data.copy()
    data["matchNum"] = [i+1 for i in range(len(data))]
    chart = alt.Chart(data).mark_line(
            color="#83c9ff",
            strokeWidth=2,
        ).encode(
            x=alt.X("matchNum", axis=alt.Axis(title="Match #")),
            y=alt.Y("newTeamRating", axis=alt.Axis(title="Rating"))
    )
    return chart
