import argparse, detect_http_methods
from colorama import Fore, init
init(autoreset=True)

def main():
    title = """
╔╦╗┌─┐┌┬┐┌─┐┌─┐┌┬┐  ╦ ╦╔╦╗╔╦╗╔═╗   ╔╦╗┌─┐┌┬┐┬ ┬┌─┐┌┬┐┌─┐
 ║║├┤  │ ├┤ │   │   ╠═╣ ║  ║ ╠═╝───║║║├┤  │ ├─┤│ │ ││└─┐
═╩╝└─┘ ┴ └─┘└─┘ ┴   ╩ ╩ ╩  ╩ ╩     ╩ ╩└─┘ ┴ ┴ ┴└─┘─┴┘└─┘
"""
    parser = argparse.ArgumentParser(f"""Detect supported HTTP methods for a given URL\n{title}""")
    parser.add_argument(
        "-u", "--url", 
        required=True,
        help="Target URL (z.B. https://example.com)"
    )
    args = parser.parse_args()
    print(title)
    
    print(Fore.YELLOW + f"[INFO] Testing HTTP methods for: {args.url}...")
    print(Fore.MAGENTA + "[INFO] Supported HTTP methods:")
    try:
        for method, allowed in detect_http_methods.Detect_Http_Method(args.url).discover_http_methods().items():
            if allowed == True:
                print(Fore.GREEN + f"  [+] {method}")
            else:
                print(Fore.RED + f"  [ ] {method}")
    except Exception as e:
        print(Fore.RED + f"{e}")
    except KeyboardInterrupt:
        print("User stopped")
if __name__ == "__main__":
    main()