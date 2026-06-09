import plotly.graph_objects as go


def create_gauge(title, value):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"thickness": 0.25},
                "steps": [
                    {"range": [0, 50], "color": "#ef4444"},
                    {"range": [50, 80], "color": "#f59e0b"},
                    {"range": [80, 100], "color": "#22c55e"}
                ]
            }
        )
    )

    fig.update_layout(
        height=320,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            color="white",
            size=16
        )
    )

    return fig