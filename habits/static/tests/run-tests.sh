#!/bin/bash

(cd ../server/; source venv/bin/activate; python run.py 2>/dev/null &)
java -jar -Dwebdriver.gecko.driver=./lib/geckodriver lib/selenium-server-standalone-3.8.0.jar 2>/dev/null &
jprocess=$!

node_modules/.bin/wdio tests/conf/wdio.conf.js

kill $jprocess
killall python
