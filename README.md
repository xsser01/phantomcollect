# 👻 PhantomCollect

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.6%2B-green)
![License](https://img.shields.io/badge/license-MIT-orange)
[![CodeFactor](https://www.codefactor.io/repository/github/xsser01/phantomcollect/badge)](https://www.codefactor.io/repository/github/xsser01/phantomcollect)
[![Security](https://img.shields.io/badge/Security-Enabled-brightgreen)](https://github.com/xsser01/phantomcollect/security)
[![Dependabot](https://img.shields.io/badge/dependabot-enabled-brightgreen)](https://github.com/xsser01/phantomcollect/network/updates)
[![Snyk Security](https://snyk.io/test/github/xsser01/phantomcollect/badge.svg)](https://snyk.io/test/github/xsser01/phantomcollect)

**Advanced Stealth Web Data Collection Framework**

## 🎯 Features

- 📍 **Precise GPS Location Tracking**
- 🌐 **Public IP & Geo-Location Detection** 
- 💻 **Complete Device Fingerprinting**
- 📡 **Network & Connection Information**
- 🔋 **Battery Status & Power Management**
- 🛡️ **Stealth Data Collection**
- 💾 **Multiple Storage Backends** (SQLite, JSON)
- 📊 **Real-time Terminal Display**

## 🚀 Quick Start

### Installation
```bash
pip install phantomcollect

Basic Usage

```bash
phantomcollect
```
From AUR (Arch Linux):
```bash
yay -S phantomcollect
```
Access the Interface

```
http://localhost:8080
```

🔧 Advanced Usage

Make it Public (Ngrok)

```bash
phantomcollect &
ngrok http 8080
```

Custom Port

```bash
phantomcollect --port 8081
```

View Collected Data

```bash
# View all collected data
sqlite3 victims.db "SELECT * FROM victims;"

# Delete all data
rm victims.db
```

📊 Data Collection Schema

Database Structure:

```sql
-- victims table schema
CREATE TABLE victims (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,                    -- Visit time
    ip TEXT,                          -- Public IP address  
    user_agent TEXT,                  -- Browser/device info
    location TEXT,                    -- Geographic location
    device_info TEXT,                 -- Hardware specifications
    all_data TEXT                     -- Complete JSON data
);
```

JSON Data Structure:

```json{
  "timestamp": "DateTime",
  "collectedData": {
    "basicInfo": {
      "userAgent": "String",
      "platform": "String", 
      "vendor": "String",
      "appName": "String",
      "appVersion": "String",
      "language": "String",
      "languages": ["Array"]
    },
    "screenInfo": {
      "width": "Number",
      "height": "Number",
      "availWidth": "Number",
      "availHeight": "Number", 
      "colorDepth": "Number",
      "pixelDepth": "Number"
    },
    "locationInfo": {
      "timezone": "String",
      "timezoneOffset": "Number"
    },
    "networkInfo": {
      "effectiveType": "String",
      "downlink": "Number",
      "rtt": "Number",
      "saveData": "Boolean"
    },
    "batteryInfo": {
      "charging": "Boolean",
      "level": "Number",
      "chargingTime": "Number",
      "dischargingTime": "Number"
    },
    "hardwareInfo": {
      "hardwareConcurrency": "Number",
      "deviceMemory": "Number",
      "maxTouchPoints": "Number"
    },
    "privacyInfo": {
      "cookieEnabled": "Boolean",
      "doNotTrack": "Boolean",
      "pdfViewerEnabled": "Boolean",
      "webdriver": "Boolean"
    },
    "gpsError": "String",
    "publicIP": "String",
    "ipGeoInfo": {
      "status": "String",
      "country": "String",
      "countryCode": "String",
      "region": "String",
      "regionName": "String",
      "city": "String",
      "zip": "String",
      "lat": "Number",
      "lon": "Number",
      "timezone": "String",
      "isp": "String",
      "org": "String",
      "as": "String",
      "query": "String"
    }
  }
}
```

📁 Data Collected

Data Type Details
Location GPS coordinates, IP-based location
Device Hardware specs, screen info, platform
Network Connection type, speed, IP address
Browser User agent, languages, timezone
Battery Level, charging status, timing

⚠️ Legal Disclaimer

This tool is for educational and authorized security testing purposes only. Users are solely responsible for complying with all applicable laws.

🔐 Security Features

· No external dependencies
· Local data storage only
· Transparent data collection notification
· Educational focus

👨‍💻 Developer

xsser01 - Security Researcher

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Use Responsibly. Secure Ethically.

## 🌐 Featured On

[![SourceForge](https://img.shields.io/badge/Listed%20on-SourceForge-orange?logo=sourceforge)](https://sourceforge.net/projects/phantomcollect/)  
[![AlternativeTo](https://img.shields.io/badge/Listed%20on-AlternativeTo-blue?logo=alternativeto)](https://alternativeto.net/software/phantomcollect/about/)  
[![LibHunt](https://img.shields.io/badge/Tracked%20by-LibHunt-green?logo=github)](https://www.libhunt.com/r/phantomcollect)
[![Launchpad](https://img.shields.io/badge/Listed%20on-Launchpad-blueviolet?logo=launchpad)](https://launchpad.net/phantomcollect)
[![Codeberg](https://img.shields.io/badge/Mirror%20on-Codeberg-blue?logo=git)](https://codeberg.org/xsser01/phantomcollect)
[![StackShare](http://img.shields.io/badge/tech-stack-0690fa.svg?style=flat)](https://stackshare.io/phantomcollect)
[![ArchWiki](https://img.shields.io/badge/docs-ArchWiki-blue?logo=arch-linux&logoColor=white)](https://wiki.archlinux.org/title/User:Xsser01/Phantomcollect)
[![Upstract](https://img.shields.io/badge/featured-Upstract-orange?logo=news&logoColor=white)](https://upstract.com/x/42be27b020ecb86f)
[![Hacker News](https://img.shields.io/badge/Hacker_News-Discussed-orange?logo=ycombinator&logoColor=white)](https://news.ycombinator.com/item?id=45885013)
