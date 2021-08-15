Bienvenue dans la doc.

Pour commencer à s'amuser :
# Numerik Plays

## C kwa ce truc
En gros, le projet permet lance 2 emulateur de pokemon et un serveur web. Sur le front end, on choisit entre un mode anarchie et un mode démocratie, chaque mode permet de controller l'une des fenêtres.


## Dependance
<ul>
<li>
    <b>Nginx</b> N'importe quel tuto vous aidera mieux à le paramètrer que moi
</li>

<li>
    <b>Python3</b> <pre>sudo apt install python3</pre> ou qqch du genre, 
</li>

<li>
    <b>pip3</b> <pre>sudo apt-get -y install python3-pip</pre>
</li>
</ul>


## Instructions
```source env/bin/activate ```

```pip3 install -r ./requirements.txt```

```gunicorn --workers 1 --bind unix:numerikplays.sock -m 007 wsgi:app```

Si tout se passe bien et que j'ai bient fait mon boulot, 2 fenêtres de Saphir vont s'ouvrir et un serveur hébergé sur votre IP va s'ouvrir.


## Offre d'emplois/insultes
Pour l'inévitable moment où vous en aurez envie @LucasTrg sur Telegram
