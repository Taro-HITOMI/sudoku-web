#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>CGI Test</title></head><body>"
echo "<h1>CGI is working!</h1>"
echo "<p>現在時刻: $(date)</p>"
echo "</body></html>"
