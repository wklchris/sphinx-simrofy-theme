$serveport = 8123
Start-Process "http://localhost:$serveport"
python -m http.server $serveport --directory docs/