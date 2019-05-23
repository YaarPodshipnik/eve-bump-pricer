# eve-bump-pricer

A tiny, simple, script to monitor cliboard for EVE online orders,
calculate new +/-0.01 price, and put it back to clipboard.
Helps dealing with updating multiple orders (no EULA-breaking
automation).

Best used by compiling into standalone exe and run when required.

The boundled release Win10 64bit executable was built with pyinstaller,
in a very limited conda env, with UPX available. Build instructions below:

```bash
conda create --name eve-bump-pricer python=3.7 pyperclip pyinstaller
conda activate eve-bump-pricer
pyinstaller --clean --onefile eve-bump-pricer.py
```
