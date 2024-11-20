import os
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def main_menu():
    """Главное меню программы."""
    console.print("[bold cyan]Welcome to the OSINT & Pentest Tool![/bold cyan]")
    console.print("""
    [1] OSINT
    [2] Pentest
    [3] Exit
    """)
    choice = Prompt.ask("[bold green]Choose an option[/bold green]", choices=["1", "2", "3"])
    return choice

def osint_menu():
    """Меню OSINT функционала."""
    console.print("""
    [bold yellow]OSINT Options:[/bold yellow]
    [1] Nickname
    [2] Mail
    [3] Phone number
    [4] Personality
    [5] Back
    """)
    choice = Prompt.ask("[bold green]Choose an option[/bold green]", choices=["1", "2", "3", "4", "5"])
    return choice

def pentest_menu():
    """Меню Pentest функционала."""
    console.print("""
    [bold yellow]Pentest Options:[/bold yellow]
    [1] Whois
    [2] Subdomains
    [3] Networks
    [4] Scanning
    [5] Back
    """)
    choice = Prompt.ask("[bold green]Choose an option[/bold green]", choices=["1", "2", "3", "4", "5"])
    return choice

def osint_actions(choice):
    """Обработка действий в OSINT."""
    if choice == "1":
        console.print("[bold cyan]Performing Nickname OSINT...[/bold cyan]")
        # Запуск nickname.py
        os.system("python nickname/nickname.py")
    elif choice == "2":
        console.print("[bold cyan]Performing Mail OSINT...[/bold cyan]")
        # Заглушка для почты
    elif choice == "3":
        console.print("[bold cyan]Performing Phone Number OSINT...[/bold cyan]")
        # Заглушка для телефона
    elif choice == "4":
        console.print("[bold cyan]Performing Personality OSINT...[/bold cyan]")
        # Заглушка для анализа личности
    elif choice == "5":
        return

def pentest_actions(choice):
    """Обработка действий в Pentest."""
    if choice == "1":
        console.print("[bold cyan]Performing Whois Lookup...[/bold cyan]")
        # Заглушка для Whois
    elif choice == "2":
        console.print("[bold cyan]Performing Subdomain Enumeration...[/bold cyan]")
        # Заглушка для субдоменов
    elif choice == "3":
        console.print("[bold cyan]Performing Network Analysis...[/bold cyan]")
        # Заглушка для анализа сети
    elif choice == "4":
        console.print("[bold cyan]Performing Scanning...[/bold cyan]")
        # Заглушка для сканирования
    elif choice == "5":
        return

def main():
    """Основной цикл программы."""
    while True:
        choice = main_menu()
        if choice == "1":
            while True:
                osint_choice = osint_menu()
                if osint_choice == "5":
                    break
                osint_actions(osint_choice)
        elif choice == "2":
            while True:
                pentest_choice = pentest_menu()
                if pentest_choice == "5":
                    break
                pentest_actions(pentest_choice)
        elif choice == "3":
            console.print("[bold green]Goodbye![/bold green]")
            break

if __name__ == "__main__":
    main()
