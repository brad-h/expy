#!/usr/bin/env sh

echo -n "Site name: "
read site
mkdir $site
echo -n "Author: "
read author
echo -n "Do you want a folder for JavaScript? "
read has_js
echo -n "Do you want a folder for CSS? "
read has_css

if echo "$has_js" | grep -iq "^y" ;then
    js_snippet="<script src=\"main.js\"><\/script>"
    mkdir "$site/js"
else
    js_snippet=''
fi
if echo "$has_css" | grep -iq "^y" ;then
    css_snippet="<link rel=\"stylesheet\" type=\"text\/css\" media=\"screen\" href=\"main.css\" \/>"
    mkdir "$site/css"
else
    css_snippet=''
fi
cat module43.template | sed "s/{site_name}/$site/g" | sed "s/{author}/$author/g" | sed "s/{js}/$js_snippet/g" | sed "s/{css}/$css_snippet/g" > "$site/index.html"
