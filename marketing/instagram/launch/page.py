import base64,io,html,os
from PIL import Image
P=[
("01","Whitby, East Cliff","ch. VII","Whitby, August. A storm comes in off the North Sea, and with it a ship no one is steering.\n\n“Then without warning the tempest broke.”\n— Bram Stoker, Dracula, chapter VII","#Dracula #BramStoker #Whitby #GothicArt #AmentiStudios"),
("02","Lucy among the statues","ch. IX","Lucy Westenra has begun to walk in her sleep again, out into the night, past the stone figures in the garden.\n\nDracula, chapter IX.","#Dracula #BramStoker #LucyWestenra #GothicArt #AmentiStudios"),
("03","The last climb","ch. XXVII","Van Helsing leaves Mina safe inside the holy circle and goes up alone through the snow to the castle.\n\nDracula, chapter XXVII.","#Dracula #BramStoker #VanHelsing #AmentiStudios"),
("04","The helmsman","ch. VII","The last entry in the log of the Demeter, found in a bottle in the captain’s pocket, his hands tied to the wheel.\n\n“God and the Blessed Virgin and the saints help a poor ignorant soul trying to do his duty.”\n— Dracula, chapter VII","#Dracula #BramStoker #Demeter #AmentiStudios"),
("05","Introducing Amenti Studios","","Amenti Studios makes great books into something you can listen to, look at and ask about.\n\nEach novel is read aloud by a cast drawn from the Amenti Library of Legends, with Charles Darwin as Jonathan Harker, Agatha Christie as Mina and Mary Shelley as Lucy. Each one is scored and painted scene by scene.\n\nOur first production is Bram Stoker’s Dracula.","#AmentiStudios #Dracula #BramStoker #Audiobook #ClassicLiterature"),
("06","The Demeter","ch. VI–VII","Out of Varna, bound for Whitby, carrying fifty great wooden boxes of earth and one passenger no one ever sees.\n\nDracula, chapters VI–VII.","#Dracula #BramStoker #Demeter #MaritimeArt #AmentiStudios"),
("07","Mina on the steps","ch. VIII","One in the morning. Lucy’s bed is empty. Mina runs out into the town and up the East Cliff steps towards the churchyard.\n\nDracula, chapter VIII.","#Dracula #BramStoker #Whitby #MinaHarker #AmentiStudios"),
("08","The Czarina Catherine","ch. XXIV","Hunted out of London, the Count takes ship for the Black Sea and home, and the hunters follow.\n\nDracula, chapter XXIV.","#Dracula #BramStoker #MaritimeArt #AmentiStudios"),
("09","Lucy","ch. XVI","Hampstead churchyard. The woman they buried a week ago is walking among the tombs.\n\n“Come to me, Arthur. Leave these others and come to me. My arms are hungry for you.”\n— Lucy Westenra, Dracula, chapter XVI","#Dracula #BramStoker #LucyWestenra #GothicArt #AmentiStudios"),
("10","The Un-Dead","ch. XV–XVI","The children of Hampstead come home late and tell of a beautiful lady in white who walks with them at night. Van Helsing knows what she is, and Arthur must see it for himself. Lucy Westenra is Un-Dead.\n\nDracula, chapters XV–XVI.","#Dracula #BramStoker #LucyWestenra #AmentiStudios"),
("11","Dracula · Volume One","Coming soon","The Borgo Pass, where the road east runs out and the Count’s calèche is waiting.\n\nDracula · Volume One. Books I and II of Bram Stoker’s novel, chapters I–XVI, illustrated throughout, in hardcover. Every chapter links to its scored reading.\n\nComing soon from Amenti Studios.","#Dracula #BramStoker #IllustratedBooks #AmentiStudios"),
("12","Piccadilly","ch. XIII","London, broad daylight. Mina feels Jonathan’s arm grip hers. He is staring at a tall, thin man by a carriage.\n\n“I believe it is the Count, but he has grown young.”\n— Jonathan Harker, Dracula, chapter XIII","#Dracula #BramStoker #VictorianLondon #AmentiStudios"),
]
def enc(im,q):
  b=io.BytesIO();im.save(b,'JPEG',quality=q);return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
def thumb(n):
  im=Image.open(f'posts/{n}.jpg');cw=int(1350*.75);x=(1080-cw)//2;return enc(im.crop((x,0,x+cw,1350)).resize((300,400)),78)
grid=''.join(f'<a href="#p{n}"><img src="{thumb(n)}" alt="Post {int(n)}"></a>' for n in [f'{i:02d}' for i in range(12,0,-1)])
cards=''
for n,t,ch,cap,tags in P:
  i=int(n);day='Launch day' if i<=3 else f'Day {i-2}'
  cards+=f'''<article id="p{n}" class="post"><img class="full" src="{enc(Image.open(f'posts/{n}.jpg'),84)}" alt="{html.escape(t)}">
<div class="meta"><div class="row"><span class="k">Post {i} of 12 · {day}</span>{'<span class="k dim">'+ch+'</span>' if ch else ''}</div>
<h3>{html.escape(t)}</h3><pre id="c{n}">{html.escape(cap+chr(10)*2+tags)}</pre>
<button type="button" data-c="c{n}">Copy caption</button></div></article>'''
bio="Great books read aloud by a cast of legends, scored and painted scene by scene.\nNow: Bram Stoker’s Dracula\nVolume One coming soon ↓"
F='/tmp/claude-0/-home-claude/2bd1063c-47d9-5020-8010-6af81f79ced0/scratchpad/instagram-launch.html'
old=open(F).read()
head=old[:old.index('<div class="wrap">')]
script=old[old.index('<script>'):]
body=f'''<div class="wrap">
<header><div class="k">Instagram · first twelve posts</div><h1>AMENTI STUDIOS</h1>
<p>This is how the profile grid will look once all twelve are up. The newest post sits top left, so they go up in reverse: post 1 first, post 12 last.</p></header>
<div class="grid">{grid}</div>
<section class="bio"><h2>Profile</h2><dl>
<dt>Name</dt><dd>Amenti Studios</dd>
<dt>Category</dt><dd>Publisher</dd>
<dt>Bio</dt><dd><pre id="cbio" style="margin:0">{html.escape(bio)}</pre></dd>
<dt>Link</dt><dd id="clink">https://ianingram.github.io/Amenti-Studios/dracula/company/</dd></dl>
<div class="row" style="justify-content:flex-start"><button type="button" data-c="cbio">Copy bio</button><button type="button" data-c="clink">Copy link</button></div></section>
<section><h2>Posting plan</h2><ol>
<li>Launch day: posts 1, 2 and 3, a few minutes apart, so the first visitors find a full row.</li>
<li>Then one a day, posts 4 to 12, which takes nine more days. The Volume One announcement, post 11, goes up the day before the last post.</li>
<li>To save a picture on your phone, press and hold it, then choose Save to Photos.</li></ol></section>
{cards}
</div>
'''
open(F,'w').write(head.replace('first nine posts','first twelve posts')+body+script);print(os.path.getsize(F)//1024,'KB')
