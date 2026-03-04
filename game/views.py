from rest_framework import viewsets
from rest_framework.response import Response
from .models import Stock, Portfolio, Holding, Transaction, PriceHistory
from .serializers import StockSerializer, PortfolioSerializer, HoldingSerializer, TransactionSerializer, PriceHistorySerializer
import yfinance as yf


class StockViewSet(viewsets.ViewSet):
    def list(self, request):
        # Logic to list stocks
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def perform_stock_refresh(self):
        # Logic to refresh stock prices using yfinance
        stocks = Stock.objects.all()
        for stock in stocks:
            price = yf.Ticker(stock.ticker).info['currentPrice']
            # Update the Stock object with the new price
            stock.price = price
            stock.save()
            # Store price history
            PriceHistory.objects.create(stock=stock, price=price)


class PortfolioViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        # Logic to retrieve a portfolio
        portfolio = Portfolio.objects.get(pk=pk)
        serializer = PortfolioSerializer(portfolio)
        return Response(serializer.data)


class HoldingViewSet(viewsets.ViewSet):
    def buy_stock(self, request, pk=None):
        # Logic for buying stocks
        # 
        # Update holdings
        pass

    def sell_stock(self, request, pk=None):
        # Logic for selling stocks
        pass


class TransactionViewSet(viewsets.ViewSet):
    def list(self, request):
        # Logic to list transactions
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class PriceHistoryViewSet(viewsets.ViewSet):
    def list(self, request):
        # Logic to list price history
        price_history = PriceHistory.objects.all()
        serializer = PriceHistorySerializer(price_history, many=True)
        return Response(serializer.data)
