from colorama import Fore, Style



def _error_text(text: str) -> None:
    """Responsible of printing error text!"""
    print((Fore.RED + text + Style.RESET_ALL + "\n"))