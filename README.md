# Pug.tmbundle

**This was made specifically for Sublime Text 2, but was tested and works with Textmate 2 and Sublime Text 3**

A **TextMate Bundle** for the **Pug** templating language. Implemented in
JSON-tmLanguage, a compiled tmLanguage version is included. All language
features that I know of (including some undocumented ones and quircks of the
Pug parser) and some indent increase/decrease patterns are implemented.

A test.pug file is included for testing, it is a valid file, so you can
compile it with pug to check its output.

A test_errors.pug file is also included for testing some syntax/semantic errors
that are highlighted.

A highlighter using Python instead of JavaScript is also included for use with
[PyPug](https://github.com/SyrusAkbary/pypug), you can either manually select
`Pug (Python)` from the syntaxes list or give your file the extension
`.py.pug` to select automatically (only on Sublime Text). Also included is a
`test.py.pug` file that can be compiled with `pypug` to test it.

## Installation

### Using Package Control in SUblime Text 2/3

Package control is a package manager for Sublime Text extensions (think of it like "apt-get" for Sublime Text). If you haven't already, install [Package Control](https://sublime.wbond.net/installation) into your instance of Sublime Text and restart. Choose **Package Controll: Install Package** (press `Ctrl/Cmd + p` and then type `pi`), search for package named `Pug` and install. Restart if you cannot select "Pug" from syntax highlighter menu.

### TextMate 2

    mkdir -p ~/Library/Application\ Support/TextMate/Managed/Bundles
    cd ~/Library/Application\ Support/TextMate/Managed/Bundles
    git clone https://github.com/davidrios/pug-tmbundle.git Pug.tmbundle

### Sublime Text manual installation

    mkdir -p ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    git clone https://github.com/davidrios/pug-tmbundle.git Pug

Replace '2' with '3' in case of Sublime Text 3.

Patches for additions are always welcome.
