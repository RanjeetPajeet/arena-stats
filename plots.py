import pandas as pd
import altair as alt




def plot_data(data: pd.DataFrame) -> alt.Chart:
    data = data.copy()
    data["matchNum"] = [i+1 for i in range(len(data))]
    min_rating = min(data["newTeamRating"])
    max_rating = max(data["newTeamRating"])
    ylims = (int(min_rating/1.25), int(max_rating*1.2))
    chart = alt.Chart(data).mark_line(
            color="#83c9ff",
            strokeWidth=2,
        ).encode(
            x=alt.X("matchNum", axis=alt.Axis(title="Match #")),
            y=alt.Y("newTeamRating", axis=alt.Axis(title="Rating"), scale=alt.Scale(domain=ylims))
    )
    return chart
