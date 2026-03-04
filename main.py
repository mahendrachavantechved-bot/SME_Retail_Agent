import flet as ft
import json
import plotly.express as px
import plotly.graph_objects as go
from retail_pipeline import process_retail
from sme_pipeline import process_sme
from gauges import ltv_gauge, dscr_gauge
from sarvam_utils import translate_text

def main(page: ft.Page):
    page.title = "Loan Demo Final"
    page.window_width = 1200
    page.window_height = 800
    page.scroll = "auto"

    with open("retail_applicants.json") as f:
        retail_data = json.load(f)

    with open("sme_applicants.json") as f:
        sme_data = json.load(f)

    detail_panel = ft.Column(width=300)

    def show_dashboard(applicant, score, risk, is_sme=False):
        sankey = go.Figure(go.Sankey(
            node=dict(label=["Application", "Underwriting", "Approval"]),
            link=dict(source=[0,1], target=[1,2], value=[1,1])
        ))

        radar = px.line_polar(
            r=[applicant.get("cibil",0), applicant.get("ltv",0)],
            theta=["CIBIL", "LTV"],
            line_close=True
        )

        treemap = px.treemap(
            names=["Principal","Interest"],
            parents=["",""],
            values=[70,30]
        )

        dpd = px.line(
            y=applicant["dpd"],
            title="DPD Trend"
        )

        dashboard.controls.clear()
        dashboard.controls.extend([
            ft.Text(f"Risk: {risk} | Score: {score}", size=20),
            ft.PlotlyChart(sankey),
            ft.PlotlyChart(ltv_gauge(applicant.get("ltv",0))),
            ft.PlotlyChart(dscr_gauge(applicant.get("dscr",1))),
            ft.PlotlyChart(radar),
            ft.PlotlyChart(treemap),
            ft.PlotlyChart(dpd)
        ])
        page.update()

    def on_select(e, is_sme=False):
        applicant = next(a for a in (sme_data if is_sme else retail_data) if a["name"] == e.control.value)
        detail_panel.controls.clear()
        for k,v in applicant.items():
            detail_panel.controls.append(ft.Text(f"{k}: {v}"))
        page.update()

    retail_dropdown = ft.Dropdown(
        label="Search Retail Applicant",
        options=[ft.dropdown.Option(a["name"]) for a in retail_data],
        on_change=lambda e: on_select(e, False),
        width=400
    )

    sme_dropdown = ft.Dropdown(
        label="Search SME Applicant",
        options=[ft.dropdown.Option(a["name"]) for a in sme_data],
        on_change=lambda e: on_select(e, True),
        width=400
    )

    dashboard = ft.Column()

    page.add(
        ft.Tabs(
            tabs=[
                ft.Tab(text="Retail Loans", content=retail_dropdown),
                ft.Tab(text="SME Loans", content=sme_dropdown),
                ft.Tab(text="Dashboard", content=dashboard)
            ]
        ),
        detail_panel
    )

ft.app(target=main)
