tech.agilitynerd.com/?tag=python
http://tech.agilitynerd.com/tag/python.html

if ($args ~ "^tag=(.*)") {
   set $p $1;
   rewrite ^/.*$ /tag/$p.html? permanent;
}
