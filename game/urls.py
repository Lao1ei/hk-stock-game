from rest_framework import routers
from .views import StockViewSet, PortfolioViewSet, HoldingsViewSet, TransactionsViewSet, PriceHistoryViewSet

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'stocks', StockViewSet)
router.register(r'portfolio', PortfolioViewSet)
router.register(r'holdings', HoldingsViewSet)
router.register(r'transactions', TransactionsViewSet)
router.register(r'price-history', PriceHistoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls