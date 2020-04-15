# tech-agilitynerd

tech.agilitynerd.com pelican driven content

## Develop

source ~/.virtualenvs/pelican-new/bin/activate

make devserver

cd output && python -m SimpleHTTPServer&

pelican -r content

## Deploy

pelican -s publishconf.py --ignore-cache content
