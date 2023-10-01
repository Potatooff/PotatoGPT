from colorama import Fore, Style



def _error_text(text: str) -> None:
    """Responsible of printing error text!"""
    print((Fore.RED + text + Style.RESET_ALL + "\n"))


def _success_text(text: str) -> None:
    """Responsible of printing success text!"""
    print((Fore.GREEN + text + Style.RESET_ALL + "\n"))

def _info_text(text: str) -> None:
    """Responsible of printing info text!"""
    text = "INFO: " + text
    print((Fore.BLUE + text + Style.RESET_ALL + "\n"))

def _input_text(text: str) -> str:
    """Responsible of printing input text!"""
    return input((Fore.YELLOW + text + Style.RESET_ALL))


