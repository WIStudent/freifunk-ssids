# freifunk-ssids [![Build Status](https://travis-ci.org/WIStudent/freifunk-ssids.svg?branch=master)](https://travis-ci.org/WIStudent/freifunk-ssids)

This repository contains a list of SSIDs that are used by Freifunk.

## How to add SSIDs
If you are missing an SSID in the list, you can either send a Pull Request on the master branch or submit it [here](https://github.com/WIStudent/freifunk-ssids/issues/1).

## Validation
Use the included Python script to validate your changes.
```
python validator.py ssids.json
```

## Purpose
This repository was primarily created to make updating the SSID list in the [Freifunk Auto Connect App](https://github.com/WIStudent/FreifunkAutoConnectApp) easier. To check for new SSIDs the app downloads the latest `ssids.json` file form the `freifunk_auto_connect_production` branch.
