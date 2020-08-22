## python modules install localy
```bash
pip3 install -t python/lib/python3.7/site-packages -r requirements.txt
zip -r python.zip python/
```

## chrome binary and chrome driver download path
```bash
mkdir chrome; cd chrome
# chrome driver
curl -O https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
# headless chromium
curl -O -L https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-37/stable-headless-chromium-amazonlinux-2017-03.zip
unzip stable-headless-chromium-amazonlinux-2017-03.zip
rm stable-headless-chromium-amazonlinux-2017-03.zip
cd ..
zip -r chrome.zip chrome/
```

### reference
https://www.yamamanx.com/aws-lambdapython3-selenium-chrome-headless/
