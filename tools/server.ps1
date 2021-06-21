# Remember to Ctrl+F5 the suspecious webpage before debuging
$serveport = 8123
Start-Process "http://localhost:$serveport"
python -m http.server $serveport --directory docs/