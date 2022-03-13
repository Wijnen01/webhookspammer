import requests
from colorama import Fore

url = input(f"{Fore.RED}[{Fore.GREEN}?{Fore.RED}]{Fore.GREEN} Stuur je webhook: {Fore.RED}> ")

result = requests.request(method="DELETE", url=url)

try:
    result.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"{Fore.RED}[{Fore.GREEN}!{Fore.RED}]{Fore.GREEN} " + str(err))
else:
    print(f"{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.GREEN} Webhook is met suc6 verwijderd!\n{Fore.RED}[{Fore.GREEN}*{Fore.RED}]{Fore.GREEN} Status code is: {result.status_code}")
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
