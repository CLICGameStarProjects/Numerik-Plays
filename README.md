Bienvenue dans la doc.

Pour commencer à s'amuser :

```source env/bin/activate```
```gunicorn --workers 1 --bind unix:numerikplays.sock -m 007 wsgi:app```

Si tout se passe bien et que j'ai bient fait mon boulot, 2 fenêtres de Saphir vont s'ouvrir et un serveur hébergé sur votre IP va s'ouvrir.
 

