import plotly.graph_objects as go

def ltv_gauge(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': "LTV"},
        gauge={'axis': {'range': [0, 100]}}
    ))
    return fig

def dscr_gauge(value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': "DSCR"},
        gauge={'axis': {'range': [0, 3]}}
    ))
    return fig
