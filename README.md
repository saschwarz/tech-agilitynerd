# tech-agilitynerd

tech.agilitynerd.com pelican driven content


## Develop

workon pelican

cd output && python -m SimpleHTTPServer&

pelican -r content

## Deploy

pelican -s publishconf.py --ignore-cache content
