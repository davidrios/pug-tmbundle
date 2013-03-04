# Jade.tmbundle

**This was made specifically for Sublime Text 2, but was tested and works with Textmate 2**

A **TextMate Bundle** for the **Jade** templating language. Implemented in
JSON-tmLanguage, a compiled tmLanguage version is included. All language
features that I know of (including some undocumented ones and quircks of the
Jade parser) and some indent increase/decrease patterns are implemented.

A test.jade file is included for testing, it is a valid file, so you can
compile it with jade to check its output.

A test_errors.jade file is also included for testing some syntax/semantic errors
that are highlighted.

## Installation

### TextMate 2

    mkdir -p ~/Library/Application\ Support/TextMate/Managed/Bundles
    cd ~/Library/Application\ Support/TextMate/Managed/Bundles
    git clone https://github.com/davidrios/jade-tmbundle.git Jade.tmbundle

### Sublime Text 2

    mkdir -p ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages
    git clone https://github.com/davidrios/jade-tmbundle.git Jade.tmbundle

Patches for additions are always welcome.