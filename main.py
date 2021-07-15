import re
import sys

import colorama

import auto_complete_pkg
import initialization_pkg
# main:
# Have to modes:
#  * initialization mode - reads all the files under the folder to suffix tree
#  * query mode - load the suffix tree from the data_file
# accepts search text & responsible for performing the autocomplete


def handle_input(text):
    text = re.sub(r'[^a-z+ ' ']', '', text.lower())
    text = " ".join(text.split())
    return  text
def run_cli(mode):
    text=''
    if mode == 'initialization':
        print("Loading the files and prepariong the system...")
        load_file = initialization_pkg.Initialization()
        load_file.get_directory_files('file')
        print("The system is ready. ", end='')
        return
    elif mode == 'query':
        initialization_pkg.Initialization().load_file()
    print("If you want reset your input - please insert \'#\' without space")
    text_search = input("Enter your text:\n")
    while True:
        if text == '#':
            text_search = None
        else:
            auto_complete = auto_complete_pkg.AutoComplete()
            text_search= handle_input(text_search)
            print_auto_complete = auto_complete.get_best_k_completions(text_search)
            if len(print_auto_complete) > 0:
                for index, to_print in enumerate(print_auto_complete):
                    print(f'{index+1}. {to_print[0]}, {to_print[1]}')
            else:
                print(colorama.Fore.RED+"No data was found for the inserted word"+colorama.Fore.RESET)
        check_text = text_search if text_search is not None else ""
        text = input(f'Enter your text:\n{colorama.Fore.GREEN+check_text+colorama.Fore.RESET}')
        text_search= check_text+ text

if __name__ == '__main__':
    run_cli(sys.argv[1])

