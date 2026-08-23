import requests
from dotenv import load_dotenv
from utils.curreny_converter import CurrencyConverter
import os 
from langchain.tools import tool
load_dotenv()
from typing import List


class CurrencyConverterTool:

    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the currency converter tool"""

        @tool
        def convert_currency(
            amount: float,
            from_currency: str,
            to_currency: str
        ):
            """Convert amount from one currency to another"""
            return self.currency_service.convert(
                amount,
                from_currency,
                to_currency
            )

        return [convert_currency]