# Fileless-PE

## Overview

- The provided Python program Fileless-PEloader.py generates a Python script (PEloader.py) to load a DLL or EXE file from a given URL. It provides functionality to specify a method to execute if the file is a DLL. The script utilizes the pythonmemorymodule library for memory manipulation.

## Features

- Dynamic Code Generation: Generates Python script (PEloader.py) based on user input for URL, file type (DLL or EXE), and method (if applicable).
- DLL and EXE Loading: Loads DLL or EXE files from a specified URL using the pythonmemorymodule library.
- Method Execution (DLL): Executes a specified method within a DLL file if provided by the user.
- Error Handling: Provides error messages and gracefully exits in case of invalid user input or interruption.

## How to Use

1. **Clone the Repository:**

    `git clone https://github.com/malwarekid/Fileless-PE.git &&
    cd Fileless-PE`

2. **Run the Script:**

    `python3 Fileless-PE.py`

```

    _______ __     __                     ____  ______
   / ____(_) /__  / /__  __________      / __ \/ ____/
  / /_  / / / _ \/ / _ \/ ___/ ___/_____/ /_/ / __/   
 / __/ / / /  __/ /  __(__  |__  )_____/ ____/ /___   
/_/   /_/_/\___/_/\___/____/____/     /_/   /_____/    
                                      By @malwarekid

Enter the URL: url
Enter the file type (dll or exe): dll
Enter the method (Example Method: DLLRegisterServer): DLLRegisterServer
Enter the output file name (default: PEloader.py): 
Code generated and saved to PEloader.py
```

3. **Enter Input Parameters:**

   - **URL:** Enter the URL from which you want to load the DLL or EXE file.

   - **File Type:** Choose the type of file you want to load (dll or exe). Enter the corresponding option.

   - **Method (if applicable):** If you selected dll as the file type, you'll be prompted to enter the method you want to execute within the DLL file. Provide the method name when prompted.

   - **Output File Name:** Optionally, you can specify a custom output file name for the generated Python script. If left empty, the default name PEloader.py will be used.

4. - Optionally, choose to pre-encode the command if it contains special characters like `'`, `"`, or `$`.

5. - The generated Python script (`PEloader.py`) will be saved in the current directory.

6. - Press Ctrl+C at any time to cancel the operation.

## Requirements

- Python 3.x
- `pythonmemorymodule` library

## Contributors

- [MalwareKid](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Notes

Feel free to contribute, report issues, or provide feedback and dont forget to follow me on [Instagram](https://www.instagram.com/malwarekid/) and [github](https://github.com/malwarekid/) Happy Hacking!
