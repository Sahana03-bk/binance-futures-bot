import typer
from rich import print
from rich.panel import Panel
from rich.console import Console
from bot.orders import execute_order, format_order_response
from bot.client import get_client

app = typer.Typer(help="📈 Binance Trading Bot CLI")

order_app = typer.Typer(help="Order related commands")
account_app = typer.Typer(help="Account related commands")

app.add_typer(order_app, name="order")
app.add_typer(account_app, name="account")

console = Console()


@order_app.command("place")
def place_order(
    symbol: str = typer.Option(..., help="Trading symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., help="BUY or SELL"),
    type: str = typer.Option(..., help="MARKET or LIMIT"),
    quantity: float = typer.Option(..., help="Order quantity"),
    price: float = typer.Option(None, help="Price (required for LIMIT)")
):
    """Place a MARKET or LIMIT order."""

    try:
        console.print(Panel.fit("[bold yellow]Placing Order...[/bold yellow]"))

        response = execute_order(
            symbol=symbol,
            side=side,
            order_type=type,
            quantity=quantity,
            price=price
        )

        format_order_response(response)

        console.print("[bold green]✅ Order executed successfully[/bold green]")

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")


@order_app.command("open")
def open_orders(symbol: str = typer.Option(None, help="Filter by symbol")):
    """View open orders."""
    try:
        client = get_client()
        orders = client.get_open_orders(symbol=symbol) if symbol else client.get_open_orders()

        if not orders:
            console.print("[bold yellow]No open orders found.[/bold yellow]")
            return

        console.print(Panel.fit("[bold cyan]Open Orders[/bold cyan]"))
        for order in orders:
            print(order)

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")


@account_app.command("balance")
def balance():
    """Check account balances."""
    try:
        client = get_client()
        account_info = client.account()

        console.print(Panel.fit("[bold cyan]Account Balances[/bold cyan]"))

        for asset in account_info["balances"]:
            if float(asset["free"]) > 0:
                print(f"{asset['asset']}: {asset['free']}")

    except Exception as e:
        console.print(f"[bold red]❌ Error: {str(e)}[/bold red]")


if __name__ == "__main__":
    app()
