pelican content -o output -s publishconf.py && ghp-import output && git push origin master gh-pages
echo Press any key to Continue.
pause > nul