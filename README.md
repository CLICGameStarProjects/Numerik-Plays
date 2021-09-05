Bienvenue dans la doc.

Pour commencer à s'amuser :
# Numerik Plays

## C kwa ce truc
En gros, le projet permet lance 2 emulateur de pokemon et un serveur web. Sur le front end, on choisit entre un mode anarchie et un mode démocratie, chaque mode permet de controller l'une des fenêtres.

## Dependance
Les seuls OS qui fonctionnent pour le moment sont ceux basés sur GNU/Linux. 
<ul>
<li>
    <b>Nginx</b> N'importe quel tuto vous aidera mieux à le paramètrer que moi, l'idée c'est de créer un websocket avec gunicorn par exemple, et de servir ce socket avec un reverse proxy
</li>

<li>
    <b>Python3</b> <pre>sudo apt install python3</pre> ou qqch du genre, 
</li>

<li>
    <b>pip3</b> <pre>sudo apt-get -y install python3-pip</pre>
</li>
<li>
    <b>NPM</b> Désolé. <pre>sudo apt install npm</pre> 
</li>
<li>
    <b>mGBA</b> <pre>sudo apt install mgba</pre> 
</li>

<li>
    <b>wmctrl</b> Normalement, il est inclu dans votre distrib, sinon dispo en ppa : <pre>sudo apt install wmctrl</pre>
</li>
<li>
    <b>xdottool</b> utilisé pour manipuler les fenêtres: <pre>sudo apt install xdottool</pre>
</li>

</ul>


## Instructions
Première chose, dès que vous bossez sur la webbapp, passez direct sur l'environnement virtuel.

```source env/bin/activate ```

On installe les requirements python

```pip3 install -r ./requirements.txt```

On installe chartkick.js ou un truc du genre

```npm i```

Inch, ça tourne : on lance le socket, et on donnes les permissions de lectures. www-data est chez moi le user utilisé par nginx. 

```gunicorn --workers 1 --bind unix:numerikplays.sock -m 007 wsgi:app```
```sudo chown www-data:www-data numerikplays.sock```
```sudo chmod 777 numerikplays.sock```

Si tout se passe bien et que j'ai bient fait mon boulot, 2 fenêtres de Saphir vont s'ouvrir et un serveur hébergé sur votre IP va s'ouvrir.

## Contingency plan in case eveything goes very bad during the event 

Go into vscode the vscode terminal
Interrupt (CTRL+C)

go into the first window, press SHIFT + F1 to quicksave into quicksave slot 1 (If you only press F1, you'll quickload and fuck up everything even more)

go into the second window, press SHIFT + F2 to quicksave into quicksave slot 2 (If you only press F2, you'll quickload and fuck up everything even more)

Go into the VS code terminal again
<pre>gunicorn -- workers 1 --bind unix:/home/lucastrg/Projects/NumerikPlaysFlask/numerikplays.sock -m 007 wsgi:app</pre>

Dans la première poké fenêtre, press F1
Dans la seconde poké fenêtre, press F2

 
Open a new terminal
<pre>systemctl restart nginx</pre>





## Offre d'emplois/insultes
Pour l'inévitable moment où vous en aurez envie @LucasTrg sur Telegram

