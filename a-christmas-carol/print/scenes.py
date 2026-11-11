# A Christmas Carol: one painting per print spread (42), plus the reference portraits to paint first.
# Each scene: (stave, anchor cue, title, light, description). Characters are written the same way every time.
import json
SCROOGE = "a thin old man of about seventy\\, pointed nose\\, shrivelled cheeks\\, thin pale lips\\, wiry white eyebrows and a frosty white stubble on his chin\\, clean-shaven\\, no beard"
BOB = "Bob Cratchit\\, a thin careworn clerk of about thirty\\, clean-shaven\\, threadbare dark coat and a long white woollen comforter"
FRED = "Scrooge's nephew Fred\\, a ruddy handsome young man of twenty-eight with bright eyes\\, dark curly hair\\, a fine dark overcoat"
MARLEY = "the ghost of Jacob Marley\\, a transparent grey old man in pigtail\\, waistcoat\\, tights and boots\\, a white bandage tied round his jaw\\, a long chain wound about him made of cash-boxes\\, keys\\, padlocks\\, ledgers and heavy steel purses"
PAST = "the Ghost of Christmas Past\\, a strange small figure like a child and an old man at once\\, long white hair\\, smooth youthful face\\, white tunic belted with a lustrous belt\\, a branch of fresh green holly in its hand\\, a bright clear jet of light springing from its crown"
PRESENT = "the Ghost of Christmas Present\\, a jolly giant in a simple deep green robe bordered with white fur\\, bare feet\\, dark brown curls\\, a holly wreath with icicles on his head\\, carrying a glowing torch shaped like a horn of plenty"
YET = "the Ghost of Christmas Yet to Come\\, a tall solemn phantom shrouded in a deep black hooded garment that hides its head and face entirely\\, one outstretched pale hand pointing"
MRS = "Mrs Cratchit\\, a brave cheerful mother of forty in a twice-turned gown made brave with cheap ribbons"
TIM = "Tiny Tim\\, a small pale boy of six with a little crutch and his limbs supported by an iron frame"
BELLE = "Belle\\, a fair young woman of twenty in a modest black mourning dress"
YOUNG = "young Scrooge\\, a man in the prime of life of about thirty\\, clean-shaven\\, dark hair\\, an eager greedy restless look in his eye\\, dark frock coat"
FEZ = "old Fezziwig\\, a jolly stout old gentleman in a Welsh wig and a long waistcoat"

