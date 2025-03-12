import yfinance as yf
import plotly.express as px


def plot_price(ticker):

    data = yf.download(
    ticker,
    multi_level_index=False
    )

    fig = px.line(
        data.reset_index(),
        x = 'Date', y = ['Close']
    )

    return fig



def get_stock_data(ticker, start_date, end_date):
    """Obtém dados históricos de ações do Yahoo Finance."""
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

# Exemplo de uso
ticker = "AAPL"  # Apple
start_date = "2024-01-01"
end_date = "2024-03-01"

data = get_stock_data(ticker, start_date, end_date)
print(data.head())