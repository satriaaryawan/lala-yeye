#!/bin/bash

pip3 install -r requirement.txt
shodan init "$(cat shodan_api_key.txt)"
npm i -g wappalyzer