S = [
 # STAVE I
 (1, 15, "Fred at the counting-house door", "candle", f"Christmas Eve in Scrooge's dim counting-house\\, {SCROOGE} at his high desk\\, {FRED} bursting in from the foggy street glowing with cold\\, {BOB} copying letters in a small dismal cell beyond\\, one tiny coal fire"),
 (1, 50, "Humbug", "candle", f"{SCROOGE} scowling across his desk at {FRED}\\, who laughs good-humouredly with his hat in his hand\\, ledgers and a single candle\\, fog pressing at the windows"),
 (1, 100, "The two gentlemen", "candle", f"two portly pleasant gentlemen with books and papers in hand\\, hats off\\, standing before {SCROOGE} at his desk\\, who regards them coldly\\, dim counting-house\\, fog at the window"),
 (1, 148, "Bob on the slide", "night", f"{BOB} sliding down an icy slide on Cornhill at the end of a line of laughing boys\\, the long ends of his comforter flying\\, snowy London street at dusk\\, warm gas-lit shop windows\\, church tower"),
 (1, 150, "Marley's face in the knocker", "night", f"a dark old London door at night with a large brass knocker that has become the pale ghostly face of an old man\\, a dismal light about it\\, hair stirred as if by breath\\, {SCROOGE} with a key in the lock\\, staring\\, fog"),
 (1, 162, "Marley comes through the door", "candle", f"{MARLEY} passing straight through a heavy closed door into a gloomy old bedroom\\, the dying flame in the small fireplace leaping up\\, {SCROOGE} in dressing-gown and nightcap seated by the fire with a basin of gruel\\, aghast"),
 (1, 185, "Marley's Ghost", "candle", f"{MARLEY} seated motionless across the low fireplace from {SCROOGE} in dressing-gown and nightcap\\, the ghost's hair and coat-skirts stirring as if in hot vapour\\, Dutch tiles round the fireplace\\, deep shadows"),
 (1, 235, "Marley drops his jaw", "candle", f"{MARLEY} rising and raising a frightful cry\\, shaking his chain\\, {SCROOGE} fallen to his knees clasping his hands before his face in terror\\, gloomy bedroom\\, low fire"),
 (1, 295, "Mankind was my business", "candle", f"{MARLEY} standing erect\\, holding up his chain\\, wringing his hands\\, lamenting\\, {SCROOGE} trembling by the fireplace\\, candle guttering\\, deep chiaroscuro"),
 (1, 314, "The air filled with phantoms", "night", f"{SCROOGE} in nightcap looking out of an open sash window at night\\, the foggy air filled with wailing phantoms wandering in restless haste\\, every one wearing chains\\, a ghost in a white waistcoat with a great iron safe\\, below a poor woman and infant on a doorstep in the snow"),
 # STAVE II
 (2, 35, "The first of the three Spirits", "candle", f"the curtains of a dark old four-poster bed drawn aside by {PAST}\\, its light filling the room\\, {SCROOGE} in nightcap starting up half-recumbent\\, startled"),
 (2, 65, "The country road", "day", f"{SCROOGE} in dressing-gown and {PAST} standing hand in hand on an open country road in winter\\, fields covered with snow\\, a little market town with bridge\\, church and winding river\\, boys on shaggy ponies trotting by calling Merry Christmas\\, clear cold day"),
 (2, 85, "The lonely boy", "candle", f"a long bare melancholy schoolroom with plain deal desks\\, a lonely boy of ten reading near a feeble fire\\, {SCROOGE} and {PAST} watching from the shadows\\, {SCROOGE} weeping silently"),
 (2, 110, "Fan comes for her brother", "candle", f"a little girl of eight in a bonnet running into a bare schoolroom and putting her arms about the neck of a boy of twelve\\, kissing him\\, joyful\\, {SCROOGE} and {PAST} watching"),
 (2, 150, "Old Fezziwig", "candle", f"a warm old London warehouse office on Christmas Eve\\, {FEZ} behind a lofty desk laughing\\, rubbing his hands\\, calling Yo ho my boys\\, two young apprentices putting up the shutters\\, the floor swept for a dance\\, lamps trimmed\\, bright fire"),
 (2, 165, "Fezziwig's ball", "candle", f"Fezziwig's Christmas ball in a warehouse room\\, {FEZ} and his stout smiling wife leading a country dance\\, a fiddler at the high desk\\, three daughters\\, young men and women\\, housemaid and baker\\, joyous\\, warm lamplight\\, a fire"),
 (2, 200, "Belle", "day", f"{BELLE} sitting beside {YOUNG}\\, she speaks gently and sadly while he looks away\\, an English parlour in the grey light of a winter afternoon"),
 (2, 232, "Belle sets him free", "day", f"{BELLE} rising and turning away from {YOUNG}\\, who sits stiffly\\, a plain parlour\\, winter light from the window\\, quiet farewell"),
 (2, 250, "The father comes home", "candle", f"a warm comfortable parlour on Christmas Eve\\, a happy mother and her pretty daughter by the winter fire\\, a crowd of joyful children rushing a father who comes in laden with Christmas toys and parcels\\, a porter carrying more\\, firelight"),
 # STAVE III
 (3, 30, "The Ghost of Christmas Present", "candle", f"{SCROOGE} in dressing-gown at the door of his own room\\, transformed\\, walls hung with holly\\, mistletoe and ivy\\, a mighty roaring fire\\, heaped on the floor turkeys\\, geese\\, puddings\\, oysters\\, chestnuts\\, cakes and bowls of punch forming a throne\\, upon it {PRESENT}\\, glorious"),
 (3, 38, "Christmas morning in the city", "day", f"London streets on Christmas morning\\, people scraping snow from the pavements and roofs\\, boys throwing snowballs\\, the sky gloomy with dingy mist\\, housetops white with snow\\, cheerful and brisk"),
 (3, 50, "The Grocers'", "day", f"a glowing Victorian grocer's shop on Christmas morning with shutters half down\\, canisters\\, raisins\\, figs and candied fruits\\, customers hurrying with parcels\\, people carrying their dinners to the bakers' shops\\, {PRESENT} sprinkling incense from his torch over them unseen"),
 (3, 85, "Bob comes home with Tiny Tim", "candle", f"the Cratchits' small four-roomed house\\, {MRS} laying the cloth\\, children around the boiling saucepan of potatoes\\, {BOB} coming in with {TIM} upon his shoulder\\, warm and poor\\, {PRESENT} and {SCROOGE} at the threshold"),
 (3, 100, "The goose", "candle", f"the Cratchit family at their small table for Christmas dinner\\, {MRS} carving the goose\\, {BOB} with {TIM} beside him\\, children eager\\, apple sauce and mashed potatoes\\, warm candlelight\\, humble room"),
 (3, 120, "The pudding", "candle", f"{MRS} entering the little room proudly bearing the Christmas pudding\\, like a speckled cannonball\\, blazing in brandy with a sprig of holly stuck in the top\\, the Cratchit family delighted\\, {BOB} and {TIM}"),
 (3, 150, "God bless us every one", "candle", f"the Cratchit family drawn round the hearth\\, {BOB} raising a glass in a toast\\, {TIM} on his little stool close at his father's side\\, chestnuts on the fire\\, glasses and a custard cup\\, firelight on their faces"),
 (3, 160, "The lighthouse", "night", f"a solitary lighthouse built on a dismal reef of sunken rocks far out at sea\\, the waters chafing and dashing\\, two lighthouse keepers in rough clothes wishing each other Merry Christmas by their fire\\, a streak of fiery red in the west"),
 (3, 180, "Fred's laugh", "candle", f"a bright warm drawing-room at Christmas\\, {FRED} laughing heartily holding his sides\\, his very pretty young wife with a dimpled face laughing too\\, friends around\\, firelight and candles\\, {PRESENT} and {SCROOGE} watching unseen"),
 (3, 197, "Blind man's buff", "candle", f"a Christmas party game of blind man's buff in a warm drawing-room\\, a young man blindfolded chasing a plump young woman in a lace tucker among chairs and the piano\\, laughing guests\\, {SCROOGE} and {PRESENT} watching unseen"),
 (3, 215, "The Spirit grows old", "night", f"{PRESENT}\\, now grown old with grey hair\\, standing with {SCROOGE} in an open snowy London place at night\\, children leaving a Twelfth Night party in the distance\\, lamps"),
 (3, 240, "Ignorance and Want", "night", f"{PRESENT}\\, old\\, opening the folds of his green robe to reveal two thin pale ragged children\\, a boy and a girl\\, kneeling down at his feet clinging to the outside of his garment\\, {SCROOGE} recoiling\\, a bleak open place at night"),
 # STAVE IV
 (4, 30, "The Phantom", "night", f"{YET} moving slowly through a dark London street\\, its hand pointing\\, {SCROOGE} in dressing-gown following in the shadow of its dress\\, the city springing up about them\\, merchants in top hats on the Exchange"),
 (4, 50, "Old Joe's shop", "candle", f"a low beetling rag-and-bone shop in a foul obscure part of London\\, iron\\, old rags\\, bottles\\, bones and greasy offal heaped inside\\, a grey-haired rascal of seventy smoking a pipe by a charcoal stove\\, a rag curtain behind him"),
 (4, 65, "The bundles", "candle", f"in a dim rag-and-bone shop a charwoman\\, a laundress and an undertaker's man in faded black opening bundles of bed-curtains\\, blankets and a shirt before an old man smoking a pipe by a small stove\\, a lamp\\, {SCROOGE} and {YET} in the shadows"),
 (4, 85, "The dark chamber", "night", f"a bare dark bedroom\\, the curtains torn from the bed\\, on the bed under a ragged sheet a covered still form\\, face not shown\\, a pale light falling upon it\\, {SCROOGE} recoiling in horror\\, {YET} pointing"),
 (4, 105, "A happier house", "candle", f"a poor room by firelight\\, a young mother with her children waiting anxiously\\, her careworn husband coming in with a face of serious delight\\, {SCROOGE} and {YET} watching"),
 (4, 140, "The quiet house", "candle", f"the Cratchits' small room\\, very quiet\\, {MRS} sewing by the lamp\\, children still as statues in one corner\\, Peter reading a book\\, {TIM}'s little crutch leaning by an empty stool by the fire"),
 (4, 175, "Bob comes home", "candle", f"{BOB} coming home and sitting by the fire\\, his family drawing about him\\, {MRS} at his side\\, the children's faces pressed to his\\, quiet sorrowful love\\, lamplight"),
 (4, 215, "The churchyard", "night", f"a neglected overgrown London churchyard behind an iron gate at night\\, walled in by houses\\, {YET} pointing to a lonely untended gravestone\\, {SCROOGE} in dressing-gown creeping towards it trembling"),
 # STAVE V
 (5, 40, "Hallo here!", "day", f"{SCROOGE} in nightcap and nightgown leaning joyfully out of his opened window on a bright clear cold Christmas morning\\, golden sunlight\\, sweet fresh air\\, a boy in Sunday clothes in the snowy street below looking up\\, church bells"),
 (5, 90, "Scrooge in the streets", "day", f"{SCROOGE} in his best clothes walking happily through snowy London streets on Christmas morning\\, smiling and patting children on the head\\, people pouring forth from their houses\\, sunlight"),
 (5, 125, "A merry Christmas, Bob", "candle", f"Scrooge's counting-house\\, {SCROOGE} beaming and clapping {BOB} on the back\\, a big bright coal fire built up\\, a steaming bowl of Christmas punch on the desk\\, morning light"),
]
# reference portraits to paint first (3:4, plain dark background)
REFS = [("scrooge",SCROOGE+"\\, black frock coat"),("bob",BOB),("fred",FRED),("marley",MARLEY),("past",PAST),("present",PRESENT),("mrs-cratchit",MRS),("tiny-tim",TIM),("belle",BELLE),("young-scrooge",YOUNG),("fezziwig",FEZ)]
SREF={'day':'https://ianingram.github.io/Amenti-Readings/dracula/art/ch01-b5-2.jpg','night':'https://ianingram.github.io/Amenti-Studios/a-christmas-carol/carol-hero.jpg','candle':'https://ianingram.github.io/Amenti-Readings/dracula/art/ch03-b1-1.jpg'}
LIGHT={'day':'luminous winter daylight\\, plein air','night':'dramatic chiaroscuro\\, snowy gas-lit night','candle':'warm candlelight and firelight\\, dramatic chiaroscuro'}
ST=['I','II','III','IV','V'];out=[];cnt={}
for i,(st,cue,title,light,desc) in enumerate(S):
  cnt[st]=cnt.get(st,0)+1;tag=f"CC{ST[st-1]}-{chr(64+cnt[st])}"
  no='--no modern\\, text\\, letters'+(', beard' if 'Scrooge' in desc or 'SCROOGE' in desc else '')
  p=f"{tag} {desc.replace(chr(92)+',',',')}, oil painting, London 1843, rich academic realism, {LIGHT[light].replace(chr(92)+',',',')} --ar 16:9 --sref {SREF[light]} "+no.replace(chr(92)+",",",")
  out.append({'n':i+1,'tag':tag,'stave':st,'cue':cue,'title':title,'light':light,'prompt':p,'img':f'cc-{i+1:02d}.jpg'})
refs=[{'name':n,'prompt':f"CCREF-{n} portrait of {d.replace(chr(92)+',',',')}, half-length, plain dark background, oil painting, 1843, rich academic realism, soft studio light --ar 3:4"} for n,d in REFS]
json.dump({'scenes':out,'refs':refs},open('/tmp/claude-0/carol/scenes.json','w'),indent=1,ensure_ascii=False)
print(len(out),'scenes',len(refs),'refs');print(out[0]['prompt']);print(refs[0]['prompt'])
