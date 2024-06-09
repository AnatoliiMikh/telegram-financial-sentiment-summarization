import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

mean_df = pd.read_csv("https://raw.githubusercontent.com/AnatoliiMikh/telegram-financial-sentiment-summarization/main/mean_values_telegram_data.csv")
IMOEX_df = pd.read_csv("https://raw.githubusercontent.com/AnatoliiMikh/telegram-financial-sentiment-summarization/main/ohlc_IMOEX.csv")

fig = make_subplots(rows=2, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.02,
                    subplot_titles=('Чем ближе к нулю, тем более нейтральный новостной фон:', ''))

fig.add_trace(
    go.Bar(
        x=mean_df['date'],
        y=mean_df['mean_value'],
        name='Диаграмма настроения новостей',
    ),
    row=1, col=1
)

fig.add_trace(
    go.Ohlc(
        x=IMOEX_df['TRADEDATE'],
        open=IMOEX_df['OPEN'],
        high=IMOEX_df['HIGH'],
        low=IMOEX_df['LOW'],
        close=IMOEX_df['CLOSE'],
        name="График индекса МосБиржи",
    ),
    row=2, col=1
)
# Для скриншота:
# fig.update_layout(height=1200, width=1700, title_text="Объединение графиков настроения экономических новостей и индекса МосБиржи (IMOEX) за 2023 год:")
# Для веб-интерфейса:
fig.update_layout(height=1000, width=1500, title_text="Объединение графиков настроения экономических новостей и индекса МосБиржи (IMOEX) за 2023 год:")


fig.update_yaxes(title_text="Окраска новостного фона", row=1, col=1)
fig.update_yaxes(title_text="Индекс МосБиржи", row=2, col=1)

fig.update_xaxes(title_text="Дата", row=2, col=1)

# Для скриншота:
# fig.update_layout(legend=dict(yanchor='bottom', xanchor='center', y=-0.12, x=0.5, orientation='h'))
# Для веб-интерфейса:
fig.update_layout(legend=dict(yanchor='bottom', xanchor='center', y=-0.45, x=0.5, orientation='h'))

# Для скриншота:
# fig.update_layout(xaxis2_rangeslider_visible=False)

fig.update_layout(
    font=dict(
        family="Times New Roman",
        size=22, 
        color="Black"
    )
)

fig.update_annotations(font_size=22)
    
fig.show()


from dash import Dash, html, dcc

# Initialize the app
app = Dash(__name__)
server = app.server

# App layout
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)