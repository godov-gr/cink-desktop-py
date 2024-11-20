import aiohttp
import asyncio
import json
from rich.console import Console
from rich.table import Table

console = Console()

async def check_nickname(session, username, site):
    """
    Проверка никнейма на одном сайте.
    """
    url = site.format(username)
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                return url
    except Exception:
        pass
    return None

async def search_nickname(username):
    """
    Асинхронный поиск никнейма на нескольких сайтах.
    """
    console.print(f"[bold cyan]Searching for username: {username}[/bold cyan]")
    
    # Загружаем сайты из JSON
    with open("sites.json", "r") as f:
        sites = json.load(f)
    
    found = []
    
    # Создаем сессию для асинхронных запросов
    async with aiohttp.ClientSession() as session:
        tasks = [check_nickname(session, username, site) for site in sites]
        results = await asyncio.gather(*tasks)
    
    for result in results:
        if result:
            found.append(result)
    
    return found

def display_results(username, results):
    """
    Отображение найденных результатов.
    """
    if results:
        table = Table(title=f"Results for '{username}'")
        table.add_column("Site", style="cyan")
        for result in results:
            table.add_row(result)
        console.print(table)
    else:
        console.print("[bold red]No results found.[/bold red]")

def main():
    """
    Основной процесс поиска никнейма.
    """
    console.print("[bold green]Welcome to Nickname OSINT Tool![/bold green]")
    username = input("Enter a username to search: ").strip()
    results = asyncio.run(search_nickname(username))
    display_results(username, results)

if __name__ == "__main__":
    main()
