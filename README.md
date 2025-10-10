<div align="center">
  <img src="https://github.com/mynameissami/CommandLine/blob/main/hackerbox-low-resolution-logo-color-on-transparent-background.png?raw=true" alt="HackerBox Logo" width="300">
  
  # HackerBox - Beta
  
  [![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
  [![GitHub Stars](https://img.shields.io/github/stars/mynameissami/HackerBox?style=social)](https://github.com/mynameissami/HackerBox/stargazers)
  
  A powerful, multi-functional cybersecurity toolkit for security professionals and enthusiasts.
</div>

## Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [Documentation](#-documentation)
- [FAQ](#-faq)
- [License](#-license)
- [About Me](#-about-me)

## Features

- Site Testers.
- DDoS / DoS Attackers.
- IP Inforamtion and Configuration.
- BruteForcers.
{{ ... }}
- Host IP Finders.
- YouTube video Downloader.
- Pinging websites.
- Scan Ports.
- Wifi password Extactor.
- Giga Byte & Mega Byte Convertor.
- Network Speed test.
- Shutdown Options.
- Git-Repository Clonner.
- Giga Byte & Mega Byte Convertor.
- Show near by networks.
- Settings.ini for Customization of Terminal.





## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/mynameissami/HackerBox.git
cd HackerBox

# Install dependencies
pip install -r requirements.txt

# Run HackerBox
python HackerBox.py
```

## 📚 Documentation

For detailed documentation, visit our [Documentation](https://linktodocumentation).

## ⚙️ Configuration

Download Now! Check it Out.

```bash
  git clone https://github.com/mynameissami/HackerBox.git
  cd HackerBox
  python ./HackerBox.py
```

### Dependencies

HackerBox has a few dependencies that need to be installed for full functionality:

```bash
pip install -r requirements.txt
```

If you prefer to run with minimal dependencies, the application will still work with reduced functionality:
- Without `plumbum`: Terminal colors will be disabled
- Without `plyer`: System notifications will be replaced with console messages
    
## Settings.ini - Settings of HackerBox
Inside view of Settings.ini.
```
[DEFAULT]
file-type = Settings
name = HackerBox
description = Settings File for HackerBox - Editable.
warning = Only Change this if you know what are you doing!

[Main Settings]
auto-update = True
ask-for-administrator = True
show-disclaimer = True
auto-file-sort = True

[Commands Configuration]
custom-package-download-directory = Default
github-clone-directory = nil

[Youtube Settings]
videos-output-directory = .
audio-output-directory = .

[Commandline Settings]
prompt-autocomplete = True
show-errors-log = False

```
How To Change : Open The Settings.ini in a Text Editor.
```
To change settings you can simply change True to False.

[Main Settings]
auto-update = True // Change this to False to make this not occur in program.
ask-for-administrator = True
show-disclaimer = True
auto-file-sort = True

If you want Custom directory for Saving of files you can also do that by :
In Settings.ini Change The "Default" or "nil" to the directory you want to 
save.

For Example:

[Commands Configuration]
custom-package-download-directory = C:\Users\%Username%\Desktop
github-clone-directory = C:\Users\%Username%\Desktop

You can also change the directory from default to Custom by changing "."
to the directory you want Files to be :

Example 

[Youtube Settings]

videos-output-directory = C:\Users\%Username%\Desktop
audio-output-directory = C:\Users\%Username%\Desktop
```
For More Information About Settings Read Documentation.

## FAQ

#### Why Should You Use This Software.

Ease of Use, Beginner Friendly , CLI - Based , Fast.

#### Is it only made for Pentesting?

No, It depends how use the Features of this software.

#### Is this Software Completely Developed?

No, This software is under Development and will be released soon.

## License
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork** the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a **Pull Request**

### 🐛 Report Bugs
Found a bug? Please [open an issue](https://github.com/mynameissami/HackerBox/issues) with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

### 💡 Feature Requests
Have an idea? [Suggest a feature](https://github.com/mynameissami/HackerBox/issues) and help us improve HackerBox!

## 📁 Project Structure

```
HackerBox/
├── Dics/                     # Dictionaries and wordlists
│   ├── AdminPanels/          # Admin panel paths
│   ├── PassLists/            # Password lists for brute force
│   ├── PayloadsTextFiles/    # XSS and other attack payloads
│   └── UserNames/            # Username lists
│
├── Scripts/                  # Core security tools
│   ├── Admin_Panel_Finder.py
│   ├── Bruteforcer.py
│   ├── CrossSiteScriptingChecker.py
│   ├── Dos.py
│   ├── Nmap-t.py
│   ├── WebAnalyzer.py
│   ├── Web_bruteforce.py
│   ├── ftp_bruteforcer.py
│   └── live_port_discovery.py
│
├── Icons/                    # Application icons and assets
│
├── HackerBox.py              # Main application entry point
├── command_completion.py     # Tab completion functionality
├── commands.py               # Command definitions and registry
├── config.py                 # Configuration settings
├── settings.py               # User settings management
├── utils.py                  # Utility functions
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 👨‍💻 About Me

<div align="center">
  <p>👋 Hi, I'm Sami - A passionate developer and cybersecurity enthusiast</p>
  
  [![Portfolio](https://img.shields.io/badge/Portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white&color=9cf)](https://samidev.rf.gd)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/msamighazi)
  [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Sami87305624)
</div>

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>Built with ❤️ by <a href="https://github.com/mynameissami">Sami</a></p>
  <p>If you find this project useful, consider giving it a ⭐️</p>
</div>
