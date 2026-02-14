from bot.client import get_client
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logger_config import setup_logger
from rich.table import Table
from rich.console import Console


logger = setup_logger()
console = Console()


def execute_order(symbol, side, order_type, quantity, price=None):

    try:
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        logger.info(f"Placing order: {symbol} {side} {order_type} Qty={quantity} Price={price}")

        client = get_client()

        if order_type == "MARKET":
            response = client.new_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        else:
            response = client.new_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )

        logger.info(f"Order response: {response}")

        return response

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise ValueError(f"Order execution failed: {str(e)}")

def format_order_response(response: dict):
    table = Table(title="Order Summary")

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    table.add_row("Symbol", str(response.get("symbol")))
    table.add_row("Order ID", str(response.get("orderId")))
    table.add_row("Type", str(response.get("type")))
    table.add_row("Side", str(response.get("side")))
    table.add_row("Status", str(response.get("status")))
    table.add_row("Executed Qty", str(response.get("executedQty")))

    if response.get("fills"):
        avg_price = response["fills"][0]["price"]
        table.add_row("Average Price", avg_price)

    console.print(table)