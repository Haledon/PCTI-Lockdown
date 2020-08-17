import random
import pickle
from colored import fore, back, style, fg, bg, attr
import string
import sys, termios, tty, os, time

def getch():
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  return ch
#sgambino223@gmail.com
#pcti123
#Update Quen cleanse
print(style.BOLD+"|"+style.RESET+"| |")

class Player:
  def __init__(self):
    self.money = 0
    self.team = []
    self.teamS = []
    self.backteam = []
    self.backteamS = []
    self.deadteam = []
    self.deadteamS = []
    self.suppteam = []
    self.suppteamS = []
    self.suppback = []
    self.suppbackS = []
    self.teamC = []
    self.backteamC = []
    self.deadteamC = []
    self.suppteamC = []
    self.suppbackC = []
    self.cteam = []
    self.cbackteam = []
    self.cdeadteam = []
    self.csuppteam = []
    self.csuppback = []
    self.teamID = []
    self.consumeinventory = []
    self.helminventory = []
    self.chestinventory = []
    self.bootsinventory = []
    self.weaponinventory = []
    self.accessinventory = []
    self.isoinventory = []
    self.questinventory = []
    self.ph1 = []
    self.ph2 = []

  def reset(self,typ):
    if typ == "Team":
      self.team = []
      self.teamS = []
      self.backteam = []
      self.backteamS = []
      self.deadteam = []
      self.deadteamS = []
    if typ == "Supp":
      for x in self.suppteam:
        self.suppback.append(x)
        self.suppbackS.append(x.name)
      self.suppteam = []
      self.suppteamS = []

class Entity:
  def __init__(self,NAME,HP,MP,AT,DF,MAT,MDF,SP,AC,EV,CT,APN,MPN,MRG,ID,GEND): 
    self.NAME = NAME        #Variables that every fighting entity share 
    self.HP = HP            #Health - Allows you to fight when > 0 
    self.MP = MP            #Mana - For casting skills"
    self.AT = AT            #Attack - Physical Damage
    self.DF = DF            #Defense - %cut of Physical damage based on rational function AT*(x/x+100)
    self.MAT = MAT          #Magic Attack - Magical Attack
    self.MDF = MDF          #Magic Defense - %cut of Magical damage based on rational function AT*(x/x+100)
    self.SP = SP            #Speed - Probability of going                                 
    self.AC = AC            #Accuracy - Chance of hitting
    self.EV = EV            #Evasion - Chance of dodgeing
    self.CT = CT            #Critical Chance - Chance of dealing bonus damage
    self.APN = APN          #Armor Penetration - Minuses Defense
    self.MPN = MPN          #Magic Penetration - Minuses Magic Defense
    self.MRG = MRG          #Mana Regeneration - Regens Mana on normal attacks
    self.cHP = HP
    self.cMP = MP
    self.cAT = AT
    self.cDF = DF
    self.cMAT = MAT
    self.cMDF = MDF
    self.cSP = SP
    self.cAC = AC
    self.cEV = EV
    self.cCT = CT
    self.CTdmg = 2
    self.cAPN = APN
    self.cMPN = MPN
    self.cMRG = MRG
    self.dmgreduct = 1
    self.isomode = False   #Indicates whether character has unlocked Iso-God Form
    self.ISOmode = False   #Indicates whether character is in Iso-God mode in battle
    self.isopoints = 500  #The amount of points accumulated for Iso-Mode, need 100 to unleashe, every 100 is a turn, gained 1 for 1 for every mana point used. 
    self.isoLevel = 5  #The level of your Iso-God Form, starts at 2. 
    self.ID = ID
    self.XP = 0
    self.LV = 1
    self.GEND = GEND
    self.GEN = []
    self.fHP = self.HP
    self.fMP = self.MP
    self.fAT = self.AT             
    self.fDF = self.DF
    self.fMAT = self.MAT
    self.fMDF = self.MDF
    self.fSP = self.SP
    self.fAC = self.AC
    self.fEV = self.EV
    self.fCT = self.CT
    self.fAPN = self.APN
    self.fMPN = self.MPN
    self.fMRG = self.MRG
    self.pAT = 1.00
    self.pDF = 1.00
    self.pMAT = 1.00
    self.pMDF = 1.00
    self.pSP = 1.00
    self.pAC = 1.00
    self.pEV = 1.00
    self.pCT = 1.00
    self.pAPN = 1.00
    self.pMPN = 1.00
    self.pMRG = 1.00    
    self.helm = ""
    self.chest = ""
    self.boots = ""
    self.weap = ""
    self.access = ""
    self.battleinventory = []
    self.skills = []  #skills
    self.CcHP = self.cHP
    self.CcMP = self.cMP
    self.Cisopoints = self.isopoints
    self.Cbattleinventory = self.battleinventory
    self.Cskills = []
    self.SHP = self.HP
    self.ScHP = self.cHP
    self.SMP = self.MP
    self.ScMP = self.cMP
    self.SAT = self.AT
    self.ScAT = self.cAT
    self.SDF = self.DF
    self.ScDF = self.cDF
    self.SMAT = self.MAT
    self.ScMAT = self.cMAT
    self.SMDF = self.MDF
    self.ScMDF = self.cMDF
    self.SSP = self.SP
    self.ScSP = self.cSP
    self.SAC = self.AC
    self.ScAC = self.cAC
    self.SEV = self.EV
    self.ScEV = self.cEV
    self.SCT = self.CT
    self.ScCT = self.cCT
    self.SAPN = self.APN
    self.ScAPN = self.cAPN
    self.SMPN = self.MPN
    self.ScMPN = self.cMPN
    self.Sbattleinventory = self.battleinventory
    self.SCTdmg = self.CTdmg
    self.Sdmgreduct = self.dmgreduct
    self.Sisopoints = self.isopoints
    self.SMRG = self.MRG
    self.ScMRG = self.cMRG
    self.Sskills = []
    self.SXP = self.XP
    self.SLV = self.LV
    self.Sisopoints = self.isopoints
    self.lastattack = ""
    self.coun = False
    self.counte = -1
    self.counterstrings = ["BLOCK","REDIRECT","DODGE","COUNTER"]
    self.wild = -1
    self.sma = -1
    self.valo = -1
    self.immort = -1
    self.barr = -1
    self.fromthes = -1
    self.run = -1  
    self.re = False
    self.res = -1
    self.shi = -1
    self.trem = -1
    self.isom = -1
    self.comb = -1
    self.callig = -1
    self.asm = -1
    self.pinp = -1
    self.bake = -1
    self.perfectr = -1
    self.rev = -1 
    self.grub = -1
    self.taun = -1
    self.knightv = -1
    self.obese = -1
    self.jabb = -1   
    self.tauntstrings = ["Your skills are inferior..*pushes up glasses*"]
    self.electr = -1
    self.silen = -1
    self.cutm = -1
    self.gunb = -1
    self.spark = -1 
    self.dar = -1
    self.da = -1
    self.dabstack = 0
    self.dabtarg = ""
    self.que = -1
    self.auto = -1
    self.chrono = -1
    self.proto = -1
    self.rub = -1
    self.falle = False
    self.fal = -1
    self.progo = -1
    self.armw = -1
    self.infe = -1
    self.selfd = -1
    self.chad = -1
    self.la = False
    self.las = -1
    self.engk = -1
    self.dsw = -1
    self.weir = -1
    self.rehe = -1
    self.powres = -1
    self.los = False
    self.lost = -1
    self.losthit = 0
    self.ling = -1
    self.grac = -1
    self.radi = -1
    self.whir = -1
    self.etern = -1
    self.now = False
    self.nowo = -1
    self.emo = -1
    self.outr = -1
    self.arri = -1
    self.recl = -1
    self.onet = -1
    self.hat = False
    self.hate = -1
    self.hatelis = []
    self.suc = -1
    self.powers = -1
    self.telep = -1
    self.mimi = -1
    self.desp = -1
    self.lifesteal = 0 #Positive Effects
    self.healmod = 1
    self.food = [0,0,0,0,0,0,0,0,0,0,0,0]
    self.pbarrier = 0
    self.invis = 0
    self.instant = False
    self.WI = False
    self.valor = 0
    self.valos = False
    self.immortal = 0
    self.enragev = 1
    self.manaflow = [0]
    self.resttimer = 21
    self.runhigh = 0
    self.SHIE = False
    self.isoboost = 0
    self.isoboostL = 0
    self.combd = [0]
    self.OB = False
    self.thehut = 0
    self.jabbaroll = 0
    self.ionized = [0]
    self.knightb = 0
    self.bonded = []
    self.darks = False
    self.dark = 0
    self.safety = 0
    self.chronotime = 0
    self.chronoslow = []
    self.quenshield = False
    self.tension = 0
    self.chadwalked = [0]
    self.chadl = False
    self.duel = []
    self.duelt = 0
    self.rehearsed = [0]
    self.prest = 0
    self.rested = 0
    self.graced = [0]
    self.radiant = [0]
    self.dmgstore = 0
    self.emmortal = 0
    self.solitude = [0]
    self.onethro = 0
    self.hater = 0
    self.surge = 0
    self.teth = []
    self.ptelepath = 0
    self.telepath = 0
    self.mimicm = 0
    self.mimit = 0
    self.revealed = 0
    self.fear = 0      #Negative Effects
    self.confusion = 0
    self.charmed = 0
    self.poisond = 0
    self.poisont = 0
    self.bleedd = 0
    self.bleedt = 0
    self.burnd = 0
    self.burnt = 0
    self.decayd = 0
    self.decayt = 0
    self.silenced = 0
    self.disarmed = 0
    self.orthoed = 0
    self.tremsl = 0
    self.chronot = 0
    self.greased = [0]
    self.marked = [0,0]
    self.revealed = 0
    self.ashamed = [0]
    self.tethered = []
    self.deturn = 0
    #Stuns
    self.stunned = False
    self.stunimmune = [0,0]
    self.tremstun = 0
    self.sparkstun = 0
    self.dance = 0
    self.rooted = 0
    self.cutfear = [0]
    self.tauntt = 0
    self.taunted = []
    self.frozen = 0
    self.paralyzed = 0
    self.repulsed = 0
    self.confused = 0
    #Supports
    self.chilled = 0
    self.beared = 0
    self.teamed = 0
    self.eag = 0
    self.caressed = 0
    #Quest-Specific Buffs
    self.Q1B = 0 #Richard fight Enraged Ishraq 2x attack boost
    self.cry = 0 #Nurse cry timer
    self.ovd = 0 #transformer overdrive
    #Mob Essentials
    self.turncount = 0
    self.setHP = 0
    self.tw1 = 0
    self.tw2 = 0
    self.tw3 = 0
    self.tw4 = 0
    #Amira
    self.ENRAGE = False  #Insane Dilemna
    self.talkEN = 0      #Insane Dilemna
    self.giantess = 0  #Giant - Abby
    self.resil = 1  #Amira prevent defeat
    #Mrs.Wells
    self.candyAC = 0
    self.notes = 0
    self.missingnotes = 0
    self.destruct = 4
    self.notecount = 0
    #Mr.Pudup
    self.blind = 0
    #Terra
    self.zanc = 0
    #Aqua
    self.rages = [0]
    self.ragestorm = False
    self.seeker = 0
    self.mvolley = 0
    self.mgh = [0]
    #Dr.Graham
    self.scirc = 0
    self.inert = 0
    self.fricf = 0
    self.glock = 0
    self.error = 0
    self.statr = False
    self.skillr = False
    self.HPlat = []
    self.MPlat = []
  
  def genderset(self):
    if "Male" in self.GEND:
      self.GEN = ["his","him","he"]
    elif "Female" in self.GEND:
      self.GEN = ["her","her","she"]

  def levelstatup(self,HP=0,MP=0,AT=0,DF=0,MAT=0,MDF=0,SP=0,AC=0,EV=0,CT=0,APN=0,MPN=0,MRG=0):
    if HP > 0:
      self.HP = self.HP + HP
    if MP > 0:
      self.MP = self.MP + MP
    if AT > 0:
      self.AT = self.AT + AT
    if DF > 0:
      self.DF = self.DF + DF
    if MAT > 0:
      self.MAT = self.MAT + MAT
    if MDF > 0:
      self.MDF = self.MDF + MDF
    if SP > 0:
      self.SP = self.SP + SP
    if AC > 0:
      self.AC = self.AC + AC
    if EV > 0:
      self.EV = self.EV + EV
    if CT > 0:
      self.CT = self.CT + CT
    if APN > 0:
      self.APN = self.APN + APN
    if MPN > 0:
      self.MPN = self.MPN + MPN
    if MRG > 0:
      self.MRG = self.MRG + MRG
    self.equipcheck()

  def savedstats(self):
    self.SHP = self.HP
    self.ScHP = self.cHP
    self.SMP = self.MP
    self.ScMP = self.cMP
    self.SAT = self.AT
    self.ScAT = self.cAT
    self.SDF = self.DF
    self.ScDF = self.cDF
    self.SMAT = self.MAT
    self.ScMAT = self.cMAT
    self.SMDF = self.MDF
    self.ScMDF = self.cMDF
    self.SSP = self.SP
    self.ScSP = self.cSP
    self.SAC = self.AC
    self.ScAC = self.cAC
    self.SEV = self.EV
    self.ScEV = self.cEV
    self.SCT = self.CT
    self.ScCT = self.cCT
    self.SAPN = self.APN
    self.ScAPN = self.cAPN
    self.SMPN = self.MPN
    self.ScMPN = self.cMPN
    self.Sisopoints = self.isopoints
    self.SCTdmg = self.CTdmg
    self.Sdmgreduct = self.dmgreduct
    self.SMRG = self.MRG
    self.ScMRG = self.cMRG
    self.SLV = self.LV
    self.SXP = self.XP
    self.Sisopoints = self.isopoints
    self.Sskills = []
    for x in self.skills:
      self.Sskills.append(x)
    self.Sbattleinventory = []
    for x in self.battleinventory:
      self.Sbattleinventory.append(x)

  def midbattlesave(self):
    self.CcHP = self.cHP
    self.CcMP = self.cMP
    self.Cisopoints = self.isopoints
    self.Cbattleinventory = []
    for x in self.battleinventory:
      self.Cbattleinventory.append(x)
    self.Cskills = []
    for x in self.skills:
      self.Cskills.append(x)

  def saverest(self,al,en,yes=""):
    if yes == "Mid":
      self.cHP = self.CcHP
      self.cMP = self.CcMP
      self.isopoints = self.Cisopoints
      self.battleinventory = []
      for x in self.Cbattleinventory:
        self.battleinventory.append(x)
      self.skills = []
      for x in self.Cskills:
        self.skills.append(x)
    else:
      self.cHP = self.ScHP
      self.cMP = self.ScMP
      self.isopoints = self.Sisopoints
      self.battleinventory = []
      for x in self.Sbattleinventory:
        self.battleinventory.append(x)
      self.skills = []
      for x in self.Sskills:
        self.skills.append(x)
    self.HP = self.SHP
    self.MP = self.SMP
    self.AT = self.SAT
    self.cAT = self.ScAT
    self.DF = self.SDF
    self.cDF = self.ScDF
    self.MAT = self.SMAT
    self.cMAT = self.ScMAT
    self.MDF = self.SMDF
    self.cMDF = self.ScMDF
    self.SP = self.SSP
    self.cSP = self.ScSP
    self.AC = self.SAC
    self.cAC = self.ScAC
    self.EV = self.SEV
    self.cEV = self.ScEV
    self.CT = self.SCT
    self.cCT = self.ScCT
    self.APN = self.SAPN
    self.cAPN = self.ScAPN
    self.MPN = self.SMPN
    self.cMPN = self.ScMPN
    self.CTdmg = self.SCTdmg
    self.dmgreduct = self.Sdmgreduct
    self.MRG = self.SMRG
    self.cMRG = self.ScMRG
    self.LV = self.SLV
    self.XP = self.SXP
    self.purge("Map Reset",al,en)
    self.purge("Death",al,en)

  def Ishraqlevelup(self,gain,Colis=False):
    xpl = [50,150,300,500,750,1050,1400,1800,2300,2900,3600,4400,5300,6300,7500,8900,10500,12300,14300,16550,19050,21800,24800,28050,31550,35300,39300,43550,48050,52800,57800,63050,68550,74300,80300,86550,93100,100000]
    broom = self.LV
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(10,0,3,0,0,0,0,0,0,0,0,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(10,0,2,0,0,0,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(15,0,3,5,0,0,0,0,0,0,0,0,0)
    if self.XP >=500 and self.LV == 4:
      self.LV = self.LV + 1 
      self.levelstatup(15,0,5,5,0,5,0,0,0,0,0,0,0)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(20,0,5,3,0,3,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(20,0,0,2,5,2,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(20,0,3,2,0,0,1,0,0,0,0,0,0)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(20,0,2,3,0,0,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.counte = self.counte + 1
      self.valo = self.valo + 1
      self.levelstatup(20,0,5,5,5,0,0,0,0,1,0,0,2)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(25,0,3,3,0,0,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(25,0,3,3,0,5,0,0,0,0,0,0,0)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(25,0,3,3,5,5,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(25,0,3,3,3,5,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,3,3,2,5,0,5,0,0,0,0,0)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(30,0,5,4,3,5,1,0,0,0,0,0,0)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(30,0,5,4,3,5,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(40,0,4,2,4,0,0,0,0,0,0,0,0)
    if self.XP >=12300 and self.LV == 18:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,3,0,0,0,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.counte = self.counte + 1
      self.valo = self.valo + 1
      self.levelstatup(100,0,8,5,0,0,0,5,0,1,5,0,2)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(75,0,5,3,2,0,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(75,0,5,3,2,0,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(75,0,5,3,2,0,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(75,0,5,3,2,0,1,0,0,0,0,0,0)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(100,0,10,8,2,0,0,5,0,1,5,0,0)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,8,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,8,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,8,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,8,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.counte = self.counte + 1
      self.valo = self.valo + 1
      self.levelstatup(80,0,8,4,0,0,0,5,0,1,5,0,2)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,5,4,2,5,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,5,3,2,5,1,0,0,0,0,0,0)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(50,0,5,3,2,5,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,5,0,2,5,0,0,0,0,0,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(100,0,10,10,2,5,0,0,0,1,5,0,0)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,0,2,0,5,0,0,0,0,0,0,0)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,0,2,0,0,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,0,2,0,0,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,0,2,0,0,0,0,0,0,0,0,0)
    if broom != self.LV:
      if Colis != True:
        print(self.NAME,"gains",gain,"XP...")
      revival(self,o=True)
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print(self.NAME,"levels up to level",str(broom)+"!")
    else:
      print(self.NAME,"gains",gain,"XP!",(xpl[((self.LV)-1)]-self.XP),"XP until level up!")

  def Daniellevelup(self,gain,Colis=False):
    broom = self.LV
    xpl = [50,150,300,500,750,1050,1400,1800,2300,2900,3600,4400,5300,6300,7500,8900,10500,12300,14300,16550,19050,21800,24800,28050,31550,35300,39300,43550,48050,52800,57800,63050,68550,74300,80300,86550,93100,100000]
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(5,5,2,3,3,5,0,0,0,0,0,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(5,5,2,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,2,4,4,4,0,0,0,0,0,0,0)
    if self.XP >=500 and self.LV == 4:
      self.LV = self.LV + 1 
      self.levelstatup(20,10,2,5,5,3,0,0,0,1,0,5,0)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(20,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.grub = self.grub + 1
      self.taun = self.taun + 1
      self.levelstatup(25,10,2,5,5,4,0,0,0,1,0,0,1)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(25,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(25,5,2,5,5,4,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,2,5,5,4,0,0,0,1,0,5,0)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,2,3,2,2,0,0,0,0,0,0,0)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(30,5,2,3,2,2,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,2,3,2,2,0,0,0,0,0,0,0)
    if self.XP >=12300 and self.LV == 18:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,2,3,3,2,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.grub = self.grub + 1
      self.taun = self.taun + 1
      self.levelstatup(70,10,2,3,1,2,0,5,0,1,0,0,1)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,3,2,2,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,2,1,1,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,2,1,1,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,2,1,1,0,0,0,0,0,0,0)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,2,2,1,0,0,0,1,0,5,0)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,2,2,1,0,0,0,0,0,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,2,2,1,1,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,2,3,2,1,0,0,0,0,0,0,0)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,3,2,3,1,0,0,0,0,0,0,0)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.grub = self.grub + 1
      self.taun = self.taun + 1
      self.levelstatup(100,10,2,3,2,1,0,0,0,1,0,0,1)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,3,3,2,1,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,3,3,3,1,0,0,0,0,0,0,0)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(80,5,3,3,3,1,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,3,3,3,1,0,0,0,0,0,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(80,15,3,5,3,1,0,0,0,0,0,5,0)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(75,10,3,5,3,1,0,0,0,0,0,0,0)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(75,10,3,5,3,1,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(75,10,3,5,3,1,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(75,15,4,5,0,1,0,0,0,0,0,0,0)
    if broom != self.LV:
      if Colis != True:
        print(self.NAME,"gains",gain,"XP...")
      revival(self,o=True)
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print(self.NAME,"levels up to level",str(broom)+"!")
    else:
      print(self.NAME,"gains",gain,"XP!",(xpl[((self.LV)-1)]-self.XP),"XP until level up!")

  def Juliuslevelup(self,gain,Colis=False):
    broom = self.LV
    xpl = [50,150,300,500,750,1050,1400,1800,2300,2900,3600,4400,5300,6300,7500,8900,10500,12300,14300,16550,19050,21800,24800,28050,31550,35300,39300,43550,48050,52800,57800,63050,68550,74300,80300,86550,93100,100000]
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(10,5,2,2,0,2,0,0,0,0,0,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(10,5,2,3,0,3,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(10,5,2,2,0,2,0,0,0,0,0,0,0)
    if self.XP >=500 and self.LV == 4:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,3,0,3,0,0,0,1,0,0,1)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(20,5,3,2,5,3,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,2,2,5,2,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,2,0,2,1,0,0,0,0,0,0)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,2,2,0,0,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.res = self.res + 1
      self.run = self.run + 1
      self.levelstatup(20,5,5,2,0,0,0,5,5,0,0,0,0)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(30,0,3,2,5,0,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(30,0,3,3,5,3,0,0,0,0,0,0,1)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(30,0,3,2,0,3,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(30,0,3,3,0,2,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(30,0,3,5,0,3,0,0,0,1,0,0,0)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,4,3,5,2,1,0,0,0,0,0,0)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(50,5,4,3,5,3,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,4,3,0,2,0,0,0,0,0,0,0)
    if self.XP >=12300 and self.LV == 18:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,4,0,3,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.res = self.res + 1
      self.run = self.run + 1
      self.levelstatup(150,10,5,3,0,2,0,5,5,0,0,0,1)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,4,4,5,3,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,4,4,5,2,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,4,3,0,3,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(80,0,6,3,0,1,1,0,0,0,0,0,0)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(180,0,6,5,0,1,0,0,0,1,0,0,0)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(100,0,6,5,5,0,0,0,0,0,0,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(100,0,5,5,5,0,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(100,0,5,5,0,0,0,0,0,0,0,0,0)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(100,0,4,5,0,0,0,0,0,0,0,0,0)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.res = self.res + 1
      self.run = self.run + 1
      self.levelstatup(200,0,4,3,0,0,0,0,0,0,0,0,1)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(75,5,4,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(75,5,4,4,0,0,1,0,0,0,0,0,0)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(75,5,4,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(75,5,5,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,5,4,0,0,0,0,0,1,0,0,0)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,5,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,5,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,5,2,0,0,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,0,2,0,0,0,0,0,0,0,0,0)
    if broom != self.LV:
      if Colis != True:
        print(self.NAME,"gains",gain,"XP...")
      revival(self,o=True)
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print(self.NAME,"levels up to level",str(broom)+"!")
    else:
      print(self.NAME,"gains",gain,"XP!",(xpl[((self.LV)-1)]-self.XP),"XP until level up!")

  def Kellylevelup(self,gain,Colis=False):
    broom = self.LV
    xpl = [50,150,300,500,750,1050,1400,1800,2300,2900,3600,4400,5300,6300,7500,8900,10500,12300,14300,16550,19050,21800,24800,28050,31550,35300,39300,43550,48050,52800,57800,63050,68550,74300,80300,86550,93100,100000]
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(5,5,3,2,3,0,0,0,0,0,0,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(5,5,2,1,4,3,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(10,5,3,2,3,2,0,0,0,0,0,0,0)
    if self.XP >=500 and self.LV == 4:
      self.LV = self.LV + 1 
      self.levelstatup(15,10,5,5,8,5,0,0,0,1,0,5,0)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(15,5,3,3,5,4,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,2,5,4,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,2,5,3,1,0,0,0,0,0,0)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,2,3,5,4,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.callig = self.callig + 1
      self.asm = self.asm + 1
      self.levelstatup(25,10,5,5,5,5,0,5,0,0,5,0,1)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,2,2,4,2,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(20,5,3,2,3,2,0,0,0,0,0,0,0)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,2,2,3,2,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(20,5,2,1,2,1,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(20,10,4,3,3,3,0,0,0,1,5,0,0)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,2,1,5,2,1,0,0,0,0,0,0)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(30,5,2,1,4,1,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,2,1,4,2,0,0,0,0,0,0,0)
    if self.XP >=12300 and self.LV == 18:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,3,1,3,2,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.callig = self.callig + 1
      self.asm = self.asm + 1
      self.levelstatup(30,10,2,1,4,3,0,0,5,0,0,5,1)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,0,5,2,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,0,3,2,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,0,3,2,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,0,4,2,1,0,0,0,0,0,0)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,0,5,2,0,0,0,1,0,5,0)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,2,2,4,2,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,2,4,2,0,0,0,0,0,0,0)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,2,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.callig = self.callig + 1
      self.asm = self.asm + 1
      self.levelstatup(100,10,3,2,4,2,0,5,0,0,5,0,1)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,2,5,3,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,2,5,3,1,0,0,0,0,0,0)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(40,5,3,2,5,3,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,3,2,5,4,0,0,0,0,0,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,3,2,5,3,0,0,0,2,0,0,0)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,3,0,5,2,0,0,0,0,0,0,0)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,3,0,5,2,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,3,0,5,3,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,3,0,5,0,0,0,0,0,0,0,0)
    if broom != self.LV:
      if Colis != True:
        print(self.NAME,"gains",gain,"XP...")
      revival(self,o=True)
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print(self.NAME,"levels up to level",str(broom)+"!")
    else:
      print(self.NAME,"gains",gain,"XP!",(xpl[((self.LV)-1)]-self.XP),"XP until level up!")

  def Timlevelup(self,gain,Colis=False):
    broom = self.LV
    xpl = [50,150,300,500,750,1050,1400,1800,2300,2900,3600,4400,5300,6300,7500,8900,10500,12300,14300,16550,19050,21800,24800,28050,31550,35300,39300,43550,48050,52800,57800,63050,68550,74300,80300,86550,93100,100000]
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(10,5,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(10,5,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(10,5,3,3,3,4,0,0,0,0,0,0,0)
    if self.XP >=500 and self.LV == 4:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,2,3,4,0,0,5,0,0,0,0)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(15,5,3,2,3,4,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,2,3,4,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,4,2,4,4,1,0,0,0,0,0,0)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,2,3,3,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.da = self.da + 1
      self.que = self.que + 1
      self.levelstatup(25,10,4,2,4,3,0,0,0,1,0,0,0)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(30,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(25,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(25,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(25,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(25,10,3,3,3,2,0,0,5,0,0,0,1)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(30,10,3,3,3,2,1,0,0,0,0,0,0)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(30,10,3,2,3,2,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,4,2,4,2,0,0,0,0,0,0,0)
    if self.XP >=12300 and self.LV == 18:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,4,2,4,2,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.da = self.da + 1
      self.que = self.que + 1
      self.levelstatup(50,10,4,2,4,2,0,0,0,1,0,0,1)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,3,2,3,3,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,3,2,3,2,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,3,2,3,2,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,3,2,3,2,1,0,0,0,0,0,0)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,3,2,3,3,0,0,5,0,0,0,0)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,4,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(50,15,4,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(75,15,3,2,3,2,0,0,0,0,0,0,0)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(75,15,3,2,3,3,0,0,0,0,0,0,0)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.da = self.da + 1
      self.que = self.que + 1
      self.levelstatup(60,15,5,2,5,2,0,0,0,1,0,0,1)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,4,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,4,2,4,3,1,0,0,0,0,0,0)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(60,5,4,2,4,4,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,4,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,4,2,4,2,0,0,5,0,0,0,0)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(40,5,3,2,3,3,0,0,0,0,0,0,0)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,4,0,4,2,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,0,3,2,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,0,2,3,0,0,0,0,0,0,0)
    if broom != self.LV:
      if Colis != True:
        print(self.NAME,"gains",gain,"XP...")
      revival(self,o=True)
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print(self.NAME,"levels up to level",str(broom)+"!")
    else:
      print(self.NAME,"gains",gain,"XP!",(xpl[((self.LV)-1)]-self.XP),"XP until level up!")

  def Arwynlevelup(self,gain,Colis=False):
    broom = self.LV
    xpl = [50,150,300,500,750,1050,1400,1800,2300,2900,3600,4400,5300,6300,7500,8900,10500,12300,14300,16550,19050,21800,24800,28050,31550,35300,39300,43550,48050,52800,57800,63050,68550,74300,80300,86550,93100,100000]
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(15,5,3,4,5,4,0,0,0,0,3,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(15,5,3,3,5,3,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,4,5,4,0,0,0,0,0,3,0)
    if self.XP >=500 and self.LV == 4:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,4,5,3,0,0,0,0,0,0,1)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(20,5,3,3,5,4,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,3,3,4,1,0,0,1,0,0,0)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,3,4,4,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.silen = self.silen + 1
      self.cutm = self.cutm + 1
      self.levelstatup(20,10,3,3,5,6,0,0,0,0,3,0,1)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,3,4,3,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(20,5,3,2,4,2,0,0,0,0,0,3,0)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(20,5,3,2,3,2,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,2,4,2,0,0,5,0,0,0,1)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,2,4,2,1,0,0,1,0,0,0)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(20,5,3,2,4,3,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,2,3,2,0,0,0,0,3,0,0)
    if self.XP >=12300 and self.LV == 18:
      self.LV = self.LV + 1 
      self.levelstatup(20,5,4,2,5,2,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.silen = self.silen + 1
      self.cutm = self.cutm + 1
      self.levelstatup(20,5,3,2,5,3,0,0,0,0,0,3,1)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,4,2,3,3,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,4,2,4,2,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,3,0,3,2,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,3,0,4,2,1,0,0,1,0,0,0)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,0,3,3,0,0,5,0,0,0,0)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,4,0,4,2,0,0,0,0,3,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,4,0,4,2,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,4,0,5,2,0,0,0,0,0,3,0)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,4,0,5,3,0,0,0,0,0,0,1)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.silen = self.silen + 1
      self.cutm = self.cutm + 1
      self.levelstatup(50,5,3,4,5,3,0,0,0,0,0,0,0)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,4,5,2,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,4,5,2,1,0,0,1,0,0,1)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(50,5,3,4,5,2,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,3,4,5,2,0,0,0,0,3,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,3,0,5,2,0,0,0,0,0,0,0)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,3,0,5,2,0,0,0,0,0,3,0)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,3,0,5,0,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,3,0,3,0,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(80,5,2,0,2,0,0,0,0,0,0,0,0)
    if broom != self.LV:
      if Colis != True:
        print(self.NAME,"gains",gain,"XP...")
      revival(self,o=True)
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print(self.NAME,"levels up to level",str(broom)+"!")
    else:
      print(self.NAME,"gains",gain,"XP!",(xpl[((self.LV)-1)]-self.XP),"XP until level up!")

  def Isopower(self,al,EW=False):
    if EW == True:
      self.skills.insert(0,"Runner's High")
      self.shi = self.shi - 3
      self.ISOmode = False
    else:
      if self.ISOmode == True:
        if self.cHP > 0:
          if self.isopoints < 100:
            self.isopoints = 0
          else:
            self.isopoints = self.isopoints - 100
        if self.isopoints <= 0 or (self.cHP <= 0 and self.immortal <= 0):
          self.isopoints = 0
          time.sleep(1)
          if self.cHP > 0:
            print("\n"+self.NAME,"reverts back to their normal state, exiting ISO-mode!")
          if self.NAME == "Ishraq":
            self.skills.remove("Enrage")
            self.skills.insert(0,"Wild Instinct")
            self.enragev = 1
            self.counte = self.counte - 3
          if self.NAME == "Ian" or self.NAME == "Julius":
            self.skills.insert(0,"Runner's High")
            self.shi = self.shi - 3
          if self.NAME == "Kelly":
            self.skills.remove("Omniheal")
            self.skills.insert(3,"Heal")
            self.perfectr = self.perfectr - 3
          if self.NAME == "Daniel":
            self.skills.insert(4,"Enlargen")
            self.skills.remove("Grubby Tides")
            self.skills.insert(0,"Grubby Hands")
            self.jabb = self.jabb - 3
          if self.NAME == "Taco Lord":
            if self.cHP > 0:
              al.teamS.remove(self.NAME)
              al.teamID.remove(self.ID)
              self.NAME = "Tim"
              al.teamS.append(self.NAME)
              al.teamID.append(self.ID)
            self.skills.remove("Taco Tuesday")
            self.da = self.da - 3
          if self.NAME == "Arwyn":
            self.fromthes = self.fromthes - 3
          self.ISOmode = False

  def learnskill(self,skillname):
    if skillname not in self.skills:
      self.skills.append(skillname)
    if skillname == "Counter":
      self.skills.remove("Counter")
      self.counte = self.counte + 1
      self.coun = True
    if skillname == "Wild Instinct":
      self.wild = self.wild + 1
    if skillname == "Valorous Chant":
      self.valo = self.valo + 1
    if skillname == "Smash":
      self.sma = self.sma + 1
    if skillname == "Immortality":
      self.immort = self.immort + 1
    if skillname == "Barrier":
      self.barr = self.barr + 1
    if skillname == "From The Shadows":
      self.fromthes = self.fromthes + 1
    if skillname == "Rest":
      self.skills.remove("Rest")
      self.res = self.res + 1
      self.re = True
    if skillname == "Runner's High":
      self.run = self.run + 1    
    if skillname == "Shield":
      self.shi = self.shi + 1
    if skillname == "Tremors":
      self.trem = self.trem + 1
    if skillname == "Isometric Drawings":
      self.isom = self.isom + 1
    if skillname == "Combo":
      self.comb = self.comb + 1
    if skillname == "Calligraphy":
      self.callig = self.callig + 1
    if skillname == "ASMR":
      self.asm = self.asm + 1
    if skillname == "Pinpoint":
      self.pinp = self.pinp + 1
    if skillname == "Heal":
      self.bake = self.bake + 1
    if skillname == "Perfect Requiem":
      self.perfectr = self.perfectr + 1
    if skillname == "Revive":
      self.rev = self.rev + 1
    if skillname == "Grubby Hands":
      self.grub = self.grub + 1
    if skillname == "Taunt":
      self.taun = self.taun + 1
    if skillname == "Knight's Vow":
      self.knightv = self.knightv + 1
    if skillname == "Photosynthesis":
      self.obese = self.obese + 1
    if skillname == "Enlargen":
      self.jabb = self.jabb + 1
    if skillname == "Electron":
      self.electr = self.electr + 1
    if skillname == "Silence":
      self.silen = self.silen + 1
    if skillname == "Cut Myself":
      self.cutm = self.cutm + 1
    if skillname == "Gunblade":
      self.gunb = self.gunb + 1
    if skillname == "Spark Net":
      self.spark = self.spark + 1
    if skillname == "Darkness":
      self.dar = self.dar + 1
    if skillname == "Dab":
      self.da = self.da + 1
    if skillname == "Quen":
      self.que = self.que + 1
    if skillname == "Autosentry":
      self.auto = self.auto + 1
    if skillname == "Chronopower":
      self.chrono = self.chrono + 1
    if skillname == "Safety Belt":
      self.proto = self.proto + 1
    if skillname == "Rubix Cube":
      self.rub = self.rub + 1
    if skillname == "Fallen Symbol":
      self.skills.remove("Fallen Symbol")
      self.fal = self.fal + 1
      self.falle = True
    if skillname == "Progressive Overload":
      self.progo = self.progo + 1
    if skillname == "Arm Wrestling":
      self.armw = self.armw + 1
    if skillname == "Inferno":
      self.infe = self.infe + 1
    if skillname == "Self-Destruct":
      self.selfd = self.selfd + 1
    if skillname == "Chad Walk":
      self.chad = self.chad + 1
    if skillname == "No Women":
      self.now = True
      self.skills.remove("No Women")
      self.nowo = self.nowo + 1
    if skillname == "Outrage":
      self.outr = self.outr + 1
    if skillname == "Arrivederci":
      self.arri = self.arri + 1
    if skillname == "Recluse":
      self.recl = self.recl + 1
    if skillname == "One Throat":
      self.onet = self.onet + 1
    if skillname == "Lost Love":
      self.lost = self.lost + 1
      self.skills.remove("Lost Love")
      self.los = True
    if skillname == "Graceful Gales":
      self.grac = self.grac + 1
    if skillname == "Lingering Light":
      self.ling = self.ling + 1
    if skillname == "Whirling Winds":
      self.whir = self.whir + 1
    if skillname == "Radiant Resilience":
      self.radi = self.radi + 1
    if skillname == "Eternal Equinox":
      self.etern = self.etern + 1
    if skillname == "Lash":
      self.la = True
      self.las = self.las + 1
      self.skills.remove("Lash")
    if skillname == "Energy Kick":
      self.engk = self.engk + 1
    if skillname == "Dancer's Swiftness":
      self.dsw = self.dsw + 1
    if skillname == "Weird Flex":
      self.weir = self.weir + 1
    if skillname == "Rehearsal":
      self.rehe = self.rehe + 1
    if skillname == "Power Rest":
      self.powres = self.powres + 1
    if skillname == "Haters":
      self.skills.remove("Haters")
      self.hate = self.hate + 1
      self.hat = True
    if skillname == "Suck":
      self.suc = self.suc + 1
    if skillname == "Power Surge":
      self.powers = self.powers + 1
    if skillname == "Telepathy":
      self.telep = self.telep + 1
    if skillname == "Mimic":
      self.mimi = self.mimi + 1
    if skillname == "Desperation":
      self.desp = self.desp + 1
    

  def effects(self,ally,enemy): #Non-Global effects(so no timer here for onhit or onturn)
    global player1
    global player2

    #Map effect
    if self.mgh[0] > 0:
      if self.mgh[1] in enemy.team:
        if self.mgh[1].runhigh <= 0 or self.mgh[1].stunimmune[0] != 1:
          self.pSP = self.pSP * 0.7
      else:
        if self.mgh[1] == self:
          self.fEV = self.fEV + 40
      
    if self.darks == True:
      self.pAPN = self.pAPN * (1.3+(0.1*self.dar))
      self.pMPN = self.pMPN * (1.3+(0.1*self.dar))
      self.fCT = self.fCT + (15+(5*self.dar))
      self.CTdmg = self.CTdmg + (0.10+(0.05*self.dar))

    if self.dark > 0:
      for x in enemy.team:
        if x.darks == True:
          self.fAC = self.fAC - (20+(10*x.dar))
          break

    if self.chilled > 0:
      if self.runhigh <= 0 or self.stunimmune[0] != 1:
        self.pSP = self.pSP * 0.6

    #Normal effect

    if self.food[0] > 0:
      self.fAT = self.fAT + self.food[1]
      self.fDF = self.fDF + self.food[2]
      self.fMAT = self.fMAT + self.food[3]
      self.fMDF = self.fMDF + self.food[4]
      self.fSP = self.fSP + self.food[5]
      self.fAC = self.fAC + self.food[6]
      self.fEV = self.fEV + self.food[7]
      self.fCT = self.fCT + self.food[8]
      self.fAPN = self.APN + self.food[9]
      self.fMPN = self.fMPN + self.food[10]
      self.fMRG = self.fMRG + self.food[11]

    if self.teamed > 0:
      self.fDF = self.fDF + (40+round((20/240)*self.supportscale()))

    if self.eag > 0:
      self.fAC = self.fAC + (30+round((30/240)*self.supportscale()))
      self.fCT = self.fCT + (25+round((10/240)*self.supportscale()))

    if self.caressed > 0:
      self.fAC = self.fAC - (20+round((20/240)*self.supportscale()))

    if self.chronot > 0:
      for x in enemy.team:
        if self in x.chronoslow:
          self.fSP = self.fSP - ((0.1+(0.05*x.chrono))*self.SP)
          if self.fSP <=0:
            self.fSP = 1
    
    if len(self.chronoslow) > 0:
      for x in self.chronoslow:
        if x.chronot > 0:
          self.fSP = self.fSP + ((0.1+(0.05*self.chrono))*x.SP)
        else:
          self.chronoslow.remove(x)

    if self.combd[0] > 0:
      self.fAPN = self.fAPN + ((self.combd[1].SP*(1+(0.05*self.combd[1].comb)))+self.combd[2].SP)
      self.fMPN = self.fMPN + ((self.combd[1].SP*(1+(0.05*self.combd[1].comb)))+self.combd[2].SP)

    if len(self.teth) > 0:
      split = (0.1+(0.05*self.powers))
      people = len(self.teth)
      dsplit = split/people
      for x in self.teth:
        self.fAT = self.fAT + (dsplit*x.AT)
        self.fMAT = self.fMAT + (dsplit*x.MAT)

    if len(self.tethered) > 0:
      split = (0.1+(0.05*self.tethered[0].powers))
      people = len(self.tethered[0].teth)
      if people > 0:
        dsplit = split/people
        self.fAT = self.fAT - (dsplit*self.AT)
        self.fMAT = self.fMAT - (dsplit*self.MAT)
      else:
        self.tethered.remove(self.tethered[0])

    if self.hat == True:
      for x in self.hatelis:
        self.fEV = self.fEV + (5+(2.5*self.hate))
        self.fCT = self.fCT + (5+(2.5*self.hate))

    if self.burnt > 0:    #On Turn Debuff
      self.pAT = self.pAT * 0.75
      self.pMAT = self.pMAT *0.75
    
    if self.bleedt >0:    #On Turn Debuff
      if self.runhigh <= 0 or self.stunimmune[0] != 1:
        self.pSP = self.pSP *0.75

    if self.poisont >0:   #On Turn Debuff
      self.pDF = self.pDF *0.75
      self.pMDF = self.pMDF* 0.75

    if self.fear > 0:
      self.dmgreduct = self.dmgreduct * 1.25
      self.pAT = self.pAT * 0.75
      self.pMAT = self.pMAT * 0.75

    if self.rehearsed[0] > 0:
      self.fEV = self.fEV + ((0.2+(0.05*self.rehearsed[1].dsw))*self.rehearsed[1].EV)

    if self.ashamed[0] > 0:
      self.pMAT = self.pMAT * (0.6-(self.ashamed[1].weir*0.05))
      self.pMPN = self.pMPN * (0.2-(self.ashamed[1].weir*0.025))

    if self.onethro > 0:
      self.fAPN = self.fAPN + (30+(self.onet*7.5))
      self.fMPN = self.fMPN + (30+(self.onet*7.5))

    if self.marked[0] > 0:
      self.dmgreduct = self.dmgreduct * (1.09+(0.04*self.marked[2].arri))
    
    if self.solitude[0] > 0:
      self.pAT = self.pAT * (1.1+(0.05*self.solitude[1].recl))
      self.pMAT = self.pMAT * (1.1+(0.05*self.solitude[1].recl))
      if self == self.solitude[1]:
        self.pMDF = self.pMDF * (0.8-(0.05*self.recl))
        self.pDF = self.pDF * (0.8-(0.05*self.recl))

    if self.blind > 0:
      self.pEV = self.pEV * 0.75
      self.pAC = self.pAC * 0.75
      self.pCT = self.pCT * 0.75

    if self.ISOmode == True:
      if self.NAME == "Ishraq":
        self.pAT = self.pAT * 1.5
        self.fEV = self.fEV + 55
        self.fCT = self.fCT + 55
        self.pDF = self.pDF * 1.1
        self.pMDF = self.pMDF * 1.5
        self.pSP = self.pSP * 1.5
        self.pAT = self.pAT * self.enragev
        self.pSP = self.pSP * self.enragev
      elif self.NAME == "Julius" or self.NAME == "Ian":
        self.pAT = self.pAT * 1.75
        self.pDF = self.pDF * 1.75
        self.pMDF = self.pMDF * 1.5
        self.pMAT = self.pMAT * 1.3
        self.pAC = self.pAC * 1.3
        self.pEV = self.pEV * 1.3
        self.pSP = self.pSP * 1.3
      elif self.NAME == "Kelly":
        self.pMAT = self.pMAT * 1.6
        self.pAC = self.pAC * 2
        self.pAT = self.pAT * 1.4
        self.pDF = self.pDF * 1.4
        self.pMDF = self.pMDF * 1.1
        self.pEV = self.pEV * 1.4
      elif self.NAME == "Daniel":
        self.pDF = self.pDF * 1.8
        self.pMDF = self.pMDF * 2
        self.pAT = self.pAT * 1.6
        self.pMAT = self.pMAT * 1.4
        self.pAC = self.pAC * 1.5
      elif self.NAME == "Tim":
        self.pAT = self.pAT * 1.3
        self.pDF = self.pDF * 1.3
        self.pMDF = self.pMDF * 1.3
        self.pMAT = self.pMAT * 1.3
        self.pAPN = self.pAPN * 4
        self.pMPN = self.pMPN * 4
        self.pSP = self.pSP * 1.3
      elif self.NAME == "Arwyn":
        self.pAT = self.pAT * 1.3
        self.pDF = self.pDF * 1.3
        self.pMDF = self.pMDF * 1.3
        self.pMAT = self.pMAT * 1.3
        self.pAPN = self.pAPN * 2
        self.pMPN = self.pMPN * 2
        self.pCT = self.pCT * 3
      elif self.NAME == "The Soul of Kelly":
        self.pAT = self.pAT * 1.5
        self.pMAT = self.pMAT * 1.5
        self.pSP = self.pSP * 1.5
        self.pAC = self.pAC * 2
        self.pEV = self.pEV * 1.5
        self.pCT = self.pCT * 1.5
        self.pAPN = self.pAPN * 2
        self.pMPN = self.pMPN * 2

    if self.WI == True:    #Permanent Passive
      self.pAT = self.pAT * (1.15 + (0.025*self.wild))
      self.pSP = self.pSP * (1.35 + (0.05*self.wild))
      self.fEV = self.fEV + (30 + (5*self.wild))
      self.fCT = self.fCT + (30 + (5*self.wild))
      self.pMAT = self.pMAT * 0.8 
      self.pMDF = self.pMDF * 0.8
      self.pAC = self.pAC * 0.8

    if self.valor >0:
      for x in ally.team:
        if x.valos == True:
          if len(ally.team) >1:
            self.pAT = self.pAT * (1.2 + (0.05*x.valo))
          if len(ally.team) > 2:
            self.pDF = self.pDF * (1.2 + (0.05*x.valo))
          if len(ally.team) > 3:
            self.pSP = self.pSP * (1.2 + (0.05*x.valo))
          break

    if self.immortal > 0:   #On turn buff
      self.lifesteal = self.lifesteal + (0.3+(0.1*self.immort))
    
    if self.emmortal > 0:
      self.lifesteal = self.lifesteal + (0.75+(0.15*self.emo))
      self.dmgreduct = self.dmgreduct * (1.3+(0.05*self.emo)) 

    if self.radiant[0] > 0:
      self.pDF = self.pDF * (1.5+(0.1*self.radiant[1].radi)) 
      self.pMDF = self.pMDF * (1.5+(0.1*self.radiant[1].radi)) 

    if self.graced[0] > 0:
      self.healmod = self.healmod + 0.25

    if self.pbarrier > 0:   #On hit buff
      self.fDF = self.fDF + 100000
      self.pDF = self.pDF * 100
      
    if self.manaflow[0] > 0:   #On turn buff 
      self.pMRG = self.pMRG * (2 + (0.5*self.manaflow[1].asm))

    if self.runhigh > 0:    #Global buff
      self.pAT = self.pAT * (1.5+(0.05*self.run))
      self.pDF = self.pDF * (1.5+(0.05*self.run))
      
    if self.tremsl > 0:    #Global debuff
      if self.runhigh <= 0 or self.stunimmune[0] != 1:
        self.pSP = self.pSP * 0.5

    if self.greased[0] > 0:    #On hit debuff   
      self.fEV = self.fEV - (20+(10*self.greased[1].grub))

    if self.OB == True:    #Permanent Passive
      self.pAT = self.pAT * (0.2 + (0.05*self.obese))

    if self.ionized[0] > 0:    #On turn BUff    
      self.fAC = self.fAC + (20 + (5*self.ionized[1].electr))
      self.fEV = self.fEV + (20 + (5*self.ionized[1].electr))
      self.pMAT = self.pMAT * (1.15 + (0.1*self.ionized[1].electr))
      self.fSP = self.fSP + (10 + (5*self.ionized[1].electr))

    if self.cutfear[0] > 0:       
      self.pDF = self.pDF * (0.7 - (0.05*self.cutfear[1].cutm))
      self.pMDF = self.pMDF * (0.7 - (0.05*self.cutfear[1].cutm)) 

    if self.safety > 0:
      self.fEV = self.fEV + 100000

    if self.SHIE == True:
      self.dmgreduct = self.dmgreduct * (0.6-(0.025*self.shi))

    if self.isoboostL > 0:
      self.counte = self.counte + 1
      self.res = self.res + 1 
      self.fal = self.fal + 1
      self.hate = self.hate + 1
      self.wild = self.wild + 1    
      self.valo = self.valo + 1    
      self.sma = self.sma + 1    
      self.immort = self.immort + 1    
      self.barr = self.barr + 1   
      self.fromthes = self.fromthes + 1    
      self.run = self.run + 1        
      self.shi = self.shi + 1    
      self.trem = self.trem + 1    
      self.isom = self.isom + 1   
      self.comb = self.comb + 1
      self.callig = self.callig + 1
      self.asm = self.asm + 1 
      self.pinp = self.pinp + 1   
      self.bake = self.bake + 1
      self.perfectr = self.perfectr + 1
      self.rev = self.rev + 1
      self.grub = self.grub + 1
      self.taun = self.taun + 1
      self.knightv = self.knightv + 1
      self.obese = self.obese + 1
      self.jabb = self.jabb + 1
      self.electr = self.electr + 1
      self.silen = self.silen + 1
      self.cutm = self.cutm + 1
      self.gunb = self.gunb + 1
      self.infe = self.infe + 1
      self.spark = self.spark + 1
      self.dar = self.dar + 1
      self.da = self.da + 1      
      self.que = self.que + 1
      self.auto = self.auto + 1     
      self.chrono = self.chrono + 1      
      self.proto = self.proto + 1        
      self.rub = self.rub + 1
      self.progo = self.progo + 1
      self.armw = self.armw + 1
      self.selfd = self.selfd + 1
      self.chad = self.chad + 1
      self.infe = self.infe + 1
      self.las = self.las + 1
      self.engk = self.engk + 1
      self.dsw = self.dsw + 1
      self.weir = self.weir + 1
      self.rehe = self.rehe + 1
      self.powres = self.powres + 1
      self.lost = self.lost + 1
      self.ling = self.ling + 1
      self.grac = self.grac + 1
      self.radi = self.radi + 1
      self.whir = self.whir + 1
      self.etern = self.etern + 1
      self.nowo = self.nowo + 1
      self.emo = self.emo + 1
      self.outr = self.outr + 1
      self.arri = self.arri + 1
      self.recl = self.recl + 1
      self.onet = self.onet + 1
      self.suc = self.suc + 1
      self.mimi = self.mimi + 1
      self.telep = self.telep + 1
      self.desp = self.desp + 1
      self.powers = self.powers + 1
      self.isoboostL = 0
         
    if self.thehut > 0:
      self.dmgreduct = self.dmgreduct * (0.7-(0.05*self.jabb))
      self.pAT = self.pAT * (1.125 + (0.125*self.jabb))
      self.pEV = self.pEV * 0.5

    if len(self.bonded) > 0:
      self.dmgreduct = self.dmgreduct * (0.6-(0.05*self.bonded[1].knightv))
      self.fAT = self.fAT + ((0.02+(0.005*self.bonded[1].knightv))*self.bonded[1].fHP)
      self.fMAT = self.fMAT + ((0.02+(0.005*self.bonded[1].knightv))*self.bonded[1].fHP)

    if self.rested > 0:
      self.pAT = self.pAT * (1.3+(0.075*self.powres))
      self.fCT = self.fCT + (40+(5*self.powres))

    if self.tension > 0:
      self.pAT = self.pAT * ((1.7+(0.1*self.progo))+((0.8+(0.05*self.progo))*self.tension))
      if self.tension >= 3 and self.tension < 5:
        self.pAC = self.pAC * (1.6 + (0.1*self.progo))
        self.fAPN = self.fAPN + (50 + (12.5*self.progo))
      elif self.tension == 5:
        self.pAC = self.pAC * (2+(0.125*self.progo))
        self.fAPN = self.fAPN + (100 + (25*self.progo))

    for x in ally.deadteam:
      if x.falle == True:
        self.pAT = self.pAT * (1.1+(0.05*x.fal))
        self.pMAT = self.pMAT * (1.1+(0.05*x.fal))
        self.dmgreduct = self.dmgreduct * (0.9-(0.05*x.fal))

    for x in allfighters:
      if len(x.duel) > 0:
        if self == x.duel[0] and self.duelt > 0:
          self.pAT = self.pAT * (1.2+(0.025*self.armw))
          self.pMAT = self.pMAT * (1.2+(0.025*self.armw))
          self.dmgreduct = self.dmgreduct * (0.9-(0.025*self.armw))
        elif self == x.duel[1] and self.duelt <=0:
          self.pDF = self.pDF * (0.8 - (0.05*x.duel[0].armw))
          self.pMDF = self.pMDF * (0.8 - (0.05*x.duel[0].armw))
          self.fEV = self.fEV - (30 + (5*x.duel[0].armw))

    if self.chadwalked[0] > 0:
      if self.chadl == True:
        self.fCT = self.fCT + (40 + (12.5*self.chad))
      else:
        self.fCT = self.fCT + 40
      self.CTdmg = self.CTdmg + (0.1 + ((0.15/4)*self.chadwalked[1].chad))

    if self.Q1B > 0:
      self.pAT = self.pAT*2

    if self.giantess > 0:
      self.pAT = self.pAT * 4
      self.fEV = self.fEV - 100
      self.pMAT = self.pMAT * 0.25

    if self.NAME == "Amira" and self.ID !="11":
      for x in ally.team:
        if x.NAME == "Kelly" and x.cHP > 0: 
          self.pDF = self.pDF * 10
          self.pMDF = self.pMDF * 10
        if x.NAME == "Jackie" and x.cHP > 0: 
          self.fEV = self.fEV + 100
          self.fCT = self.fCT + 50
        if x.NAME == "Abby" and x.cHP > 0: 
          self.fAC = self.fAC + 100
          self.fCT = self.fCT + 50
        if x.NAME == "Meryem" and x.cHP > 0: 
          self.fAPN = self.fAPN + 100
          self.fMPN = self.fMPN + 100
      if self.cHP <= (0.2*self.fHP):
        if self.talkEN == 0 and self.ENRAGE == False:
          self.talkEN = 5
          time.sleep(1)
          print(fore.GREY_0 + back.CYAN_1 + style.BOLD + "\nAmira: DO YOU HATE ME!!??" + style.RESET)
          time.sleep(1)
          self.purge("Cleanse",bots,you)
          self.currentstats(bots,you)
        if self.ENRAGE == True and self.talkEN == 0:
          self.talkEN = -1
          self.ENRAGE = False
          for x in player2.team:
            if x.NAME == "Kelly" or x.NAME == "Jackie" or x.NAME == "Abby" or x.NAME == "Meryem":
              x.cHP = x.fHP
          for x in player2.deadteam:
            x.cHP = x.fHP
            player2.team.append(x)
            player2.teamS.append(x.NAME)
            player2.teamID.append(x.ID)
            if x.NAME == "Kelly":
              time.sleep(0.1) 
              print(fore.MAGENTA_1 + "\nKelly is zapped back to life!" + style.RESET)
            if x.NAME == "Jackie":
              time.sleep(0.1)   
              print(fore.GREEN_1 + "\nJackie is zapped back to life!" + style.RESET)
            if x.NAME == "Abby":
              time.sleep(0.1) 
              print(fore.YELLOW_1 + "\nAbby is zapped back to life!" + style.RESET)
            if x.NAME == "Meryem":
              time.sleep(0.1) 
              print(fore.RED_1 + "\nMeryem is zapped back to life!" + style.RESET)
          player2.deadteam = []
          player2.deadteamS = []

    if self.talkEN > 0:
      self.fEV = self.fEV + 1000
    
    if self.candyAC > 0:
      self.pAC = self.pAC * 0
    
    if self.cry > 0:
      self.fEV = self.fEV - 40
      self.fSP = self.fSP - 15

    if self.ovd > 0:
      self.pSP = self.pSP * 3
    
    if self.scirc > 0:
      self.pAT = self.pAT * 10
      self.pMAT = self.pMAT * 10

  def maptimers(self,ally,enemy): #Map effects, on no matter what, usually with global timers
    global sett

    if self.mgh[0] > 0:
      self.mgh[0] = self.mgh[0] - 1
      if self.mgh[0] == 0:
        time.sleep(0.5)
        print("\nThe battlefield is unwarped!")
        for x in allfighters:
          x.mgh = [0]

    if self.rages[0] > 0:
      self.rages[0] = self.rages[0] - 1
      if self.rages[0] == 0:
        time.sleep(0.5)
        print("\nThe flames cease to rage across the battlefield!")
        for x in ally.team:
          x.rages = [0]
          x.burnt = 0
        for x in ally.backteam:
          x.rages = [0]
          x.burnt = 0
        for x in ally.deadteam:
          x.rages = [0]
          x.burnt = 0
        for x in enemy.team:
          if x.ragestorm == True:
            x.ragestorm = False

    if self.dark > 0:
      self.dark = self.dark - 1
      if self.dark == 0:
        time.sleep(0.5)
        print("\nThe darkness is lifted from the battlefield!")
        for x in ally.team:
          x.dark = 0
        for x in ally.backteam:
          x.dark = 0
        for x in ally.deadteam:
          x.dark = 0
        for x in enemy.team:
          if x.darks == True:
            x.darks = False
    
    if self.chilled > 0:
      self.chilled = self.chilled - 1
      if self.chilled == 0:
        time.sleep(0.5)
        print("\nThe chill vibes sway away from the battlefield!")
        for x in ally.team:
          x.chilled = 0
        for x in ally.backteam:
          x.chilled = 0
        for x in ally.deadteam:
          x.chilled = 0

  def globaltimers(self):
    global sett
    global player1
    global player2

    if self.runhigh > 0:
      self.runhigh = self.runhigh - 1
      if self.runhigh == 0:
        time.sleep(0.5)
        print("\n" + self.NAME,"exits the runner's high!")

    if self.tremsl > 0:
      self.tremsl = self.tremsl - 1

    if self.ovd > 0:
      self.ovd = self.ovd - 1
      if self.ovd == 0:
        time.sleep(0.5)
        print("\n"+self.NAME,"is no longer in overdrive!")

    if self.NAME == "Note Packet":
      self.destruct = self.destruct - 1
      if self.destruct == 0:
        time.sleep(0.5)
        print("\nA note packet burns itself up!")
        self.cHP = 0
        player2.team.remove(self)
        player2.teamS.remove(self.NAME)
        player2.teamID.remove(self.ID)
        allfighters.remove(self)
        for x in player2.team:
          if x.NAME == "Mrs. Wells":
            x.missingnotes = x.missingnotes + 1

    if self.statr == True:
      HPlist = []
      MPlist = []
      ATlist = []
      DFlist = []
      MATlist = []
      MDFlist = []
      SPlist = []
      AClist = []
      EVlist = []
      CTlist = []
      APNlist = []
      MPNlist = []
      MRGlist = []
      for x in player1.team:
        x.HPlat = []
        x.MPlat = []
        x.HPlat.append(x.cHP)
        x.MPlat.append(x.cMP)
        x.HPlat.append(x.HP)
        x.MPlat.append(x.MP)
        HPlist.append(x.HPlat)
        MPlist.append(x.MPlat)
        ATlist.append(x.AT)
        DFlist.append(x.DF)
        MATlist.append(x.MAT)
        MDFlist.append(x.MDF)
        SPlist.append(x.SP)
        AClist.append(x.AC)
        EVlist.append(x.EV)
        CTlist.append(x.CT)
        APNlist.append(x.APN)
        MPNlist.append(x.MPN)
        MRGlist.append(x.MRG)
      for x in player1.backteam:
        x.HPlat = []
        x.MPlat = []
        x.HPlat.append(x.cHP)
        x.MPlat.append(x.cMP)
        x.HPlat.append(x.HP)
        x.MPlat.append(x.MP)
        HPlist.append(x.HPlat)
        MPlist.append(x.MPlat)
        ATlist.append(x.AT)
        DFlist.append(x.DF)
        MATlist.append(x.MAT)
        MDFlist.append(x.MDF)
        SPlist.append(x.SP)
        AClist.append(x.AC)
        EVlist.append(x.EV)
        CTlist.append(x.CT)
        APNlist.append(x.APN)
        MPNlist.append(x.MPN)
        MRGlist.append(x.MRG)
      for x in player1.team:
        rnd = random.choice(HPlist)
        HPlist.remove(rnd)
        x.cHP = rnd[0]
        x.HP = rnd[1]
        rnd = random.choice(MPlist)
        MPlist.remove(rnd)
        x.cMP = rnd[0]
        x.MP = rnd[1]
        rnd = random.choice(ATlist)
        ATlist.remove(rnd)
        x.AT = rnd
        rnd = random.choice(DFlist)
        DFlist.remove(rnd)
        x.DF = rnd
        rnd = random.choice(MATlist)
        MATlist.remove(rnd)
        x.MAT = rnd
        rnd = random.choice(MDFlist)
        MDFlist.remove(rnd)
        x.MDF = rnd
        rnd = random.choice(SPlist)
        SPlist.remove(rnd)
        x.SP = rnd
        rnd = random.choice(AClist)
        AClist.remove(rnd)
        x.AC = rnd
        rnd = random.choice(EVlist)
        EVlist.remove(rnd)
        x.EV = rnd
        rnd = random.choice(CTlist)
        CTlist.remove(rnd)
        x.CT = rnd
        rnd = random.choice(APNlist)
        APNlist.remove(rnd)
        x.APN = rnd
        rnd = random.choice(MPNlist)
        MPNlist.remove(rnd)
        x.MPN = rnd
        rnd = random.choice(MRGlist)
        MRGlist.remove(rnd)
        x.MRG = rnd
      for x in player1.backteam:
        rnd = random.choice(HPlist)
        HPlist.remove(rnd)
        x.cHP = rnd[0]
        x.HP = rnd[1]
        rnd = random.choice(MPlist)
        MPlist.remove(rnd)
        x.cMP = rnd[0]
        x.MP = rnd[1]
        rnd = random.choice(ATlist)
        ATlist.remove(rnd)
        x.AT = rnd
        rnd = random.choice(DFlist)
        DFlist.remove(rnd)
        x.DF = rnd
        rnd = random.choice(MATlist)
        MATlist.remove(rnd)
        x.MAT = rnd
        rnd = random.choice(MDFlist)
        MDFlist.remove(rnd)
        x.MDF = rnd
        rnd = random.choice(SPlist)
        SPlist.remove(rnd)
        x.SP = rnd
        rnd = random.choice(AClist)
        AClist.remove(rnd)
        x.AC = rnd
        rnd = random.choice(EVlist)
        EVlist.remove(rnd)
        x.EV = rnd
        rnd = random.choice(CTlist)
        CTlist.remove(rnd)
        x.CT = rnd
        rnd = random.choice(APNlist)
        APNlist.remove(rnd)
        x.APN = rnd
        rnd = random.choice(MPNlist)
        MPNlist.remove(rnd)
        x.MPN = rnd
        rnd = random.choice(MRGlist)
        MRGlist.remove(rnd)
        x.MRG = rnd

    if self.skillr == True:
      bigteam = []
      for x in player1.team:
        x.coun = False
        x.re = False
        x.falle = False
        x.hat = False
        x.hatelis = []
        bigteam.append(x)
      for x in player1.backteam:
        x.coun = False
        x.re = False
        x.falle = False
        x.hat = False
        x.hatelis = []
        bigteam.append(x)
      skillpool = ["Counter","Fallen Symbol","Rest","Haters"]
      for x in bigteam:
        for y in x.skills:
          skillpool.append(y)
        x.skills = []
      while len(skillpool) > 0:
        for x in bigteam:
          if len(skillpool) > 0:
            ski = random.choice(skillpool)
            x.skills.append(ski)
            skillpool.remove(ski)
            if ski == "Counter":
              x.skills.remove(ski)
              x.coun = True
            if ski == "Fallen Symbol":
              x.skills.remove(ski)
              x.falle = True
            if ski == "Rest":
              x.skills.remove(ski)
              x.re = True
            if ski == "Haters":
              x.skills.remove(ski)
              x.hat = True


  def defense(self,enemy,ty,dmg):
    if "Physical" in ty:
      if enemy.cAPN > self.cDF or self.cDF <= 0:
        self.cHP = self.cHP - round(dmg*self.dmgreduct)
      else:
        self.cHP = self.cHP - round(self.dmgreduct*dmg*(1-(((self.cDF)-enemy.cAPN)/((self.cDF+100)-enemy.cAPN))))
    elif "Magical" in ty:
      if enemy.cMPN > self.cMDF or self.cMDF <= 0:
        self.cHP = self.cHP - round(dmg*self.dmgreduct)
      else:
        self.cHP = self.cHP - round(self.dmgreduct*dmg*(1-(((self.cMDF)-enemy.cMPN)/((self.cMDF+100)-enemy.cMPN))))
        
  def onhittimersdefense(self,ene,timer,dmg=0,mr=""):

    global sett
    global player1
    global player2

    yik = 0
    ari = 0

    if self.beared == 1:
      self.beared = 0
      if self.NAME == "Metin":
        print("\nMetin protects himself from all harm, nullifying all damage taken!")
      else:
        print("\nMetin protects",self.NAME,"from all harm, nullifying all damage taken!")
      self.cHP = sett

    if self.cHP <= 0:   #Defensive affects that go through death/(Shields,etc.)
      if (sett-self.cHP) <= (400*(1+self.que)) and self.quenshield == True: 
        self.cHP = sett
        self.quenshield = False
        print("\n"+self.NAME,"is completely protected by quen!",self.NAME,"is back to",self.cHP,"health!")
      elif (sett-self.cHP) > (400*(1+self.que)) and self.quenshield == True:
        self.cHP = self.cHP + (400*(1+self.que)) 
        self.quenshield = False
        time.sleep(timer)
        if self.cHP >0:
          print("\n"+self.NAME,"is partially protected by quen!",self.NAME,"is back to",self.cHP,"health!")

      if (sett-self.cHP) > 0:
        self.dmgstore = self.dmgstore + (sett-self.cHP)
        yik = 1
        if self.marked[0] > 0:
          self.marked[1] = self.marked[1] + ((0.1+(0.05*self.marked[2].arri))*(sett-self.cHP))
          ari = 1

      if self.NAME == "Amira" and self.resil == 1 and self.ID !="11":
        self.cHP = 1
        time.sleep(timer)
        print(fore.GREY_0 + back.CYAN_1 + style.BOLD + "\nAmira: I can't die to these idiots...I have a 4.6! GPA" + style.RESET)
        self.resil = 0

      if self in player2.team and self.NAME == "Julius" and "Kelly" in player1.teamS:
        for x in player1.team:
          if x.NAME == "Kelly":
            self.charm(x)

      if self.seeker > 0 and "Melee" in mr:
        self.prehiteffects(ene)
        self.seeker = self.seeker - 1
        sett = ene.cHP
        time.sleep(timer)
        dmg = 2*self.cMAT
        ene.defense(self,"Physical",dmg)
        if ene.cHP > 0:
          if (sett-ene.cHP) == 0:
            print("\nThe mines seek out",ene.NAME,"but deal no damage!")
          else:
            print("\nThe mines seek out",ene.NAME+", dealing",fore.ORANGE_1 + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
        else:
          print("\nThe mines seek out",ene.NAME+", dealing",fore.ORANGE_1 + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
        if self.seeker == 0:
          time.sleep(timer)
          print("\nThe mines have run out!")
        ene.onhittimersdefense(self,0.4,dmg,"Physical Ranged")
        
    if self.cHP > 0:
      if (sett-self.cHP) <= (400*(1+self.que)) and self.quenshield == True: 
        self.cHP = sett
        self.quenshield = False
        print("\n"+self.NAME,"is completely protected by quen!",self.NAME,"is back to",self.cHP,"health!")
      elif (sett-self.cHP) > (400*(1+self.que)) and self.quenshield == True:
        self.cHP = self.cHP + (400*(1+self.que)) 
        self.quenshield = False
        time.sleep(timer)
        if self.cHP >0:
          print("\n"+self.NAME,"is partially protected by quen!",self.NAME,"is back to",self.cHP,"health!")

      if self.seeker > 0 and "Melee" in mr:
        self.prehiteffects(ene)
        self.seeker = self.seeker - 1
        sett = ene.cHP
        time.sleep(timer)
        dmg = 2*self.cMAT
        ene.defense(self,"Physical",dmg)
        if ene.cHP > 0:
          if (sett-ene.cHP) == 0:
            print("\nThe mines seek out",ene.NAME,"but deal no damage!")
          else:
            print("\nThe mines seek out",ene.NAME+", dealing",fore.ORANGE_1 + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
        else:
          print("\nThe mines seek out",ene.NAME+", dealing",fore.ORANGE_1 + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
        if self.seeker == 0:
          time.sleep(timer)
          print("\nThe mines have run out!")
        ene.onhittimersdefense(self,0.4,dmg,"Physical Ranged")

      if self.pbarrier > 0:
        self.pbarrier = self.pbarrier - 1
        if self.pbarrier == 0:
          time.sleep(timer)
          print("\n" + self.NAME + "'s physical barrier breaks!")

      if self.teamed > 0:
        self.teamed = self.teamed - 1
        if self.teamed == 0:
          time.sleep(timer)
          print("\n"+self.NAME,"is no longer teamed with David!")

      if self.radiant[0] > 0:
        self.radiant[0] = self.radiant[0] - 1
        if self.radiant[0] == 0:
          time.sleep(timer)
          print("\n"+self.NAME,"is no longer protected by the sun!")
          self.radiant = [0]

      if self.greased[0] > 0:
        self.greased[0] = self.greased[0] - 1
        if self.greased[0] == 0:
          time.sleep(timer)
          print("\n" + self.NAME, "is ungreased!")  
          self.greased = [0]

      if self.cutfear[0] > 0:
        self.cutfear[0] = self.cutfear[0] - 1
        if self.cutfear[0] == 0:
          time.sleep(timer)
          print("\n"+self.NAME,"is no longer feared by cutting!")  
          self.cutfear = [0] 

      if self.rehearsed[0] > 0:
        self.rehearsed[0] = self.rehearsed[0] - 1
        if self.rehearsed[0] == 0:
          time.sleep(timer)
          print("\n"+self.NAME,"is no longer apart of the rehearsal!")
          self.rehearsed = [0]

      if self.safety > 0:
        self.safety = self.safety - 1

      if self.talkEN > 0:
        self.talkEN = self.talkEN - 1
        time.sleep(timer)
        if self.talkEN == 4:
          print(fore.GREY_0 + back.CYAN_1 + style.BOLD + "\nAmira: Of course you do..." + style.RESET)    
        if self.talkEN == 3:
          print(fore.GREY_0 + back.CYAN_1 + style.BOLD + "\nAmira: She's so stupid...crazy...annoying...insecure.." + style.RESET)
        if self.talkEN == 2:
          print(fore.GREY_0 + back.CYAN_1 + style.BOLD + "\nAmira: She's too smart...too beautiful...she tries too hard..." + style.RESET)
        if self.talkEN == 1:
          print(fore.GREY_0 + back.CYAN_1 + style.BOLD + "\nAmira: Haters only make me stronger." + style.RESET)
        if self.talkEN == 0:
          print(fore.GREY_0 + back.CYAN_1 + style.BOLD + "\nAmira: Farewell." + style.RESET)
          self.ENRAGE = True
        time.sleep(timer)

      if len(self.bonded) > 0:
        if self.bonded[1].cHP < 0:
          self.bonded = []
        else:
          dmg = (sett-self.cHP)
          settt = self.bonded[1].cHP
          if ene.cMPN > self.bonded[1].cMDF or self.bonded[1].cMDF <= 0:    
            self.bonded[1].cHP = self.bonded[1].cHP - round(dmg * ((1-(0.6-(0.05*self.bonded[1].knightv)))/(0.6-(0.05*self.bonded[1].knightv))) * self.bonded[1].dmgreduct)
          else:
            self.bonded[1].cHP = self.bonded[1].cHP - round(dmg * ((1-(0.6-(0.05*self.bonded[1].knightv)))/(0.6-(0.05*self.bonded[1].knightv))) * (1-(((self.bonded[1].cMDF)-ene.cMPN)/((self.bonded[1].cMDF+100)-ene.cMPN))) *self.bonded[1].dmgreduct)
          time.sleep(timer)
          if (settt-self.bonded[1].cHP) > 0 and self.bonded[1].cHP > 0:
            print("\n"+self.bonded[1].NAME,"takes",fore.PURPLE_1B + str(settt-self.bonded[1].cHP) + style.RESET,"damage for",self.NAME+"!",self.bonded[1].NAME,"has",self.bonded[1].cHP,"health remaining!")
          elif (settt-self.bonded[1].cHP) > 0 and self.bonded[1].cHP <= 0:
            print("\n"+self.bonded[1].NAME,"takes",fore.PURPLE_1B + str(settt-self.bonded[1].cHP) + style.RESET,"damage for",self.NAME+"!",self.bonded[1].NAME,"falls...")

      if ene.tension > 0 and "Physical" in mr and "Support" not in mr:
        ene.tension = 0
        time.sleep(timer)
        print("\n"+ene.NAME,"releases all tension!")

      if (sett-self.cHP) > 0:
        if yik == 0:
          self.dmgstore = self.dmgstore + (sett-self.cHP)
        if ari == 0 and self.marked[0] > 0:
          self.marked[1] = self.marked[1] + ((0.1+(0.05*self.marked[2].arri))*(sett-self.cHP))
        
  def prehiteffects(self,ene):
    global sett
    global player1
    global player2

    if self in player1.team:
      self.currentstats(player1,player2)
      ene.currentstats(player2,player1)
    elif self in player2.team:
      self.currentstats(player2,player1)
      ene.currentstats(player1,player2)

    if ene.revealed > 0:
      self.fAC = self.fAC + 50
      self.cAC = round(self.fAC*self.pAC)

    if ene.bleedt > 0:
      self.cCT = round(self.cCT * 1.5)

    if ene.hat == True: 
      self.hater = 2
      if self not in ene.hatelis:
        ene.hatelis.append(self)
      ene.cMP = ene.cMP + ene.cMRG
      if ene.cMP > ene.fMP:
        ene.cMP = ene.fMP

    if self.now == True:
      if ene.GEND == "Female":
        self.cAT = ((1.25+(0.05*self.nowo))*self.cAT)
        self.cMAT = ((1.25+(0.05*self.nowo))*self.cMAT)
    
    if ene.now == True:
      if self.GEND == "Female":
        self.cAT = ((1.25+(0.05*ene.nowo))*self.cAT)
        self.cMAT = ((1.25+(0.05*ene.nowo))*self.cMAT)

    if self.hat == True and ene in self.hatelis:
      self.cAPN = round(self.cAPN * (1.4+(0.4*self.hate)))
      self.cMPN = round(self.cMPN * (1.4+(0.4*self.hate)))

    if (len(self.duel) >0 and ene not in self.duel) or (len(ene.duel)>0 and self not in ene.duel):
      self.cAT = 0
      self.cMAT = 0
      
  def onhittimersoffense(self,ene,timer,mr=""):
    global sett
    global player1
    global player2

    if self.lifesteal > 0:
      if (sett-ene.cHP) >0 and round(self.lifesteal*(sett-ene.cHP)) >0:
        butt = self.cHP 
        self.cHP = self.cHP + round(self.lifesteal*(sett-ene.cHP))
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        time.sleep(timer)
        print("\n" + self.NAME,"heals for",fore.MEDIUM_SPRING_GREEN + str(self.cHP-butt) + style.RESET,"health! They now have",self.cHP,"health!")

    if self.los == True:
      if self.ISOmode == True:
        self.prehiteffects(ene) 
        time.sleep(timer) 
        diff = ene.cEV - self.cAC
        if random.randint(1,100) <= diff:
          print("\n"+self.NAME, "slashes the wind at",ene.NAME + ", but misses!")
          ene.specialdodgecases(self,0.5,"True Ranged")
        else:
          settt = ene.cHP
          dmg = round(self.cMAT*(0.6+(self.lost*0.1)))
          ene.cHP = ene.cHP - round(dmg)
          if ene.cHP > 0:
            print("\n"+self.NAME, "slashes the wind at",ene.NAME+", dealing",style.BOLD + str(settt-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
          else:
            print("\n"+self.NAME, "slashes the wind at",ene.NAME+", dealing",style.BOLD + str(settt-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
          ene.onhittimersdefense(self,0.5,dmg,"True Ranged")
        selfsett = self.cHP
        self.cHP = self.cHP + round(self.healmod*(0.6+(0.1*self.lost))*(sett-ene.cHP))
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        time.sleep(timer)
        print("\n"+self.NAME,"absorbs the light from",ene.NAME+", healing for",fore.MEDIUM_SPRING_GREEN +str(self.cHP-selfsett)+style.RESET,"health! She has",self.cHP,"health now!")
      else:
        if self.losthit == 0:
          self.prehiteffects(ene) 
          time.sleep(timer) 
          diff = ene.cEV - self.cAC
          if random.randint(1,100) <= diff:
            print("\n"+self.NAME, "slashes the wind at",ene.NAME + ", but misses!")
            ene.specialdodgecases(self,0.5,"Magical Ranged")
          else:
            sett = ene.cHP
            dmg = self.cMAT*(0.6+(self.lost*0.1))
            ene.defense(self,"Magical",dmg)
            if ene.cHP > 0:
              if (sett-ene.cHP) == 0:
                print("\n"+self.NAME, "slashes the wind",ene.NAME +", but deals no damage!")
              else:
                print("\n"+self.NAME, "slashes the wind at",ene.NAME+", dealing",fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
            else:
              print("\n"+self.NAME, "slashes the wind at",ene.NAME+", dealing",fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
            ene.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
          self.losthit = 1
        elif self.losthit == 1:
          selfsett = self.cHP
          self.cHP = self.cHP + round(self.healmod*(0.6+(0.1*self.lost))*(sett-ene.cHP))
          if self.cHP > self.fHP:
            self.cHP = self.fHP
          time.sleep(timer)
          print("\n"+self.NAME,"absorbs the light from",ene.NAME+", healing for",fore.MEDIUM_SPRING_GREEN +str(self.cHP-selfsett)+style.RESET,"health! She has",self.cHP,"health now!")
          self.losthit = 0

    if self.chronotime > 0:
      self.prehiteffects(ene)
      sett = ene.cHP
      if ene.cHP >0:
        dmg = (1+(0.2*self.chrono))*self.cMAT
        ene.defense(self,"Magical",dmg)
        self.chronotime = self.chronotime - 1
        if ene not in self.chronoslow:
          self.chronoslow.append(ene)
        ene.chronot = 3
        time.sleep(timer)
        if ene.cHP > 0:
          if (sett-ene.cHP) == 0:
            print("\nThe essence of time affects",ene.NAME+", reaping their speed to",self.NAME+", but it deals no damage!")
          else:
            print("\nThe essence of time affects",ene.NAME+", reaping their speed to",self.NAME+", and dealing",fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
        else:
          print("\nThe essence of time affects",ene.NAME+", reaping their speed to",self.NAME+", and dealing",fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"falls...")
        ene.onhittimersdefense(self,0,dmg,"Magical")

    if self.darks == True and (self.invis > 0 or self.instant == True):
      self.prehiteffects(ene)
      if ene.cHP > 0:
        sett = ene.cHP
        dmg = (0.6+(0.1*self.fromthes))*self.cMAT
        ene.defense(self,"Magical",dmg)
        time.sleep(timer)
        if ene.cHP > 0:
          if (sett-ene.cHP) == 0:
            print("\nThe shadows slash",ene.NAME + ", but deal no damage!")
          else:
            print("\nThe shadows slash",ene.NAME + ", dealing",fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
        else:
          print("\nThe shadows slash",ene.NAME + ", dealing",fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
        ene.onhittimersdefense(self,0,dmg,"Magical")
        if ene in player1.team:
          if ene.cHP > 0:     
            ene.currentstats(player1,player2)
        elif ene in player2.team:
          if ene.cHP > 0: 
            ene.currentstats(player2,player1)

    if self.mvolley == 3:
      self.mvolley = 0
      time.sleep(timer)
      print("\n"+self.NAME+"'s accumulated power discharges three balls of light!")
      bruh = []
      for x in player1.team:
        if (x.invis <=0 or x.revealed > 0):
          bruh.append(x)
      for x in range(3):
        time.sleep(timer/4)
        if len(bruh) > 0:
          targ = random.choice(bruh)
          if len(self.duel) > 0:
            if self.duel[1] in bruh:
              targ = self.duel[1]
          elif len(self.taunted) > 0:
            if self.taunted[1] in bruh:
              targ = self.taunted[1]
        else:
          break
        self.prehiteffects(targ)
        diff = targ.cEV - self.cAC 
        if random.randint(1,100) <= diff:
          print("\nThe ball tracks",targ.NAME +", but they dodge it!")
          targ.specialdodgecases(self,0.5,"Magical Ranged")
        else:
          sett = targ.cHP
          dmg = self.cMAT
          targ.defense(self,"Magical",dmg)
          if targ.cHP > 0:
            if (sett-targ.cHP) == 0:
              print("\nThe ball tracks",targ.NAME +", but deals no damage!")
            else:
              print("\nThe ball tracks",targ.NAME +", dealing", fore.PURPLE_1B + str(sett-targ.cHP) + style.RESET,"damage!",targ.NAME,"has",targ.cHP,"health remaining!")
            targ.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
          else:
            print("\nThe ball tracks",targ.NAME +", dealing", fore.PURPLE_1B + str(sett-targ.cHP) + style.RESET,"damage!",targ.NAME,"falls...")
          targ.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
          if targ.cHP <= 0:
            bruh.remove(targ)
          else:
            targ.currentstats(player1,player2)

    if self.ptelepath < 3 and self.telep >=0 and "Telepathy" in self.skills:
      self.ptelepath = self.ptelepath + 1
      if self.ptelepath == 3:
        self.prehiteffects(ene)
        self.ptelepath = 0
        time.sleep(timer)
        print("\n"+self.NAME+": Do you hate me",ene.NAME+"...?")
        time.sleep(timer)
        diff = ene.cEV - self.cAC 
        if random.randint(1,100) <= diff:
          print("\n"+ene.NAME,"is unaffected by the telepathic attack!")
          ene.specialdodgecases(self,timer,"Magical")
        else:
          sett = ene.cHP
          dmg = (1.5+(0.25*self.telep))*self.cMAT
          ene.defense(self,"Magical",dmg)
          if ene.cHP > 0:
            if (sett-ene.cHP) == 0:
              print("\n"+ene.NAME,"is affected by the telepathic attack but takes no damage!")
            else:
              print("\n"+ene.NAME,"is affected by the telpathic attack, taking", fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
          else:
            print("\n"+ene.NAME,"is affected by the telpathic attack, taking", fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
          ene.onhittimersdefense(self,timer,dmg,"Magical")

    if self.telepath > 0:
      self.telepath = self.telepath - 1
      self.prehiteffects(ene)
      time.sleep(timer)
      print("\n"+self.NAME+": Do you hate me",ene.NAME+"...?")
      time.sleep(timer)
      diff = ene.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        print("\n"+ene.NAME,"is unaffected by the telepathic attack!")
        ene.specialdodgecases(self,timer,"Magical")
      else:
        sett = ene.cHP
        dmg = (1.5+(0.25*self.telep))*self.cMAT
        ene.defense(self,"Magical",dmg)
        if ene.cHP > 0:
          if (sett-ene.cHP) == 0:
            print("\n"+ene.NAME,"is affected by the telepathic attack but takes no damage!")
          else:
            print("\n"+ene.NAME,"is affected by the telpathic attack, taking", fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"has",ene.cHP,"health remaining!")
        else:
          print("\n"+ene.NAME,"is affected by the telpathic attack, taking", fore.PURPLE_1B + str(sett-ene.cHP) + style.RESET,"damage!",ene.NAME,"falls...")
        ene.onhittimersdefense(self,timer,dmg,"Magical")

  def onturntimers(self,ally,enemy):

    if self.OB == True:
      sett = self.cHP
      self.cHP = self.cHP + round(self.healmod*(0.03+(0.01*self.obese))*self.fHP)
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      time.sleep(0.3)
      print("\n" +self.NAME+ "'s self-sustainability heals",self.GEN[1],"for",fore.MEDIUM_SPRING_GREEN + str(self.cHP-sett) + style.RESET,"health! He has",self.cHP,"health now!")

    if self.graced[0] > 0:
      self.graced[0] = self.graced[0] - 1
      selfsett = self.cHP
      self.cHP = self.cHP + round(self.healmod*(0.3+(self.graced[1].grac*0.05))*self.graced[1].cMAT)
      time.sleep(0.3)
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      print("\n"+self.NAME,"feels the breeze, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+ style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")
      if self.graced[0] == 0:
        time.sleep(0.4)
        print("\n"+self.NAME,"no longer feels the breeze!")

    if self.immortal > 0:
      if self.immortal != 1 and self.ISOmode == False:
        self.immortal = self.immortal - 1
      if self.immortal == 0:
        time.sleep(0.5)
        print("\n" + self.NAME,"is mortal again!")

    if self.emmortal > 0:
      self.emmortal = self.emmortal - 1
      if self.emmortal == 0:
        time.sleep(0.5)
        print("\n" + self.NAME,"is mortal again!")
    
    if self.WI == True:
      sett = self.cHP
      self.cHP = self.cHP - round(0.025*self.fHP)
      time.sleep(0.2)
      if self.cHP <=0:
        self.WI = False
        self.cHP = 1
        print("\n"+self.NAME,"loses",(sett-self.cHP),"health from",self.GEN[0],"wild instincts!",self.GEN[2].capitalize(),"is at critical health, exiting wild instinct!")
      else:
        print("\n"+self.NAME,"loses",(sett-self.cHP),"health from",self.GEN[0],"wild instincts!",self.GEN[2].capitalize(),"has",self.cHP,"health now!")

    if self.burnt > 0:
      sett = self.cHP
      if self.rages[0] > 0:
        if self.rages[1] in enemy.team:
          self.burnd = self.burnd + ((0.1*(22-self.rages[1].rages[0]))*self.rages[1].cMAT)
      self.cHP = self.cHP - round(self.burnd * (1-(self.cMDF/(self.cMDF+100))))
      if self.rages[0] > 0:
        if self.rages[1] in enemy.team:
          self.burnd = self.burnd - ((0.1*(22-self.rages[1].rages[0]))*self.rages[1].cMAT)
      time.sleep(0.5)
      self.burnt = self.burnt - 1
      if self.cHP > 0:
        print("\n" + self.NAME,"takes",fore.ORANGE_RED_1 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.ORANGE_RED_1,"burn damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.burnt == 0 and self.rages[0] <=0:
          time.sleep(0.5)
          print("\n" + self.NAME,"is relieved of burning!")
          self.burnd = 0
        if self.rages[0] > 0 and self.burnt <=0:
          self.burnt = 1
      else:
        print("\n" + self.NAME,"takes",fore.ORANGE_RED_1 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.ORANGE_RED_1,"burn damage!" + style.RESET,self.NAME,"falls...")

    if self.poisont > 0:
      self.poisont = self.poisont - 1
      sett = self.cHP
      self.cHP = self.cHP - round(self.poisond * (1-(self.cDF/(self.cDF+100))))
      time.sleep(0.5)
      if self.cHP > 0:
        print("\n" + self.NAME,"takes",fore.GREEN_4 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.GREEN_4,"poison damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.poisont == 0:
          time.sleep(0.5)
          print("\n" + self.NAME,"is cured of poisoning!")
          self.poisond = 0
      else: 
        print("\n" + self.NAME,"takes",fore.GREEN_4 + style.BOLD + str(sett-self.cHP) + style.RESET + fore.GREEN_4,"poison damage!" + style.RESET,self.NAME,"falls...")
      
    if self.bleedt > 0:
      self.bleedt = self.bleedt - 1
      sett = self.cHP
      self.cHP = self.cHP - round(self.bleedd * (1-(self.cDF/(self.cDF+100))))
      time.sleep(0.5)
      if self.cHP > 0:
        print("\n" + self.NAME,"takes",fore.LIGHT_RED + style.BOLD + str(sett-self.cHP) + style.RESET + fore.LIGHT_RED,"bleed damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.bleedt == 0:
          time.sleep(0.5)
          print("\n" + self.NAME,"stops bleeding!")
          self.bleedd = 0
      else:
        print("\n" + self.NAME,"takes",fore.LIGHT_RED + style.BOLD + str(sett-self.cHP) + style.RESET + fore.LIGHT_RED,"bleed damage!" + style.RESET,self.NAME,"falls...")

    if self.decayt > 0:
      self.decayt = self.decayt - 1
      sett = self.cHP
      self.cHP = self.cHP - round(self.decayd)
      time.sleep(0.5)
      if self.cHP > 0:
        print(back.GREY_100 + fore.BLACK + "\n" + self.NAME,"takes",style.BOLD + str(sett-self.cHP) + style.RESET + fore.BLACK + back.GREY_100,"decay damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        if self.decayt == 0:
          time.sleep(0.5)
          print("\n" + self.NAME,"stops decaying!")
          self.decayd = 0
      else:
        print(back.GREY_100 + fore.BLACK + "\n" + self.NAME,"takes",style.BOLD + str(sett-self.cHP) + style.RESET + fore.BLACK + back.GREY_100,"decay damage!" + style.RESET,self.NAME,"falls...")

    for x in enemy.team:
      if x.NAME == "Arwyn" and x.ISOmode == True:
        sett = self.cHP
        self.cHP = self.cHP - round(0.25*x.cMAT)
        time.sleep(0.5)
        if self.cHP > 0:
          print(back.GREY_100 + fore.BLACK + "\n" + self.NAME,"takes",style.BOLD + str(sett-self.cHP) + style.RESET + fore.BLACK + back.GREY_100,"decay damage!" + style.RESET,self.NAME,"has",self.cHP,"health remaining!")
        else:
          print(back.GREY_100 + fore.BLACK + "\n" + self.NAME,"takes",style.BOLD + str(sett-self.cHP) + style.RESET + fore.BLACK + back.GREY_100,"decay damage!" + style.RESET,self.NAME,"falls...")

    if self.marked[0] > 0:
      self.marked[0] = self.marked[0] - 1
      if self.marked[0] == 0:
        selfsett = self.cHP
        self.cHP = self.cHP - round(self.marked[1])
        if self.cHP > 0:
          print(back.GREY_100 + fore.BLACK + style.BOLD+ "\nThe death mark pops on",self.NAME+", dealing",(selfsett-self.cHP),"damage!",self.NAME,"has",self.cHP,"health remaining!"+style.RESET)
        else:
          print(back.GREY_100 + fore.BLACK + style.BOLD+"\nThe death mark pops on",self.NAME+", dealing",(selfsett-self.cHP),"damage!",self.NAME,"falls..."+style.RESET)
        self.marked = [0,0]
    
    if self.scirc > 0:
      self.scirc = self.scirc - 1
      if self.scirc == 1:
        print("\n"+self.NAME,"is about to short circuit!")
      if self.scirc == 0:
        self.cHP = 0
        print("\n"+self.NAME,"short circuits and dies!")

    if (self.immortal > 0 or self.emmortal > 0) and self.cHP <=0:
      time.sleep(0.5)
      print("\n"+self.NAME,"gets back up!")
      self.cHP = 1

    if self.NAME == "Julius" and self.ISOmode == True:
      if self.cHP <=0:
        self.ISOmode = False
        self.cHP = self.fHP
        self.isoboost = 6
        self.isoboostL = 1
        self.runhigh  = 26
        time.sleep(1)
        print("\n"+self.NAME,"embraces his eternal will, standing back up to fight! He is fully powered-up by the runner's high and the isometric drawings!")
        self.Isopower(player1,EW=True)

    if self.stunimmune[1] > 0:
      if self.stunimmune[1] != 1 and self.ISOmode == False:
        self.stunimmune[1] = self.stunimmune[1] - 1
      if self.stunimmune[1] == 0:
        if self.stunimmune[0] == 1:
          print("\n"+self.NAME,"is no longer immune to disables!")
        self.stunimmune[0] = 0

    if self.food[0] > 0:
      self.food[0] = self.food[0] - 1
      if self.food[0] == 0:        
        self.food[1] = 0
        self.food[2] = 0
        self.food[3] = 0
        self.food[4] = 0
        self.food[5] = 0
        self.food[6] = 0
        self.food[7] = 0
        self.food[8] = 0
        self.food[9] = 0
        self.food[10] = 0
        self.food[11] = 0
        time.sleep(0.5)
        print("\n"+self.NAME,"loses the boosts from the food they ate.")

    if self.chadwalked[0] > 0:
      self.chadwalked[0] = self.chadwalked[0] - 1
      if self.chadwalked[0] == 0:  
        for x in ally.team:
          x.chadwalked = [0]
          x.chadl = False
        time.sleep(0.5)
        print("\nThe battle is no longer affected by the chadness of",self.chadwalked[1].NAME+".")

    if self.duelt > 0:
      self.duelt = self.duelt - 1
      if self.duelt == 0:       
        for x in allfighters:
          if len(x.duel) > 0:
            if self == x.duel[1]:
              x.duel = []
        self.duel = []
        time.sleep(0.2)
        print("\n"+self.NAME,"exits",self.GEN[0],"arm-wrestling match!")

    if self.tauntt > 0:
      self.tauntt = self.tauntt - 1
      if len(self.taunted) == 0:
        self.tauntt = 0
      else:
        if self.taunted[1].cHP <= 0:
          self.tauntt = 0
          self.taunted = []
        if self.tauntt == 0:
          time.sleep(0.2)
          print("\n" + self.NAME,"stops focusing",self.taunted[1].NAME+"!")
          self.taunted = []

    if self.fear > 0:
      self.fear = self.fear - 1
      if self.fear == 0:
        time.sleep(0.4)
        print("\n"+self.NAME,"is no longer feared!")

    if self.blind > 0:
      self.blind = self.blind - 1
      if self.blind == 0:
        time.sleep(0.4)
        print("\n"+self.NAME,"is no longer blinded ")

    if self.chronot > 0:
      self.chronot = self.chronot - 1
      if self.chronot == 0:
        time.sleep(0.4)
        for x in enemy.team:
          if self in x.chronoslow:
            x.chronoslow.remove(self)
            print("\n"+self.NAME+"'s speed is not being reaped by",x.NAME,"anymore!")

    if self.valos == True:
      self.valor = self.valor - 1
      if len(ally.team) == 1:
        self.valor = 0
      if self.valor == 0:
        time.sleep(0.5)
        print("\nThe team is not boosted by",self.NAME+"'s chant anymore!")
        for x in ally.team:
          x.valor = 0
        self.valos = False
      
    if self.SHIE == True:
      self.SHIE = False

    if self.isoboost > 0:
      self.isoboost = self.isoboost - 1
      if self.isoboost == 0:
        time.sleep(0.5)
        print("\n" + self.NAME,"is not boosted from the isometric drawings anymore!")
        self.setskills()

    if self.combd[0] >0:
      self.combd[0] = self.combd[0] - 1
      if self.combd[0] == 0:
        time.sleep(0.5)
        print("\n"+self.NAME,"is no longer vibing!")
    
    if self.silenced > 0:
      self.silenced = self.silenced - 1
      if self.silenced == 0:
        time.sleep(0.5)
        print("\n" + self.NAME,"is unsilenced!")

    if self.ionized[0] > 0:
      self.ionized[0] = self.ionized[0] - 1
      if self.ionized[0] == 0:
        time.sleep(0.5)
        print("\n" + self.NAME,"is not an electron anymore!")
        self.ionized = [0]

    if self.manaflow[0] > 0:
      self.manaflow[0] = self.manaflow[0] - 1
      if self.manaflow[0] == 0:
        time.sleep(0.3)
        print("\n" + self.NAME,"exits the flow state!")
        self.manaflow = [0]

    if self.thehut > 0:
      self.thehut = self.thehut - 1
      if self.thehut == 0:
        time.sleep(0.5)
        print("\n"+self.NAME,"turns back to",self.GEN[0],"normal self, exiting Enlargen!")
        if self.jabbaroll > 0:
          self.jabbaroll = 0

    if self.knightb > 0:
      self.knightb = self.knightb - 1
      if self.knightb == 0:
        time.sleep(0.3)
        print("\n" + self.NAME,"is unbinded from",self.GEN[0],"ally!")
        for x in ally.team:
          if len(x.bonded) > 0:
            if self == x.bonded[1]:
              x.bonded = []

    if self.revealed > 0:
      self.revealed = self.revealed - 1
      if self.revealed == 0:
        time.sleep(0.3)
        print("\n"+self.NAME,"is no longer revealed!")
        if self.invis > 0:
          if self.NAME in ally.teamS:
            ally.teamS.remove(self.NAME)
          if self.ID in ally.teamID:
            ally.teamID.remove(self.ID)


    if self.rested > 0:
      self.rested = self.rested - 1
      if self.rested == 0:
        time.sleep(0.3)
        print("\n"+self.NAME,"is no longer well rested!")

    if self.hater > 0:
      self.hater = self.hater - 1
      if self.hater == 0:
        time.sleep(0.3)
        print("\n"+self.NAME,"is no longer hating!")
        for x in allfighters:
          if self in x.hatelis:
            x.hatelis.remove(self)

    if self.surge > 0:
      self.surge = self.surge - 1
      if self.surge == 0:
        time.sleep(0.3)
        print("\n"+self.NAME+"'s tethers release from all enemies!")
        self.teth = []
        for x in enemy.team:
          if self in x.tethered:
            x.tethered.remove(self)

    if self.onethro > 0:
      self.onethro = self.onethro - 1
      if self.onethro == 0:
        time.sleep(0.3)
        print("\n"+self.NAME,"is no longer extra edgy!")

    if self.solitude[0] > 0:
      self.solitude[0] = self.solitude[0] - 1
      if self.solitude[0] == 0:
        time.sleep(0.3)
        if self == self.solitude[1]:
          if self.ISOmode == True:
            print("\n"+self.NAME,"is no longer friends with anyone!")
          else:
            print("\n"+self.NAME,"is no longer alone!")
        else:
          print("\n"+self.NAME,"is no longer friends with",self.solitude[1].NAME+"!")
        self.solitude = [0]

    if self.eag > 0:
      self.eag = self.eag - 1
      if self.eag == 0:
        time.sleep(0.3)
        if self.NAME == "Matvey":
          print("\n"+self.NAME,"is no longer in eagle-eye mode!")
        else:
          print("\n"+self.NAME,"is no longer granted eagle eyes from Matvey!")

    if self.caressed > 0:
      self.caressed = self.caressed - 1
      if self.caressed == 0:
        time.sleep(0.3)
        print("\n"+self.NAME,"is no longer creeped out by Dereck.")

    if self.giantess > 0:
      self.giantess = self.giantess - 1
      if self.giantess == 0:
        time.sleep(0.3)
        print("\n" + self.NAME,"is back to",self.GEN[0],"normal size!")

    if self.candyAC > 0:
      self.candyAC = self.candyAC - 1
      if self.candyAC == 0:
        time.sleep(0.2)
        print("\n"+self.NAME+"'s accuracy is no longer being reduced by the chocolate bar!")

  def stuns(self):
    global bad
    global player1
    global player2
    
    self.stunned = False
    if self.prest > 0:
      time.sleep(0.5)
      self.prest = 0
      self.stunned = True
      self.rested = 5
      selfsett = self.cHP
      self.cHP = self.cHP + round(self.healmod*(2+(0.4*self.powres))*self.cMAT)
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      print("\n"+self.NAME,"is power resting, healing for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health and increasing",self.GEN[0],"attack and critical chance!",self.GEN[2].capitalize(),"is at",self.cHP,"health now!")
    elif self.stunimmune[0] == 1:
      if self.dance > 0 or self.sparkstun > 0 or self.tremstun >0 or self.rooted > 0 or self.frozen > 0 or self.repulsed > 0 or self.confused > 0:
        self.dance = 0
        self.sparkstun = 0
        self.tremstun = 0
        self.rooted = 0
        self.frozen = 0
        self.repulsed = 0
        self.confused = 0
        if self.NAME == "Mr. Pudup":
          time.sleep(0.5)
          print("\nMr. Pudup: That was a pitiful attempt to try and stop my movements.")
        if self.NAME == "Julius":
          ri = random.randint(1,2)
          time.sleep(0.5)          
          if ri == 1: 
            print(fore.GREEN_1 +style.BOLD+"\nJulius: I'm unstoppable baby'!"+style.RESET)
          else:
            print(fore.GREEN_1 +style.BOLD+"\nJulius: Can't stop, won't stop!"+style.RESET)
    else:
      if self.rooted > 0:
        time.sleep(0.5)
        self.rooted = self.rooted - 1
        self.stunned = True
        print("\n"+self.NAME,"is rooted!")
      elif self.sparkstun > 0:
        time.sleep(0.5)
        self.sparkstun = self.sparkstun - 1
        self.stunned = True
        print("\n"+self.NAME,"is paralyzed!")
      elif self.tremstun > 0:
        time.sleep(0.5)
        self.tremstun = self.tremstun - 1
        self.stunned = True
        print("\n"+self.NAME,"is on the ground!")
      elif self.frozen > 0:
        time.sleep(0.5)
        self.frozen = self.frozen - 1
        self.stunned = True
        print("\n"+self.NAME,"is frozen!")
      elif self.paralyzed > 0:
        time.sleep(0.5)
        self.paralyzed = self.paralyzed - 1
        self.stunned = True
        print("\n"+self.NAME,"is paralyzed!")
      elif self.repulsed > 0:
        time.sleep(0.5)
        self.repulsed = self.repulsed - 1
        self.stunned = True
        print("\n"+self.NAME,"is magnetically locked!")
      elif self.dance > 0:
        time.sleep(0.5)
        self.dance = self.dance - 1
        self.stunned = True
        allf = []
        if self in player1.team:
          for x in player1.team:
            allf.append(x)
        if self in player2.team:
          for x in player2.team:
            allf.append(x)
        allf.remove(self)
        for x in allf:
          if x.cHP <= 0:
            allf.remove(x)
          if x.invis > 0 and x.cHP >0 and x in allf:
            allf.remove(x)
        if len(allf) > 0:
          att = random.choice(allf)
          print("\n"+self.NAME,"is dancing uncontrollably, attacking a random target!")
          self.attack(att)
        else:
          print("\n"+self.NAME,"dances uncontrollably!")
      elif self.confused > 0:
        time.sleep(0.5)
        self.confused = self.confused - 1
        self.stunned = True
        allf = []
        for x in player1.team:
          allf.append(x)
        for x in player2.team:
          allf.append(x)
        for x in allf:
          if x.cHP <= 0:
            allf.remove(x)
          if x.invis > 0 and x.cHP >0 and x in allf:
            allf.remove(x)
        att = random.choice(allf)
        print("\n"+self.NAME,"is confused, attacking a random target!")
        self.attack(att)
      elif self.zanc == 1:
        if self in bots.team:
          self.enemyattacksys(self.zanslash,"Zantetsuken")
        elif self in you.team:
          uga = 0
          while uga == 0:
            print("\n"+self.NAME,"is ready to slash!")
            if len(bots.teamS) > 1:
              print("")
              print(bots.teamS)
              self.target(self.zanslash,bots.team,bots.teamID)
            else:
              if len(bots.teamS) == 0:
                print("\nThere is no one to slash!")
                break
              else:
                for x in bots.team:
                  if x.ID in bots.teamID and x.invis <=0:
                    self.zanslash(x)
            if bad == False:
              uga = 1
        self.stunned = True
        
        
  def equipcheck(self,dr=False):
    self.fHP = self.HP
    self.fMP = self.MP
    self.fAT = self.AT             
    self.fDF = self.DF
    self.fMAT = self.MAT
    self.fMDF = self.MDF
    self.fSP = self.SP
    self.fAC = self.AC
    self.fEV = self.EV
    self.fCT = self.CT
    self.fAPN = self.APN
    self.fMPN = self.MPN
    self.fMRG = self.MRG

    #Headgear

    if self.helm == "Glasses":
      self.fMAT = self.fMAT + (self.MAT*.05)
      self.fAC = self.fAC + (self.AC*.05)
    if self.helm == "Hairband":
      self.fHP = self.fHP + (self.HP*.02)

    #Chestpieces 

    if self.chest == "Track Warm-Up":
      self.fDF = self.fDF + (self.DF*.04)
      self.fSP = self.fSP + (self.SP*.04)
    if self.chest == "School Uniform":
      self.fDF = self.fDF + (self.DF*.02)

    #Boots 

    if self.boots == "Vans":
      self.fHP = self.fHP + (self.HP*.02)
    if self.boots == "Jays":
      self.fHP = self.fHP + (self.HP*.05)
    if self.boots == "Flats":
      self.fMDF = self.fMDF + (self.MDF*.06)
    if self.boots == "Roshes":
      self.fHP = self.fHP + (self.HP*.1)
      self.fSP = self.fSP - (self.SP*.02)
    if self.boots == "Sneakers":
      self.fHP = self.fHP + (self.HP*.03)
      self.fSP = self.fSP + (self.SP*.02)

    #Weapons

    if self.weap == "Pencil":   
      self.fAT = self.fAT + (self.AT*.05)
      self.fCT = self.fCT + (self.CT*.02)
      self.fAPN = self.fAPN + (self.APN*.2)
    if self.weap == "Ruler":
      self.fAT = self.fAT + (self.AT*.07)
      self.fMRG = self.fMRG + (self.MRG*.2)
    if self.weap == "Keyboard":
      self.fAT = self.fAT + (self.AT*.1)
    if self.weap == "Pen":
      self.fAT = self.fAT + (self.AT*.02)
      self.fMAT = self.fMAT + (self.MAT*.04)
    if self.weap == "Track Baton":
      self.fAT = self.fAT + (self.AT*.08)
      self.fSP = self.fSP + (self.SP*.02)
    if self.weap == "Slingshot":
      self.fAT = self.fAT + (self.AT*.1)
      self.fAC = self.fAC + (self.AC*.03)
      self.fCT = self.fCT + (self.CT*.02)
    if self.weap == "Scissors":
      self.fAT = self.fAT + (self.AT*.12)
      self.fCT = self.fCT + (self.CT*.03)    

    #Accessories
    
    if self.access == "Agenda":
      self.fMP = self.fMP + (self.MP*.05)
      self.fMRG = self.fMRG + (self.MRG*.4)
    
    if dr == False:
      self.fHP = round(self.fHP)
      self.fMP = round(self.fMP)


  def currentstats(self,ally,enemy):
    self.equipcheck()
    self.pAT = 1.00
    self.pDF = 1.00
    self.pMAT = 1.00
    self.pMDF = 1.00
    self.pSP = 1.00
    self.pAC = 1.00
    self.pEV = 1.00
    self.pCT = 1.00
    self.CTdmg = 2
    self.pAPN = 1.00
    self.pMPN = 1.00
    self.pMRG = 1.00
    self.lifesteal = 0
    self.healmod = 1
    self.dmgreduct = 1
    self.effects(ally,enemy)
    self.cAT = round(self.fAT*self.pAT)
    self.cDF = round(self.fDF*self.pDF)
    self.cMAT = round(self.fMAT*self.pMAT)
    self.cMDF = round(self.fMDF*self.pMDF)
    self.cSP = round(self.fSP*self.pSP)
    self.cAC = round(self.fAC*self.pAC)
    self.cEV = round(self.fEV*self.pEV)
    self.cCT = round(self.fCT*self.pCT)
    self.cAPN = round(self.fAPN*self.pAPN)
    self.cMPN = round(self.fMPN*self.pMPN)
    self.cMRG = round(self.fMRG*self.pMRG)

  def attack(self,enemy):
    #print(self.HP,self.MP,self.AT,self.DF,self.MAT,self.MDF,self.SP,self.AC,self.EV,self.CT,self.APN,self.MPN,self.MRG)
    global sett
    global lastat
    self.prehiteffects(enemy)
    CT = random.randint(1,100)
    sett = enemy.cHP
    self.cMP = self.cMP + self.cMRG
    if self.cMP > self.fMP:
      self.cMP = self.fMP 
    self.lastattack = "Auto"
    lastat = "Auto"
    if self.cAT <= 0:
      time.sleep(1)
      print("\n" + self.NAME, "attacks", enemy.NAME + ", but deals no damage!")
    else:
      diff = enemy.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        time.sleep(1)
        if enemy.NAME == "Note Packet":
          print("\n"+self.NAME,"is too distracted to pick up the note packet!")
        else:
          print("\n" + self.NAME, "attacks, but", enemy.NAME, "dodges!")
        enemy.specialdodgecases(self,0.5,"Physical Melee",CT)
      else:
        time.sleep(1)
        if enemy.NAME == "Note Packet":
          print("\n"+self.NAME,"picks up the Note Packet!")
          enemy.cHP = 0
        else:
          if enemy.coun == True:
            enemy.counter(self,CT) 
          if CT <= self.cCT:
            dmg = self.CTdmg*self.cAT
            enemy.defense(self,"Physical",dmg)
            if enemy.cHP > 0:
              if (sett-enemy.cHP) == 0:
                print("\n" + self.NAME, "critically attacks", enemy.NAME +  ", but deals no damage!")
              else:
                print("\n" + self.NAME, "critically attacks", enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              print("\n" + self.NAME, "critically attacks", enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
            enemy.onhittimersdefense(self,0.4,dmg,"Physical Melee")
          else:
            dmg = self.cAT
            enemy.defense(self,"Physical",dmg)
            if enemy.cHP > 0:
              if (sett-enemy.cHP) == 0:
                print("\n" + self.NAME, "attacks", enemy.NAME +  ", but deals no damage!")
              else:
                print("\n" + self.NAME, "attacks", enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              print("\n" + self.NAME, "attacks", enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
            enemy.onhittimersdefense(self,0.4,dmg,"Physical Melee")
          self.onhittimersoffense(enemy,0.5,"Physical Melee") 

  def specialdodgecases(self,enemy,timer,mr="",CT=""):
    global sett
    global player1
    global player2

    if self.coun == True and "Melee" in mr:
      redat = ((.48+(0.03*self.counte))*enemy.cAT)+self.cMAT
      selfsett = enemy.cHP
      time.sleep(timer)
      if CT != "":
        if CT <= enemy.cCT:
          if enemy.cDF <=0:
            enemy.cHP = enemy.cHP - round(enemy.CTdmg*redat*enemy.dmgreduct)
          else:
            enemy.cHP = enemy.cHP - round(enemy.dmgreduct*enemy.CTdmg*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
          if enemy.cHP >0:            
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            enemy.cHP = 1
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"is at critical health!")
        else:
          if enemy.cDF <=0:
            enemy.cHP = enemy.cHP - round(redat*enemy.dmgreduct)
          else:
            enemy.cHP = enemy.cHP - round(enemy.dmgreduct*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
          if enemy.cHP > 0:
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            enemy.cHP = 1
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
      else:
        if enemy.cDF <=0:
          enemy.cHP = enemy.cHP - round(redat*enemy.dmgreduct)
        else:
          enemy.cHP = enemy.cHP - round(enemy.dmgreduct*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
        if enemy.cHP > 0:
          print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          enemy.cHP = 1
          print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")

    if self.la == True:
      self.prehiteffects(enemy)
      sett = enemy.cHP
      time.sleep(timer)
      dmg = self.cAT*(1+(0.1*self.las))
      enemy.defense(self,"Physical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME,"lashes back at",enemy.NAME+", but deals no damage!")
        else:
          print("\n"+self.NAME,"lashes back at",enemy.NAME+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+self.NAME,"lashes back at",enemy.NAME+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,timer,dmg,"Physical Melee")

    if self.NAME == "Amira" and self.ID != "11":
      for x in player2.team:
        if x.NAME == "Jackie" and x.cHP > 0:
          self.prehiteffects(enemy)
          sett = enemy.cHP
          time.sleep(timer)
          dmg = self.cAT
          enemy.defense(self,"Physical",dmg)
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"lashes back at",enemy.NAME+", but deals no damage!")
            else:
              print("\n"+self.NAME,"lashes back at",enemy.NAME+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME,"lashes back at",enemy.NAME+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
          enemy.onhittimersdefense(self,0.4,dmg,"Physical Melee")

    if self.NAME == "Amira" and self.cHP <= round(0.2*self.fHP) and self.ID != "11":
      self.onhittimersdefense(enemy,timer)
     
    if self.safety > 0:
      self.safety = self.safety - 1

    if enemy.tension > 0 and "Physical" in mr and "Support" not in mr:
      enemy.tension = 0
      time.sleep(timer)
      print("\n"+enemy.NAME,"releases all tension!")

  def allyattacksys(self,ally,enemy):
    global seq
    global bad
    seq = 0
    if self.stunned == True:
      self.stunned = False
    else:
      while seq == 0:
        if self.ID == "1":
          print(fore.RED_1 + "\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "2":
          print(fore.MAGENTA_1 + "\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "3":
          print(fore.GREEN_1 + "\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "4":
          print(fore.YELLOW_1 + "\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "5":
          print(fore.CYAN_1 + "\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "6":
          print(fore.DODGER_BLUE_1+"\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "7":
          print(fore.ORANGE_RED_1+"\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "8":
          print(fore.GREEN_3A+"\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "9":
          print(fore.WHEAT_1+"\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "10":
          print(fore.LIGHT_CYAN_1+"\nIt's",self.NAME+"'s turn." + style.RESET)
        elif self.ID == "11":
          print(fore.SKY_BLUE_1+"\nIt's",self.NAME+"'s turn." + style.RESET)
        else:
          print(style.BOLD+"\nIt's",self.NAME+"'s turn."+style.RESET)
        if self.isomode == True and self.isopoints >= 100 and self.ISOmode == False:
          fight = input(fore.GREY_100 + "Attack, Skills, Items, Recover, Check, Support, or Transform? " + style.RESET)
        else:
          fight = input(fore.GREY_100 + "Attack, Skills, Items, Recover, Check, or Support? " + style.RESET)
        if fight == "1" or fight.lower() == "attack":
          bad = False
          if len(enemy.teamS) == 0:
            print("\nThere is no one to attack!")
            continue
          else:
            if self.ID == "6" and self.silenced > 0:
              if len(enemy.teamS) > 1:
                print("")
                print(enemy.teamS)
                self.target(self.silenceattack,enemy.team,enemy.teamID)
                if bad == True:
                  continue
              else:
                for x in enemy.team:
                  if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                    self.silenceattack(x)
            elif self.jabbaroll == 1:
              self.jabbaattack(enemy)
            else:
              if len(enemy.teamS) > 1:
                print("")
                print(enemy.teamS)
                self.target(self.attack,enemy.team,enemy.teamID)
                if bad == True:
                  continue
              else:
                for x in enemy.team:
                  if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                    self.attack(x)
            self.dabtarg = ""
            self.dabstack = 0
            seq = 1
        elif fight == "2" or fight.lower() == "skills":
          msett = self.cMP
          bad = False
          self.skillsystem(ally,enemy)
          if bad == True:
            continue
          if self.isomode == True and self.ISOmode == False and (self.cMP < msett):
            self.isopoints = self.isopoints + (msett-self.cMP)
            if self.isopoints > (100*self.isoLevel):
              self.isopoints = (100*self.isoLevel)
          seq = 1
        elif fight == "3" or fight.lower() == "items":
          bad = False
          self.inventorysystem(ally,enemy)
          if bad == True:
            continue
          seq = 1
        elif fight == "4" or fight.lower() == "recover":
          buttsss = self.cMP
          time.sleep(1)
          self.cMP = self.cMP + (2*self.cMRG)
          if self.cMP > self.fMP:
            self.cMP = self.fMP 
          print("\n" + self.NAME, "relaxes to recover their inner strength, recovering",(self.cMP-buttsss),"mana!",self.NAME,"now has",self.cMP,"mana!")
          seq = 1
        elif fight == "5" or fight.lower() == "check":
          pepe = input("\nAllies or Enemies? ")
          if pepe == "1" or pepe.lower() == "allies":
            print("")
            print(ally.teamS)
            self.target(self.check,ally.team,ally.teamID)
          elif pepe == "2" or pepe.lower() == "enemies":
            print("")
            print(enemy.teamS)
            self.target(self.check,enemy.team,enemy.teamID)
          continue
        elif fight == "6" or fight.lower() == "support":
          bad = False
          self.supportsystem(ally,enemy)
          if len(enemy.team) == 1:
            if enemy.team[0].cHP <=0:
              seq = 1
        elif fight == "7" or fight.lower() == "transform":
          if self.isomode == False or self.isopoints < 100 or self.ISOmode == True:
            continue
          else:
            time.sleep(1)
            self.isopoints = ((self.isopoints//100)*100)
            if self.NAME == "Ishraq":
              input(fore.RED_1+"\nIshraq: You're done."+style.RESET)
              input(fore.RED_1+style.BOLD +"Ishraq: ENRRAAAAGED!!!"+style.RESET)
              if "Wild Instinct" in self.skills:
                self.skills.remove("Wild Instinct")
              self.skills.insert(0,"Enrage")
              self.WI = False
              self.immortal = (self.isopoints/100)+1
              self.counte = self.counte + 3
              self.enragev = 1 + (1-(self.cHP/self.fHP))
            elif self.NAME == "Julius":
              if self.NAME == "Julius":
                input(fore.GREEN_1+"\nJulius: Iso...Iso..."+style.RESET)
                input(fore.GREEN_1+style.BOLD +"Julius: ISOOOMETRIC DRRAAAA-AWWWIINGSS!!"+style.RESET)
              else:
                input(fore.GREEN_1+"\nIan: Minecraft?"+style.RESET)
                input(fore.GREEN_1+style.BOLD +"Ian: MMMIIIIINNNNEEECRAAAFTTT!!!"+style.RESET)
              sett = self.cHP
              self.cHP = self.cHP + round(0.2*self.fHP)
              self.skills.remove("Runner's High")
              self.runhigh = 0
              self.stunimmune = [1,(self.isopoints/100)+1]
              self.shi = self.shi + 3
              if self.cHP > self.fHP:
                self.cHP = self.fHP
            elif self.NAME == "Kelly":
              input(fore.MAGENTA_1 + "\nKelly: Excuse me?"+style.RESET)
              input(fore.MAGENTA_1 + style.BOLD +"Kelly: I'm grading you."+style.RESET)
              self.perfectr = self.perfectr + 3
              self.skills.remove("Heal")
              self.skills.insert(3,"Omniheal")
              sett = self.cMP
              self.cMP = self.cMP + round(0.4*self.fMP)
              if self.cMP > self.fMP:
                self.cMP = self.fMP
            elif self.NAME == "Daniel":
              input(fore.YELLOW_1 + "\nDaniel: I...LIKE.."+style.RESET)
              input(fore.YELLOW_1 +style.BOLD+ "Daniel: MEEENN!!!"+style.RESET)
              self.skills.remove("Enlargen")
              self.skills.remove("Grubby Hands")
              self.skills.insert(0,"Grubby Tides")
              self.thehut = (self.isopoints/100)+1
              self.jabbaroll = 1
              self.jabb = self.jabb + 3
              for x in enemy.team:
                if x.fear < 4:
                  x.fear = 4
            elif self.NAME == "Tim":
              input(fore.CYAN_1 + "\nTim: It's raining tacos...!!!"+style.RESET)
              input(fore.CYAN_1 + style.BOLD + "Taco Lord: FROM OUTTAA THE SKIES! TACOS..DON'T NEED TO ASK WHY!!"+style.RESET)
              ally.teamS.remove("Tim")
              ally.teamID.remove(self.ID)
              ally.teamS.append("Taco Lord")
              ally.teamID.append(self.ID)
              self.skills.insert(1,"Taco Tuesday")
              self.da = self.da + 3
              self.purge("Cleanse",ally,enemy)
              self.quenshield = True
              self.NAME = "Taco Lord"
            elif self.NAME == "Arwyn":
              input(fore.DODGER_BLUE_1+"\nArwyn: All I wanted...was to play league."+style.RESET)
              input(fore.DODGER_BLUE_1+ style.BOLD +"Arwyn: But now all I want...is to kill you."+style.RESET)
              self.fromthes = self.fromthes + 3
              self.darks = True
              for x in enemy.team:
                x.dark = 26
            print("\n"+self.NAME,"borrows strength from the future, breaking all their limits to increase their power tremendously!")
            time.sleep(0.2)
            if self.NAME == "Ishraq":
              print("\n"+self.NAME,"instantly becomes immortal and enrages, increasing his attack and speed appropriately to his current health!")
            if self.NAME == "Julius":
              print("\n"+self.NAME,"heals for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET+" health! He has",self.cHP,"health now!")
            if self.NAME == "Kelly":
              print("\n"+self.NAME,"recovers",str(self.cMP-sett),"mana! She has",self.cMP,"mana now!")
            if self.NAME == "Taco Lord":
              print("\n"+self.NAME,"puts a quen shield on himself!")
            if self.NAME == "Daniel":
              print("\n"+self.NAME,"gains the benefits of Enlargen and fears all enemies!")
            if self.NAME == "Arwyn":
              print("\n"+self.NAME,"sets up a shroud of darkness and causes all enemies to decay!")
            self.ISOmode = True
            for x in ally.team:
              x.currentstats(ally,enemy)
            for x in enemy.team:
              x.currentstats(enemy,ally)
              

  def check(self,ally):
    print("\n"+ally.NAME+"'s Current Stats:\nHP:",str(ally.cHP)+"/"+str(ally.fHP)+"\nMP:",str(ally.cMP)+"/"+str(ally.fMP)+"\nMRG:",str(ally.cMRG)+"\nAT:",str(ally.cAT)+"\nDF:",str(ally.cDF)+"\nMAT:",str(ally.cMAT)+"\nMDF:",str(ally.cMDF),"\nSP:",str(ally.cSP)+"\nAC:",str(ally.cAC)+"\nEV:",str(ally.cEV)+"\nCT:",str(ally.cCT)+"\nAPN:",str(ally.cAPN)+"\nMPN:",str(ally.cMPN))
    if self.isomode == True:
      print("ISO:",str(ally.isopoints))


  def skillsystem(self,ally,enemy):
    global bad
    wop = 0
    bad = False
    if len(self.skills) == 0:
      print("\n" + self.NAME,"does not have any skills!")
    elif self.silenced > 0:
      print("\n" + self.NAME,"is silenced!")
    else:
      print("")
      print(self.skills)
      print(self.NAME, "has",self.cMP,"mana.")
      it = input(fore.GREY_100 + "Which skill do you want to use? " + style.RESET)
      if it.isdigit() == True and it != "0": 
        if len(self.skills) > (int(it)-1):
          check = self.skills[(int(it)-1)]
          self.skillcatalog(check,ally,enemy)
          wop = 1
      for x in self.skills:
        if it.lower() == x.lower():
          self.skillcatalog(x,ally,enemy) 
          wop = 1
    if wop == 0:
      bad = True

  def skillcatalog(self,skill,ally,enemy):
    global bad
    global lastat
    if skill == "Wild Instinct":
      self.allyskillscost("Wild Instinct",0,"Ultra")
      if bad != True:
        self.wildinstinct()
    elif skill == "Smash":
      self.allyskillscost("Smash",40,"Ultra")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.smash,enemy.team,enemy.teamID,al=ally,en=enemy)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to smash!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.smash(x,ally,enemy)
    elif skill == "Valorous Chant":
      self.allyskillscost("Valorous Chant",60,"Basic")
      if bad != True:
        self.valorouschant(ally,enemy)
    elif skill == "Immortality":
      self.allyskillscost("Immortality",80,"Mega")
      if bad != True:
        self.immortality()
    elif skill == "Barrier":
      self.allyskillscost("Barrier",50,"Basic")
      if bad != True:
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.barrier,ally.team,ally.teamID)
        else:
          self.barrier(self)
    elif skill == "From The Shadows":
      self.allyskillscost("From The Shadows",75,"Ultra")
      if bad != True:
        self.fromtheshadows(ally,enemy)
    elif skill == "Enrage":
      self.allyskillscost("Enrage",0,"Ultimate")
      if bad != True:
        self.enrage()
    elif skill == "Calligraphy":
      self.allyskillscost("Calligraphy",20,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.calligraphy,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.calligraphy(x)
    elif skill == "ASMR":
      self.allyskillscost("ASMR",0,"Basic")
      if bad != True:
        self.asmr(ally)
    elif skill == "Pinpoint":
      self.allyskillscost("Pinpoint",10,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.pinpoint,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.pinpoint(x)
    elif skill == "Heal":
      self.allyskillscost("Heal",60,"Mega")
      if bad != True:
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.heal,ally.team,ally.teamID)
        else:
          self.heal(self)
    elif skill == "Omniheal":
      self.allyskillscost("Omniheal",60,"Ultra")
      if bad != True:
        self.omniheal(ally)
    elif skill == "Perfect Requiem":
      self.allyskillscost("Perfect Requiem",100,"Ultra")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.perfectrequiem,enemy.team,enemy.teamID,ally,enemy)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to kill!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.perfectrequiem(x,ally,enemy)
    elif skill == "Revive":
      self.allyskillscost("Revive",100,"Ultra")
      if bad != True:
        if len(ally.deadteam) == 0:
          print("\nEveryone is alive!")
          bad = True
        else:
          print("")
          print(ally.deadteamS)
          self.target(self.revive,ally.deadteam,ally.deadteamS,al=ally)
    elif skill == "Runner's High":
      self.allyskillscost("Runner's High",25,"Basic")
      if bad != True:
        self.runnershigh()
    elif skill == "Shield":
      self.allyskillscost("Shield",0,"Basic")
      if bad != True:
        self.shield()
    elif skill == "Tremors":
      self.allyskillscost("Tremors",55,"Mega")
      if bad != True:
        self.tremors(enemy)
    elif skill == "Isometric Drawings":
      self.allyskillscost("Isometric Drawings",70,"Ultra")
      if bad != True:
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.isometricdrawings,ally.team,ally.teamID)
        else:
          self.isometricdrawings(self)
    elif skill == "Combo":
      self.allyskillscost("Combo",100,"Ultra")
      if bad != True:
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.combo,ally.team,ally.teamID,ally,enemy)
        else:
          print("\n"+self.NAME, "cannot cast this skill by himself!")
          bad = True
    elif skill == "Grubby Hands":
      self.allyskillscost("Grubby Hands",20,"Basic")
      if bad != True:       
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.grubbyhands,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to touch!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.grubbyhands(x)
    elif skill == "Grubby Tides":
      self.allyskillscost("Grubby Tides",20,"Basic")
      if bad != True:
        self.grubbytides(enemy)     
    elif skill == "Taunt":
      self.allyskillscost("Taunt",0,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:  
          print("")
          print(enemy.teamS)
          self.target(self.taunt,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to taunt!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.taunt(x)
    elif skill == "Knight's Vow":
      self.allyskillscost("Knight's Vow",60,"Ultra")
      if bad != True: 
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.knightsvow,ally.team,ally.teamID,al=ally)
        else:
          print("\n"+self.NAME,"cannot cast this skill on himself!")
          bad = True
    elif skill == "Photosynthesis":
      self.allyskillscost("Photosynthesis",0,"Mega")
      if bad != True:
        self.photosynthesis()
    elif skill == "Enlargen":
      self.allyskillscost("Enlargen",80,"Mega")
      if bad != True:
        self.enlargen()
    elif skill == "Electron":
      self.allyskillscost("Electron",100,"Mega")
      if bad != True:
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.electron,ally.team,ally.teamID)
        else:
          self.electron(self)
    elif skill == "Dab": 
      self.allyskillscost("Dab",20,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.dab,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to dab on!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.dab(x)
    elif skill == "Safety Belt":
      self.allyskillscost("Safety Belt",35,"Mega")
      if bad != True:
        self.protobelt(enemy)
    elif skill == "Quen":
      self.allyskillscost("Quen",80,"Ultra")
      if bad != True:
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.quen,ally.team,ally.teamID,ally,enemy)
        else:
          self.quen(self,ally,enemy)
    elif skill == "Taco Tuesday":
      self.allyskillscost("Taco Tuesday",80,"Ultra")
      if bad != True:
        self.tacotuesday(ally,enemy)
    elif skill == "Chronopower":
      self.allyskillscost("Chronopower",0,"Mega")
      if bad != True:
        self.chronopower()
    elif skill == "Rubix Cube":
      self.allyskillscost("Rubix Cube",75,"Ultra")
      if bad != True:
        self.rubixcube(enemy)
    elif skill == "Autosentry":
      self.allyskillscost("Autosentry",100,"Ultra")
      if bad != True:
        self.autosentry(ally)
    elif skill == "Silence":
      self.allyskillscost("Silence",0,"Basic")
      if bad != True:
        self.silence()
    elif skill == "Cut Myself":
      self.allyskillscost("Cut Myself",35,"Basic")
      if bad != True:
        self.cutmyself(enemy)
    elif skill == "Gunblade":
      self.allyskillscost("Gunblade",30,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.gunblade,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.gunblade(x) 
    elif skill == "Spark Net":
      self.allyskillscost("Spark Net",50,"Mega")
      if bad != True:
        self.sparknet(ally,enemy)
    elif skill == "Darkness":
      self.allyskillscost("Darkness",60,"Ultra")
      if bad != True:
        self.darkness(enemy)
    elif skill == "Progressive Overload":
      if self.tension >= 3:
        print("\n"+self.NAME,"is at maximum tension!")
        bad = True
      else:
        self.allyskillscost("Progressive Overload",0,"Basic")  
        if bad != True:
          self.progressiveoverload()
    elif skill == "Sick Pump": 
      if self.tension >= 5:
        print("\n"+self.NAME,"cannot become more CHAD!")
        bad = True
      else:
        self.allyskillscost("Sick Pump",0,"Basic")  
        if bad != True:
          self.sickpump()
    elif skill == "Arm Wrestling":  
      self.allyskillscost("Arm Wrestling",50,"Ultra")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.armwrestling,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nNO ONE WANTS TO ARM WRESTLE!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.armwrestling(x)
    elif skill == "Inferno":
      self.allyskillscost("Inferno",30,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.inferno,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.inferno(x)
    elif skill == "Self-Destruct":
      self.allyskillscost("Self-Destruct",0,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.selfdestruct,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to bomb!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.selfdestruct(x)
    elif skill == "Chad Walk":
      self.allyskillscost("Chad Walk",80,"Ultra")
      if bad != True:
        self.chadwalk(ally)
    elif skill == "Suck":
      self.allyskillscost("Suck",80,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.suck,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to suck!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.suck(x)
    elif skill == "Power Surge":
      self.allyskillscost("Power Surge",75,"Ultra")
      if bad != True:
        self.powersurge(enemy)
    elif skill == "Telepathy":
      self.allyskillscost("Telepathy",35,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.telepathy,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to whisper to!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.telepathy(x)
    elif skill == "Mimic":
      if self.mimit == 1:
        lis = input("\n(1) Allies  (2) Enemies\nAction: ")
        if lis == "1" or lis.lower() == "allies":
          if len(ally.teamS) > 1:
            print("")
            print(ally.teamS)
            self.target(self.mimic,ally.team,ally.teamID,al=ally,en=enemy)
          else:
            self.mimic(self,ally,enemy)
        elif lis == "2" or lis.lower() == "enemies":
          if len(enemy.teamS) > 1:
            print("")
            print(enemy.teamS)
            self.target(self.mimic,enemy.team,enemy.teamID,al=ally,en=enemy)
          else:
            if len(enemy.teamS) == 0:
              print("\nThere is no one to mimic!")
              bad = True
            else:
              for x in enemy.team:
                if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                  self.mimic(x,ally,enemy)
        else:
          bad = True
      else:
        self.mimic(al=ally,targ=enemy)
    elif skill == "Desperation":
      self.allyskillscost("Desperation",50,"Mega")
      if bad != True:
        self.desperation(ally,enemy)
    elif skill == "Emo Phase":
      self.allyskillscost("Emo Phase",75,"Ultra")
      if bad != True:
        self.emophase()
    elif skill == "Outrage":
      self.allyskillscost("Outrage",80,"Ultra")
      if bad != True:
        if self.onethro > 0:
          self.outrageAOE(enemy)
        else:
          if len(enemy.teamS) > 1:
            print("")
            print(enemy.teamS)
            self.target(self.outrage,enemy.team,enemy.teamID)
          else:
            if len(enemy.teamS) == 0:
              print("\nThere is no one to flame!")
              bad = True
            else:
              for x in enemy.team:
                if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                  self.outrage(x)
    elif skill == "Arrivederci":
      self.allyskillscost("Arrivederci",45,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.arrivederci,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to bid farwell!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.arrivederci(x)
    elif skill == "Recluse":
      self.allyskillscost("Recluse",35,"Mega")
      if bad != True:
        self.recluse()
    elif skill == "Friends":
      self.allyskillscost("Friends",35,"Mega")
      if bad != True:
        self.friends(ally)
    elif skill == "One Throat":
      self.allyskillscost("One Throat",50,"Mega")
      if bad != True:
        self.onethroat()
    elif skill == "Energy Kick":
      self.allyskillscost("Energy Kick",0,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.energykick,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to kick!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.energykick(x)
    elif skill == "Virginity Theft":
      self.allyskillscost("Virginity Theft",0,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.virginitytheft,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to sex!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.virginitytheft(x)
    elif skill == "Dancer's Swiftness":
      self.allyskillscost("Dancer's Swiftness",80,"Ultra")
      if bad != True:
        self.dancersswiftness()
    elif skill == "Weird Flex":
      self.allyskillscost("Weird Flex",35,"Mega")
      if bad != True:
        self.weirdflex(enemy)
    elif skill == "Rehearsal":
      self.allyskillscost("Rehearsal",65,"Ultra")
      if bad != True:
        self.rehearsal(ally)
    elif skill == "Power Rest":
      self.allyskillscost("Power Rest",40,"Mega")
      if bad != True:
        self.powerrest()
    elif skill == "Graceful Gales":
      self.allyskillscost("Graceful Gales",25,"Basic")
      if bad != True:
        self.gracefulgales(ally)
    elif skill == "Lingering Light":
      self.allyskillscost("Lingering Light",20,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.lingeringlight,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to illuminate!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.lingeringlight(x)
    elif skill == "Whirling Winds":
      self.allyskillscost("Whirling Winds",40,"Mega")
      if bad != True:
        self.whirlingwinds(enemy)
    elif skill == "Radiant Resilience":
      self.allyskillscost("Radiant Resilience",70,"Ultra")
      if bad != True:
        self.radiantresilience(ally)
    elif skill == "Eternal Equinox":
      self.allyskillscost("Eternal Equinox",100,"Ultra")
      if bad != True:
        self.eternalequinox(ally,enemy)
    elif skill == "Groot Root":
      self.allyskillscost("Groot Root",5,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.grootroot,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to root!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.grootroot(x)
      if bad != True:
        self.cMP = self.cMP - 5
    elif skill == "Mixtape":
      self.allyskillscost("Mixtape",5,"Basic")
      if bad != True:
        self.mixtape(enemy)
        self.cMP = self.cMP - 5
    elif skill == "Chill Vibes":
      self.allyskillscost("Chill Vibes",5,"Basic")
      if bad != True:
        self.chillvibes(enemy)
        self.cMP = self.cMP - 5
    elif skill == "Teaming":
      self.allyskillscost("Teaming",5,"Basic")
      if bad != True:
        self.teaming(ally)
        self.cMP = self.cMP - 5
    elif skill == "Bear":
      self.allyskillscost("Bear",5,"Basic")
      if bad != True:
        if len(ally.teamS) > 1:
          print("")
          print(ally.teamS)
          self.target(self.bear,ally.team,ally.teamID)
        else:
          self.bear(self)
      if bad != True:
        self.cMP = self.cMP - 5
    elif skill == "Boxing Combo":
      self.allyskillscost("Boxing Combo",5,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.boxingcombo,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to combo!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.boxingcombo(x)
      if bad != True:
        self.cMP = self.cMP - 5
    elif skill == "Gaze":
      self.allyskillscost("Gaze",5,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.gaze,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to gaze at!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.gaze(x)
      if bad != True:
        self.cMP = self.cMP - 5
    elif skill == "Buckets":
      self.allyskillscost("Buckets",5,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.buckets,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to dunk on!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.buckets(x)
      if bad != True:
        self.cMP = self.cMP - 5
    elif skill == "Accurate Strike":
      self.allyskillscost("Accurate Strike",5,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.accuratestrike,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.accuratestrike(x)
      if bad != True:
        self.cMP = self.cMP - 5
    elif skill == "Cripple":
      self.allyskillscost("Cripple",5,"Basic")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.cripple,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to cripple!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.cripple(x)
      if bad != True:
        self.cMP = self.cMP - 5
    elif skill == "Giant":
      self.allyskillscost("Giant",0,"Ultra")
      if bad != True:
        self.giant()
    elif skill == "Minus Full Points":
      self.allyskillscost("Minus Full Points",0,"Ultra")
      if bad != True:
        self.minusfullpoints(enemy)
    elif skill == "Candy":
      self.allyskillscost("Candy",0,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.candy,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to give candy to!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.candy(x)
    elif skill == "Notebook Evaluation":
      self.allyskillscost("Notebook Evaluation",0,"Ultimate")
    elif skill == "Roast":
      self.allyskillscost("Roast",0,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.roast,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to roast!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.roast(x)
    elif skill == "Shiny Bald Head":
      self.allyskillscost("Shiny Bald Head",0,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.shinybaldhead,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one blind!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.shinybaldhead(x)
    elif skill == "Quick Mafs":
      self.allyskillscost("Quick Mafs",0,"Ultimate")
    elif skill == "Laugh":
      self.allyskillscost("Laugh",0,"Mega")
      if bad != True:
        self.laugh(enemy)
    elif skill == "Dark Firaga":
      self.allyskillscost("Dark Firaga",0,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.darkfiraga,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to burn!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.darkfiraga(x)
    elif skill == "Zantetsuken":
      self.allyskillscost("Zantetsuken",0,"Mega")
      if bad != True:
        self.zantetsuken()
    elif skill == "Sacrifice":
      self.allyskillscost("Sacrifice",0,"Mega")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.sacrifice,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.sacrifice(x)
    elif skill == "Ars Solum":
      self.allyskillscost("Ars Solum",0,"Ultra")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.ars,enemy.team,enemy.teamID,al=ally,en=enemy)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to smash!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.ars(x,ally,enemy)
    elif skill == "Glacier":
      self.allyskillscost("Glacier",0,"Ultra")
      if bad != True:
        self.glacier(enemy)
    elif skill == "Magic Hour":
      self.allyskillscost("Magic Hour",0,"Ultra")
      if bad != True:
        self.magichour(enemy,ally)
    elif skill == "Thunder Shot":
      self.allyskillscost("Thunder Shot",0,"Ultra")
      if bad != True:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.thundershot,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to electrocute!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.thundershot(x)
    elif skill == "Raging Storm":
      self.allyskillscost("Raging Storm",0,"Ultra")
      if bad != True:
        self.ragingstorm(enemy)
    elif skill == "Seeking Mine":
      self.allyskillscost("Seeking Mine",0,"Mega")
      if bad != True:
        self.seekingmine()
    else:
      print("yes")
      bad = True
    if bad != True:
      if skill != "Dab":
        self.dabtarg = ""
        self.dabstack = 0
      self.lastattack = skill
      lastat = skill
      
  def allyskillscost(self,skill,cost,level):
    global bad
    global skl
    skl = level
    bad = False
    if self.mimicm == 1:
      if level == "Ultimate":
        print("\n"+self.NAME,"can't mimic ultimate skills!")
        bad = True
      elif level == "Ultra":
        if self.mimi < 4:
          print("\n"+self.NAME,"can't mimic ultra skills yet!")
          bad = True
      elif level == "Mega":
        if self.mimi < 2:
          print("\n"+self.NAME,"can't mimic mega skills yet!")
          bad = True
      if bad != True:
        if level == "Ultra":
          if cost > round(self.fMP*(0.5-(0.05*self.mimi))):
            if self.cMP < cost:
              print("\n" + self.NAME, "does not have enough mana! She needs",cost,"mana to cast!")
              bad = True
          elif cost < round(self.fMP*(0.5-(0.05*self.mimi))):
            if self.cMP < round(self.fMP*(0.5-(0.05*self.mimi))):
              print("\n" + self.NAME, "does not have enough mana! She needs",round(self.fMP*(0.5-(0.05*self.mimi))),"mana to cast!")
              bad = True
        elif level == "Mega":
          if cost > round(self.fMP*(0.4-(0.05*self.mimi))):
            if self.cMP < cost:
              print("\n" + self.NAME, "does not have enough mana! She needs",cost,"mana to cast!")
              bad = True
          elif cost < round(self.fMP*(0.4-(0.05*self.mimi))):
            if self.cMP < round(self.fMP*(0.4-(0.05*self.mimi))):
              print("\n" + self.NAME, "does not have enough mana! She needs",round(self.fMP*(0.4-(0.05*self.mimi))),"mana to cast!")
              bad = True
        elif level == "Basic":
          if cost > round(self.fMP*(0.3-(0.05*self.mimi))):
            if self.cMP < cost:
              print("\n" + self.NAME, "does not have enough mana! She needs",cost,"mana to cast!")
              bad = True
          elif cost < round(self.fMP*(0.3-(0.05*self.mimi))):
            if self.cMP < round(self.fMP*(0.3-(0.05*self.mimi))):
              print("\n" + self.NAME, "does not have enough mana! She needs",round(self.fMP*(0.3-(0.05*self.mimi))),"mana to cast!")
              bad = True
    else:
      if self.cMP < cost:
        print("\n" + self.NAME, "does not have enough mana!",self.GEN[2].capitalize(),"needs",cost,"mana to cast!")
        bad = True

  def inventorysystem(self,tea,ene):
    global bad
    wop = 0
    bad = False
    if len(self.battleinventory) == 0:
      print("\n"+self.NAME,"has no items!")
    else:
      print("")
      print(self.battleinventory)
      it = input(fore.GREY_100 + "Use what item? " + style.RESET)
      if it.isdigit() == True and it != "0":
        if len(self.battleinventory) > (int(it)-1):
          check = self.battleinventory[(int(it)-1)]
          self.itemcatalog(check,tea,ene)
          wop = 1
      for x in self.battleinventory:
        if it.lower() == x.lower():
          self.itemcatalog(x,tea,ene) 
          wop = 1
    if wop == 0:
      bad = True

  def equipcatalog(self,item1,item2,sec):

    self.equipcheck(dr=True)
    dHP = self.fHP   
    dMP = self.fMP
    dMRG = self.fMRG
    dAT = self.fAT
    dDF = self.fDF
    dMAT = self.fMAT
    dMDF = self.fMDF
    dSP = self.fSP
    dAC = self.fAC
    dEV = self.fEV
    dCT = self.fCT
    dAPN = self.fAPN
    dMPN = self.fMPN
    no = 0
    eff = ""

    #Headgear

    if item2 == "Glasses":
      dMAT = dMAT + (self.MAT*.05)
      dAC = dAC + (self.AC*.05)
    if item2 == "Hairband":
      dHP = dHP + (self.HP*.02)

    #Chestpieces 

    if item2 == "Track Warm-Up":
      dDF = dDF + (self.DF*.04)
      dSP = dSP + (self.SP*.04)
    if item2 == "School Uniform":
      dDF = dDF + (self.DF*.02)

    #Boots 

    if item2 == "Vans":
      dHP = dHP + (self.HP*.02)
    if item2 == "Jays":
      dHP = dHP + (self.HP*.05)
    if item2 == "Flats":
      dMDF = dMDF + (self.MDF*.06)
    if item2 == "Roshes":
      dHP = dHP + (self.HP*.1)
      dSP = dSP - (self.SP*.02)
    if item2 == "Sneakers":
      dHP = dHP + (self.HP*.03)
      dSP = dSP + (self.SP*.02)

    #Weapons

    if item2 == "Pencil":   
      dAT = dAT + (self.AT*.05)
      dCT = dCT + (self.CT*.02)
      dAPN = dAPN + (self.APN*.2)
    if item2 == "Ruler":
      dAT = dAT + (self.AT*.07)
      dMRG = dMRG + (self.MRG*.2)
    if item2 == "Keyboard":
      dAT = dAT + (self.AT*.1)
    if item2 == "Pen":
      dAT = dAT + (self.AT*.02)
      dMAT = dMAT + (self.MAT*.04)
    if item2 == "Track Baton":
      dAT = dAT + (self.AT*.08)
      dSP = dSP + (self.SP*.02)
    if item2 == "Slingshot":
      dAT = dAT + (self.AT*.1)
      dAC = dAC + (self.AC*.03)
      dCT = dCT + (self.CT*.02)
    if item2 == "Scissors":
      dAT = dAT + (self.AT*.12)
      dCT = dCT + (self.CT*.03)    

    #Accessories
    
    if item2 == "Agenda":
      dMP = dMP + (self.MP*.05)
      dMRG = dMRG + (self.MRG*.4)

    #Headgear

    if item1 == "Glasses":
      dMAT = dMAT - (self.MAT*.05)
      dAC = dAC - (self.AC*.05)
    if item1 == "Hairband":
      dHP = dHP - (self.HP*.02)

    #Chestpieces 

    if item1 == "Track Warm-Up":
      dDF = dDF - (self.DF*.04)
      dSP = dSP - (self.SP*.04)
    if item1 == "School Uniform":
      dDF = dDF - (self.DF*.02)

    #Boots 

    if item1 == "Vans":
      dHP = dHP - (self.HP*.02)
    if item1 == "Jays":
      dHP = dHP - (self.HP*.05)
    if item1 == "Flats":
      dMDF = dMDF - (self.MDF*.06)
    if item1 == "Roshes":
      dHP = dHP - (self.HP*.1)
      dSP = dSP + (self.SP*.02)
    if item1 == "Sneakers":
      dHP = dHP - (self.HP*.03)
      dSP = dSP - (self.SP*.02)

    #Weapons

    if item1 == "Pencil":   
      dAT = dAT - (self.AT*.05)
      dCT = dCT - (self.CT*.02)
      dAPN = dAPN - (self.APN*.2)
    if item1 == "Ruler":
      dAT = dAT - (self.AT*.07)
      dMRG = dMRG - (self.MRG*.2)
    if item1 == "Keyboard":
      dAT = dAT - (self.AT*.1)
    if item1 == "Pen":
      dAT = dAT - (self.AT*.02)
      dMAT = dMAT - (self.MAT*.04)
    if item1 == "Track Baton":
      dAT = dAT - (self.AT*.08)
      dSP = dSP - (self.SP*.02)
    if item1 == "Slingshot":
      dAT = dAT - (self.AT*.1)
      dAC = dAC - (self.AC*.03)
      dCT = dCT - (self.CT*.02)
    if item1 == "Scissors":
      dAT = dAT - (self.AT*.12)
      dCT = dCT - (self.CT*.03)    

    #Accessories
    
    if item1 == "Agenda":
      dMP = dMP - (self.MP*.05)
      dMRG = dMRG - (self.MRG*.4)

    if item2 != "":
      print("\nStat Changes from equipping",item2+":")
    else:
      print("\nStat Changes from de-equipping",item1+":")
    if dHP != self.fHP:
      if dHP > self.fHP:
        print("HP:",round(self.fHP),fore.GREEN_1+"->",round(dHP),style.RESET)
      else:
        print("HP:",round(self.fHP),fore.RED_1+"->",round(dHP),style.RESET)
    if dMP != self.fMP:
      if dMP > self.fMP:
        print("MP:",round(self.fMP),fore.GREEN_1+"->",round(dMP),style.RESET)
      else:
        print("MP:",round(self.fMP),fore.RED_1+"->",round(dMP),style.RESET)
    if dMRG != self.fMRG:
      if dMRG > self.fMRG:
        print("MRG:",round(self.fMRG),fore.GREEN_1+"->",round(dMRG),style.RESET)
      else:
        print("MRG:",round(self.fMRG),fore.RED_1+"->",round(dMRG),style.RESET)
    if dAT != self.fAT:
      if dAT > self.fAT:
        print("AT:",round(self.fAT),fore.GREEN_1+"->",round(dAT),style.RESET)
      else:
        print("AT:",round(self.fAT),fore.RED_1+"->",round(dAT),style.RESET)
    if dDF != self.fDF:
      if dDF > self.fDF:
        print("DF:",round(self.fDF),fore.GREEN_1+"->",round(dDF),style.RESET)
      else:
        print("DF:",round(self.fDF),fore.RED_1+"->",round(dDF),style.RESET)
    if dMAT != self.fMAT:
      if dMAT > self.fMAT:
        print("MAT:",round(self.fMAT),fore.GREEN_1+"->",round(dMAT),style.RESET)
      else:
        print("MAT:",round(self.fMAT),fore.RED_1+"->",round(dMAT),style.RESET)
    if dMDF != self.fMDF:
      if dMDF > self.fMDF:
        print("MDF:",round(self.fMDF),fore.GREEN_1+"->",round(dMDF),style.RESET)
      else:
        print("MDF:",round(self.fMDF),fore.RED_1+"->",round(dMDF),style.RESET)
    if dSP != self.fSP:
      if dSP > self.fSP:
        print("SP:",round(self.fSP),fore.GREEN_1+"->",round(dSP),style.RESET)
      else:
        print("SP:",round(self.fSP),fore.RED_1+"->",round(dSP),style.RESET)
    if dAC != self.fAC:
      if dAC > self.fAC:
        print("AC:",round(self.fAC),fore.GREEN_1+"->",round(dAC),style.RESET)
      else:
        print("AC:",round(self.fAC),fore.RED_1+"->",round(dAC),style.RESET)
    if dEV != self.fEV:
      if dEV > self.fEV:
        print("EV:",round(self.fEV),fore.GREEN_1+"->",round(dEV),style.RESET)
      else:
        print("EV:",round(self.fEV),fore.RED_1+"->",round(dEV),style.RESET)
    if dCT != self.fCT:
      if dCT > self.fCT:
        print("CT:",round(self.fCT),fore.GREEN_1+"->",round(dCT),style.RESET)
      else:
        print("CT:",round(self.fCT),fore.RED_1+"->",round(dCT),style.RESET)
    if dAPN != self.fAPN:
      if dAPN > self.fAPN:
        print("APN:",round(self.fAPN),fore.GREEN_1+"->",round(dAPN),style.RESET)
      else:
        print("APN:",round(self.fAPN),fore.RED_1+"->",round(dAPN),style.RESET)
    if dMPN != self.fMPN:
      if dMPN > self.fMPN:
        print("MPN:",round(self.fMPN),fore.GREEN_1+"->",round(dMPN),style.RESET)
      else:
        print("MPN:",round(self.fMPN),fore.RED_1+"->",round(dMPN),style.RESET)
    if eff != "":
      print("\n"+eff)
      print("")
    while no == 0:
      if item2 != "":
        choi = input("\nAre you sure you want to equip this?\n(1) Yes  (2) No\nAction: ")
      else:
        choi = input("\nAre you sure you want to de-equip this?\n(1) Yes  (2) No\nAction: ")
      if choi == "1" or choi.lower() == "yes":
        if item2 != "":
          print("\n"+self.NAME,"equips",item2+"!")
        else:
          print("\n"+self.NAME,"de-equips",item1+"!")
        if sec == 1:
          if item2 != "":
            you.weaponinventory.remove(item2)
          self.weap = item2
        elif sec == 2:
          if item2 != "":
            you.helminventory.remove(item2)
          self.helm = item2
        elif sec == 3:
          if item2 != "":
            you.chestinventory.remove(item2)
          self.chest = item2
        elif sec == 4:
          if item2 != "":
            you.bootsinventory.remove(item2)
          self.boots = item2
        elif sec == 5:
          if item2 != "":
            you.accessinventory.remove(item2)
          self.access = item2
        if item1 != "":
          if sec == 1:
            you.weaponinventory.append(item1)
          elif sec == 2:
            you.helminventory.append(item1)
          elif sec == 3:
            you.chestinventory.append(item1)
          elif sec == 4:
            you.bootsinventory.append(item1)
          elif sec == 5:
            you.accessinventory.append(item1)   
        self.equipcheck()
        no = 1
      if choi == "2" or choi.lower() == "no":
        no = 1
    

  def addbattleitem(self,Item):
    self.battleinventory.append(Item)

  def itemcatalog(self,item,tea,ene):
    global bad
    #[1] = AT
    #[2] = DF
    #[3] = MAT
    #[4] = MDF
    #[5] = SP
    #[6] = AC
    #[7] = EV
    #[8] = CT
    #[9] = APN
    #[10] = MPN
    #[11] = MRG
    if self.cHP > 0:
      if item == "Chips":
        sett = self.cHP
        self.cHP = self.cHP + 10
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        time.sleep(1)
        print("\n"+self.NAME,"eats chips, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")
      if item == "Taco":
        sett = self.cHP
        self.cHP = self.cHP + round(0.25*self.fHP)
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        self.purge("Cleanse",tea,ene)
        time.sleep(1)
        print("\n"+self.NAME,"eats Tim's taco, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and cleansing them!",self.NAME,"has",self.cHP,"health now!")
      if item == "Bandages":
        sett = self.cHP
        self.cHP = self.cHP + (30+round(0.1*self.fHP))
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        time.sleep(1)
        print("\n"+self.NAME,"wraps themselves with bandages, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")
      if item == "Med-Kit":
        sett = self.cHP
        self.cHP = self.cHP + (100+round(0.3*self.fHP))
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        time.sleep(1)
        print("\n"+self.NAME,"uses a med-kit, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")
      if item == "Scooby Snacks":
        sett = self.cHP
        self.cHP = self.cHP + 24
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        if self.food[0] > 4:
          self.food[0] = 4
        self.food[2] = self.food[2] + 5
        time.sleep(1)
        print("\n"+self.NAME,"eats scooby snacks, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and slightly inreasing their physical defense!",self.NAME,"has",self.cHP,"health now!")
      if item == "Blue Doritos":
        sett = self.cHP
        self.cHP = self.cHP + 15
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        if self.food[0] > 3:
          self.food[0] = 3
        self.food[3] = self.food[11] + 5
        time.sleep(1)
        print("\n"+self.NAME,"eats cool ranch doritos, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and inreasing their magic attack!",self.NAME,"has",self.cHP,"health now!")
      if item == "Fuze":
        sett = self.cHP
        self.cHP = self.cHP + 35
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        if self.food[0] > 5:
          self.food[0] = 5
        self.food[6] = self.food[6] + 5
        time.sleep(1)
        print("\n"+self.NAME,"drinks Fuze, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and slightly inreasing their accuracy!",self.NAME,"has",self.cHP,"health now!")
      if item == "Daisy Cookie":
        sett = self.cHP
        self.cHP = self.cHP + 22
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        if self.food[0] > 5:
          self.food[0] = 5
        self.food[2] = self.food[2] + 9
        time.sleep(1)
        print("\n"+self.NAME,"eats a daisy cookie, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and inreasing their physical defense!",self.NAME,"has",self.cHP,"health now!")
      if item == "Cupcake":
        sett = self.cHP
        self.cHP = self.cHP + 14
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        if self.food[0] > 3:
          self.food[0] = 3
        self.food[4] = self.food[4] + 9
        time.sleep(1)
        print("\n"+self.NAME,"eats a cupcake, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and inreasing their magical defense!",self.NAME,"has",self.cHP,"health now!")
      if item == "Cereal Bar":
        sett = self.cHP
        self.cHP = self.cHP + 20
        if self.cHP > self.fHP:
          self.cHP = self.fHP
        if self.food[0] > 3:
          self.food[0] = 3
        self.food[2] = self.food[2] + 4
        self.food[4] = self.food[4] + 4
        time.sleep(1)
        print("\n"+self.NAME,"eats a cereal bar, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and slightly inreasing their physical and magical defense!",self.NAME,"has",self.cHP,"health now!")
      self.battleinventory.remove(item)
    else:
      print("\n"+self.NAME,"is fallen and cannot consume this item!")
      bad = True


  def supportsystem(self,ally,enemy):
    global bad
    global player1
    wop = 0
    bad = False
    if len(player1.suppteam) == 0:
      print("\nYou do not have any support allies!")
    else:
      print("")
      print(player1.suppteamS)
      it = input(fore.GREY_100 + "Call who? " + style.RESET)
      if it.isdigit() == True and it != "0":
        if len(player1.suppteam) > (int(it)-1):
          check = player1.suppteam[(int(it)-1)]
          self.supportcatalog(check,ally,enemy)
          wop = 1
      for x in player1.suppteam:
        if it.lower() == x.name.lower():
          self.supportcatalog(x,ally,enemy) 
          wop = 1
    if wop == 0:
      bad = True

  def supportcatalog(self,per,ally,enemy):
    global bad

    if per.ccd > 0:
      print("\n"+per.name,"is on cooldown!")
      bad = True
    
    else:

      if per.name == "Brandon":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.grootroot,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\nThere is no one to root!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.grootroot(x)
      
      elif per.name == "Edmond":
        if self.NAME == "Julius":
          self.chillvibes(enemy)
        else:
          self.mixtape(enemy)

      elif per.name == "David":
        self.teaming(ally)
      
      elif per.name == "Metin":
        self.bear(self)
      
      elif per.name == "Noah":
        if self.NAME == "Ishraq":
          if len(enemy.teamS) > 1:
            print("")
            print(enemy.teamS)
            self.target(self.boxingcombo,enemy.team,enemy.teamID)
          else:
            if len(enemy.teamS) == 0:
              print("\There is no one to attack!")
              bad = True
            else:
              for x in enemy.team:
                if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                  self.boxingcombo(x)
        else:
          if len(enemy.teamS) > 1:
            print("")
            print(enemy.teamS)
            self.target(self.gaze,enemy.team,enemy.teamID)
          else:
            if len(enemy.teamS) == 0:
              print("\There is no one to gaze at!")
              bad = True
            else:
              for x in enemy.team:
                if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                  self.gaze(x)

      elif per.name == "Hassan":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.buckets,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to dunk on!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.buckets(x)

      elif per.name == "Alvaro":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.accuratestrike,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.accuratestrike(x)
      
      elif per.name == "Octavio":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.cripple,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to cripple!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.cripple(x)

      elif per.name == "Dylan":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.strangle,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one strangle!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.strangle(x)

      elif per.name == "Andrew":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.insult,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to curse out!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.insult(x)

      elif per.name == "Jahir":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.headbutt,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to charge!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.headbutt(x)
      
      elif per.name == "Shannae":
        self.snacks()
      
      elif per.name == "Matvey":
        self.eagle()

      elif per.name == "Lascelles":
        if self.NAME == "Kelly" or self.NAME == "Tim" or self.NAME == "Julius" or self.NAME == "Ian" or self.NAME == "Arwyn":
          self.godandanime(ally)
        else:
          self.orangejustice(enemy)

      elif per.name == "Kenny":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.stayshut,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to shut up!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.stayshut(x)

      elif per.name == "Dereck":
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.awkwardtouch,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to touch!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and (x.invis <=0 or x.revealed > 0):
                self.awkwardtouch(x)
          
    if bad != True:
      per.use()
  
  def supportscale(self):
    global player1
    TL = 0
    for x in player1.team:
      TL = TL + x.LV
    for x in player1.backteam:
      TL = TL + x.LV
    for x in player1.deadteam:
      TL = TL + x.LV
    return TL
  
  def grootroot(self,enemy):
    time.sleep(1)
    brandAC = 100 + round((100/240)*self.supportscale())
    diff = enemy.cEV - brandAC
    if random.randint(1,100) <= diff:
      print("\nBrandon erupts the roots in the ground, but",enemy.NAME,"dodges the roots!")
    else:
      print("\nBrandon erupts the roots in the ground, rooting",enemy.NAME+"!")
      enemy.rooted = 1
    
  def chillvibes(self,enemy):
    time.sleep(1)
    print("\nEdmond brings the chill vibes into the battlefield, slowing all enemies down!")
    for x in enemy.team:
      x.chilled = 21
      x.currentstats(bots,you)

  def mixtape(self,enemy):
    time.sleep(1)
    print("\nEdmond plays his fire mixtape!")
    edAC = 80 + round((60/240)*self.supportscale())
    for x in enemy.team:
      diff = x.cEV - edAC
      if random.randint(1,100) <= diff:
        print("\n"+x.NAME,"doesn't feel the music, remaining unaffected!")
      else:
        if x.burnt < 2:
          x.burnt = 2
        x.burnd = x.burnd + (13 + round((137/240)*self.supportscale()))
        print("\n"+x.NAME,"feels the music, and starts to roast alive!")
        x.currentstats(bots,you)

  def teaming(self,ally):
    time.sleep(1)
    print("\nDavid flaps his arm across his chest repeatedly, increasing the team's defense for 2 hits!")
    for x in ally.team:
      x.teamed = 2
      x.currentstats(you,bots)

  def bear(self,ally):
    time.sleep(1)
    if ally.NAME == "Metin":
      print("\nMetin guards himself with his sheer mass, putting up a barrier!")
    else:
      print("\nMetin guards",ally.NAME,"with his sheer mass, acting as a barrier!")
    ally.beared = 1

  def gaze(self,enemy):
    time.sleep(1)
    print("\nNoah gazez at",enemy.NAME,"with his glorious eyes, blinding them for 3 turns!")
    enemy.blind = 3
    enemy.currentstats(bots,you)

  def boxingcombo(self,enemy):
    global sett
    time.sleep(1)
    print("\nNoah swarms",enemy.NAME,"with a flurry of 3 fast punches!")
    NAC = 100 + round((30/240)*self.supportscale())
    NAT = 15 + round((100/240)*self.supportscale())
    RI = 0
    for x in range(3):
      time.sleep(0.4)
      RI = RI + 1
      diff = enemy.cEV - NAC
      if random.randint(1,100) <= diff:
        print("\n"+enemy.NAME,"dodges a punch!")
        enemy.specialdodgecases(self,0,"Physical Support")
      else:
        sett = enemy.cHP
        dmg = NAT*(1+(0.25*(RI-1)))
        enemy.cHP = enemy.cHP - round(self.dmgreduct*dmg*(1-((enemy.cDF)/(enemy.cDF+100))))
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+enemy.NAME,"is hit, but takes no damage!")
          else:
            print("\n"+enemy.NAME,"is hit, taking",fore.ORANGE_1  + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+enemy.NAME,"is hit, taking",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
          enemy.cHP = 1
        enemy.onhittimersdefense(self,0,dmg,"Physical Support") 
        enemy.currentstats(bots,you)

  def buckets(self,enemy):
    global sett
    time.sleep(1)
    diff = enemy.cEV - 100
    if random.randint(1,100) <= diff:
      print("\nHassan tries to dunk on",enemy.NAME,"but they reject him!")
      enemy.specialdodgecases(self,0,"Physical Support")
    else:
      sett = enemy.cHP
      dmg = ((enemy.HP-enemy.cHP)*0.25)+round((100/240)*self.supportscale())
      enemy.cHP = enemy.cHP - round(enemy.dmgreduct*dmg*(1-((enemy.cDF)/(enemy.cDF+100))))
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\nHassan dunks on",enemy.NAME+", but deals no damage!")
        else:
          print("\nHassan dunks on",enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\nHassan dunks on",enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
        enemy.cHP = 1
      enemy.onhittimersdefense(self,0,dmg,"Physical Support") 
      enemy.currentstats(bots,you)

  def accuratestrike(self,enemy):
    global sett
    time.sleep(1)
    ALAC = 150 + round((100/240)*self.supportscale())
    ALAT = 18 + round((142/240)*self.supportscale())
    diff = enemy.cEV - ALAC
    if random.randint(1,100) <= diff:
      print("\nAlvaro tries to accuretly strikes",enemy.NAME,"but still misses!")
      enemy.specialdodgecases(self,0,"Physical Support")
    else:
      sett = enemy.cHP
      dmg = ALAT
      enemy.cHP = enemy.cHP - round(enemy.dmgreduct*dmg*(1-((enemy.cDF)/(enemy.cDF+100))))
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\nAlvaro accurately strikes",enemy.NAME+", but deals no damage!")
        else:
          print("\nAlvaro accurately strikes",enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\nAlvaro accurately strikes",enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
        enemy.cHP = 1
      enemy.onhittimersdefense(self,0,dmg,"Physical Support")
      enemy.currentstats(bots,you)

  def cripple(self,enemy):
    global sett
    time.sleep(1)
    OCAT = 22 + round((138/240)*self.supportscale())
    diff = enemy.cEV - 110
    if random.randint(1,100) <= diff:
      print("\nOctavio tries to cripple",enemy.NAME,"but fails!")
      enemy.specialdodgecases(self,0,"Physical Support")
    else:
      sett = enemy.cHP
      dmg = OCAT
      enemy.cHP = enemy.cHP - round(enemy.dmgreduct*dmg*(1-((enemy.cDF)/(enemy.cDF+100))))
      if enemy.bleedt < 2:
        enemy.bleedt = 2
      enemy.bleedd = enemy.bleedd + (10 + round((70/240)*self.supportscale()))
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\nOctavio cripples",enemy.NAME+", dealing no damage but causing them to bleed!")
        else:
          print("\nOctavio cripples",enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage and causing them to bleed!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\nOctavio cripples",enemy.NAME + ", dealing",fore.ORANGE_1  + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
        enemy.cHP = 1
      enemy.onhittimersdefense(self,0,dmg,"Physical Support")
      enemy.currentstats(bots,you)

  def snacks(self):
    time.sleep(1)
    bruh = random.randint(1,3)
    sett = self.cHP
    time.sleep(1)
    if bruh == 1:
      print("\nShannae gives",self.NAME,"a daisy cookie to eat!")
      self.cHP = self.cHP + 22
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if self.food[0] > 5:
        self.food[0] = 5
      self.food[2] = self.food[2] + 9 
      time.sleep(0.5)
      print("\n"+self.NAME,"eats a daisy cookie, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and inreasing their physical defense!",self.NAME,"has",self.cHP,"health now!")
    elif bruh == 2:
      print("\nShannae gives",self.NAME,"a cereal bar to eat!")
      self.cHP = self.cHP + 20
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if self.food[0] > 3:
        self.food[0] = 3
      self.food[2] = self.food[2] + 4
      self.food[4] = self.food[4] + 4
      time.sleep(0.5)
      print("\n"+self.NAME,"eats a cereal bar, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and slightly inreasing their physical and magical defense!",self.NAME,"has",self.cHP,"health now!")
    elif bruh == 3:
      print("\nShannae gives",self.NAME,"a cupcake to eat!")      
      self.cHP = self.cHP + 14
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if self.food[0] > 3:
        self.food[0] = 3
      self.food[4] = self.food[4] + 9
      time.sleep(0.5)
      print("\n"+self.NAME,"eats a cupcake, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and inreasing their magical defense!",self.NAME,"has",self.cHP,"health now!")
    self.currentstats(you,bots)

  def insult(self,enemy):
    global sett
    time.sleep(1)
    diff = enemy.cEV - 100
    if random.randint(1,100) <= diff:
      print("\nAndrew vulgarly curses out",enemy.NAME,"poisoning them!")
    else:
      print("\nAndrew vulgarly curses out",enemy.NAME,"but they remain unphased!")
      if enemy.poisont < 2:
        enemy.poisont = 2
      enemy.poisond = enemy.poisond + (20 + round((180/240)*self.supportscale()))
      enemy.currentstats(bots,you)

  def strangle(self,enemy):
    global sett
    time.sleep(1)
    DYAT = 30 + round((170/240)*self.supportscale())
    diff = enemy.cEV - 100
    if random.randint(1,100) <= diff:
      print("\nDylan tries to grapple",enemy.NAME,"but fails!")
      enemy.specialdodgecases(self,0,"Physical Support")
    else:
      sett = enemy.cHP
      dmg = DYAT + (0.0125*enemy.cHP)
      enemy.cHP = enemy.cHP - round(enemy.dmgreduct*dmg*(1-((enemy.cDF)/(enemy.cDF+100))))
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\nDylan grapples",enemy.NAME,"and strangles them, but deals no damage!")
        else:
          print("\nDylan grapples",enemy.NAME,"and strangles them, dealing",fore.ORANGE_1  + str(sett-enemy.cHP) + style.RESET,"damage",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\nDylan grapples",enemy.NAME,"and strangles them, dealing",fore.ORANGE_1  + str(sett-enemy.cHP) + style.RESET,"damage",enemy.NAME,"is at critical health!")
        enemy.cHP = 1
      enemy.onhittimersdefense(self,0,dmg,"Physical Support")
      enemy.currentstats(bots,you)

  def headbutt(self,enemy):
    global sett
    time.sleep(1)
    JAAT = 25 + round((275/240)*self.supportscale())
    JACT = 30 + round((20/240)*self.supportscale())
    diff = enemy.cEV - 80
    CT = random.randint(1,100)
    if random.randint(1,100) <= diff:
      print("\nJahir bullcharges",enemy.NAME,"but misses!")
      enemy.specialdodgecases(self,0,"Physical Support")
    else:
      sett = enemy.cHP
      dmg = JAAT
      enemy.cHP = enemy.cHP - round(enemy.dmgreduct*dmg*(1-((enemy.cDF)/(enemy.cDF+100))))
      if CT <= JACT:
        enemy.confused = 1
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\nJahir bullcharges",enemy.NAME+", concussing them but dealing no damage!")
          else:
            print("\nJahir bullcharges",enemy.NAME+", concussing them and dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\nJahir bullcharges",enemy.NAME+", concussing them and dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage",enemy.NAME,"is at critical health!")
          enemy.cHP = 1
      else:
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\nJahir bullcharges",enemy.NAME+", but deals no damage!")
          else:
            print("\nJahir bullcharges",enemy.NAME+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\nJahir bullcharges",enemy.NAME+", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage",enemy.NAME,"is at critical health!")
          enemy.cHP = 1
      enemy.onhittimersdefense(self,0,dmg,"Physical Support")
      enemy.currentstats(bots,you)

  def godandanime(self,ally):
    global sett
    time.sleep(1)
    if len(ally.team) == 1:
      if self.NAME == "Lascelles":
        print("\nLascelles calls upon the power of god and anime to support himself in battle!")
      else: 
        print("\nLascelles calls upon the power of god and anime to support",self.NAME,"in battle!")
      sett = self.cHP
      self.cHP = self.cHP + round(self.fHP*(0.25+((0.25/240)*self.supportscale())))
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      msett = self.cMP
      self.cMP = self.cMP + round(self.fMP*(0.15+((0.15/240)*self.supportscale())))
      if self.cMP > self.fMP:
        self.cMP = self.fMP
      time.sleep(0.5)
      if self.NAME == "Lascelles":
        print("\n"+self.NAME,"receives blessings and empowerment, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and",fore.MEDIUM_SPRING_GREEN+str(self.cMP-msett)+style.RESET,"mana!")
      else:
        print("\n"+self.NAME,"receives Lacelles's blessings and empowerment, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health and",fore.MEDIUM_SPRING_GREEN+str(self.cMP-msett)+style.RESET,"mana!")
    else:
      print("\nLascelles calls upon the power of god and anime to support his allies in battle!")
      hps = []
      for x in ally.team:
        hps.append(x.cHP/x.fHP)
      hps.sort()
      time.sleep(0.5)
      for x in ally.team:  
        if (x.cHP/x.fHP) == hps[0]:
          sett = x.cHP
          x.cHP = x.cHP + round(x.fHP*(0.25+((0.25/240)*self.supportscale())))
          if x.cHP > x.fHP:
            x.cHP = x.fHP
          if x.NAME == "Lascelles":
            print("\n"+x.NAME,"receives blessings, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health!")
          else:
            print("\n"+x.NAME,"receives Lacelles's blessings, recovering",fore.MEDIUM_SPRING_GREEN+str(x.cHP-sett)+style.RESET,"health!")
        if (x.cHP/x.fHP) == hps[len(ally.team)-1]:
          msett = x.cMP
          x.cMP = x.cMP + round(x.fMP*(0.15+((0.15/240)*self.supportscale())))
          if x.cMP > x.fMP:
            x.cMP = x.fMP
          if x.NAME == "Lascelles":
            print("\n"+x.NAME,"receives empowerment, recovering",fore.MEDIUM_SPRING_GREEN+str(self.cHP-sett)+style.RESET,"health!")
          else:
            print("\n"+x.NAME,"receives Lacelles's empowerment, recovering",fore.MEDIUM_SPRING_GREEN+str(x.cMP-msett)+style.RESET,"mana!")

  def orangejustice(self,enemy):
    time.sleep(1)
    lasAC = 100 + round((40/240)*self.supportscale())
    diff = enemy.cEV - lasAC
    if random.randint(1,100) <= diff:
      print("\nLascelles does the orange justice on",enemy.NAME+"! They ignore him.")
    else:
      print("\nLascelles does the orange justice on",enemy.NAME+"! They feel challenged and begin to dance on him as well!")
      enemy.dance = 1

  def eagle(self):
    time.sleep(1)
    if self.NAME == "Matvey":
      print("\nMatvey goes eagle-eye mode, increasing their accuracy and critical chance for 4 turns!")
    else:
      print("\nMatvey grants his eagle-eye to",self.NAME+", increasing their accuracy and critical chance for 4 turns!")
    self.eag = 4
    self.currentstats(you,bots)

  def stayshut(self,enemy):
    time.sleep(1)
    kenAC = 70 + round((30/240)*self.supportscale())
    diff = enemy.cEV - kenAC
    if random.randint(1,100) <= diff:
      print("\nKenny tells",enemy.NAME,"to stay shut, but they don't!")
    else:
      print("\nKenny tells",enemy.NAME,"to stay shut, silencing them for 2 turns!")
      enemy.silenced = 2

  def awkwardtouch(self,enemy):
    time.sleep(1)
    derAC = 150 + round((100/240)*self.supportscale())
    diff = enemy.cEV - derAC
    if random.randint(1,100) <= diff:
      print("\nDereck tries to caresses",enemy.NAME+", but awkwardly fails!")
    else:
      print("\nDereck awkwardly caresses",enemy.NAME+", lowering their accuracy for 3 turns!")
      enemy.caressed = 4
      enemy.currentstats(bots,you)
    
  def target(self,types,location,locationS,al="",en=""):
    global bad 
    bad = False
    wop = 0
    inviscount = 0
    for x in location:
      if x.invis > 0 and x.revealed <=0:
        inviscount = inviscount + 1
    if types == self.check:
      fw = input(fore.GREY_100 + "Check who's stats? " + style.RESET)
    elif types == self.mimic:
      fw = input(fore.GREY_100 + "Mimic who? ") 
    elif self in location or types == self.revive:
      fw = input(fore.GREY_100 + "Use on who? " + style.RESET) 
    else:
      fw = input(fore.GREY_100 + "Attack who? ") 
    if len(self.duel) > 0 and fw != "" and (self not in location and self.duel[1] in location) and (types != self.check or types != self.mimic):
      if al != "" and en != "":
        types(self.duel[1],al,en)
      elif al == "" and en != "":
        types(self.duel[1],en)
      elif al != "" and en == "":
        types(self.duel[1],al)
      elif al == "" and en == "":
        types(self.duel[1])
      wop = 1
    elif self.tauntt > 0 and fw != "" and (self not in location and self.taunted[1] in location) and (types != self.check or types != self.mimic):
      if al != "" and en != "":
        types(self.taunted[1],al,en)
      elif al == "" and en != "":
        types(self.taunted[1],en)
      elif al != "" and en == "":
        types(self.taunted[1],al)
      elif al == "" and en == "":
        types(self.taunted[1])
      wop = 1
    else:
      if fw.isdigit() == True and fw != "0":
        if (len(location)-inviscount) >= int(fw):
          if locationS == you.deadteamS:
            for x in location:
              if x.NAME in locationS[(int(fw)-1)] and (x.invis <=0 or x.revealed > 0):
                if len(x.duel) > 0 and (self not in location and x in location) and (types != self.check  and types != self.mimic):
                  print("\n"+x.NAME,"is dueling!")
                else:
                  if al != "" and en != "":
                    types(x,al,en)
                  elif al == "" and en != "":
                    types(x,en)
                  elif al != "" and en == "":
                    types(x,al)
                  elif al == "" and en == "":
                    types(x)
                  wop = 1
          else:
            for x in location:
              if x.ID == locationS[(int(fw)-1)] and (x.invis <=0 or x.revealed > 0):
                if len(x.duel) > 0 and (self not in location and x in location) and (types != self.check  and types != self.mimic):
                  print("\n"+x.NAME,"is dueling!")
                else:
                  if al != "" and en != "":
                    types(x,al,en)
                  elif al == "" and en != "":
                    types(x,en)
                  elif al != "" and en == "":
                    types(x,al)
                  elif al == "" and en == "":
                    types(x)
                  wop = 1
      for x in location:
        if fw.lower() == x.NAME.lower() and (x.invis <=0 or x.revealed > 0):
          if len(x.duel) > 0 and (self not in location and x in location) and (types != self.check and types != self.mimic):
            print("\n"+x.NAME,"is dueling!")
          else:
            if al != "" and en != "":
              types(x,al,en)
            elif al == "" and en != "":
              types(x,en)
            elif al != "" and en == "":
              types(x,al)
            elif al == "" and en == "":
              types(x)
            wop = 1
            break
    if wop != 1:
      bad = True

  def counter(self,enemy,CT=""):
    selfsett = enemy.cHP
    redat = ((.48+(0.03*self.counte))*enemy.cAT)+self.cMAT
    if random.randint(1,100) <= (30+(5*enemy.counte)): 
      response = "a"             
      c = "b"                    
      score = 0     
      start = time.time()        
      elapsed = 0 
      count = 0               
      while elapsed < 4:          
        c = random.choice(enemy.counterstrings)
        print(back.RED_1 + fore.GREY_100 + "\n!!!"+style.RESET,c,back.RED_1+fore.GREY_100+"!!!"+style.RESET)
        response = input(fore.GREY_100 + "\nType the word above quickly to counter: " + style.RESET)
        elapsed = time.time() - start
        count = count + 1
        if response.lower() == c.lower() and elapsed <4:      
          score = score + 1
        if count == 1:
          break
      time.sleep(1)
      if score == 0:
        print("\n"+self.NAME, "fails to counter",enemy.NAME +"!")
        time.sleep(0.5)
      else:
        enemy.cAT = (1-(.48+(0.03*self.counte)))*enemy.cAT
        enemy.cMAT = (1-(.48+(0.03*self.counte)))*enemy.cMAT
        if CT != "":
          if CT <= enemy.cCT:
            if enemy.cDF <=0:
              enemy.cHP = enemy.cHP - round(enemy.CTdmg*redat*enemy.dmgreduct)
            elif enemy.cDF > 0:
              enemy.cHP = enemy.cHP - round(enemy.dmgreduct*enemy.CTdmg*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
            if enemy.cHP > 0:            
              print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              enemy.cHP = 1
              print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"is at critical health!")
          else:
            if enemy.cDF <=0:
              enemy.cHP = enemy.cHP - round(redat*enemy.dmgreduct)
            elif enemy.cDF > 0:
              enemy.cHP = enemy.cHP - round(enemy.dmgreduct*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
            if enemy.cHP >0:            
              print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1  + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            else:
              enemy.cHP = 1
              print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
        else:
          if enemy.cDF <=0:
            enemy.cHP = enemy.cHP - round(redat*enemy.dmgreduct)
          elif enemy.cDF > 0:
            enemy.cHP = enemy.cHP - round(enemy.dmgreduct*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
          if enemy.cHP >0:            
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1  + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            enemy.cHP = 1
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
        time.sleep(0.5)
          

        


  def wildinstinct(self):
    if self.WI == False:
      time.sleep(1)
      print("\n"+self.NAME, "taps into",self.GEN[0],"wild instincts, increasing",self.GEN[0],"attack, speed, evasion, and critical chance, but reducing",self.GEN[0],"magic attack, magic defense, and accuracy!",self.GEN[0].capitalize(),"body starts to damage itself!")
      self.WI = True 
    elif self.WI == True:
      time.sleep(1)
      print("\n"+self.NAME, "reverts back to",self.GEN[0],"normal state!")
      self.WI = False
  
  def smash(self,enemy,ally,targ):  #b 1 
    global sett
    self.cMP = self.cMP - 40
    self.prehiteffects(enemy)
    a1 = ""
    a2 = ""
    a3 = ""
    APN = self.cAPN
    count = 0
    time.sleep(1)
    print("\n"+self.NAME+": Boutta mack yo' ass right now.")
    time.sleep(1) 
    print("\nUse WASD to perform different punches!")   
    for x in range(3):
      good = 0
      while good == 0:
        char = getch()
        if char.lower() == "w":
          self.cCT = round(self.cCT + (10+(2.5*self.sma)))
          good = 1
        elif char.lower() == "a":
          self.cAT = round(self.cAT * (1.1+(0.025*self.sma)))
          good = 1
        elif char.lower() == "s":
          APN = round(APN * (1.2+(0.1*self.sma)))
          good = 1
        elif char.lower() == "d":
          self.fAC = round(self.cAC * (1.1+(0.05*self.sma)))
          good = 1
        else:
          print("\nEnter a valid key!")
          continue
      count = count + 1
      if count == 1:
        a1 = char.lower()
      if count == 2:
        a2 = char.lower()
      if count == 3:
        a3 = char.lower()
      self.cAPN = APN
      diff = enemy.cEV - self.cAC
      CT = random.randint(1,100)
      if random.randint(1,100) <= diff:
        print("\n"+self.NAME, "tries to smash",enemy.NAME + ", but they dodge!")
        enemy.specialdodgecases(self,0,"Physical Melee",CT)
      else:
        sett = enemy.cHP
        if enemy.coun == True:
          enemy.counter(self,CT) 
        if CT <= self.cCT:
          dmg = self.cAT*self.CTdmg
          enemy.defense(self,"Physical",dmg)
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"violently smashes",enemy.NAME + ", but deals no damage!")
            else:
              print("\n"+self.NAME,"violently smashes",enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME,"violently smashes",enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        else:
          dmg = 0.9*self.cAT
          enemy.defense(self,"Physical",dmg)
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"smashes",enemy.NAME + ", but deals no damage!")
            else:
              print("\n"+self.NAME,"smashes",enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME,"smashes",enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0,dmg,"Physical Melee") 
    if (a1 == "a" and a2 == "a" and a3 == "a") or (a1 == "d" and a2 == "d" and a3 == "d"):
      time.sleep(0.5)
      print("\n"+self.NAME,"spins around, attacking everyone!")
      for x in targ.team:
        time.sleep(0.15)
        self.prehiteffects(x)
        sett = x.cHP
        diff = x.cEV - self.cAC 
        if random.randint(1,100) <= diff:
          print("\n"+x.NAME,"dodges the attack!")
          x.specialdodgecases(self,0.0,"Physical Ranged")
        else:
          dmg = self.cAT
          x.defense(self,"Physical",dmg)
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n"+x.NAME,"is hit, but takes no damage!")
            else:
              print("\n"+x.NAME,"is hit, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.NAME,"is hit, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0,dmg,"Physical Ranged") 
    elif (a2 == "w" and a3 == "s"):
      time.sleep(0.5)
      diff = enemy.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n"+self.NAME, "tries to grab",enemy.NAME + ", but they dodge!")
        enemy.specialdodgecases(self,0,"Physical Melee")
      else:
        sett = enemy.cHP
        if enemy.coun == True:
          enemy.counter(self) 
        dmg = 1.2*self.cAT
        enemy.defense(self,"Physical",dmg)
        enemy.tremstun = 1
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME,"slams",enemy.NAME,"into the ground, but deals no damage!")
          else:
            print("\n"+self.NAME,"slams",enemy.NAME,"into the ground, dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME,"slams",enemy.NAME,"into the ground, dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.5,dmg,"Physical Ranged")        
          
  def valorouschant(self,ally,targ):
    self.cMP = self.cMP - 60
    for x in targ.team:
      x.fear = 4
    if len(ally.team) > 1:
      self.valos = True
      for x in ally.team:
        x.valor = 5
      time.sleep(0.5)
      if len(ally.team) == 2:
        print("\n"+self.NAME,"rallies up the team, increasing everyone's physical attack and intimidating all enemies!")
      elif len(ally.team) == 3:
        print("\n"+self.NAME,"rallies up the team, increasing everyone's physical attack, defense, and intimidating all enemies!")
      elif len(ally.team) == 4: 
        print("\n"+self.NAME,"rallies up the team, increasing everyone's physical attack, defense, speed, and intimidating all enemies!")
    else:
      print("\n"+self.NAME,"shouts at the enemies, causing them fear through intimidation!")
       

  def immortality(self): 
    self.cMP = self.cMP - 80
    self.immortal = 4
    time.sleep(1)
    print("\n"+self.NAME, "becomes hellbent, refusing to die for the next 3 turns!")
    
  def barrier(self,ally):   
    self.cMP = self.cMP - 50
    ally.pbarrier = 1 + self.barr
    time.sleep(1)
    if ally.NAME == self.NAME:
      print("\n"+self.NAME,"casts a barrier on",self.GEN[1]+"self, guarding",self.GEN[1],"from physical damage for",ally.pbarrier,"hits!")
    else:
      print("\n"+self.NAME,"casts a barrier on",ally.NAME + ", guarding them from physical damage for",ally.pbarrier,"hits!")

  def fromtheshadows(self,ally,targ): #b
    global sett
    global seq
    global bad
    if self.invis == 0 and self.instant == False:
      if self.revealed <= 0:
        ally.teamS.remove(self.NAME)
        ally.teamID.remove(self.ID)
      self.invis = 4
      self.cMP = self.cMP - 75
      time.sleep(1)
      print("\n"+self.NAME, "goes invisible...")
    else:
      seq = 0
      while seq == 0:
        if self.instant == True:
          time.sleep(1)
          print(style.BOLD + "\n"+self.NAME, "appears from the shadows!" + style.RESET)
          time.sleep(1) 
          bruh = []
          for x in targ.team:
            if (x.invis <=0 or x.revealed > 0):
              bruh.append(x)
          for x in bruh:
            if len(x.duel) > 0 and self not in x.duel:
              bruh.remove(x)
          response = "a"              
          c = "b"                          
          count = 0
          start = time.time()         
          elapsed = 0
          print(fore.GREY_100 + "\nType the letters or numbers displayed!" + style.RESET)  
          while elapsed < 1.25:           
            c = random.choice(string.ascii_uppercase + string.digits)
            print("\n",fore.YELLOW_1+c+style.RESET)                 
            char = getch()
            elapsed = time.time() - start 
            count = count + 1
            if char.lower() == c.lower() and elapsed <1.25:       
              elapsed = 0
              start = time.time() 
              cut = random.choice(bruh)
              if len(self.duel) > 0:
                if self.duel[1].cHP > 0:
                  cut = self.duel[1]
              elif len(self.taunted) > 0:
                if self.taunted[1].cHP > 0:
                  cut = self.taunted[1]
              self.prehiteffects(cut)
              diff = cut.cEV - self.cAC
              CT = random.randint(1,100)
              if random.randint(1,100) <= diff:
                print("\n"+self.NAME, "slashes",cut.NAME + ", but they dodge!")
                cut.specialdodgecases(self,0,"Physical Melee",CT)
              else:
                sett = cut.cHP
                if cut.coun == True:
                  cut.counter(self,CT) 
                if CT <= self.cCT:
                  dmg = (self.CTdmg*(0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT)
                  cut.defense(self,"Physical",dmg)
                  if cut.cHP > 0:
                    if (sett-cut.cHP) == 0:
                      print("\n"+self.NAME,"critically slashes",cut.NAME + ", but deals no damage!")
                    else:
                      print("\n"+self.NAME,"critically slashes",cut.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"has",cut.cHP,"health remaining!")
                  else:
                    print("\n"+self.NAME,"critically slashes",cut.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"falls...")
                  cut.onhittimersdefense(self,0,dmg,"Physical Melee") 
                  if cut.cHP <= 0:
                    bruh.remove(cut)
                  else:
                    cut.currentstats(targ,ally)
                else:
                  dmg = ((0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT)
                  cut.defense(self,"Physical",dmg)
                  if cut.cHP > 0:
                    if (sett-cut.cHP) == 0:
                      print("\n"+self.NAME,"slashes",cut.NAME + ", but deals no damage!")
                    else:
                      print("\n"+self.NAME,"slashes",cut.NAME + ", dealing",fore.ORANGE_1 + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"has",cut.cHP,"health remaining!")
                  else:
                    print("\n"+self.NAME,"slashes",cut.NAME + ", dealing",fore.ORANGE_1 + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"falls...")
                  cut.onhittimersdefense(self,0,dmg,"Physical Melee")
                  if cut.cHP <= 0:
                    bruh.remove(cut)
                  else:
                    cut.currentstats(targ,ally)
                self.onhittimersoffense(cut,0,"Physical Melee") 
            else:
              time.sleep(1)
              print("\n"+self.NAME, "fails to slash!")
              self.invis = 0
              ally.teamS.append(self.NAME)
              ally.teamID.append(self.ID)
              seq = 1
              break
            if count == 6 or len(bruh) == 0:
              time.sleep(1)
              print("\n"+self.NAME, "successfully cuts through the enemies!")
              self.invis = 0
              ally.teamS.append(self.NAME)
              ally.teamID.append(self.ID)
              seq = 1
              break
          self.instant = False
        else:
          if self.revealed <= 0 and self in ally.teamS:
            ally.teamS.remove(self.NAME)
            ally.teamID.remove(self.ID)
          print(back.GREY_100 + fore.BLACK + style.BOLD+"\nIt's",self.NAME+"'s turn." + style.RESET)
          fight = input(fore.GREY_100 + style.BOLD+"Flashcut, Items, Recover, or Check? " + style.RESET)
          if fight == "1" or fight.lower() == "flashcut":
            time.sleep(1)
            print(style.BOLD + "\n"+self.NAME, "appears from the shadows!" + style.RESET)
            time.sleep(1)
            bruh = []
            for x in targ.team:
              if (x.invis <=0 or x.revealed > 0):
                bruh.append(x)
            for x in bruh:
              if len(x.duel) > 0 and self not in x.duel:
                bruh.remove(x)
            response = "a"              
            c = "b"                          
            count = 0
            start = time.time()         
            elapsed = 0                 
            print(fore.GREY_100 + "\nType the letters or numbers displayed!" + style.RESET)  
            while elapsed < 1.25:           
              c = random.choice(string.ascii_uppercase + string.digits)
              print("\n",fore.YELLOW_1+c+style.RESET)                
              char = getch()
              elapsed = time.time() - start 
              count = count + 1
              if char.lower() == c.lower() and elapsed <1.25:      
                elapsed = 0
                start = time.time() 
                cut = random.choice(bruh)
                if len(self.duel) > 0:
                  if self.duel[1].cHP > 0:
                    cut = self.duel[1]
                elif len(self.taunted) > 0:
                  if self.taunted[1].cHP > 0:
                    cut = self.taunted[1]
                self.prehiteffects(cut)
                diff = cut.cEV - self.cAC
                CT = random.randint(1,100)
                if random.randint(1,100) <= diff:
                  print("\n"+self.NAME, "slashes",cut.NAME +", but they dodge!")
                  cut.specialdodgecases(self,0,"Physical Melee",CT)
                else:
                  sett = cut.cHP
                  if cut.coun == True:
                    cut.counter(self,CT) 
                  if CT <= self.cCT:
                    dmg = (self.CTdmg*(0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT)
                    cut.defense(self,"Physical",dmg)
                    if cut.cHP > 0:
                      if (sett-cut.cHP) == 0:
                        print("\n"+self.NAME,"critically slashes",cut.NAME + ", but deals no damage!")
                      else:
                        print("\n"+self.NAME,"critically slashes",cut.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"has",cut.cHP,"health remaining!")
                    else:
                      print("\n"+self.NAME,"critically slashes",cut.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"falls...")
                    cut.onhittimersdefense(self,0,dmg,"Physical Melee")
                    if cut.cHP <= 0:
                      bruh.remove(cut)
                    else:
                      cut.currentstats(targ,ally)
                  else:
                    dmg = ((0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT)
                    cut.defense(self,"Physical",dmg)
                    if cut.cHP > 0:
                      if (sett-cut.cHP) == 0:
                        print("\n"+self.NAME,"slashes",cut.NAME + ", but deals no damage!")
                      else:
                        print("\n"+self.NAME,"slashes",cut.NAME + ", dealing",fore.ORANGE_1 + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"has",cut.cHP,"health remaining!")
                    else:
                      print("\n"+self.NAME,"slashes",cut.NAME + ", dealing",fore.ORANGE_1 + str(sett-cut.cHP) + style.RESET,"damage!",cut.NAME,"falls...")
                    cut.onhittimersdefense(self,0,dmg,"Physical Melee")
                    if cut.cHP <= 0:
                      bruh.remove(cut)
                    else:
                      cut.currentstats(targ,ally)
                  self.onhittimersoffense(cut,0,"Physical Melee")
              else:
                time.sleep(1)
                print("\n"+self.NAME,"fails to slash!")
                self.invis = 0
                ally.teamS.append(self.NAME)
                ally.teamID.append(self.ID)
                seq = 1
                break
              if count == 6 or len(bruh) == 0:
                time.sleep(1)
                print("\n"+self.NAME, "successfully cuts through the enemies!")
                self.invis = 0
                ally.teamS.append(self.NAME)
                ally.teamID.append(self.ID)
                seq = 1
                break
          elif fight == "2" or fight.lower() == "items":
            bad = False
            self.inventorysystem(ally,targ)
            if bad == True:
              continue
            seq = 1
          elif fight == "3" or fight.lower() == "recover":
            buttsss = self.cMP
            time.sleep(1)
            self.cMP = self.cMP + (2*self.cMRG)
            if self.cMP > self.fMP:
              self.cMP = self.fMP 
            print("\n" + self.NAME, "relaxes to recover their inner strength, recovering",(self.cMP-buttsss),"mana!",self.NAME,"now has",self.cMP,"mana!")
            seq = 1
          elif fight == "4" or fight.lower() == "check":
            pepe = input("\nAllies or Enemies? ")
            if pepe == "1" or pepe.lower() == "allies":
              print("")
              print(ally.teamS)  
              self.target(self.check,ally.team,ally.teamS)
            elif pepe == "2" or pepe.lower() == "enemies":
              print("")
              print(targ.teamS)
              self.target(self.check,targ.team,targ.teamID)
            continue
          

  def enrage(self):
    time.sleep(1)
    self.enragev = 1 + (1-(self.cHP/self.fHP))
    print("\n"+self.NAME, "enrages appropriately to his current injuries, changing his attack and speed!")


  def calligraphy(self,enemy):  
    global sett
    self.cMP = self.cMP - 20
    self.isopoints = self.isopoints + 60
    self.prehiteffects(enemy) 
    time.sleep(1) 
    spac = round((2+(0.5*self.callig))*self.cAC)
    diff = enemy.cEV - spac
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "takes out",self.GEN[0],"magic pen and summons the power of",self.GEN[0],"calligraphy! It strides towards",enemy.NAME + ", but misses!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      sett = enemy.cHP
      if random.randint(1,100) <=self.cCT:
        dmg = self.CTdmg*self.cMAT*(1+(self.callig*0.25))
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME, "takes out",self.GEN[0],"magic pen and draws the power of",self.GEN[0],"calligraphy! It strides towards",enemy.NAME +", but deals no damage!")
          else:
            print("\n"+self.NAME, "takes out",self.GEN[0],"magic pen and draws the power of",self.GEN[0],"calligraphy! It strides towards",enemy.NAME,"dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "takes out",self.GEN[0],"magic pen and draws the power of",self.GEN[0],"calligraphy! It strides towards",enemy.NAME,"dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"falls...")
      else:
        dmg = self.cMAT*(1+(self.callig*0.25))
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME, "takes out",self.GEN[0],"magic pen and draws the power of",self.GEN[0],"calligraphy! It strides towards",enemy.NAME +", but deals no damage!")
          else:
            print("\n"+self.NAME, "takes out",self.GEN[0],"magic pen and draws the power of",self.GEN[0],"calligraphy! It strides towards",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "takes out",self.GEN[0],"magic pen and draws the power of",self.GEN[0],"calligraphy! It strides towards",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
        
  def asmr(self,ally):   #a
    global sett 
    time.sleep(1)
    sett = self.cHP
    self.cHP = self.cHP - round(0.2*self.fHP)
    self.cMP = self.cMP + (30+(5*self.asm))
    if self.cMP > self.fMP:
      self.cMP = self.fMP
    for x in ally.team:
      x.manaflow = [5,self]
    if len(ally.team) == 1:
      print("\n"+self.NAME,"performs ASMR, recovering",(30+(5*self.asm)),"mana at the cost of",(sett-self.cHP),"of",self.GEN[0],"health!",self.GEN[2].capitalize(),"reaches a state of flow, increasing",self.GEN[0],"mana regeneration drastically!")
    else:
      print("\n"+self.NAME, "performs ASMR for everyone, recovering",(30+(5*self.asm)),"mana at the cost of",(sett-self.cHP),"of",self.GEN[0],"health! Everyone reaches a state of flow, gaining drastically increased mana regeneration!")
    if self.cHP <=0:
      time.sleep(1)
      print("\n"+self.NAME,"dies due to exhaustion...")
    self.onhittimersdefense(self,0.5)
  
  def pinpoint(self,enemy): 
    global sett
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 10
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    CT = random.randint(1,100)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "pinpoints a vital target on the enemy and attempts to attack it, but misses!")
      enemy.specialdodgecases(self,0.5,"True Melee",CT)
    else:
      if enemy.coun == True:
        enemy.counter(self,CT)
      if enemy.bleedt < 1:
        enemy.bleedt = 1
      enemy.bleedd = enemy.bleedd + ((1 + (0.2*self.pinp))*self.cAC)
      sett = enemy.cHP
      tdmg = round((0.6+(0.1*self.pinp))*self.cAT)
      enemy.cHP = enemy.cHP - tdmg 
      if CT <=self.cCT:
        dmg = self.CTdmg*self.cAT
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          print("\n"+self.NAME, "pinpoints a vital target on the enemy and precisely attacks it, dealing",style.BOLD+str(sett-enemy.cHP)+style.RESET,"damage, and causing them to bleed heavily!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "pinpoints a vital target on the enemy and precisely attacks it, dealing",style.BOLD+str(sett-enemy.cHP)+style.RESET,"damage, and causing them to bleed heavily!",enemy.NAME,"falls...")
      else:
        dmg = self.cAT
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          print("\n"+self.NAME, "pinpoints a vital target on the enemy and attacks it, dealing",(sett-enemy.cHP),"damage, and causing them to bleed heavily!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "pinpoints a vital target on the enemy and attacks it, dealing",(sett-enemy.cHP),"damage, and causing them to bleed heavily!",enemy.NAME,"falls...")
      tot = tdmg + dmg
      enemy.onhittimersdefense(self,0.5,tot,"True Melee")
      
  def heal(self,ally):  
    global sett
    self.cMP = self.cMP - 60
    sett = ally.cHP
    ally.cHP = ally.cHP + round(ally.healmod*((0.1*ally.fHP)+((2+(0.125*self.bake))*self.cMAT)))
    if ally.cHP > ally.fHP:
      ally.cHP = ally.fHP
    time.sleep(0.5)
    if ally == self:
      print("\n"+self.NAME,"calls upon higher powers to heal",self.GEN[1]+"self for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett)+style.RESET,"health!",self.GEN[2].capitalize(),"has",ally.cHP,"health now!")
    else:
      print("\n"+self.NAME,"calls upon higher powers to heal",ally.NAME,"for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett)+style.RESET,"health!",ally.GEN[2].capitalize(),"has",ally.cHP,"health now!")

  def omniheal(self,ally): #a
    global sett
    self.cMP = self.cMP - 60
    time.sleep(0.5)
    print("\n"+self.NAME,"opens the gates of heaven, healing everyone on the team!\n")
    time.sleep(0.2)
    for x in ally.team:
      sett = x.cHP
      x.cHP = x.cHP + round(x.healmod*((0.1*x.fHP)+((2+(0.125*self.bake))*self.cMAT)))
      if x.cHP > x.fHP:
        x.cHP = x.fHP
      print(x.NAME,"heals for",fore.MEDIUM_SPRING_GREEN+ str(x.cHP-sett)+style.RESET,"health! They have",x.cHP," health now!")
      
  def perfectrequiem(self,enemy,al,targ):  
    global sett
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 100
    time.sleep(1)
    print("\n"+self.NAME,"takes out",self.GEN[0],'violin and breathes, "Perfect Requiem..."')
    time.sleep(1)
    response = "a"              
    c = "b"                     
    score = 0      
    count = 0
    start = time.time()         
    elapsed = 0     
    print(fore.GREY_100 + style.BOLD + "\nType the letters or numbers displayed!" + style.RESET)
    time.sleep(0.25)
    while elapsed < 9:           
      c = random.choice(string.ascii_uppercase + string.digits)
      print("\n",c)              
      char = getch() 
      elapsed = time.time() - start 
      count = count + 1
      if char.lower() == c.lower() and elapsed <9:       
        score = score + 1
      if count == 10:
        break
      if score == 10:
        break
    dod = score
    for x in range(dod):
      diff = enemy.cEV - self.cAC
      if random.randint(1,100) <= diff:
        score = score - 1
    totat = score*(0.3+(0.05*self.perfectr))
    blow = 5+(0.5*self.perfectr)
    sett = enemy.cHP
    time.sleep(1)
    if dod == 0:
      print("\n"+self.NAME,"misses all",self.GEN[0],"notes!")
    else:
      if score == 0:
        print("\n"+self.NAME, "plays through the battle, but",enemy.NAME,"dodges all the notes!")
        enemy.specialdodgecases(self,0.5,"Magical Ranged")
      else:
        dmg = totat*self.cMAT
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME, "plays through the battle, striking",self.GEN[0],"notes to hit",enemy.NAME,score,"times, but deals no damage!")  
          else:
            print("\n"+self.NAME, "plays through the battle, striking",self.GEN[0],"notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!") 
        else:
          print("\n"+self.NAME, "plays through the battle, striking",self.GEN[0],"notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
      CT = random.randint(1,100)
      if enemy.cHP >0 and dod == 10:
        enemy.currentstats(targ,al)
        diff = enemy.cEV - round(2*self.cAC)
        if random.randint(1,100) <= diff:
          print("\n"+self.NAME, "attempts to stun",self.GEN[0],"opponent, but fails!")
          enemy.specialdodgecases(self,0.5,"Magical Melee",CT)
        else:
          time.sleep(1)
          print("\n"+self.NAME, "achieves stunning",self.GEN[0],"opponent.")
          time.sleep(1)
          print(""+self.NAME+": The finale...")
          time.sleep(1)
          sett = enemy.cHP
          self.cMPN = round(self.cMPN*2)
          if enemy.coun == True:
            enemy.counter(self,CT) 
          if CT <= self.cCT:
            dmg = self.CTdmg*blow*self.cMAT
            enemy.defense(self,"Magical",dmg)
            if enemy.cHP > 0:
              if (sett-enemy.cHP) == 0:
                print("\n"+self.NAME, "delivers the ultimate final blow, but deals no damage!")
              else:
                print("\n"+self.NAME, "delivers the ultimate final blow, dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME, "has",enemy.cHP,"health remaining!")
            else:
              print("\n"+self.NAME, "delivers the ultimate final blow, dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"fades into specs of light...")   
          else:
            dmg = blow*self.cMAT
            enemy.defense(self,"Magical",dmg)
            if enemy.cHP > 0:
              if (sett-enemy.cHP) == 0:
                print("\n"+self.NAME, "delivers the final blow, but deals no damage!")
              else:
                print("\n"+self.NAME, "delivers the final blow, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME, "has",enemy.cHP,"health remaining!")
            else:
              print("\n"+self.NAME, "delivers the final blow, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")   
          enemy.onhittimersdefense(self,0.5,dmg,"Magical Melee")            

  def revive(self,ally,a):  #a
    self.cMP = self.cMP - 100
    if len(a.team) < 4:
      a.team.append(ally)
      a.teamS.append(ally.NAME)
      a.teamID.append(ally.ID)
    else:
      a.backteam.append(ally)
      a.backteamS.append(ally.NAME)
    a.deadteam.remove(ally)
    a.deadteamS.remove(ally.NAME)
    ally.deturn = 0
    ally.cHP = round(((0.3+(self.rev*0.05))*ally.fHP))
    if ally.re == True:
      ally.resttimer = 26 - (ally.res)
    time.sleep(1)
    print(back.GREY_100 + fore.BLACK + style.BOLD+"\n"+self.NAME,"revives",ally.NAME+"!" + style.RESET)

  def runnershigh(self):
    self.cMP = self.cMP - 25
    self.runhigh = 26
    time.sleep(1)
    print("\n" + self.NAME, "enters the runner's high, removing and becoming immune to slows and increasing",self.GEN[0],"attack and defense!")

  def shield(self):
    time.sleep(1)
    sett = self.cHP
    self.cHP = self.cHP + round(self.healmod*(0.1+(0.01*self.shi))*self.fHP)
    self.SHIE = True
    if self.cHP > self.fHP:
      self.cHP = self.fHP
    print("\n" + self.NAME,"shields",self.GEN[1]+"self, healing for",fore.MEDIUM_SPRING_GREEN+ str(self.cHP-sett) + style.RESET,"health, and gaining damage reduction!",self.GEN[2].capitalize(),"has",self.cHP,"health now!")

  def tremors(self,targ):
    global sett
    self.tstun = 50 + (5*self.trem)
    self.cMP = self.cMP - 55
    time.sleep(1)
    print("\n" + self.NAME, "sends tremors through the ground!\n")
    time.sleep(0.5)
    for x in targ.team:
      self.prehiteffects(x)
      sett = x.cHP
      diff = x.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        print(x.NAME,"jumps off the ground before they can fall!")
        x.specialdodgecases(self,0.1,"Physical Ranged")
      else:
        dmg = (((0.7+(0.05*self.trem))*self.cAT)+((1.0+(0.2*self.trem))*self.cMAT))
        x.defense(self,"Physical",dmg)
        dmg1 = sett - x.cHP
        if random.randint(0,100) <= self.tstun:
          x.tremstun = 1
          if x.cHP > 0:
            if dmg1 == 0:
              print(x.NAME,"topples over, but takes no damage!")
            else:
              print(x.NAME,"topples over, taking",fore.ORANGE_1 + str(dmg1) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print(x.NAME,"topples over, taking",fore.ORANGE_1 + str(dmg1) + style.RESET,"damage!",x.NAME,"falls...")    
          x.onhittimersdefense(self,0.2,dmg,"Physical Ranged")
        else:
          x.tremsl = 2
          if x.cHP > 0:
            if dmg1 == 0:
              print(x.NAME,"trembles, but takes no damage!")
            else:
              print(x.NAME,"trembles, taking",fore.ORANGE_1 + str(dmg1) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print(x.NAME,"trembles, taking",fore.ORANGE_1 + str(dmg1) + style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Physical Ranged")
       
 
  def isometricdrawings(self,ally):
    self.cMP = self.cMP - 70
    ally.isoboost = 6
    ally.isoboostL = 1
    ally.isopoints = ally.isopoints + (100+(50*self.isom))
    if ally.isopoints > (100*ally.isoLevel):
      ally.isopoints = (100*ally.isoLevel)
    time.sleep(1)
    if ally == self:
      print("\n"+self.NAME,"sings the isometric drawings song, boosting the level of all",self.GEN[0],"skills by 1, and recovering",self.GEN[0],"ISO-points to",str(ally.isopoints)+"!")
    else:
      print("\n"+self.NAME, "sings the isometric drawings song, boosting the level of all of",ally.NAME+ "'s skills by 1, and recovering their ISO-points to",str(ally.isopoints)+"!")

  def setskills(self):
    self.counte = self.counte - 1
    self.res = self.res - 1 
    self.fal = self.fal - 1
    self.hate = self.hate - 1
    self.wild = self.wild - 1
    self.valo = self.valo - 1
    self.sma = self.sma - 1
    self.immort = self.immort - 1  
    self.barr = self.barr - 1
    self.fromthes = self.fromthes - 1  
    self.run = self.run - 1    
    self.shi = self.shi - 1
    self.trem = self.trem - 1
    self.isom = self.isom - 1
    self.comb = self.comb - 1
    self.callig = self.callig - 1
    self.asm = self.asm - 1
    self.pinp = self.pinp - 1
    self.bake = self.bake - 1
    self.perfectr = self.perfectr - 1
    self.rev = self.rev - 1
    self.grub = self.grub - 1
    self.taun = self.taun - 1
    self.knightv = self.knightv - 1
    self.obese = self.obese - 1
    self.jabb = self.jabb - 1
    self.electr = self.electr - 1
    self.silen = self.silen - 1
    self.cutm = self.cutm - 1
    self.gunb = self.gunb - 1
    self.infe = self.infe - 1
    self.spark = self.spark - 1
    self.dar = self.dar - 1
    self.da = self.da - 1
    self.que = self.que - 1
    self.auto = self.auto - 1
    self.chrono = self.chrono - 1
    self.proto = self.proto - 1
    self.rub = self.rub - 1
    self.progo = self.progo - 1
    self.armw = self.armw - 1
    self.selfd = self.selfd - 1
    self.chad = self.chad - 1
    self.infe = self.infe - 1
    self.las = self.las - 1
    self.engk = self.engk - 1
    self.dsw = self.dsw - 1
    self.weir = self.weir - 1
    self.rehe = self.rehe - 1
    self.powres = self.powres - 1
    self.lost = self.lost - 1
    self.ling = self.ling - 1
    self.grac = self.grac - 1
    self.radi = self.radi - 1
    self.whir = self.whir - 1
    self.etern = self.etern - 1
    self.nowo = self.nowo - 1
    self.emo = self.emo - 1
    self.outr = self.outr - 1
    self.arri = self.arri - 1
    self.recl = self.recl - 1
    self.onet = self.onet - 1
    self.suc = self.suc - 1
    self.mimi = self.mimi - 1
    self.telep = self.telep - 1
    self.desp = self.desp - 1
    self.powers = self.powers - 1
      
  def combo(self,ally,tea,targ):
    global sett
    global bad
    bad = False
    if ally == self:
      print("\n"+self.NAME,"cannot do this with ",self.GEN[1]+"self!")
      bad = True
    else:
      self.cMP = self.cMP - 100
      if ally.NAME == "Ishraq" or (self.NAME == "Ishraq" and ally.NAME == "Julius"):
        time.sleep(1)
        print("\n"+self.NAME+": Ishraq! Iso-Lock them with me! SPRINT!")
        time.sleep(1)
        print("\n"+self.NAME,"and Ishraq run around the enemies from opposite directions, making an Iso-Circle on the ground. The circle locks and shrinks down to the size of an atom, trapping all enemies and explodes!")
        self.cMPN = self.cMPN + ally.cMPN
        time.sleep(0.9)
        for x in targ.team:
          self.prehiteffects(x)
          time.sleep(0.1)
          diff = x.cEV - (self.cAC+ally.cAC)
          if random.randint(1,100) <= diff:
            print("\n"+x.NAME,"gets out of the circumference!")
            x.specialdodgecases(self,0.1,"Magical Ranged")
          else:
            sett = x.cHP
            dmg = (self.cAT + ally.cAT)*(2+(0.1*self.comb))
            x.defense(self,"Magical",dmg)
            if x.cHP > 0:
              if (sett-x.cHP) == 0:
                print("\n"+x.NAME,"takes no damage!")
              else:
                print("\n"+x.NAME,"takes",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaning!")
            else:
              print("\n"+x.NAME,"takes",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")       
            x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")   
      elif ally.NAME == "Kelly" or (self.NAME == "Kelly" and ally.NAME == "Julius"):
        time.sleep(1)
        combMAT = (self.cMAT + ally.cMAT)*(2+(0.2*self.comb))
        for x in tea.team:
          x.cHP = x.cHP + round(x.healmod*combMAT)
          if x.cHP > x.fHP:
            x.cHP = x.fHP
        print("\n"+self.NAME+": Kelly! Sing with me!")
        time.sleep(0.5)
        print("\n"+self.NAME,"and Kelly sing the isometric drawings song, healing everyone for",fore.MEDIUM_SPRING_GREEN+ str(round(combMAT)) + style.RESET,"health!\n")
        for x in tea.team:
          time.sleep(0.1)
          print(x.NAME,"has",x.cHP,"health now!")
      elif ally.NAME == "Daniel" or (self.NAME == "Daniel" and ally.NAME == "Julius"):
        time.sleep(1)
        combMAT = (self.cMAT + ally.cMAT)*(2+(0.1*self.comb))
        print("\n"+self.NAME+": Daniel! Summon the tides with me!")
        time.sleep(0.7)
        print("\n"+self.NAME,"and Daniel combine their abnormal chemical accumulation of hand grease to create a tide of grease which crashes down on all enemies, poisoining them and lowering their evasion!")
        for x in targ.team:
          if x.poisont < 3:
            x.poisont = 3
          x.greased = [3,self]
          x.poisond = x.poisond + round(combMAT)
      elif ally.NAME == "Arwyn" or (self.NAME == "Arwyn" and ally.NAME == "Julius"): #$
        time.sleep(1)
        print("\n"+self.NAME+": Arwyn! Dance with me!")
        combSP = ((self.SP*(1+(0.05*self.comb)))+ally.SP)
        time.sleep(0.7)
        print("\n"+self.NAME,"and Arwyn, the Best Dancer, dance with each other, increasing everyone's armor and magic penetration by",str(round(combSP))+"!")
        for x in tea.team:
          x.combd = [4,self,ally]
      elif (ally.NAME == "Tim" or ally.NAME == "Taco Lord") or ((self.NAME == "Tim" or self.NAME == "Taco Lord") and ally.NAME == "Julius"):
        print("")
        print(targ.teamS)
        self.target(self.timcomboattack,targ.team,targ.teamS,tea)
        if bad == True:
          self.cMP = self.cMP + 100
         
  def timcomboattack(self,enemy,tea):
    global sett
    self.prehiteffects(enemy)
    bro = 0
    for x in tea.team:
      if x.NAME == "Tim":
        bro = x
    diff = enemy.cEV - (self.cAC + bro.cAC)
    print("\n"+self.NAME+": Tim! Surround",enemy.NAME,"with the T-Pose!")
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME,"and Tim corner",enemy.NAME,"and T-Pose on them, but they ignore its call for dominance!")
      enemy.specialdodgecases(self,0.5,"Physical Ranged")
    else:
      sett = enemy.cHP
      self.cAPN = self.cAPN + bro.cAPN
      dmg = (self.cAT + bro.cAT + self.cMAT + bro.cMAT)*(3+(0.2*self.comb))
      enemy.defense(self,"Physical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME,"and Tim corner",enemy.NAME,"and T-Pose on them, but its dominating power doesn't phase them!")
        else:
          print("\n"+self.NAME,"and Tim corner",enemy.NAME,"and T-Pose on them, its dominating power dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+self.NAME,"and Tim corner",enemy.NAME,"and T-Pose on them, its dominating power dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")  
      enemy.onhittimersdefense(self,0.5,dmg,"Physical Ranged")

  def grubbyhands(self,enemy):
    self.cMP = self.cMP - 20
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n" + self.NAME, "tries to rub",self.GEN[0],"greasy hands on",enemy.NAME + ", but they push ",self.GEN[1],"back!")
    else:
      if enemy.poisont < 3:
        enemy.poisont = 3
      enemy.greased = [3,self]
      enemy.poisond = enemy.poisond + ((0.4 + (0.1*self.grub))*self.cMAT) 
      print("\n" + self.NAME, "rubs",self.GEN[0],"greasy hands on",enemy.NAME + ", poisoning them and lowering their evasion!")

  def grubbytides(self,targ):
    global sett
    self.cMP = self.cMP - 20
    time.sleep(1)
    print("\n"+self.NAME,"summons the tides of grease, splashing the collosal waves onto all the enemies, damaging and poisoning them, and lowering their evasion!")
    for x in targ.team:
      self.prehiteffects(x)
      time.sleep(0.1)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n"+x.NAME,"avoids the wave!")
        x.specialdodgecases(self,0.1,"Magical Ranged")
      else:
        sett = x.cHP
        if x.poisont < 3:
          x.poisont = 3
        x.greased = [3,self]
        x.poisond = x.poisond + ((0.4 + (0.1*self.grub))*self.cMAT)
        dmg = (1+(0.1*self.grub))*self.cMAT
        x.defense(self,"Magical",dmg)
        if x.cHP >0:
          if (sett-x.cHP) == 0:
            print("\n" + x.NAME, "is squashed by the wave, but takes no damage!")
          else:
            print("\n" + x.NAME, "is squashed by the wave, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          print("\n" + x.NAME, "is squashed by the wave, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
        

  def taunt(self,enemy):
    time.sleep(1)
    print("\nDaniel:",random.choice(self.tauntstrings))
    time.sleep(0.3)
    if random.randint(1,100) <= round(50+(12.5*self.taun)):
      enemy.tauntt = 3
      enemy.taunted = [enemy,self]
      print("\n"+enemy.NAME,"takes the bait and is now focusing",self.NAME +"!")
    else:
      print("\n"+enemy.NAME,"doesn't fall for the bait!")

  def knightsvow(self,ally,tea):
    global bad
    bad = False
    if ally == self:
      print("\n"+self.NAME,"cannot cast this skill on",self.GEN[1]+"self!")
      bad = True
    else:
      self.cMP = self.cMP - 60
      for x in tea.team:
        if len(x.bonded)>0:
          if self == x.bonded[1]:
            x.bonded = []
      ally.bonded = [ally,self]
      self.knightb = 5
      time.sleep(1)
      print("\n"+self.NAME,"bonds",self.GEN[1]+"self with",ally.NAME+", protecting them from damage and increasing their physical and magical attack!")
    
  def photosynthesis(self):
    if self.OB == False:
      time.sleep(1)
      print("\n"+self.NAME,"generates food in his body to keep on eating, causing",self.GEN[1],"to regenerate health but lowering",self.GEN[0],"attack drastically!")
      self.OB = True 
    elif self.OB == True:
      time.sleep(1)
      print("\n"+self.NAME,"stops doing photosynthesis!")
      self.OB = False

  def enlargen(self):
    self.cMP = self.cMP - 80
    self.thehut = 5
    self.jabbaroll = 1
    time.sleep(1)
    print("\n"+self.NAME,"increases in size, taking the shape of a round ball!")

  def jabbaattack(self,targ):
    global sett
    global lastat
    self.jabbaroll = 0
    self.lastattack = "Jabba Roll"
    lastat = "Jabba Roll"
    self.cMP = self.cMP + self.cMRG
    if self.cMP > self.fMP:
      self.cMP = self.fMP
    self.fAT = self.fAT * (1.125 + (0.125*self.jabb))
    self.cAT = round(self.fAT*self.pAT)
    time.sleep(1)
    print(back.YELLOW_1 + fore.BLACK + "\n!!!" + style.RESET,self.NAME,"starts rolling towards the enemies...",back.YELLOW_1 + fore.BLACK + "!!!" + style.RESET)
    for x in targ.team:
      self.prehiteffects(x)
      time.sleep(0.2)
      sett = x.cHP
      diff = x.cEV - self.cAC 
      CT = random.randint(1,100)
      if random.randint(1,100) <= diff:
        print("\n" + x.NAME,"moves out of the way!")
        x.specialdodgecases(self,0.1,"Physical Melee",CT)
      else:
        if x.coun == True:
          x.counter(self,CT) 
        if CT <= self.cCT:
          dmg = self.CTdmg*self.cAT
          x.defense(self,"Physical",dmg)
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n" + x.NAME,"is crushed but takes no damage!")
            else:
              print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 +style.BOLD+ str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 + style.BOLD+str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Physical Melee")
        else:
          dmg = self.cAT
          x.defense(self,"Physical",dmg)
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n" + x.NAME,"is crushed but takes no damage!")
            else:
              print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n" + x.NAME, "is crushed, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Physical Melee")

  def electron(self,ally):
    self.cMP = self.cMP - 100
    ally.ionized = [4,self]
    time.sleep(1)
    if ally.NAME == self.NAME:
      print("\n"+self.NAME,"turns",self.GEN[1]+"self into an electron, increasing his accuracy, evasion, speed, and magic attack for 3 turns!")
    else:
      print("\n"+self.NAME,"turns",ally.NAME,"into an electron, increasing their accuracy, evasion, speed, and magic attack for 3 turns!")

  def dab(self,enemy): 
    global sett  
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 20
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n" + self.NAME,"dabs on",enemy.NAME+", but it's power doesn't reach them!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      sett = enemy.cHP
      techm = 1.00
      if self.dabstack == 0:
        daba = 1.00
      else:
        daba = (1.1**self.dabstack)
        if enemy.ID != self.dabtarg:
          daba = 1.00
      speedm = 1.00 + ((0.005+(0.005*self.da))*self.cSP)
      if self.cAC > 100:
        techm = 1.00 + ((0.005+(0.005*self.da))*(self.cAC - 100))
      dmg = ((0.8+(0.1*self.da))*self.cAT)*techm*speedm*daba
      enemy.defense(self,"Magical",dmg)
      if self.dabstack >= 0 and self.dabtarg != enemy.ID:
        self.dabstack = 1
        self.dabtarg = enemy.ID
      elif self.dabstack > 0 and self.dabtarg == enemy.ID:
        self.dabstack = self.dabstack + 1
      tier = "dabs"
      if self.dabstack == 2:
        tier = "Great-dabs"
      elif self.dabstack == 3:
        tier = "Mega-dabs"
      elif self.dabstack == 4:
        tier = "Amazing-dabs"
      elif self.dabstack == 5:
        tier = "Ultra-dabs"
      elif self.dabstack == 6:
        tier = "Spectacular-dabs"
      elif self.dabstack == 7:
        tier = "Super-dabs"
      elif self.dabstack == 8:
        tier = "Superior-dabs"
      elif self.dabstack == 9:
        tier = "Supreme-dabs"
      elif self.dabstack == 10:
        tier = "Ultimate-dabs"
      elif self.dabstack == 11:
        tier = "Legendary-dabs"
      elif self.dabstack == 12:
        tier = "God-dabs"
      elif self.dabstack == 12:
        tier = "Graham-dabs"
      if enemy.cHP >0:
        if (sett-enemy.cHP) == 0:
          print("\n" + self.NAME,tier,"on",enemy.NAME,"sending the trifecta of power, technique, and speed of the dab at them, but deals no damage!")
        else:
          print("\n" + self.NAME,tier,"on",enemy.NAME,"sending the trifecta of power, technique, and speed of the dab at them, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n" + self.NAME,tier,"on",enemy.NAME,"sending the trifecta of power, technique, and speed of the dab at them, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")

  def quen(self,ally,tea,ene):
    self.cMP = self.cMP - 80
    ally.purge("Cleanse",tea,ene)
    ally.quenshield = True
    time.sleep(1)
    if ally.NAME == self.NAME:
      print("\n"+self.NAME,"conjures a quen shield on",self.GEN[1]+"self, cleansing",self.GEN[0],"debuffs and protecting",self.GEN[1],"from damage for 1 hit!")
    else:
      print("\n"+self.NAME,"conjures a quen shield on",ally.NAME+", cleansing them of their debuffs and protecting them from damage for 1 hit!")

  def purge(self,types,ally,enemy,mid=False,op=False):
    if types == "Map Reset":
      self.rages = [0]
      self.mgh = [0]
      self.dark = 0
      self.glock = 0
      self.chilled = 0
    if types == "Purge":
      None
    if types == "Cleanse":
      self.fear = 0      #Negative Effects
      self.confusion = 0
      self.charmed = 0
      self.poisond = 0
      self.poisont = 0
      self.bleedd = 0
      self.bleedt = 0
      self.burnd = 0
      self.burnt = 0
      self.decayd = 0
      self.decayt = 0
      self.silenced = 0
      self.disarmed = 0
      self.orthoed = 0
      self.tremsl = 0
      self.chronot = 0
      self.greased = [0]
      self.marked = [0,0]
      self.revealed = 0
      self.ashamed = [0]
      if len(self.tethered) > 0:
        for x in self.tethered:
          x.teth.remove(self)          
      self.tethered = []
      self.stunned = False
      self.tremstun = 0
      self.sparkstun = 0
      self.dance = 0
      self.rooted = 0
      self.cutfear = [0]
      self.frozen = 0
      self.paralyzed = 0
      self.repulsed = 0
      self.confused = 0
      self.taunted = []
      self.tauntt = 0
      if op == False:
        for x in allfighters:
          if len(x.taunted) > 0:
            if self == x.taunted[1]:
              x.taunted = []
      #Boss debuffs
      self.candyAC = 0
      self.blind = 0
      self.scirc = 0
      #Supports
      self.caressed = 0
    elif types == "Death": 
      self.ISOmode = False
      if self.NAME == "Taco Lord":
        self.NAME == "Tim"
      self.skills = []
      if mid == False:
        for x in self.Sskills:
          self.skills.append(x)
      else:
        for x in self.Cskills:
          self.skills.append(x)
      self.food = [0,0,0,0,0,0,0,0,0,0,0,0]
      self.pbarrier = 0
      self.invis = 0
      self.instant = False
      self.WI = False
      if self.valos == True:
        for x in ally.team:
          x.valor = 0
      self.valos = False
      self.valor = 0
      self.enragev = 1
      self.manaflow = [0]
      self.resttimer = 21 - self.res
      self.runhigh = 0
      self.SHIE = False
      if self.isoboost > 0:
        self.setskills()
      self.isoboost = 0
      self.isoboostL = 0
      self.combd = [0]
      self.OB = False
      self.thehut = 0
      self.jabbaroll = 0
      self.ionized = [0]
      self.knightb = 0
      self.bonded = []
      for x in ally.team:
        if len(x.bonded) > 0:
          if self == x.bonded[1]:
            x.bonded = []
      if self.darks == True:
        for x in enemy.team:
          x.dark = 0
        for x in enemy.backteam:
          x.dark = 0
        for x in enemy.deadteam:
          x.dark = 0
      self.darks = False
      self.dark = 0
      self.safety = 0
      self.chronotime = 0
      self.chronoslow = []
      self.quenshield = False
      self.tension = 0
      self.duelt = 0
      self.duel = []
      if op == False:
        for x in allfighters:
          if len(x.duel) >0:
            if self == x.duel[1]:
              x.duel = []
              x.duelt = 0
      self.chadwalked = [0]
      self.chadl = False
      self.hater = 0
      self.hatelis = []
      self.surge = 0
      if len(self.teth) > 0:
        for x in self.teth:
          x.tethered.remove(self)
      self.teth = []
      self.ptelepath = 0
      self.telepath = 0
      self.mimicm = 0
      self.rehearsed = [0]
      self.prest = 0
      self.rested = 0
      self.graced = [0]
      self.radiant = [0]
      self.dmgstore = 0
      self.emmortal = 0
      self.solitude = [0]
      self.onethro = 0
      self.fear = 0      #Negative Effects
      self.confusion = 0
      self.charmed = 0
      self.poisond = 0
      self.poisont = 0
      self.bleedd = 0
      self.bleedt = 0
      self.burnd = 0
      self.burnt = 0
      self.decayd = 0
      self.decayt = 0
      self.silenced = 0
      self.disarmed = 0
      self.orthoed = 0
      self.tremsl = 0
      self.chronot = 0
      self.greased = [0]
      self.marked = [0,0]
      self.revealed = 0
      self.ashamed = [0]
      if len(self.tethered) > 0:
        for x in self.tethered:
          x.teth.remove(self)          
      self.tethered = []
      self.stunned = False
      self.stunimmune = [0,0]
      self.tremstun = 0
      self.sparkstun = 0
      self.dance = 0
      self.rooted = 0
      self.cutfear = [0]
      self.frozen = 0
      self.paralyzed = 0
      self.repulsed = 0
      self.deturn = 0
      self.taunted = []
      self.tauntt = 0
      if op == False:
        for x in allfighters:
          if len(x.taunted) > 0:
            if self == x.taunted[1]:
              x.taunted = []
      #Supports
      self.chilled = 0
      self.beared = 0
      self.teamed = 0
      self.eag = 0
      self.caressed = 0
      #Quest-Specific Buffs
      self.Q1B = 0 #Richard fight Enraged Ishraq 2x attack boost
      self.cry = 0 #Nurse cry timer
      self.ovd = 0 #transformer overdrive
      #Mob Essentials
      self.turncount = 0
      self.setHP = 0
      self.tw1 = 0
      self.tw2 = 0
      self.tw3 = 0
      self.tw4 = 0
      #Amira
      self.ENRAGE = False  #Insane Dilemna
      self.talkEN = 0      #Insane Dilemna
      self.giantess = 0  #Giant - Abby
      self.resil = 1  #Amira prevent defeat
      #Mrs.Wells
      self.candyAC = 0
      self.notes = 0
      self.missingnotes = 0
      self.destruct = 4
      self.notecount = 0
      #Mr.Pudup
      self.blind = 0
      #Terra
      self.zanc = 0
      #Aqua
      self.seeker = 0
      self.mvolley = 0
      if self.ragestorm == True:
        for x in enemy.team:
          x.rages = [0]
        for x in enemy.backteam:
          x.rages = [0]
        for x in enemy.deadteam:
          x.rages = [0]
      self.ragestorm = False
      #Dr.Graham
      self.scirc = 0
      self.inert = 0
      self.fricf = 0
      self.error = 0
      self.statr = False
      self.skillr = False
    
  def chronopower(self):
    time.sleep(0.5)
    print("\n" + self.NAME,"activates the power of time, igniting",self.GEN[0],"weapon with its essence for 3 hits!")
    self.chronotime = 3

  def protobelt(self,targ):
    global sett
    self.cMP = self.cMP - 35
    time.sleep(1)
    print("\n" + self.NAME,"activates",self.GEN[0],"safety belt, sending missiles at every enemy and blowing",self.GEN[1],"back, bringing",self.GEN[1],"to safety for 1 hit!")
    for x in targ.team:
      self.prehiteffects(x)
      time.sleep(0.2)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n" + x.NAME,"dodges the missle!")
        x.specialdodgecases(self,0.1,"Magical Ranged")
      else:
        sett = x.cHP
        dmg = (0.7+(0.15*self.proto))*self.cMAT
        x.defense(self,"Magical",dmg)
        if x.cHP >0:
          if (sett-x.cHP) == 0:
            print("\n" + x.NAME, "is hit by a missle, but takes no damage!")
          else:
            print("\n" + x.NAME, "is hit by a missle, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          print("\n" + x.NAME, "is hit by a missle, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
    self.safety = 1

  def rubixcube(self,targ):
    self.cMP = self.cMP - 75
    time.sleep(1)
    print("\n"+self.NAME,"throws",self.GEN[0],"rubix cube onto the stage! It solves itself and explodes, causing all enemies to start dancing!")
    throw = round(((1)+(0.1*self.rub))*self.cAC)
    bruh = []
    for x in targ.team:
      bruh.append(x)
    if len(bruh) > 3:
      yes = random.choice(bruh)
      bruh.remove(yes)
    for x in bruh:
      diff = x.cEV - throw
      if random.randint(1,100) <= diff:
        time.sleep(0.3)
        print("\n" + x.NAME,"avoids the blast!")
      else:
        x.dance = 1
        time.sleep(0.3)
        print("\n"+x.NAME,"is his by the blast and starts to dance!")

  def autosentry(self):
    self.cMP = self.cMP - 100
    time.sleep(1)
    print("\n"+self.NAME,"activates an auto-sentry to help fight off the enemies!")
    

  def tacotuesday(self,tea,targ):
    self.cMP = self.cMP - 100
    time.sleep(1)
    print("\n"+self.NAME+": Guys! It's taco tuesday!!!")
    time.sleep(0.5)
    print("\n"+self.NAME,"summons tacos from the air, raining super hot tacos of doom onto the enemies, and perfectly delicious tacos on all allies! A taco is added into everyone's inventory!")
    for x in tea.team:
      x.battleinventory.append("Taco")
    for x in targ.team:
      if x.burnt < 2:
        x.burnt = 2 
      x.burnd = x.burnd + round(self.cMAT) 

  def silence(self):
    self.silenced = 4
    time.sleep(1)
    print("\n" + self.NAME,"shuts",self.GEN[1]+"self up...")
    
  def silenceattack(self,enemy):
    global sett
    global lastat
    self.prehiteffects(enemy)
    sett = enemy.cHP
    diff = enemy.cEV - self.cAC 
    self.lastattack = "Silenced Auto"
    lastat = "Silenced Auto"
    self.cMP = self.cMP + self.cMRG
    if self.cMP > self.fMP:
      self.cMP = self.fMP 
    CT = random.randint(1,100)
    if random.randint(1,100) <= diff:
      time.sleep(1)
      print("\n" + self.NAME, "attacks, but", enemy.NAME, "dodges!")
      enemy.specialdodgecases(self,0.5,"True Melee")
    else:
      time.sleep(1)
      if enemy.coun == True:
        enemy.counter(self,CT) 
      if CT <= self.cCT:
        dmg = round((self.CTdmg*self.cAT)+((0.5+(0.05*self.silen))*self.cMAT)+((0.5+(0.05*self.silen))*self.cAT))
        enemy.cHP = enemy.cHP - dmg
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n" + self.NAME, "dead silently attacks", enemy.NAME +  ", but deals no damage!")
          else:
            print("\n" + self.NAME, "dead silently attacks", enemy.NAME + ", dealing",fore.GREY_100 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n" + self.NAME, "dead silently attacks", enemy.NAME + ", dealing",fore.GREY_100 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.5,dmg,"True Melee")
      else:
        dmg = round(self.cAT+((0.5+(0.05*self.silen))*self.cMAT)+((0.5+(0.05*self.silen))*self.cAT))
        enemy.cHP = enemy.cHP - dmg
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n" + self.NAME, "silently attacks", enemy.NAME +  ", but deals no damage!")
          else:
            print("\n" + self.NAME, "silently attacks", enemy.NAME + ", dealing",fore.GREY_100 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n" + self.NAME, "silently attacks", enemy.NAME + ", dealing",fore.GREY_100 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.5,dmg,"True Melee")

  def cutmyself(self,targ):
    self.cMP = self.cMP - 35
    for x in targ.team:
      x.cutfear = [3,self]
    self.bleedt = 3
    self.bleedd = self.bleedd + (0.067*self.fHP)
    time.sleep(1)
    print("\n" + self.NAME,"starts cutting",self.GEN[1]+"self, lowering all enemy defense and magic defense!")

  def gunblade(self,enemy):
    global sett
    self.cMP = self.cMP - 30
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "jumps and tries to slash",enemy.NAME+", but misses!")
      enemy.specialdodgecases(self,0.5,"Physical Magical Melee Ranged")
    else:
      sett = enemy.cHP
      if enemy.coun == True:
        enemy.counter(self)
      pdmg = (1.2+(0.2*self.gunb))*self.cAT
      enemy.defense(self,"Physical",pdmg)
      mdmg = (1.5+(0.25*self.gunb))*self.cMAT
      enemy.defense(self,"Magical",mdmg)
      selfsett = self.cHP
      self.cHP = self.cHP + round(self.healmod*(0.5+(0.1*self.gunb))*(sett-enemy.cHP))
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      if enemy.cHP >0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME, "jumps and slashes",enemy.NAME,"with his gunblade, and shoots them, but deals no damage!")
        else:
          print("\n"+self.NAME, "jumps and slashes",enemy.NAME,"with his gunblade, and shoots them, dealing",fore.DEEP_PINK_3A + str(sett-enemy.cHP) + style.RESET,"mixed damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")      
      else:
        print("\n"+self.NAME, "jumps and slashes",enemy.NAME,"with his gunblade, and shoots them, dealing",fore.DEEP_PINK_3A + str(sett-enemy.cHP) + style.RESET,"mixed damage!",enemy.NAME,"falls...")
      tot = pdmg + mdmg
      enemy.onhittimersdefense(self,0.5,tot,"Physical Magical Melee Ranged")  
      time.sleep(0.5)
      print("\nThe gunblade restores",self.NAME+"'s health with its stored energy, healing him for",fore.MEDIUM_SPRING_GREEN + str(selfsett-self.cHP) + style.RESET,"health! Arwyn has",self.cHP,"health now!") 
      
  def sparknet(self,ally,eteam):
    global sett
    self.cMP = self.cMP - 50
    bruh = []
    for x in eteam.team:
      if (x.invis <=0 or x.revealed > 0):
        bruh.append(x)
    time.sleep(1)
    if len(bruh) == 1:
      enemy = bruh[0]
      self.prehiteffects(enemy)
      diff = enemy.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        print("\n" + self.NAME, "attempts to strike", enemy.NAME, "with a lightning bolt, but they dodge!")
        enemy.specialdodgecases(self,0.5,"Magical Ranged")
      else:
        enemy.sparkstun = enemy.sparkstun + 1
        sett = enemy.cHP
        dmg =  (0.8+(0.1*self.spark))*self.cMAT
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n" + self.NAME, "strikes", enemy.NAME, "with a lightning bolt, paralyzing them but dealing no damage!")
          else:
            print("\n" + self.NAME, "strikes", enemy.NAME, "with a lightning bolt, paralyzing them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n" + self.NAME, "strikes", enemy.NAME, "with a lightning bolt, paralyzing them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
    else:
      print("\n" + self.NAME, "sends out a sparknet that bounces between the enemies!")
      temp = None
      final = 0
      for boob in range(6):
        CTI = False
        time.sleep(0.3)
        if len(bruh) == 0 and temp != None:
          bruh.append(temp)
          temp = None
          final = 1
        if len(bruh) > 0:
          if len(self.duel) > 0:
            if self.duel[1] != temp:
              targ = self.duel[1]
            else:
              targ = random.choice(bruh)
          elif len(self.taunted) > 0:
            if self.taunted[1] != temp:
              targ = self.taunted[1]
            else:
              targ = random.choice(bruh)
          else:
            targ = random.choice(bruh)
        else:
          break
        self.prehiteffects(targ)
        diff = targ.cEV - self.cAC 
        if random.randint(1,100) <= diff:
          print("\nThe lightning bounces to", targ.NAME + ", but they dodge!")
          targ.specialdodgecases(self,0.5,"Magical Ranged")
          break
        else:
          if random.randint(1,100) <= self.cCT:
            targ.sparkstun = targ.sparkstun + 1
            CTI = True
          sett = targ.cHP
          dmg = (0.4+(0.05*self.spark))*self.cMAT
          targ.defense(self,"Magical",dmg)
          if targ.cHP > 0:
            if CTI == True:
              if (sett-targ.cHP) == 0:
                print("\nThe lightning bounces to", targ.NAME + ", paralyzing them but dealing no damage!")
              else:
                print("\nThe lightning bounces to", targ.NAME + ", paralyzing them and dealing", fore.PURPLE_1B + str(sett-targ.cHP) + style.RESET,"damage!",targ.NAME,"has",targ.cHP,"health remaining!")
            else:
              if (sett-targ.cHP) == 0:
                print("\nThe lightning bounces to", targ.NAME + ", but deals no damage!")
              else:
                print("\nThe lightning bounces to", targ.NAME + ", dealing", fore.PURPLE_1B + str(sett-targ.cHP) + style.RESET,"damage!",targ.NAME,"has",targ.cHP,"health remaining!")
            targ.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
            if temp != None:
              bruh.append(temp)
            if final == 1:
              break
            temp = targ
            bruh.remove(targ)
          else:
            if CTI == True:
              print("\nThe lightning bounces to", targ.NAME + ", paralyzing them and dealing", fore.PURPLE_1B + str(sett-targ.cHP) + style.RESET,"damage!",targ.NAME,"falls...")
            else:
              print("\nThe lightning bounces to", targ.NAME + ", dealing", fore.PURPLE_1B + str(sett-targ.cHP) + style.RESET,"damage!",targ.NAME,"falls...")
            targ.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
            if targ.cHP <= 0:
              bruh.remove(targ)
            else:
              targ.currentstats(eteam,ally)

  def darkness(self,targ):
    self.cMP = self.cMP - 60
    self.darks = True
    for x in targ.team:
      x.dark = 26
    time.sleep(1)
    print("\n" + self.NAME,"shrouds the area in darkness, reducing all enemy accuracies and increasing his crit damage, chance, and penetrations!")

  def progressiveoverload(self):
    time.sleep(1)
    self.tension = self.tension + 1
    if self.tension == 1:
      print("\n"+self.NAME,"tenses up, increasing",self.GEN[0],"strength for",self.GEN[0],"next physical attack!")
    elif self.tension == 2:
      print("\n"+self.NAME,"tenses up greatly, further increasing",self.GEN[0],"strength for",self.GEN[0],"next physical attack!")
    elif self.tension == 3:
      print("\n"+self.NAME,"tenses up immensely, extremely increasing",self.GEN[0],"strength for",self.GEN[0],"next physical attack!")

  def sickpump(self):
    time.sleep(1)
    if self.tension >= 3:
      self.tension = self.tension + 1
      if self.tension == 5:
        print(fore.ORANGE_RED_1+"\n"+self.NAME+": Protein...protein..."+style.BOLD+"MOM I NEED PROTEIN!!!"+style.RESET)
        time.sleep(1)
        print("\n"+self.NAME,"chugs gallons of proteins, and starts to beetle stride.",self.GEN[0].capitalize(),"eyes dart forward and arms start flailing around.",self.GEN[2].capitalize(),"becomes the epitome of CHAD, tension boosting to the limit of infinity!")
      else:
        print("\n"+self.NAME,"does the most CHAD pump, tension boosting beyond max!")
    elif self.tension < 3:
      self.tension = 3
      print("\n"+self.NAME,"does a sick pump, tension boosting to max!")
    
  def armwrestling(self,enemy):
    self.cMP = self.cMP - 50
    time.sleep(1)
    print("\n"+self.NAME,"starts an arm-wrestling match with",enemy.NAME+", locking both of them into a duel!")
    if len(enemy.duel) >0:
      enemy.duel[1].duel = []
      enemy.duel[1].duelt = 0
    for x in allfighters:
      if len(x.duel) > 0:
        if self in x.duel:
          x.duel = []
    self.duelt = 5
    self.duel = [self,enemy]
    enemy.duel = [enemy,self]
  
  
  def inferno(self,enemy):
    global sett
    self.cMP = self.cMP - 30
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "exerts the fiery inferno of working out onto",enemy.NAME + ", but misses!")
      enemy.specialdodgecases(self,0.5,"Physical Magical Melee")
    else:
      sett = enemy.cHP
      if enemy.coun == True:
        enemy.counter(self)
      pdmg = (0.7+(0.1*self.infe))*self.cAT
      enemy.defense(self,"Physical",pdmg)
      mdmg = (1+(0.1*self.infe))*self.cMAT
      enemy.defense(self,"Magical",mdmg)
      enemy.burnd = enemy.burnd + ((sett-enemy.cHP)*(0.1+(0.05*self.infe)))
      if enemy.cHP >0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME, "exerts the fiery inferno of working out onto",enemy.NAME + ", but it deals no damage!")
        else:
          print("\n"+self.NAME, "exerts the fiery inferno of working out onto",enemy.NAME + ", dealing",fore.DEEP_PINK_3A + str(sett-enemy.cHP) + style.RESET,"mixed damage and burning them!", enemy.NAME,"has",enemy.cHP,"health remaining!")
          if enemy.burnt < 2:
            enemy.burnt = 2
      else:
        print("\n"+self.NAME, "exerts the fiery inferno of working out onto",enemy.NAME + ", dealing",fore.DEEP_PINK_3A + str(sett-enemy.cHP) + style.RESET,"mixed damage and burning them!", enemy.NAME,"falls...")
        if enemy.burnt < 2:
          enemy.burnt = 2
      tot = pdmg + mdmg
      enemy.onhittimersdefense(self,0.5,tot,"Physical Magical Melee")
      self.onhittimersoffense(self,0.5,"Physical Magical Melee") 

  def selfdestruct(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    sett = enemy.cHP
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "tries to grapple",enemy.NAME + ", but they break out!")
      enemy.specialdodgecases(self,0.5,"True Melee")
    else:
      if enemy.coun == True:
        enemy.counter(self)
      selfsett = self.cHP
      self.cHP = self.cHP - round(0.75*self.fHP)
      dmg = selfsett-self.cHP
      print("\n"+self.NAME, "grapples",enemy.NAME + ", locking them down.")
      time.sleep(0.5)
      print("\n"+self.NAME+": Allahu Akbar")
      time.sleep(0.5)
      enemy.cHP = enemy.cHP - round((0.6+(0.1*self.selfd))*dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME,"self-destructs on",enemy.NAME+", but deals no damage!")
        else:
          print("\n"+self.NAME,"self-destructs on",enemy.NAME+", dealing",style.BOLD + str(sett-enemy.cHP) + style.RESET,"true damage!",enemy.NAME,"has",enemy.cHP,"health remaning!")
      else:
        print("\n"+self.NAME,"self-destructs on",enemy.NAME+", dealing",style.BOLD + str(sett-enemy.cHP) + style.RESET,"true damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"True Melee") 
      if self.cHP >0:
        print(self.NAME,"takes",dmg,"damage!",self.NAME,"has",self.cHP,"health now!")
      else:
        print(self.NAME,"takes",dmg,"damage!",self.NAME,"falls...")
      self.onhittimersdefense(self,0.5)
      
  def chadwalk(self,ally):
    self.cMP = self.cMP - 80
    time.sleep(1)
    print("\n"+self.NAME,"chad-walks across the battlefield to make up for",self.GEN[0],"fragile masculinity, increasing allied and decreasing enemy critical chance and damage!")
    for x in ally.team:
      x.chadwalked = [5,self]
    self.chadl = True
      
  def suck(self,enemy):
    global sett
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 80
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "tries to suck off",enemy.NAME+", but they back off!")
      enemy.specialdodgecases(self,0.5,"Magical Melee")
    else:
      sett = enemy.cHP
      if enemy.coun == True:
        enemy.counter(self)
      selfsett = self.cHP
      self.cHP = self.cHP + round(self.healmod*(self.fHP-self.cHP)*(0.3+(0.05*self.suc)))
      if "Male" in enemy.GEND:
        dmg = self.CTdmg*self.cMAT*(1+(self.suc*0.5))
        enemy.defense(self,"Magical",dmg)
        enemy.bleedt = 2
        enemy.bleedd = enemy.bleedd + ((0.5+(0.125*self.suc))*self.cMAT)
      else:
        dmg = self.cMAT*(1+(self.suc*0.4))
        enemy.defense(self,"Magical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME, "sucks off",enemy.NAME +", but deals no damage!")
        else:
          if "Male" in enemy.GEND:
            print("\n"+self.NAME, "sucks off and bites",enemy.NAME,"dealing",fore.PURPLE_1B+style.BOLD+str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME, "sucks off",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        if "Male" in enemy.GEND:
          print("\n"+self.NAME, "sucks off and bites",enemy.NAME,"dealing",fore.PURPLE_1B+style.BOLD+str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        else:
          print("\n"+self.NAME, "sucks off",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      time.sleep(0.5)
      print("\n"+self.NAME,"heals for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Melee")
  
  def powersurge(self,targ):
    self.cMP = self.cMP - 75
    time.sleep(1)
    print("\n"+self.NAME,"unleashes tethers from",self.GEN[0],"body, clinging onto all enemies to drain their attack and magic attack!")
    self.surge = 6
    self.teth = []
    for x in targ.team:
      self.teth.append(x)
      x.tethered.append(self)
  
  def telepathy(self,enemy):
    self.cMP = self.cMP - 35
    time.sleep(1)
    if enemy.fear < 3:
      enemy.fear = 3
    print("\n"+self.NAME+", inside of",enemy.NAME+"'s head: Doyouhatemedoyouhatemedoyouhateme...")
    time.sleep(0.5)
    print(enemy.NAME,"is afraid for their life, becoming feared for 3 turns!")
    time.sleep(0.3)
    print(self.NAME,"is ready to unleash telepathic attacks for the next 3 hits!")
    self.telepath = 3

  def mimic(self,enemy="",al="",targ=""):
    global sett
    global bad
    global lastat
    global skl
    self.mimicm = 1
    if self.mimit == 1:
      if enemy.lastattack == "":
        print("\n"+self.NAME,"can't mimic nothing!")
        bad = True
      elif enemy == self:
        print("\n"+self.NAME,"can't mimic herself!")
        bad = True
      elif enemy.lastattack == "Auto":
        if len(targ.teamS) > 1:
          print("")
          print(targ.teamS)
          self.target(self.attack,targ.team,targ.teamS)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and (x.invis <=0 or x.revealed > 0):
              self.attack(x)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      elif enemy.lastattack == "Jabba Roll":
        self.jabbaattack(targ)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      elif enemy.lastattack == "Silenced Auto":
        if len(targ.teamS) > 1:
          print("")
          print(targ.teamS)
          self.target(self.silenceattack,targ.team,targ.teamS)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and (x.invis <=0 or x.revealed > 0):
              self.silenceattack(x)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      else:
        msett = self.cMP
        self.skillcatalog(enemy.lastattack,al,targ)
        if bad != True:
          mlost = (msett-self.cMP)
          if skl == "Ultra":
            if mlost < round(self.fMP*(0.5-(0.05*self.mimi))):
              self.cMP = msett - round(self.fMP*(0.5-(0.05*self.mimi)))
          elif skl == "Mega":
            if mlost < round(self.fMP*(0.4-(0.05*self.mimi))):
              self.cMP = msett - round(self.fMP*(0.4-(0.05*self.mimi)))
          elif skl == "Basic":
            if mlost < round(self.fMP*(0.3-(0.05*self.mimi))):
              self.cMP = msett - round(self.fMP*(0.3-(0.05*self.mimi)))
    else:
      if lastat == "":
        print("\n"+self.NAME,"can't mimic nothing!")
        bad = True
      elif lastat in self.skills:
        print("\n"+self.NAME,"can't mimic herself!")
        bad = True
      elif lastat == "Auto":
        if len(targ.teamS) > 1:
          print("")
          print(targ.teamS)
          self.target(self.attack,targ.team,targ.teamS)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and (x.invis <=0 or x.revealed > 0):
              self.attack(x)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      elif lastat == "Jabba Roll":
        self.jabbaattack(targ)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      elif lastat == "Silenced Auto":
        if len(targ.teamS) > 1:
          print("")
          print(targ.teamS)
          self.target(self.silenceattack,targ.team,targ.teamS)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and (x.invis <=0 or x.revealed > 0):
              self.silenceattack(x)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      else:
        msett = self.cMP
        self.skillcatalog(lastat,al,targ)
        if bad != True:
          mlost = (msett-self.cMP)
          if skl == "Ultra":
            if mlost < round(self.fMP*(0.5-(0.05*self.mimi))):
              self.cMP = msett - round(self.fMP*(0.5-(0.05*self.mimi)))
          elif skl == "Mega":
            if mlost < round(self.fMP*(0.4-(0.05*self.mimi))):
              self.cMP = msett - round(self.fMP*(0.4-(0.05*self.mimi)))
          elif skl == "Basic":
            if mlost < round(self.fMP*(0.3-(0.05*self.mimi))):
              self.cMP = msett - round(self.fMP*(0.3-(0.05*self.mimi)))
    self.mimicm = 0

  def desperation(self,ally,targ):
    global sett
    self.cMP = self.cMP - 50
    time.sleep(0.5)
    print("\n" + self.NAME,"kneels and observes the battlefield...")
    time.sleep(1)
    if len(ally.team) == 1:
      print("\n"+self.NAME+": Everyone's gone...they're all leaving...LEAVING ME!!!")
    if len(ally.team) == 2:
      print("\n"+self.NAME+": They say friends are always replacable...but it's...IT'S THE ONLY FRIEND I HAVE LEFT!!!")
    if len(ally.team) == 3:
      print("\n"+self.NAME+": Fake ones will be cut down...why is it that...THAT MY FRIENDS ARE ALL FAKE?!!")
    if len(ally.team) == 4:
      print("\n"+self.NAME+": You're all fake...")
    time.sleep(1)
    print("\n"+self.NAME,"emanates a malefic aura across the battlefield!\n")
    dmg = (self.cMAT*(((0.6+(0.1*self.desp))+((1+(0.25*self.desp))*(1-(self.cHP/self.fHP))))*((1.2+(0.05*self.desp))**(4-len(ally.team)))))
    for x in targ.team:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print(x.NAME,"is unaffected by the aura!")
        x.specialdodgecases(self,0,"Magical Ranged")
      else:
        sett = x.cHP
        x.defense(self,"Magical",dmg)
        if x.cHP >0:
          if (sett-x.cHP) == 0:
            print(x.NAME, "is blasted by the aura, but takes no damage!!")
          else:
            print(x.NAME, "is blasted by the aura, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          print(x.NAME, "is blasted by the aura",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0,dmg,"Magical Ranged")

  def energykick(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    selfsett = self.cHP
    self.cHP = self.cHP - round(0.04*self.fHP)
    diff = enemy.cEV - self.cAC
    CT = random.randint(1,100)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "tries to attack",enemy.NAME,"with an energized kick at the cost of",str(selfsett-self.cHP),"health, but misses!")
      enemy.specialdodgecases(self,0.5,"Physical Melee",CT)
    else:
      sett = enemy.cHP
      msett = enemy.cMP
      if enemy.cMP > round(0.1*enemy.fMP):
        self.cMP = self.cMP + round(0.1*enemy.fMP)
        enemy.cMP = enemy.cMP - round(0.1*enemy.fMP)
      else:
        self.cMP = self.cMP + enemy.cMP
        enemy.cMP = 0
      self.isopoints = self.isopoints + (msett-enemy.cMP)
      if self.isopoints > (100*self.isoLevel):
        self.isopoints = (100*self.isoLevel)
      if self.cMP > self.fMP:
        self.cMP = self.fMP
      if enemy.coun == True:
        enemy.counter(self,CT) 
      if CT <= self.cCT:
        dmg = self.CTdmg*(((1+(0.25*self.engk))*self.cAT)+self.cMAT)
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          print("\n"+self.NAME, "attacks",enemy.NAME,"with an energized kick at the cost of",str(selfsett-self.cHP),"health, dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"critical damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "attacks",enemy.NAME,"with an energized kick at the cost of",str(selfsett-self.cHP),"health, dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"critical damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"falls...")
      else:
        dmg = (((1+(0.25*self.engk))*self.cAT)+self.cMAT)
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          print("\n"+self.NAME, "attacks",enemy.NAME,"with an energized kick at the cost of",str(selfsett-self.cHP),"health, dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "attacks",enemy.NAME,"with an energized kick at the cost of",str(selfsett-self.cHP),"health, dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Physical Melee")
    if self.cHP <=0:
      time.sleep(1)
      print("\n"+self.NAME,"dies due to exhaustion...")
      self.onhittimersdefense(self,0.5)

  def virginitytheft(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    CT = random.randint(1,100)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "tries to steal",enemy.NAME+"'s virginity, but they resist",self.GEN[1]+"!")
      enemy.specialdodgecases(self,0.5,"Physical Magical Melee")
    else:
      sett = enemy.cHP
      msett = enemy.cMP
      if enemy.cMP > round(0.1*enemy.fMP):
        self.cMP = self.cMP + round(0.1*enemy.fMP)
        enemy.cMP = enemy.cMP - round(0.1*enemy.fMP)
      else:
        self.cMP = self.cMP + enemy.cMP
        enemy.cMP = 0
      if self.cMP > self.fMP:
        self.cMP = self.fMP
      if enemy.coun == True:
        enemy.counter(self,CT) 
      if CT <= self.cCT:
        pdmg = self.CTdmg*(((1+(0.25*self.engk))*self.cAT)+self.cMAT)
        enemy.defense(self,"Physical",pdmg)
        mdmg = self.CTdmg*(msett-enemy.cMP)*(3+(0.5*self.engk))
        enemy.defense(self,"Magical",mdmg)
        if enemy.cHP >0:
          print("\n"+self.NAME, "steals",enemy.NAME+"'s virginity, dealing",fore.DEEP_PINK_3A + style.BOLD + str(sett-enemy.cHP) + style.RESET,"critical damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "steals",enemy.NAME+"'s virginity, dealing",fore.DEEP_PINK_3A + style.BOLD + str(sett-enemy.cHP) + style.RESET,"critical damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"falls...")
      else:
        pdmg = ((1+(0.25*self.engk))*self.cAT)+self.cMAT
        enemy.defense(self,"Physical",pdmg)
        mdmg = (msett-enemy.cMP)*(3+(0.5*self.engk))
        if enemy.cHP >0:
          print("\n"+self.NAME, "steals",enemy.NAME+"'s virginity, dealing",fore.DEEP_PINK_3A + str(sett-enemy.cHP) + style.RESET,"damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "steals",enemy.NAME+"'s virginity, dealing",fore.DEEP_PINK_3A + str(sett-enemy.cHP) + style.RESET,"damage, and stealing",str(msett-enemy.cMP),"mana!",enemy.NAME,"falls...")
      tot = pdmg + mdmg
      enemy.onhittimersdefense(self,0.5,tot,"Physical Melee")

  def dancersswiftness(self):
    self.cMP = self.cMP - 80
    self.EV = self.EV + (1+self.dsw)
    time.sleep(1)
    print("\n"+self.NAME,"dances around to increase",self.GEN[0],"range of motion, permanently increasing",self.GEN[0],"evasion by",str(1+self.dsw)+"%!")
  
  def weirdflex(self,targ):
    self.cMP = self.cMP - 35
    time.sleep(1)
    quote = random.randint(1,3)
    if quote == 1:
      print("\n"+self.NAME+": Man, my boyfriend's cock tasted so fucking good yesterday!")
    elif quote == 2:
      print("\n"+self.NAME+": God, having sex with that random guy was so fun yesterday!")
    elif quote == 3:
      print("\n"+self.NAME+": Haha, I was gonna have sex with this boy yesterday, but he was under 8. *sigh*")
    time.sleep(1)
    print("\n"+self.NAME,"flexes how much sex",self.GEN[2],"had, making everyone ashamed of themselves, lowering their magic attack and magic penetration!")
    for x in targ.team:
      x.ashamed = [3,self]

  def rehearsal(self,tea):
    self.cMP = self.cMP - 65
    time.sleep(1)
    print("\n"+self.NAME,"rehearses with everyone, increasing everyone's evasion by a percentage of hers!")
    for x in tea.team:
      x.rehearsed = [3,self]

  def powerrest(self):
    self.cMP = self.cMP - 40
    time.sleep(1)
    print("\n"+self.NAME,"takes a power rest!")
    self.prest = 1

  def emophase(self):
    self.cMP = self.cMP - 75
    self.emmortal = 6
    time.sleep(1)
    print("\n"+self.NAME,"enters",self.GEN[0],"emo phase, lowering",self.GEN[0],"damage reduction, gaining extreme lifesteal, and becoming immortal!")
  
  def outrage(self,enemy):
    global sett
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 80
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "releases",self.GEN[0],"pent-up emotions onto",enemy.NAME+", but they don't care!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      sett = enemy.cHP
      if self.cMAT != 0:
        self.cMAT = 1
      dmg = self.cMAT*self.dmgstore*(0.1+(self.outr*0.05))
      enemy.defense(self,"Magical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME, "releases",self.GEN[0],"pent-up emotions onto",enemy.NAME +", but deals no damage!")
        else:
          print("\n"+self.NAME, "releases",self.GEN[0],"pent-up emotions onto",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+self.NAME, "releases",self.GEN[0],"pent-up emotions onto",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
    self.dmgstore = 0

  def outrageAOE(self,targ):
    global sett
    self.cMP = self.cMP - 80
    time.sleep(1)
    print("\n"+self.NAME,"releases",self.GEN[0],"pent-up emotions, sending out a wave of repulsion towards the enemies!")
    for x in targ.team:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n"+x.NAME,"avoids the wave!")
        x.specialdodgecases(self,0.5,"Magical Ranged")
      else:
        sett = x.cHP
        if self.cMAT != 0:
          self.cMAT = 1
        dmg = self.cMAT*self.dmgstore*(0.1+(self.outr*0.05))
        x.defense(self,"Magical",dmg)
        if x.cHP > 0:
          if (sett-x.cHP) == 0:
            print("\n"+x.NAME,"is hit by the wave, but takes no damage!")
          else:
            print("\n"+x.NAME,"is hit by the wave, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          print("\n"+x.NAME,"is hit by the wave, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
    self.dmgstore = 0

  def arrivederci(self,enemy):
    self.cMP = self.cMP - 45
    if len(enemy.marked) == 3:
      if self not in enemy.marked:
        enemy.marked[2] = self
    else:
      enemy.marked.append(self)
    enemy.marked[0] = 3
    time.sleep(1)
    print("\n"+self.NAME+": Arrivederci...")
    time.sleep(0.5)
    print("\n"+self.NAME,"bids farewell to",enemy.NAME+", exposing them and marking them for death!")

  def recluse(self):
    self.cMP = self.cMP - 35
    self.solitude = [4,self]
    time.sleep(1)
    print("\n"+self.NAME,"secludes",self.GEN[1]+"self from everyone, increasing",self.GEN[0],"damages but lowering",self.GEN[0],"defenses!")

  def friends(self,ally):
    self.cMP = self.cMP - 35
    for x in ally.team:
      x.solitude = [4,self]
    time.sleep(1)
    print("\n"+self.NAME,"becomes friends with everyone, increasing their damages but reducing",self.GEN[0],"defenses!")

  def onethroat(self):
    self.cMP = self.cMP - 50
    self.onethro = 5
    time.sleep(1)
    print("\n"+self.NAME+": If you all had but one throat...I would slit it.")
    time.sleep(0.75)
    print("\n"+self.NAME,"gets extra edgy, increasing his penetrations and causing his single target attacks to become multi-target!")

  def gracefulgales(self,ally):
    self.cMP = self.cMP - 25
    time.sleep(1)
    print("\n"+self.NAME,"sends a graceful gale onto",self.GEN[0],"allies, causing them to regenerate their health and increasing their healing from all sources.")
    for x in ally.team:
      x.graced = [3,self]

  def lingeringlight(self,enemy):
    global sett
    self.cMP = self.cMP - 20
    self.prehiteffects(enemy) 
    time.sleep(1) 
    diff = enemy.cEV - (1.4*self.cAC)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "tries to illuminate",enemy.NAME,"with a lingering light, but misses!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      sett = enemy.cHP
      dmg = self.cMAT*(1.5+(self.ling*0.25))
      enemy.defense(self,"Magical",dmg)
      enemy.revealed = 4
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME, "illuminates",enemy.NAME,"with a lingering light, revealing them but dealing no damage!")
        else:
          print("\n"+self.NAME, "illuminates",enemy.NAME,"with a lingering light, revealing them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+self.NAME, "illuminates",enemy.NAME,"with a lingering light, revealing them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
  
  def whirlingwinds(self,targ):
    global sett
    self.cMP = self.cMP - 40
    time.sleep(1)
    print("\n"+self.NAME,"directs a raging wind onto the enemies!")
    for x in targ.team:
      time.sleep(0.15)
      self.prehiteffects(x)
      sett = x.cHP
      diff = x.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        print("\n"+x.NAME,"resists the winds!")
        x.specialdodgecases(self,0.0,"Physical Ranged")
      else:
        if x.bleedt < 2:
          x.bleedt = 2
        x.bleedd = x.bleedd + ((0.25+(0.05*self.whir))*self.cMAT*self.CTdmg)
        dmg = (self.cAT*(1.5+(0.25*self.whir)))
        x.defense(self,"Physical",dmg)
        if x.cHP > 0:
          if (sett-x.cHP) == 0:
            print("\n"+x.NAME,"is cut by the winds, but takes no damage!")
          else:
            print("\n"+x.NAME,"is cut by the winds, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          print("\n"+x.NAME,"is cut by the winds, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0,dmg,"Physical Ranged") 
      
  def radiantresilience(self,ally):
    self.cMP = self.cMP - 70
    for x in ally.team:
      x.radiant = [4,self]
    time.sleep(1)
    print("\n"+self.NAME,"calls upon the sun's power to protect",self.GEN[0],"allies, increasing all allied defenses!")

  def eternalequinox(self,ally,targ):
    global sett
    self.cMP = self.cMP - 100
    time.sleep(1)
    print("\n"+self.NAME+": Balance in all things...Eternal Equinox.")
    time.sleep(1)
    print("\n"+self.NAME,"summons a magical seal on the ground across the battlefield! It explodes, enveloping the entire battlefield in light!")
    time.sleep(1)
    total = 0
    for x in targ.team:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n"+x.NAME, "escapes the seal's radius!")
        x.specialdodgecases(self,0.5,"Physical Magical Ranged")
      else:
        sett = x.cHP
        pdmg = (2+(0.25*self.gunb))*self.cAT
        x.defense(self,"Physical",pdmg)
        mdmg = (2+(0.5*self.gunb))*self.cMAT
        x.defense(self,"Magical",mdmg)
        if x.cHP >0:
          if (sett-x.cHP) == 0:
            print("\n"+x.NAME, "is baptised by the light, but takes no damage!")
          else:
            print("\n"+x.NAME, "is baptised by the light, taking",fore.DEEP_PINK_3A + str(sett-x.cHP) + style.RESET,"mixed damage!",x.NAME,"has",x.cHP,"health remaining!")      
        else:
          print("\n"+x.NAME, "is baptised by the light, taking",fore.DEEP_PINK_3A + str(sett-x.cHP) + style.RESET,"mixed damage!",x.NAME,"falls...")
        tot = pdmg + mdmg
        x.onhittimersdefense(self,0,tot,"Physical Magical Ranged")
        if x.cHP < sett:
          total = total + (sett-x.cHP)  
    time.sleep(0.5)
    print("\nThe holy light recovers health to all allies!")
    for x in ally.team:
      selfsett = x.cHP
      x.cHP = x.cHP + round(x.healmod*total*0.25)
      if x.cHP > x.fHP:
        x.cHP = x.fHP
      print("\n"+x.NAME,"heals for",fore.MEDIUM_SPRING_GREEN+str(x.cHP-selfsett)+style.RESET,"health!",x.NAME,"has",x.cHP,"health now!")
    
  def AIdetector(self):
    if self.stunned == True and self.NAME != "Mr. Pudup":
      self.stunned = False
    else:
      if self.NAME == "Amira" and self.ID !="11":
        self.AmiraAI()
      elif self.NAME == "Mrs. Wells":
        self.MrsWellsAI()
      elif self.NAME == "Mr. Pudup":
        self.MrPudupAI()
      elif self.NAME == "Julius":
        self.JuliusAI()
      elif self.NAME == "The Nurse":
        self.NurseAI()
      elif self.NAME == "Aqua":
        self.AquaAI()
      elif self.NAME == "Terra":
        self.TerraAI()
      elif self.NAME == "Dr. Graham":
        self.GrahamAI()
      elif self.NAME == "The Soul of Kelly":
        self.KellyAI()
      elif self.NAME == "The Librarian":
        self.LibrarianAI()
      elif self.NAME == "Transformer":
        self.TransformerAI()
      elif self.NAME == "Tim":
        self.TimAI()
      elif self.NAME == "Daniel":
        self.DanielAI()
      elif self.NAME == "Mega Daniel":
        self.MegaDanielAI()
      elif self.NAME == "Kenny":
        self.KennyAI()
      elif self.NAME == "Lascelles":
        self.LascellesAI()
      elif self.NAME == "Matvey":
        self.MatveyAI()
      elif self.NAME == "Dereck":
        self.DereckAI()
      elif self.NAME == "Trump":
        self.TrumpAI()
      elif self.NAME == "Kennedy":
        self.KennedyAI()
      elif self.NAME == "Lincoln":
        self.LincolnAI()
      elif self.NAME == "Obama":
        self.ObamaAI()
      elif self.NAME == "Sanders":
        self.SandersAI()
      elif self.NAME == "Musk":
        self.MuskAI()
      elif self.NAME == "The Fence":
        self.FenceAI()
      elif "Heal" in self.GEND:
        self.HealAI()
      else:
        self.enemyattacksys(self.attack,"Auto")
      
  def enemyattacksys(self,types,name,al="",en=""):
    global lastat
    global player1
    hit = 0
    targs = []
    for x in player1.teamS:
      targs.append(x)
    for x in player1.team:
      if len(x.duel) >0 and x not in self.duel:
        targs.remove(x.NAME)
    if len(targs) == 0:
      time.sleep(1)
      print("\n" + self.NAME,"does nothing!")
    if len(self.duel) > 0:
      hit = self.duel[1].NAME
      self.lastattack = name
      lastat = name
    elif len(self.taunted) > 0:
      hit = self.taunted[1].NAME
      self.lastattack = name
      lastat = name
    else:
      hit = random.choice(targs)
      self.lastattack = name
      lastat = name
    for x in player1.team:
      if hit == x.NAME:
        if al != "" and en != "":
          types(x,al,en)
        elif al == "" and en != "":
          types(x,en)
        elif al != "" and en == "":
          types(x,al)
        elif al == "" and en == "":
          types(x)

  def AmiraAI(self):
    global lastat
    self.skills = []
    self.turncount = self.turncount + 1
    enemy2 = ""
    enemy3 = ""
    enemy4 = ""
    enemy5 = ""
    for x in bots.team:
      if x.NAME == "Kelly":
        enemy2 = x
      if x.NAME == "Jackie":
        enemy3 = x
      if x.NAME == "Abby":
        enemy4 = x
      if x.NAME == "Meryem":
        enemy5 = x
    if self.turncount <= 3:
      if enemy2 != "":   
        self.skills.append("Calligraphy")
      self.skills.append("Auto-Attack")
    if self.turncount > 3:   
      if enemy2 != "":
        for x in range(3):
          self.skills.append("Calligraphy")
        self.skills.append("Perfect Requiem")
      for x in range(3):
        self.skills.append("Auto-Attack")
    bruh = random.choice(self.skills)
    if self.turncount == 4 and enemy2 != "":
      self.enemyattacksys(self.AmiraPerfectrequiem,"Perfect Requiem",al=bots,en=you)
    elif self.turncount == 5 and enemy4 != "":
      self.giant()
      self.lastattack = "Giant"
      lastat = "Giant"
    elif len(bots.deadteam) > 0 and enemy2 !="":
      yo = random.choice(bots.deadteam)
      self.AmiraRevive(yo)
      self.lastattack = "Revive"
      lastat = "Revive"
    elif bruh == "Calligraphy":
      self.enemyattacksys(self.calligraphy,"Calligraphy")
      self.cMP = self.cMP + 20
    elif bruh == "Auto-Attack": 
      self.enemyattacksys(self.attack,"Auto")
    elif bruh == "Perfect Requiem":
      self.enemyattacksys(self.AmiraPerfectrequiem,"Perfect Requiem",al=bots,en=you)

  def giant(self):
    time.sleep(1)
    print("\n"+self.NAME,"turns into a giant, increasing their physical damage drastically but reducing her evasion and magic attack tremendously!")
    self.giantess = 7

  def AmiraPerfectrequiem(self,enemy,al,targ):
    global sett
    time.sleep(1)
    print("\n"+self.NAME,"""takes out her violin and breathes, "Perfect Requiem..." """)
    time.sleep(1)
    if self.giantess > 0:
      print("\n"+self.NAME,"plays through the battle, striking her notes to hit everyone!")
      for x in targ.team:
        score = 10
        for x in range(10):
          diff = x.cEV - self.cAC
          if random.randint(1,100) <= diff:
            score = score - 1
        time.sleep(0.2)
        if score == 0:
          print("\n"+x.NAME,"dodges all hits!")
          x.specialdodgecases(self,0.5,"Magical Ranged")
        else:
          sett = x.cHP
          dmg = score*self.cMAT*0.5
          x.defense(self,"Magical",dmg)
          if x.cHP>0:
            if (sett-x.cHP) == 0:
              print("\n"+x.NAME,"gets hit",score,"times, but takes no damage!")
            else:
              print("\n"+x.NAME,"gets hit",score,"times, taking",fore.PURPLE_1B + style.BOLD + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n"+x.NAME,"gets hit",score,"times, taking",fore.PURPLE_1B + style.BOLD + str(sett-x.cHP)+ style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Magical Ranged") 
    else:    
      score = 10
      for x in range(10):
        diff = enemy.cEV - self.cAC
        if random.randint(1,100) <= diff:
          score = score - 1
      if score == 0:
        print("\n"+self.NAME,"plays through the battle, but",enemy.NAME,"dodges all the notes!")
        enemy.specialdodgecases(self,0.5,"Magical Ranged")
      else:
        sett = enemy.cHP
        dmg = score*self.cMAT*0.5
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME,"plays through the battle, striking her notes to hit",enemy.NAME,score,"times, but deals no damage!") 
          else:
            print("\n"+self.NAME,"plays through the battle, striking her notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!") 
        else:
          print("\n"+self.NAME,"plays through the battle, striking her notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.4,dmg,"Magical Ranged") 
      if enemy.cHP > 0:
        enemy.currentstats(targ,al)
        sett = enemy.cHP
        diff = enemy.cEV - round(2*self.cAC)
        self.cMPN = round(self.cMPN*2)
        CT = random.randint(1,100)
        time.sleep(2)
        if random.randint(1,100) <= diff:
          print("\n"+self.NAME, "attempts to stun her opponent, but fails!")
          enemy.specialdodgecases(self,0.5,"Magical Melee",CT)
        else:
          print("\n"+self.NAME,"achieves stunning her opponent.")
          time.sleep(1)
          print("\n"+self.NAME+": The finale...")
          time.sleep(1)
          if enemy.coun == True:
            enemy.counter(self,CT) 
          if CT <= self.cCT:
            dmg2 = self.CTdmg*7*self.cMAT
            enemy.defense(self,"Magical",dmg)
            if enemy.cHP > 0:
              if (sett-enemy.cHP) == 0:
                print("\n"+self.NAME, "delivers the ultimate final blow, but deals no damage!")
              else:
                print("\n"+self.NAME, "delivers the ultimate final blow, dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME, "has",enemy.cHP,"health remaining!")
            else:
              print("\n"+self.NAME, "delivers the ultimate final blow, dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"fades into specs of light...")   
          else:    
            dmg2 = 7*self.cMAT
            enemy.defense(self,"Magical",dmg2)
            if enemy.cHP <= 0:
              if (sett-enemy.cHP) == 0:
                print("\n"+self.NAME,"delivers the final blow, but deals no damage!")
              else:
                print("\n"+self.NAME,"delivers the final blow, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"fades into specs of light...")
            else:
              print("\n"+self.NAME,"delivers the final blow, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME, "has",enemy.cHP,"health remaining!")
          enemy.onhittimersdefense(self,0.4,dmg2,"Magical Melee") 

  def AmiraRevive(self,ally):
    bots.team.append(ally)
    bots.teamS.append(ally.NAME)
    bots.deadteam.remove(ally)
    bots.deadteamS.remove(ally.NAME)
    bots.teamID.append(ally.ID)
    ally.deturn = 0
    ally.cHP = round(0.5*ally.fHP)
    if ally.re == True:
      ally.resttimer = 21 - (ally.res)
    time.sleep(1)
    print(back.GREY_100 + fore.BLACK + style.BOLD+"\n"+self.NAME,"revives",ally.NAME+"!" + style.RESET)
  
  def MrsWellsAI(self):
    global lastat
    attacks = []
    self.turncount = self.turncount + 1
    for x in you.team:
      if x.cHP < round(0.1*x.fHP) and x.invis <=0:
        for y in range(4):
          attacks.append("Candy")
    for x in range(2):
      attacks.append("Auto-Attack")
    attacks.append("Notebook Evaluation")
    if self.tw1 > 0:
      for x in range(self.tw1):
        attacks.append("Notebook Evaluation")
    bruh = random.choice(attacks)
    if (self.turncount%5) == 0:
      self.minusfullpoints(you)
      self.lastattack = "Minus Full Points"
      lastat = "Minus Full Points"
    elif bruh == "Auto-Attack":
      self.enemyattacksys(self.attack,"Auto")
      self.tw1 = self.tw1 + 1
    elif bruh == "Candy":
      for x in you.team:
        if x.cHP < round(0.1*x.fHP) and (x.invis <=0 or x.revealed > 0):
          candyL = []
          candyL.append(x)
      if len(self.duel) > 0:
        self.candy(self.duel[1])
      if len(self.taunted) > 0:
        self.candy(self.taunted[1])
      else:
        yes = random.choice(candyL)
        self.candy(yes)
      self.lastattack = bruh
      lastat = bruh
    elif bruh == "Notebook Evaluation":
      self.notebookevaluation()
      self.lastattack = bruh
      lastat = bruh

  def notebookevaluation(self):
    time.sleep(1)
    if self.notes <=6:
      self.notecount = self.notecount + 1
      print("\n"+self.NAME,"throws out a packet of notes for calculus!")
      poo = Entity("Note Packet",1,0,0,0,0,0,0,0,0,0,0,0,0,str(self.notecount+17),"None")
      bots.team.append(poo)
      bots.teamS.append("Note Packet")
      bots.teamID.append(str(self.notecount+17))
      allfighters.append(poo)
      self.notes = self.notes + 1
    if self.notes == 7:
      print("\n"+self.NAME+": It's time for a notebook evaluation!")
      time.sleep(1)
      print("\n*"+self.NAME,"checks how many note packets the team has*")
      time.sleep(1)
      if self.missingnotes >0:
        print(self.NAME+": Missing",self.missingnotes,"packets, huh? Well, all of you will sure be missing your grades soon...")
        time.sleep(1)
        print("\n"+self.NAME,"cuts the entire team's health by",str(15*self.missingnotes)+"%!\n")
        for x in you.team:
          self.prehiteffects(x)
          sett = x.cHP
          x.cHP = x.cHP - round((0.15*self.missingnotes)*x.fHP)
          time.sleep(0.2)
          if x.cHP <= 0:
            print(x.NAME,"takes",(sett-x.cHP),"damage!",x.NAME,"falls...")
          else:
            print(x.NAME,"takes",(sett-x.cHP),"damage!",x.NAME,"has",x.cHP,"health remaining!")
      else:
        print(self.NAME+": Hmm...you've done well taking notes! Here's something for all of you.")
        time.sleep(1)
        print("\n"+self.NAME,"gives everyone candy, healing the entire team's health by 20%!\n")
        for x in you.team:
          sett = x.cHP
          x.cHP = x.cHP + round(0.2*x.fHP)
          if x.cHP > x.fHP:
            x.cHP = x.fHP
          time.sleep(0.2)
          print(x.NAME,"heals for",fore.MEDIUM_SPRING_GREEN+str(x.cHP-sett)+style.RESET,"health!",x.NAME,"has",x.cHP,"health now!")
      self.notes = 0
      self.missingnotes = 0
          
  def minusfullpoints(self,targ):
    time.sleep(1)
    print("\n"+self.NAME,"takes off all 100 points from everyone's math grade, cutting everyones health by 20%!\n")
    for x in targ.team:
      self.prehiteffects(x)    
      sett = x.cHP
      diff = x.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        print(x.NAME,"doesn't care about their grade, taking no damage!")
        x.specialdodgecases(self,0.1)
      else:
        x.cHP = x.cHP - round(0.2*x.fHP)
        time.sleep(0.2)
        if x.cHP <= 0:
          print(x.NAME,"takes",(sett-x.cHP),"damage!",x.NAME,"falls...")
        else:
          print(x.NAME,"takes",(sett-x.cHP),"damage!",x.NAME,"has",x.cHP,"health remaining!")
        
  def candy(self,enemy):
    time.sleep(1)
    sett = enemy.cHP
    enemy.cHP = enemy.cHP + round(0.5*enemy.fHP)
    if enemy.cHP > enemy.fHP:
      enemy.cHP = enemy.fHP
    enemy.candyAC = 11
    print("\n"+self.NAME,"tosses a bar of chocolate at",enemy.NAME+"! They consume it, healing",fore.MEDIUM_SPRING_GREEN+ str(enemy.cHP-sett) + style.RESET,"health, but reducing their accuracy by 100% for 10 turns!")

  def MrPudupAI(self):
    global lastat
    attacks = []
    self.turncount = self.turncount + 1
    for x in range(8):
      attacks.append("Auto-Attack")
    for x in range(3):
      attacks.append("Shiny Bald Head")
    for x in range(4):
      attacks.append("Roast")
    for x in you.team:
      if x.fear <= 0:
        attacks.append("Laugh")
      if x.burnt > 0:
        attacks.append("Shiny Bald Head")
        attacks.append("Shiny Bald Head")
    bruh = random.choice(attacks)
    if (self.turncount%6) == 0:
      self.quickmafs()
      self.lastattack = "Quick Mafs"
      lastat = "Quick Mafs"
    elif bruh == "Auto-Attack":
      self.enemyattacksys(self.attack,"Auto")
    elif bruh == "Shiny Bald Head":
      roasted = []
      for x in you.team:
        if x.burnt > 0 and (x.invis <=0 or x.revealed > 0):
          roasted.append(x)
      if len(roasted) > 0 and len(self.taunted) <=0 and len(self.duel) <=0:
        yes = random.choice(roasted)
        self.shinybaldhead(yes)
      else:
        self.enemyattacksys(self.shinybaldhead,"Shiny Bald Head")
      self.lastattack = bruh
      lastat = bruh
    elif bruh == "Laugh":
      self.laugh(you)
      self.lastattack = bruh
      lastat = bruh
    elif bruh == "Roast":
      self.enemyattacksys(self.roast,"Roast")

  def laugh(self,targ):
    time.sleep(1)
    print("\n"+self.NAME,"does his weird laugh, fearing everyone!")
    for x in targ.team:
      x.fear = 4

  def roast(self,enemy):
    time.sleep(1)
    yo = random.randint(1,2)
    if enemy.NAME == "Daniel":
      if yo == 1:
        print("\nMr. Pudup: Daniel, babies with cancer.")
        time.sleep(0.2)
        print("Daniel: BFUGHUAHAHA!")
      else:
        print("\nMr. Pudup: Imagine being the kid who Naruto runs across the hallway Daniel...*Inhales loudly*")
    if enemy.NAME == "Ishraq":
      if yo == 1:
        print("\nMr. Pudup: Holy crap Ishraq, why don't you use classes to make your game? 20k lines...jeez!")
      else:
        print("\nMr. Pudup: Can someone tell Ishraq to cut his god damn hair already?")
    if enemy.NAME == "Kelly":
      if yo == 1:
        print("\nMr. Pudup: Oh no! You got a 99 on this assignment Kelly! Shame on you!")
      else:
        print("\nMr. Pudup: Kelly, you seem to break the stereotype that people with perfect grades can't be leaders. Too bad you're a girl studying engineering. *Inhales loudly*")
    if enemy.NAME == "Julius":
      if yo == 1:
        print("\nMr. Pudup: Julius, it's honestly bad our class encourages your singing.")
      else:
        print("\nMr. Pudup: I like you Julius. We're both masochistic cross country runners. *Inhales loudly*")
    if enemy.NAME == "Tim":
      if yo == 1:
        print("\nMr. Pudup: Who keeps laughing at Tim's puns? THEY NEED TO STOP!")
      else:
        print("\nMr. Pudup: Oh god, why hasn't anyone bullied you yet Tim?")
    if enemy.NAME == "Arwyn":
      if yo == 1:
        print("\nMr. Pudup: I have never had you as a student Arwyn. So shoo.")
      else:
        print("\nMr. Pudup: You play League of Legends Arwyn? Tell your family I send my condolences.")
    time.sleep(1)
    print("\n"+self.NAME,"roasts",enemy.NAME+", igniting them!")
    if enemy.burnt < 4:
      enemy.burnt = 4
    enemy.burnd = enemy.burnd + round(self.cMAT*0.5)

  def shinybaldhead(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    print("\n"+self.NAME,"points his shiny bald head at",enemy.NAME+"!")
    diff = enemy.cEV - self.cAC
    time.sleep(0.5)
    if random.randint(1,100) <= diff:
      print("\n"+enemy.NAME,"looks away from the sun's glare reflecting from",self.NAME+"'s bald head")
      enemy.specialdodgecases(self,0.5)
    else:
      if enemy.blind <3:
        enemy.blind = 3
      print("\n"+enemy.NAME,"is blinded by the sun's glare reflecting from",self.NAME+"'s bald head")
      if enemy.burnt > 0:     
        sett = enemy.cHP
        dmg = 2*self.cMAT
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\nThe flames on",enemy.NAME,"from being roasted are sent ablaze, but deal no damage!")
          else:
            print("\nThe flames on",enemy.NAME,"from being roasted are sent ablaze, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\nThe flames on",enemy.NAME,"from being roasted are sent ablaze, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
      
  def quickmafs(self):
    time.sleep(1)
    operands = ["+","-","x"]
    math = random.choice(operands)
    choices = ["A","B","C","D"]
    if math == "+":
      c1 = random.randint(1,144)
      c2 = random.randint(1,144)
      c3 = random.randint(1,144)
      c4 = random.randint(1,144)
      c5 = random.randint(1,144)
      c6 = random.randint(1,144)
      c7 = random.randint(1,144)
      c8 = random.randint(1,144)
      A = c1 + c2
      B = c3 + c4
      C = c5 + c6
      D = c7 + c8     
    elif math == "-":
      c1 = random.randint(1,144)
      c2 = random.randint(1,144)
      c3 = random.randint(1,144)
      c4 = random.randint(1,144)
      c5 = random.randint(1,144)
      c6 = random.randint(1,144)
      c7 = random.randint(1,144)
      c8 = random.randint(1,144)
      A = c1 - c2
      B = c3 - c4
      C = c5 - c6
      D = c7 - c8
    elif math == "x":
      c1 = random.randint(1,12)
      c2 = random.randint(1,12)
      c3 = random.randint(1,12)
      c4 = random.randint(1,12)
      c5 = random.randint(1,12)
      c6 = random.randint(1,12)
      c7 = random.randint(1,12)
      c8 = random.randint(1,12)
      A = c1 * c2
      B = c3 * c4
      C = c5 * c6
      D = c7 * c8
    correctchoice = random.choice(choices)
    ans = 1                              
    start = time.time()        
    elapsed = 0               
    while elapsed < 5:          
      if correctchoice == "A":
        print("\n"+self.NAME+": What's",c1,math,str(c2)+"?")
      if correctchoice == "B":
        print("\n"+self.NAME+": What's",c3,math,str(c4)+"?")
      if correctchoice == "C":
        print("\n"+self.NAME+": What's",c5,math,str(c6)+"?")
      if correctchoice == "D":
        print("\n"+self.NAME+": What's",c7,math,str(c8)+"?")
      print("\n(A)",A," (B)",B,"\n(C)",C," (D)",D)
      ans = input("Response: ")
      elapsed = time.time() - start
      if (ans.lower() == "a" or ans.lower() == "b" or ans.lower() == "c" or ans.lower() == "d")  and elapsed <5:      
        break
    time.sleep(0.5)
    if (ans.lower() == "a" and correctchoice == "A") or (ans.lower() == "b" and correctchoice == "B") or (ans.lower() == "c" and correctchoice == "C") or (ans.lower() == "d" and correctchoice == "D"):
      yup = random.randint(1,3)
      if yup == 1:
        print("\n"+self.NAME+": Good.")
      elif yup == 2:
        print("\n"+self.NAME+": Good job.")
      elif yup == 3:
        print("\n"+self.NAME+": Yeah, around that.")
      time.sleep(0.5)
      print("\nThe team gets the question right!")
    else:
      yup = random.randint(1,2)
      if yup == 1:
        print("\n"+self.NAME+": You're all kidding, right?")
      elif yup == 2:
        print("\n"+self.NAME+": *Deep sigh*")
      time.sleep(0.5)
      print("\n"+self.NAME,"roasts everyone, igniting all allies!")
      for x in you.team:
        if x.burnt < 4:
          x.burnt = 4
        x.burnd = x.burnd + round(self.cMAT*0.5)

  def TerraAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(2):
      attacks.append("Auto")
      attacks.append("Dark Firaga")
      attacks.append("Tremors")
    if self.turncount > 4:
      for x in range(3):
        attacks.append("Zantetsuken")
      attacks.append("Sacrifice")
    if self.turncount  > 8:
      for x in range(10):
        attacks.append("Ars Solum")
    for x in you.team:
      if x.pbarrier > 0:
        for y in range(10):
          attacks.append("Ars Solum")
      break
    yo = random.choice(attacks)
    if len(you.team) == 0 and self.cMP >=55:
      self.tremors(you)
      self.lastattack = "Tremors"
      lastat = "Tremors"
    elif self.turncount == 1:
      self.enemyattacksys(self.sacrifice,"Sacrifice")
    elif yo == "Dark Firaga" and self.cMP >=50:
      self.enemyattacksys(self.darkfiraga,"Dark Firaga")
    elif yo == "Tremors" and self.cMP >=55:
      self.tremors(you)
      self.lastattack = yo
      lastat = yo
    elif yo == "Ars Solum" and self.cMP >=50:
      breakl = []
      for x in you.team:
        if x.pbarrier > 0:
          breakl.append(x)
      if len(breakl) > 0 and len(self.taunted) <=0 and len(self.duel) <=0:
        yup = random.choice(breakl)
        self.ars(yup,bots,you)
      else:
        self.enemyattacksys(self.ars,"Ars Solum",al=bots,en=you)
      self.lastattack = yo
      lastat = yo
    elif yo == "Zantetsuken" and self.cMP >=50:
      self.zantetsuken()
      self.lastattack = "Zantetsuken"
      lastat = "Zantetsuken"
    elif yo == "Sacrifice" and self.cMP >=50:
      self.enemyattacksys(self.sacrifice,"Sacrifice")
    else:
      self.enemyattacksys(self.attack,"Auto")
    
  def sacrifice(self,enemy):
    global sett 
    self.prehiteffects(enemy)
    time.sleep(1)
    self.cMP = self.cMP - 50
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME,"tries to lock",enemy.NAME,"in place, but fails!")
      enemy.specialdodgecases(self,0.5,"True Melee")
    else:
      print("\n"+self.NAME,"locks",enemy.NAME,"in place!")
      if enemy.coun == True:
        enemy.counter(self)
      sett = enemy.cHP
      selfsett = self.cHP
      self.cHP = self.cHP - round(0.1*self.cHP)
      dmg = (selfsett-self.cHP)
      enemy.cHP = enemy.cHP - dmg
      time.sleep(0.5)
      if enemy.cHP > 0:
        print("\n"+self.NAME,"sacrifices",(selfsett-self.cHP),"of his health to deal it to",enemy.NAME+"!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+self.NAME,"sacrifices",(selfsett-self.cHP),"of his health to deal it to",enemy.NAME+"!",enemy.NAME,"falls...")
      time.sleep(0.3)
      if self.cHP >=0:
        print("\n"+self.NAME,"has",self.cHP,"health now!")
      else:
        print("\n"+self.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"True Melee")
      self.onhittimersdefense(self,0.5)

  def darkfiraga(self,enemy):
    global sett
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 50
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "shoots a dark firaga at",enemy.NAME+", but misses!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      enemy.decayd = enemy.decayd + (self.cMAT)
      if enemy.decayt < 2:
        enemy.decayt = 2
      sett = enemy.cHP
      dmg = self.cMAT*2.5
      enemy.defense(self,"Magical",dmg)
      if random.randint(1,100) <= self.cCT:
        enemy.blind = 3
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME, "shoots a dark firaga at",enemy.NAME+", blinding them but dealing no damage!")
          else:
            print("\n"+self.NAME, "shoots a dark firaga at",enemy.NAME+", blinding them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "shoots a dark firaga at",enemy.NAME+", blinding them and dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      else:
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME, "shoots a dark firaga at",enemy.NAME+", but deals no damage!")
          else:
            print("\n"+self.NAME, "shoots a dark firaga at",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "shoots a dark firaga at",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")

  def zantetsuken(self):
    self.cMP = self.cMP - 50
    self.zanc = 1
    time.sleep(1)
    print("\n"+self.NAME+": You're done.")
    time.sleep(0.2)
    print(self.NAME,"is charging a devasting attack!")
  
  def zanslash(self,enemy):
    global sett
    sett = enemy.cHP
    diff = enemy.cEV - self.cAC 
    CT = random.randint(1,100)
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n" + self.NAME, "tries to cut through",enemy.NAME+", but they dodge!")
      enemy.specialdodgecases(self,0.5,"Physical Melee",CT)
    else:
      if enemy.coun == True:
        enemy.counter(self,CT) 
      if CT <= self.cCT:
        dmg = 4*self.CTdmg*self.cAT
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n" +self.NAME,"critically cuts through",enemy.NAME + ", but deals no damage!")
          else:
            print("\n" +self.NAME,"critically cuts through",enemy.NAME,"dealing",style.BOLD+ fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else: 
          print("\n" +self.NAME,"critically cuts through",enemy.NAME,"dealing",style.BOLD+ fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      else:
        dmg = 4*self.cAT
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n" +self.NAME,"cuts through",enemy.NAME + ", but deals no damage!")
          else:
            print("\n" +self.NAME,"cuts through",enemy.NAME,"dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else: 
          print("\n" +self.NAME,"cuts through",enemy.NAME,"dealing",style.BOLD+str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.4,dmg,"Physical Melee")
      self.onhittimersoffense(enemy,0.4)
    self.zanc = 0

  def ars(self,enemy,ally,targ):
    global sett
    self.cMP = self.cMP - 50
    count = 8
    time.sleep(1)
    print("\n"+self.NAME,"unleashes a series of attacks!")
    deez = 0
    bruh = []
    for x in targ.team:
      if (x.invis <=0 or x.revealed > 0):
        bruh.append(x)
    for x in range(count):
      self.prehiteffects(enemy)
      deez = deez + 1
      diff = enemy.cEV - self.cAC 
      sett = enemy.cHP
      if random.randint(1,100) <= diff:
        time.sleep(0.2)
        print("\n" + self.NAME, "attacks, but", enemy.NAME, "dodges!")
        enemy.specialdodgecases(self,0.1,"Physcial Melee")
      else:
        if enemy.coun == True:
          enemy.counter(self)
        if deez <= 5:
          time.sleep(0.2)
          dmg = self.cAT
          enemy.defense(self,"Physical",dmg)
        elif deez > 5:
          time.sleep(0.5)
          dmg = (1.3**(3-(count-deez)))*self.cAT
          if self.cAPN > enemy.cDF or enemy.cDF<=0:
            enemy.cHP = enemy.cHP - round((1.3**(3-(count-deez)))*self.cAT*enemy.dmgreduct)
          else:
            enemy.cHP = enemy.cHP - round((1.3**((3-(count-deez))) *enemy.dmgreduct *self.cAT * (1-(((enemy.cDF)-self.cAPN)/((enemy.cDF+100)-self.cAPN)))))
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n" +self.NAME,"attacks",enemy.NAME + ", but deals no damage!")
          else:
            print("\n" +self.NAME,"attacks",enemy.NAME,"dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else: 
          print("\n" +self.NAME,"attacks",enemy.NAME,"dealing",fore.ORANGE_1+style.BOLD+str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.1,dmg,"Physical Melee")
        self.onhittimersoffense(enemy,0.1)
        if enemy.cHP <=0:
          if len(bruh) > 1:
            bruh.remove(enemy)
            enemy = random.choice(bruh)
          else:
            break
        else:
          enemy.currentstats(targ,ally)

  def AquaAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    if self.cMP >=50:
      attacks.append("Glacier")
      attacks.append("Thunder Shot")
      if self.seeker <= 0:
        attacks.append("Seeking Mine")
      if self.ragestorm == False:
        for x in range(4):
          attacks.append("Raging Storm")
      for x in you.team:
        if x.mgh[0] <=0:
          attacks.append("Magic Hour")
          break
    if len(attacks) > 0:
      yo = random.choice(attacks)
    else:
      yo = ""
    if len(you.teamS) == 0:
      if self.ragestorm == False and self.cMP >=50:
        self.ragingstorm(you)
        self.lastattack = "Raging Storm"
        lastat = "Raging Storm"
      elif self.seeker <=0 and self.cMP >=50:
        self.seekingmine()
        self.lastattack = "Seeking Mine"
        lastat = "Seeking Mine"
    if yo == "Raging Storm":
      self.ragingstorm(you)
      self.lastattack = yo
      lastat = yo
    elif yo == "Seeking Mine":
      self.seekingmine()
      self.lastattack = yo
      lastat = yo
    elif yo == "Glacier":
      self.glacier(you)
      self.lastattack = yo
      lastat = yo
    elif yo == "Thunder Shot":
      self.enemyattacksys(self.thundershot,"Thunder Shot")
    elif yo == "Magic Hour":
      self.magichour(you,bots)
      self.lastattack = yo
      lastat = yo
    elif self.cMP < 50:
      self.mvolley = self.mvolley + 1
      self.enemyattacksys(self.attack,"Auto")

  def ragingstorm(self,targ):
    time.sleep(1)
    self.cMP = self.cMP - 50
    self.ragestorm = True
    for x in targ.team:
      x.rages = [21,self]
      x.burnt = 1
    for x in targ.backteam:
      x.rages = [21,self]
      x.burnt = 1
    for x in targ.deadteam:
      x.rages = [21,self]
      x.burnt = 1
    print("\n"+self.NAME,"unleashes the raging storm, summoning pillars of flames around her! The flames emanate across the battlefield!")

  def thundershot(self,enemy):
    global sett
    time.sleep(1)
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 50
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "jolts a lightning ball at",enemy.NAME+", but misses!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      enemy.paralyzed = 2
      sett = enemy.cHP
      dmg = self.cMAT*5
      enemy.defense(self,"Magical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME, "jolts a lightning ball at",enemy.NAME+", but deals no damage!")
        else:
          print("\n"+self.NAME, "jolts a lightning ball at",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+self.NAME, "jolts a lightning ball at",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")

  def seekingmine(self):
    time.sleep(1)
    self.cMP = self.cMP - 50
    self.seeker = 3
    print("\n"+self.NAME,"sets up a magic minefield around herself!")

  def glacier(self,targ):
    global sett
    time.sleep(1)
    self.cMP = self.cMP - 50
    print("\n" + self.NAME,"summons a glacier from the sky, crashing it down onto her enemies.")
    for x in targ.team:
      time.sleep(0.2)
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n" + x.NAME,"escapes the crash landing!")
        x.specialdodgecases(self,0.1,"Magical Ranged")
      else:
        x.frozen = 1
        sett = x.cHP
        dmg = 2.5*self.cMAT
        x.defense(self,"Magical",dmg)
        if x.cHP >0:
          if (sett-x.cHP) == 0:
            print("\n" + x.NAME, "is smashed by the glacier, freezing up but taking no damage!")
          else:
            print("\n" + x.NAME, "is smashed by the glacier, freezing up and taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          print("\n" + x.NAME, "is smashed by the glacier, freezing up and taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")

  def magichour(self,targ,ally):
    global sett
    self.cMP = self.cMP-50
    self.mgh = [11,self]
    for x in targ.team:
      x.mgh = [11,self]
    for x in targ.backteam:
      x.mgh = [11,self]
    for x in targ.deadteam:
      x.mgh = [11,self]
    time.sleep(1)
    print("\n"+self.NAME,"""warps the battlefield, "Magic Hour..." """)
    time.sleep(0.5)
    print("\nReality begins to bend, slowing down all allies and increasing",self.NAME+"'s evasion!")
    time.sleep(0.5)
    bruh = []
    for x in targ.team:
      if (x.invis <=0 or x.revealed > 0):
        bruh.append(x)
    for boob in range(5):
      time.sleep(0.3)
      if len(bruh) > 0:
        enemy = random.choice(bruh)
        if len(self.duel) > 0:
          if self.duel[1] in bruh:
            enemy = self.duel[1]
        elif len(self.taunted) > 0:
          if self.taunted[1] in bruh:
            enemy = self.taunted[1]
        self.prehiteffects(enemy)
        diff = enemy.cEV - self.cAC 
        if random.randint(1,100) <= diff:
          print("\n"+self.NAME,"teleports overhead and tries to dive at",enemy.NAME + ", but misses!")
          enemy.specialdodgecases(self,0.5,"Magical Melee")
        else:
          sett = enemy.cHP
          if enemy.coun == True:
            enemy.counter(self)
          dmg = self.cAT
          enemy.defense(self,"Magical",dmg)
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"teleports overhead and dives at",enemy.NAME + ", but deals no damage!")
            else:
              print("\n"+self.NAME,"teleports overhead and dives at", enemy.NAME + ", dealing", fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
            enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
          else:
            print("\n"+self.NAME,"teleports overhead and dives", enemy.NAME + ", dealing", fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
            enemy.onhittimersdefense(self,0.2,dmg,"Magical Melee")
            if enemy.cHP <= 0:
              bruh.remove(enemy)
            else:
              enemy.currentstats(targ,ally)
      else:
        break

  def NicoleAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(4):
      attacks.append("Witch's Kiss")
    for x in range(2):
      attacks.append("Beauty Guru")
      self.pbarrier = 0
    if self.nhd > 0:
      for x in range(5):
        attacks.append("Auto")
    for x in you.team:
      if (x.WI == True or x.valor > 0 or x.immortal > 0 or x.runhigh > 0 or x.SHIE > 0 or x.isoboost > 0 or x.OB > 0 or x.thehut > 0 or x.ionzied > 0 or x.knightb > 0 or x.safety > 0 or x.chronotime > 0 or x.quenshield == True or x.tension > 0 or x.chadwalked > 0 or x.manaflow > 0):
        attacks.append("Leech")
    yo = random.choice(attacks)
    if self.cHP <= round(0.3*self.fHP) and self.nap == 1:
      self.catnap()
    elif self.guardian <= 0:
      self.medicalthot()
      self.lastattack = "Medical Thot"
      lastat = "Medical Thot"
    elif self.nhd <=0 and self.turncount >5:
      self.nhdrip()
      self.lastattack = "North Haledon Drip"
      lastat = "North Haledon Drip"
    elif yo == "Leech":
      targ = []
      for x in you.team:
        if (x.WI == True or x.valor > 0 or x.immortal > 0 or x.runhigh > 0 or x.SHIE > 0 or x.isoboost > 0 or x.OB > 0 or x.thehut > 0 or x.ionzied > 0 or x.knightb > 0 or x.safety > 0 or x.chronotime > 0 or x.quenshield == True or x.tension > 0 or x.chadwalked > 0 or x.manaflow > 0):
          targ.append(x)
      at = random.choice(targ)
      self.hwleech(at)
      self.lastattack = yo
      lastat = yo
    elif yo == "Witch's Kiss":
      self.enemyattacksys(self.witchkiss,"Witch's Kiss")
    elif yo == "Beauty Guru":
      self.enemyattacksys(self.beautyguru,"Beauty Guru")
    elif yo == "Auto":
      self.enemyattacksys(self.attack,"Auto")

  def witchkiss(self,enemy):
    time.sleep(1)
    if enemy.GEN == "Male":
      diff = enemy.cEV - (2*self.cAC)
    else:
      diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "tries to kiss",enemy.NAME+", but they push her back!")
      enemy.specialdodgecases(self,0.5)
    else:
      print("\n"+self.NAME,"kisses",enemy.NAME+", poisoning them!")
      if enemy.poisont < 3:
        enemy.poisont = 3
      enemy.poisond = enemy.poisond + ((5/3)*self.cMAT)

  def hwleech(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    print("\n"+self.NAME+", slowly approaching",enemy.NAME+": Heyyy, can you give me your homework, kay' thanks bye.")
    time.sleep(0.5)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      if enemy.GEN == "Male":
        print("\n"+enemy.NAME,"does not fall for",self.NAME+"'s seduction!")
      else:
        print("\n"+enemy.NAME,"bitch-slaps",self.NAME+"!")
      enemy.specialdodgecases(self,0.5)
    else:
      if enemy.GEN == "Male":
        print("\n"+enemy.NAME,"gives up everything they have, losing all their buffs!")
      else:
        print("\n"+enemy.NAME,"is disguested, losing all their buffs!")
      time.sleep(0.5)
      sett = enemy.cHP
      if enemy.GEN == "Male" and enemy.poisont > 0:
        if self.cMPN > enemy.cMDF or enemy.cMDF<=0:
          enemy.cHP = enemy.cHP - round(self.cMAT*3*enemy.dmgreduct)
        else:
          enemy.cHP = enemy.cHP - round(self.cMAT*3*(1-(((enemy.cMDF)-self.cMPN)/((enemy.cMDF+100)-self.cMPN))) *enemy.dmgreduct)
      else:
        if self.cMPN > enemy.cMDF or enemy.cMDF<=0:
          enemy.cHP = enemy.cHP - round(self.cMAT*2*enemy.dmgreduct)
        else:
          enemy.cHP = enemy.cHP - round(self.cMAT*2*(1-(((enemy.cMDF)-self.cMPN)/((enemy.cMDF+100)-self.cMPN))) *enemy.dmgreduct)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+enemy.NAME,"takes no damage!")
        else:
          print("\n"+enemy.NAME,"takes",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+enemy.NAME,"takes",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,"Magical Ranged")
  
  def beautyguru(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    print("\n"+self.NAME,"runs her hand through her hair, shining it towards",enemy.NAME+"!")
    diff = enemy.cEV - self.cAC
    time.sleep(0.5)
    if random.randint(1,100) <= diff:
      print("\n"+enemy.NAME,"looks away from the sheen of",self.NAME+"'s hair!")
      enemy.specialdodgecases(self,0.5)
    else:
      if enemy.blind < 3:
        enemy.blind = 3
      print("\n"+enemy.NAME,"is blinded by the sheen of",self.NAME+"'s hair!")
    time.sleep(1)
    print("\n"+self.NAME+"'s Versace perfume permeates through the area, leaving a poisonous cloud over the battlefield!")

  def nhdrip(self):
    time.sleep(1)
    print("\n"+self.NAME,"flexes her Tommy-Hilfiger apparel, adding a freeze-effect to her next 3 hits!")
    self.nhd = 3

  def medicalthot(self):
    time.sleep(1)

  def catnap(self):
    time.sleep(1)
    if self.nap <=0:
      print("\n"+self.NAME,"lies down to take her catnap, beginning to regenrate her health!")
      self.nap = 5
    elif self.nap > 0:
      self.cHP = round(self.cHP + (0.05*self.fHP))
      if self.cHP > self.fHP:
        self.cHP = self.fHP
      self.nap = self.nap - 1

  def GrahamAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    if self.turncount <= 4:
      attacks.append("Impulse Punch")
    elif self.turncount > 4:
      attacks.append("Impulse Punch")
      attacks.append("Potential Disaster")
      attacks.append("Short Circuit")
      attacks.append("Gravity Lock")
      attacks.append("Inertial Defense")
      
  def impulsepunch(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME,"impulse punches",enemy.NAME,"but misses!")
      enemy.specialdodgecases(self,0.5,"Physical Melee")
    else:
      sett = enemy.cHP
      if enemy.coun == True:
        enemy.counter(self)
      dmg = 0.1*self.cSP*self.cAT
      enemy.defense(self,"Physical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME,"impulse punches", enemy.NAME +  ", but deals no damage!")
        else:
          print("\n"+self.NAME,"impulse punches", enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\n"+self.NAME,"impulse punches", enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"falls...")
      enemy.onhittimersdefense(self,0.4,dmg,"Physical Melee")

  def potentialdisaster(self,enemy):
    global sett 
    self.prehiteffects(enemy)
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME,"potentially electrocutes",enemy.NAME,"but they are unaffected!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      sett = enemy.cHP
      if enemy.repulsed > 0:
        dmg = enemy.cHP
        enemy.cHP = enemy.cHP - dmg
      else:
        dmg = self.cMAT
        enemy.defense(self,"Magical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME,"potentially electrocutes", enemy.NAME +  ", but deals no damage!")
        else:
          print("\n"+self.NAME,"potentially electrocutes", enemy.NAME + ", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        if enemy.repulsed > 0:
          print("\n"+self.NAME,"disastrously electrocutes", enemy.NAME + ", dealing",style.BOLD+ fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"falls...")
        else:
          print("\n"+self.NAME,"potentially electrocutes", enemy.NAME + ", dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"falls...")
      enemy.onhittimersdefense(self,0.4,dmg,"Magical Ranged")

  def shortcircuit(self,enemy):
    time.sleep(1)
    enemy.scirc = 2
    print("\n"+self.NAME,"short circuits",enemy.NAME+", leaving them a turn to live and increasing their attack and magic attack extremely!")

  def errorpropogation(self):
    self.error = 3
    time.sleep(1)
    print("\n"+self.NAME,"increases his error bound, increasing his evasion extremely and putting up a counter barrier!")

  def inertialdefense(self):
    self.inert = 4
    time.sleep(1)
    print("\n"+self.NAME,"increases his moment of inertia, increasing his damage resistance!")

  def frictionalforce(self):
    self.fricf = 4
    time.sleep(1)
    print("\n"+self.NAME,"increases his coefficient of friction, putting a physical redirection barrier!")
  
  def gravitylock(self,targ):
    for x in targ.team:
      x.glock = 9
    time.sleep(1)
    print("\n"+self.NAME,"increases the gravity in the battlefield, slowing everyone and reducing their evasion!")

  def kinematics(self,targ):
    global sett
    time.sleep(1)
    print("\n" + self.NAME,"creates a crater in the ground! The entire team is dragged towards Earth's core!\n")
    for x in targ.team:
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n" + x.NAME,"is resilient to the core's graviational force!")
        x.specialdodgecases(self,0.1,"Magical Ranged")
      else:
        sett = x.cHP
        if self.glock > 0:
          dmg = 50*self.cMAT
          x.defense(self,"Magical",dmg)
        else:
          dmg = 5*self.cMAT
          x.defense(self,"Magical",dmg)
        if x.cHP >0:
          if (sett-x.cHP) == 0:
            print("\n" + x.NAME, "burns up in Earth's core, but takes no damage!")
          else:
            if self.glock > 0:
              print("\n" + x.NAME, "burns up in Earth's core, taking",style.BOLD+ fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n" + x.NAME, "burns up in Earth's core, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          if self.glock > 0:
            print("\n" + x.NAME, "burns up in Earth's core, taking",style.BOLD+ fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
          else:
            print("\n" + x.NAME, "burns up in Earth's core, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")

  def simpleharmonicmotion(self):
    None
  
  def rotationalmotion(self):
    None

  def powerofgiancoli(self):
    None

  def KellyAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(4):
      attacks.append("Calligraphy")
      attacks.append("Pinpoint")
    attacks.append("Auto-Attack")
    for x in range(self.tw1):
      attacks.append("Perfect Requiem")
    yo = random.choice(attacks)      
    if yo == "Calligraphy":
      self.enemyattacksys(self.calligraphy,"Calligraphy")
      self.cMP = self.cMP + 20
    elif yo == "Pinpoint":
      self.enemyattacksys(self.pinpoint,"Pinpoint")
      self.cMP = self.cMP + 10
    elif yo == "Perfect Requiem":
      self.enemyattacksys(self.AmiraPerfectrequiem,"Perfect Requiem",al=bots,en=you)
    else:
      self.enemyattacksys(self.attack,"Auto")
    if yo != "Perfect Requiem":
      self.tw1 = self.tw1 + 1

  def JuliusAI(self):
    if self.cHP <= round(0.5*self.fHP) and Kelly in you.team:
      self.charm(Kelly)
      self.lastattack = "Charm"
      lastat = "Charm"
    else:
      self.enemyattacksys(self.attack,"Auto")

  def charm(self,enemy):
    time.sleep(1)
    if self.cHP > 0:
      print("\n"+self.NAME,"charms",enemy.NAME+", causing her to fight for him!")
    else:
      print("\n"+self.NAME,"charms",enemy.NAME,"before he falls, causing her to fight for him!")
    you.team.remove(enemy)
    you.teamS.remove(enemy.NAME)
    you.teamID.remove(enemy.ID)
    bots.teamS.append(enemy.NAME)
    bots.teamID.append(enemy.ID)

  def NurseAI(self):
    attacks = []
    death = []
    for x in range(4):
      attacks.append("Auto")
    if self.cMP > 0:
      for x in range(self.tw1):
        attacks.append("Cry")
    for x in you.team:
      if x.cHP < self.cMAT:
        death.append(x)
    yo = random.choice(attacks)
    if self.cry > 0:
      self.nursecry(you)
      self.lastattack = "Cry"
      lastat = "Cry"
    elif len(death) > 0:
      kill = random.choice(death)
      self.nursecry(you,kill)
      self.lastattack = "Cry"
      lastat = "Cry"
    elif yo == "Auto":
      self.tw1 = self.tw1 + 1
      self.enemyattacksys(self.attack,"Auto")
    elif yo == "Cry":
      self.tw1 = 0
      self.nursecry(you)    
      self.lastattack = yo
      lastat = yo
    
  def nursecry(self,targ,enemy=""):
    time.sleep(1)
    if enemy == "":
      if self.cry <= 0:
        self.cry = 4
        self.setHP = self.cHP
        print("\n"+self.NAME,"begins to cry!")
        self.cMP = self.cMP - 5
      else:
        if self.cHP < self.setHP:
          print("\n"+self.NAME,"is startled! She does a supersonic scream, shattering everyone's eardrums. Everyone falls...")
          for x in targ.team:
            x.cHP = 0
        else:
          self.cry = self.cry - 1
          if self.cry == 0:
            print("\n"+self.NAME,"becomes hostile again!")
          else:
            print("\n"+self.NAME,"continues to cry!")
    else:
      print("\n"+self.NAME,"does a supersonic scream at",enemy.NAME,"shattering thier eardrums!",enemy.NAME,"falls...")
      enemy.cHP = 0

  def LibrarianAI(self):
    global lastat
    self.turncount = self.turncount + 1
    if self.tw1 == 0 and self.cHP <= round(0.2*self.fHP):
      self.enemyattacksys(self.curse,"Curse")
      self.tw1 = 1
    elif self.turncount % 3 == 0 and self.cMP >= 10:
      self.cMP = self.cMP - 10
      self.bookflurry(you)
      self.lastattack = "Book Flurry"
      lastat = "Book Flurry"
    else:
      self.enemyattacksys(self.attack,"Auto")

  def curse(self,enemy):
    global sett
    time.sleep(1)
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME,"opens the forbidden book and tries to curse",enemy.NAME+", but they resist it!")
      enemy.specialdodgecases(self,0.1,"True")
    else:
      sett = enemy.cHP
      dmg = enemy.cHP
      print("\n"+self.NAME,"opens the forbidden book and curses",enemy.NAME+", instantly killing them!")
      enemy.cHP = enemy.cHP - dmg
      enemy.onhittimersdefense(self,0.2,dmg,"True")

  def bookflurry(self,targ):
    global sett
    time.sleep(1)
    print("\n"+self.NAME,"levitates books from the shelves and shoots a flurry of them!")
    for y in range(3):
      for x in targ.team:
        self.prehiteffects(x)
        time.sleep(0.1)
        diff = x.cEV - self.cAC
        if random.randint(1,100) <= diff:
          print("\n"+x.NAME,"dodges a book!")
          x.specialdodgecases(self,0.1,"Magical Ranged")
        else:
          sett = x.cHP
          dty = random.randint(1,2)
          if dty == 1:
            dmg = 0.25*self.cMAT
            x.defense(self,"Magical",dmg)
            if x.cHP >0:
              if (sett-x.cHP) == 0:
                print("\n" + x.NAME, "is smacked by a book, but takes no damage!")
              else:
                print("\n" + x.NAME, "is smacked by a book, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n" + x.NAME, "is smacked by a book, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
            x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
          elif dty == 2:
            dmg = 0.5*self.cAT
            x.defense(self,"Physical",dmg)
            if x.cHP >0:
              if (sett-x.cHP) == 0:
                print("\n" + x.NAME, "is smacked by a book, but takes no damage!")
              else:
                print("\n" + x.NAME, "is smacked by a book, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n" + x.NAME, "is smacked by a book, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
            x.onhittimersdefense(self,0.2,dmg,"Physical Ranged")

  def TransformerAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(3):
      attacks.append("Auto")
    attacks.append("Spin")
    yo = random.choice(attacks)
    if self.ovd < 0 and self.cMP >= 15:
      self.overdrive()
    elif yo == "Spin" and self.cMP >= 5:
      self.spin(you)
    else:
      self.enemyattacksys(self.attack,"Auto")

  def overdrive(self):
    self.cMP = self.cMP - 15
    self.ovd = 6
    print("\n"+self.NAME,"goes into overdrive mode, tripling their speed!")

  def spin(self,targ):
    global sett
    self.cMP = self.cMP - 5
    time.sleep(0.5)
    print("\n"+self.NAME,"spins around, attacking everyone!")
    for x in targ.team:
      time.sleep(0.15)
      self.prehiteffects(x)
      sett = x.cHP
      diff = x.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        print("\n"+x.NAME,"dodges the attack!")
        x.specialdodgecases(self,0.0,"Physical Melee")
      else:
        if x.coun == True:
          x.counter(self)
        dmg = self.cAT
        x.defense(self,"Physical",dmg)
        if x.cHP > 0:
          if (sett-x.cHP) == 0:
            print("\n"+x.NAME,"is hit, but takes no damage!")
          else:
            print("\n"+x.NAME,"is hit, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
        else:
          print("\n"+x.NAME,"is hit, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
        x.onhittimersdefense(self,0,dmg,"Physical Melee") 

  def TimAI(self):
    global lastat
    self.turncount = self.turncount + 1
    if self.tw1 == 0:
      self.tw1 = random.choice(you.team)
    else:
      if self.tw1.cHP <=0:
        self.tw1 = random.choice(you.team)
    if self.cMP >= 20:
      self.dab(self.tw1)
    else:
      self.enemyattacksys(self.attack,"Auto")

  def DanielAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(3):
      attacks.append("Auto")
    attacks.append("Grubby Hands")
    if self.cHP >= (0.5*self.fHP) and len(bots.team) > 1:
      attacks.append("Taunt")
    yo = random.choice(attacks)
    if yo == "Grubby Hands" and self.cMP >=20:
      self.enemyattacksys(self.grubbyhands,"Grubby Hands")
    elif yo == "Taunt":
      self.enemyattacksys(self.taunt,"Taunt")
    else:
      self.enemyattacksys(self.attack,"Auto")
  
  def MegaDanielAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(3):
      attacks.append("Auto")
    attacks.append("Grubby Tides")
    yo = random.choice(attacks)
    if (self.turncount%4) == 0:
      self.jabbaattack(you)
    elif yo == "Grubby Tides" and self.cMP >=20:
      self.grubbytides(you)   
    else:
      self.enemyattacksys(self.attack,"Auto")

  def KennyAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(2):
      attacks.append("Auto")
    attacks.append("Stay Shut")
    yo = random.choice(attacks)
    if yo == "Stay Shut" and self.cMP >=5:
      self.enemyattacksys(self.stayshut,"Stay Shut")
      self.cMP = self.cMP - 5
    else:
      self.enemyattacksys(self.attack,"Auto")

  def DereckAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in range(2):
      attacks.append("Auto")
    attacks.append("Awkward Touch")
    yo = random.choice(attacks)
    if yo == "Awkward Touch" and self.cMP >=5:
      self.enemyattacksys(self.awkwardtouch,"Awkward Touch")
      self.cMP = self.cMP - 5
    else:
      self.enemyattacksys(self.attack,"Auto")
  
  def MatveyAI(self):
    global lastat
    self.turncount = self.turncount + 1
    if self.eag <=0 and self.cMP >=5:
      self.eagle()
      self.cMP = self.cMP - 5
    else:
      self.enemyattacksys(self.attack,"Auto")

  def LascellesAI(self):
    global lastat
    self.turncount = self.turncount + 1
    attacks = []
    for x in bots.team:
      if x.cHP <= (0.5*x.fHP):
        attacks.append("God and Anime")
    attacks.append("Auto")
    yo = random.choice(attacks)
    if yo == "God and Anime" and self.cMP >= 10:
      self.godandanime(bots)
      self.cMP = self.cMP - 10
    else:
      self.enemyattacksys(self.attack,"Auto")
    
  def TrumpAI(self):
    global lastat
    self.turncount = self.turncount + 1
  
  def LincolnAI(self):
    global lastat
    self.turncount = self.turncount + 1
  
  def ObamaAI(self):
    global lastat
    self.turncount = self.turncount + 1
  
  def KennedyAI(self):
    global lastat
    self.turncount = self.turncount + 1

  def SandersAI(self):
    global lastat
    self.turncount = self.turncount + 1

  def MuskAI(self):
    global lastat
    self.turncount = self.turncount + 1

  def FenceAI(self):
    global lastat
    self.turncount = self.turncount + 1


  def HealAI(self):
    global lastat
    cos = 0
    if self.NAME == "Ryca":
      cos = 5
    tar = []
    for x in bots.team:
      if x.cHP <= round(0.5*x.fHP):
        tar.append(x)
    if len(tar) >0 and self.cMP >=cos:
      targ = random.choice(tar)
      self.enemyHeal(targ,self.cMAT,cos)
      self.lastattack = "Heal"
      lastat = "Heal"
    else:
      self.enemyattacksys(self.attack,"Auto")
     
  def enemyHeal(self,ally,amount,cost):
    self.cMP = self.cMP - cost
    time.sleep(1)
    sett = ally.cHP
    ally.cHP = ally.cHP + amount
    if ally.cHP > ally.fHP:
      ally.cHP = ally.fHP
    if ally == self:
      print("\n"+self.NAME,"heals themself for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett) + style.RESET,"health!",ally.NAME,"has",ally.cHP,"health now!")
    else:
      print("\n"+self.NAME,"heals",ally.NAME,"for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett) + style.RESET,"health!",ally.NAME,"has",ally.cHP,"health now!")


class World:
  def __init__(self,ROOM,TYPE,RID,ENC): 
    self.ROOM = ROOM
    self.TYPE = TYPE
    self.RID = RID
    self.ENC = ENC
    self.RLV = 1
    self.paths = []
    self.event = False
    self.people = []
    self.objects = []
    self.roomstr = ""
    self.q1 = []
    self.q2 = []
    self.q3 = []
    self.q4 = []
  
  def initroutes(self):
    if self.ROOM == "F-Wing Hallway 1st Floor":
      self.paths = ["FX-Wing Hallway 1st Floor","D-Wing Hallway 1st Floor","F-Wing Media Center","F-Wing Hallway 2nd Floor"]
      self.roomstr = "\n(1) F100-103  (2) F104-107\n(3) F108-11  (4) F112-15\n(5) F116-119"
      self.q1 = ["F100","F101","F102","F103"]
      self.q2 = ["F104","F105","F106","F107"]
      self.q3 = ["F108","F109","F110","F111"]
      self.q4 = ["F112","F113","F106","F107"]
    if self.ROOM == "FX-Wing Hallway 1st Floor":
      self.paths = ["F-Wing Hallway 1st Floor","H-Wing Complex 1st Floor","F-Wing Engineering Shop Room","FX-Wing Hallway 2nd Floor","FX-Wing Nurse's Office"]
      self.roomstr = "\n(1) FX120-123  (2) F124-127\n(3) F128-131  (4) F132-135"
    if self.ROOM == "D-Wing Hallway 1st Floor":
      self.paths = ["F-Wing Hallway 1st Floor","H-Wing Complex 1st Floor","C-Wing Hall 1st Floor","D-Wing Hallway Ground Floor"]
    if self.ROOM == "F-Wing Hallway 2nd Floor":
      self.paths = ["FX-Wing Hallway 2nd Floor","F-Wing Hallway 1st Floor","F-Wing Media Center"]
    if self.ROOM == "H-Wing Complex 1st Floor":
      self.paths = ["H-Wing Complex Ground Floor","D-Wing Hallway 1st Floor","FX-Wing Hallway 1st Floor"]
    if self.ROOM == "FX-Wing Hallway 2nd Floor":
      self.paths = ["F-Wing Hallway 2nd Floor","FX-Wing Hallway 1st Floor"]
    if self.ROOM == "C-Wing Hall 1st Floor":
      self.paths = ["C-Wing Hall Ground Floor","B-Wing Hallway 1st Floor","D-Wing Hallway 1st Floor","C-Wing Media Center","Main Office","Main Lobby",]
    if self.ROOM == "D-Wing Hallway Ground Floor":
      self.paths = ["C-Wing Hall Ground Floor","H-Wing Complex Ground Floor","Cafe 2","D-Wing Hallway 1st Floor"]
    if self.ROOM == "DB-Wing Sector":
      self.paths = ["D-Wing Hallway Ground Floor"]
    if self.ROOM == "H-Wing Complex Ground Floor":
      self.paths = ["H-Wing Complex 1st Floor","D-Wing Hallway Ground Floor","Automotive Building"]
    if self.ROOM == "C-Wing Hall Ground Floor":
      self.paths = ["C-Wing Hall 1st Floor","B-Wing Hallway Ground Floor","D-Wing Hallway Ground Floor","C-Wing Nurse's Office","Cafe 1","Cafe 2",]
    if self.ROOM == "B-Wing Hallway 1st Floor":
      self.paths = ["B-Wing Hallway Ground Floor","C-Wing Hall 1st Floor"]
    if self.ROOM == "Main Lobby":
      self.paths = ["Gymnasium","Auditorium","C-Wing Hall 1st Floor"]
    if self.ROOM == "B-Wing Hallway Ground Floor":
      self.paths = ["C-Wing Hall Ground Floor","B-Wing Hallway 1st Floor","Cafe 1","A-Wing Hallway"]
    if self.ROOM == "A-Wing Hallway":
      self.paths = ["B-Wing Hallway Ground Floor"]
  
  def interface(self):
    global boobs
    global sad
    global quests
    global nextr
    global fi
    global dif
    global fightid
    global fightmod
    autosave()
    #ADD
    fightid = 0
    fightmod = 0
    boobs = 0
    if self.TYPE == "Shop":
      while boobs == 0:
        sad = 0
        print("\nYou are in the",self.ROOM+".")
        choice = input("(1) Talk  (2) Upgrades  (3) Inventory/Storage  (4) Party  (5) Save  (6) Exit\nAction: ")
        if choice.lower() == "talk" or choice == "1":
          if len(self.people) == 0:
            print("\nThere is no one to talk to.")
          else:
            print("")
            print(self.people)
            self.speaktarg(self.people)
        elif choice.lower() == "inventory" or choice.lower() == "storage" or choice == "3":
          yikes = input("\n(1) Use Items  (2) Change Items  (3) Change Equipment  (4) Storage\nAction: ")
          if yikes.lower() == "use items" or yikes == "1":
            self.pltarg(self.useitem)
          elif yikes.lower() == "change items" or yikes == "2":
            self.pltarg(self.changeitem)
          elif yikes.lower() == "change equipment" or yikes == "3":
            self.pltarg(self.changeequip)
          elif yikes.lower() == "storage" or yikes == "4":
            if data[11] == 0:
              print("\nYou do not have the key to open up the storage closets.")
          boobs = 1
        elif choice.lower() == "upgrades" or choice == "2":
          if len(you.isoinventory) == 0:
            print("\nYou have no Isometric Drawings.")
          else:
            self.pltarg(self.upgrades)
          boobs = 1
        elif choice.lower() == "party" or choice == "4":
          yikes = input("\n(1) Main Party  (2) Support Party\nAction: ")
          if yikes.lower() == "main party" or yikes == "1":
            teamswitch()
          elif yikes.lower() == "guest party" or yikes == "2":
            guestswitch()
          if sad == 1:
            continue
          else:
            autosave()
            boobs = 1
        elif choice.lower() == "save" or choice == "5":
          yah = input("\nChoose a file:\n(1)  (2)  (3)  (4)  (5)\nFile: ")
          if yah.isdigit() == True and yah != "0":
            if int(yah) < 6:
              print("\nSaving...")
              save("save",int(yah))
              print("Save complete!")
        elif choice.lower() == "exit" or choice == "6":
          self.campexit()
          if sad == 1:
            continue
          else:
            boobs = 1
    elif self.TYPE == "Camp":
      while boobs == 0:
        sad = 0
        print("\nYou are in the",self.ROOM+".")
        choice = input("(1) Talk  (2) Search  (3) Inventory  (4) Party  (5) Save  (6) Exit\nAction: ")
        if choice.lower() == "talk" or choice == "1":
          if len(self.people) == 0:
            print("\nThere is no one to talk to.")
          else:
            print("")
            print(self.people)
            self.speaktarg(self.people)
          boobs = 1
        elif choice.lower() == "search" or choice == "2":
          if len(self.objects) == 0:
            print("\nThere is nothing to search here.")
          else:
            print("")
            print(self.objects)
            self.speaktarg(self.objects)
          boobs = 1
        elif choice.lower() == "inventory" or choice == "3":
          yikes = input("\n(1) Use Items  (2) Change Items  (3) Change Equipment\nAction: ")   
          if yikes.lower() == "use items" or yikes == "1":
            self.pltarg(self.useitem)
          elif yikes.lower() == "change items" or yikes == "2":
            self.pltarg(self.changeitem)
          elif yikes.lower() == "change equipment" or yikes == "3":
            self.pltarg(self.changeequip)
          boobs = 1
        elif choice.lower() == "party" or choice == "4":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1
        elif choice.lower() == "save" or choice == "5":
          yah = input("\nChoose a file:\n(1)  (2)  (3)  (4)  (5)\nFile: ")
          if yah.isdigit() == True and yah != "0":
            if int(yah) < 6:
              print("\nSaving...")
              save("save",int(yah))
              print("Save complete!")
        elif choice.lower() == "exit" or choice == "6":
          self.campexit()
          if sad == 1:
            continue
          boobs = 1
    elif self.TYPE == "Lair":
       while boobs == 0:
        sad = 0
        print("\nYou are in the",self.ROOM+".")
        choice = input("(1) Talk  (2) Save\nAction: ")
        if choice.lower() == "talk" or choice == "1":
          if len(self.people) == 0:
            print("\nThere is no one to talk to.")
          else:
            print("")
            print(self.people)
            self.speaktarg(self.people)
          boobs = 1
        elif choice.lower() == "save" or choice == "2":
          yah = input("\nChoose a file:\n(1)  (2)  (3)  (4)  (5)\nFile: ")
          if yah.isdigit() == True and yah != "0":
            if int(yah) < 6:
              print("\nSaving...")
              save("save",int(yah))
              print("Save complete!")
    elif self.TYPE == "Nurse":
      while boobs == 0:
        sad = 0
        print("\nYou are in the",self.ROOM+".")
        choice = input("(1) Talk  (2) Rest  (3) Inventory  (4) Party  (5) Save  (6) Exit\nAction: ")
        if choice.lower() == "talk" or choice == "1":
          if len(self.people) == 0:
            print("\nThere is no one to talk to.")
          else:
            print("")
            print(self.people)
            self.speaktarg(self.people)
        elif choice.lower() == "rest" or choice == "2":
          t = []
          b = []
          d = []
          for x in you.team:
            t.append(x)
          for x in you.backteam:
            b.append(x)
          for x in you.deadteam:
            d.append(x)
          for x in t:
            revival(x,o=True)
          for x in b:
            revival(x,o=True)
          for x in d:
            revival(x,o=True)
          print("\nThe team treats their wounds and rests, healing back to full health!")
        elif choice.lower() == "inventory" or choice == "3":
          yikes = input("\n(1) Use Items  (2) Change Items  (3) Change Equipment\nAction: ")   
          if yikes.lower() == "use items" or yikes == "1":
            self.pltarg(self.useitem)
          elif yikes.lower() == "change items" or yikes == "2":
            self.pltarg(self.changeitem)
          elif yikes.lower() == "change equipment" or yikes == "3":
            self.pltarg(self.changeequip)
          boobs = 1
        elif choice.lower() == "party" or choice == "4":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1
        elif choice.lower() == "save" or choice == "5":
          yah = input("\nChoose a file:\n(1)  (2)  (3)  (4)  (5)\nFile: ")
          if yah.isdigit() == True and yah != "0":
            if int(yah) < 6:
              print("\nSaving...")
              save("save",int(yah))
              print("Save complete!")
        elif choice.lower() == "exit" or choice == "6":
          self.campexit()
          if sad == 1:
            continue
          boobs = 1
    elif self.TYPE == "Hall":
      while boobs == 0:
        sad = 0
        print("\nYou are in the",self.ROOM+".")
        choice = input("(1) Travel  (2) Inventory  (3) Quests  (4) Party  (5) Save\nAction: ")
        if choice.lower() == "travel" or choice == "1":
          print("")
          uhoh = input("(1) Main Paths  (2) Classrooms\nAction: ")
          if uhoh == "1" or uhoh.lower() == "main paths":
            print("")
            for x in self.paths:
              print("("+str(self.paths.index(x)+1)+")",x)
            self.roomtarg()
            if sad == 1:
              continue
            boobs = 1
          elif uhoh == "2" or uhoh.lower() == "classrooms":
            print(self.roomstr)
        elif choice.lower() == "inventory" or choice == "2":
          yikes = input("\n(1) Use Items  (2) Change Items  (3) Change Equipment\nAction: ")   
          if yikes.lower() == "use items" or yikes == "1":
            self.pltarg(self.useitem)
          elif yikes.lower() == "change items" or yikes == "2":
            self.pltarg(self.changeitem)
          elif yikes.lower() == "change equipment" or yikes == "3":
            self.pltarg(self.changeequip)
          boobs = 1
        elif choice.lower() == "quests" or choice == "3":
          questcatalog()
          continue
        elif choice.lower() == "party" or choice == "4":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1
        elif choice.lower() == "save" or choice == "5":
          yah = input("\nChoose a file:\n(1)  (2)  (3)  (4)  (5)\nFile: ")
          if yah.isdigit() == True and yah != "0":
            if int(yah) < 6:
              print("\nSaving...")
              save("save",int(yah))
              print("Save complete!")
    elif self.TYPE == "Start": 
      nextr = None
      skip = input("\nSkip Tutorial?\n(1) Yes  (2) No\nResponse: ")
      if skip.lower() == "yes" or skip == "1":
        quests.append("All Hail..")
        world.append(self)
        croom.remove(self)
        ro = rd(1)
        world.remove(ro)
        croom.append(ro)
      elif skip.lower() == "no" or skip == "2":
        quests.append("Origins")
        quests.append("Origins-N")
      eventcheck()
    elif self.TYPE == "Demo":
      sad = 0
      while boobs == 0:
        print("\nYou are in the Colosseum.")
        choice = input("(1) Bosses  (2) Party\nResponse: ")
        if choice == "1" or choice.lower() == "bosses":
          if len(you.team) < 4:
            print("\nGo make a party first!")
          else:
            fi = input("\nWhich boss do you want to fight?\n(1) Amira  (2) Mrs. Wells  (3) Mr. Pudup\n(4) Terra & Aqua  (5) Dr. Graham  (6) Fedora Man\n(7) Wired Ishraq  (8) Bowers  (9) The Soul of Kelly\nResponse: ")
            if fi != "1" and fi != "2" and fi !="3" and fi!="4" and fi !="5" and fi != "9":
              continue
            dif = input("\nDifficulty Setting:\n(1) Easy  (2) Normal\n(3) Hard  (4) Insane\n(5) Nightmare\nResponse: ")
            if dif != "1" and dif !="2" and dif !="3" and dif!="4" and dif !="5" and fi != "9":
              continue
            eventcheck()
          continue
        elif choice == "2":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1

  def pltarg(self,ty):
    tli = input("\nWhere is this member?\n(1) Team  (2) Reserve Team  (3) Fallen Team\nAction: ")
    if tli.lower() == "team" or tli == "1":
      print("")
      for x in you.teamS:
        print("("+str(you.teamS.index(x)+1)+")",x)
      self.plt(ty,you.team,you.teamS)
    if tli.lower() == "reserve team" or tli == "2":
      if len(you.backteam) == 0:
        print("\nThere is no one on reserve!")
      else:
        print("")
        for x in you.backteamS:
          print("("+str(you.backteamS.index(x)+1)+")",x)
        self.plt(ty,you.backteam,you.backteamS)
    if tli.lower() == "fallen team" or tli == "3":
      if len(you.deadteam) == 0:
        print("\nNo one is dead!")
      else:
        print("")
        for x in you.deadteamS:
          print("("+str(you.deadteamS.index(x)+1)+")",x)
        self.plt(ty,you.deadteam,you.deadteamS)

  def plt(self,typ,ar,arS):
    poo = input("Who? ")
    if poo.isdigit() == True and poo != "0":
      if len(ar) >= int(poo):
        for x in ar:
          if x.NAME in arS[(int(poo)-1)]:
            typ(x)
    for x in ar:
      if poo.lower() == x.NAME.lower():
        typ(x)

  def useitem(self,pe):
    print("\n"+pe.NAME+"'s Current Stats:\nHP:",str(pe.cHP)+"/"+str(pe.fHP),"\nMP:",str(pe.cMP)+"/"+str(pe.fMP))
    if pe.isomode == True:
      print("ISO:",str(pe.isopoints)+"\n")
    pe.inventorysystem(you,bots)

  def changeitem(self,pe):
    nice = 0
    while nice == 0:
      print("\n"+pe.NAME+"'s Current Battle Items:")
      print(pe.battleinventory)
      print("")
      poo = input("(1) Equip Items  (2) Remove Items  (3) Exit\nAction: ")
      if poo == "1" or poo.lower() == "equip items":
        if len(you.consumeinventory) == 0:
          print("\nYou have no consumables!")
        elif len(pe.battleinventory) == 4:
          print("\n"+pe.NAME,"is already holding 4 items!")
        else:
          self.eqs(pe,you.consumeinventory)
      elif poo == "2" or poo.lower == "remove items":
        if len(pe.battleinventory) == 0:
          print("\nYou have no equipped items!")
        else:
          self.eqs(pe,pe.battleinventory)
      elif poo == "3" or poo.lower == "exit":
        nice = 1

  def eqs(self,pe,inven):
    print("")
    print(inven)
    if inven == pe.battleinventory:
      poo = input("What do you want to de-equip? ")
    else:
      poo = input("What do you want to equip? ")
    if poo.isdigit() == True and poo != "0":
      if len(inven) >= int(poo):
        item = inven[(int(poo)-1)]
        if inven == you.weaponinventory:
          pe.equipcatalog(pe.weap,item,1)
        elif inven == you.helminventory:
          pe.equipcatalog(pe.helm,item,2)
        elif inven == you.chestinventory:
          pe.equipcatalog(pe.chest,item,3)
        elif inven == you.bootsinventory:
          pe.equipcatalog(pe.boots,item,4)
        elif inven == you.accessinventory:
          pe.equipcatalog(pe.access,item,5)
        elif inven == you.consumeinventory:
          pe.battleinventory.append(item)
          you.consumeinventory.remove(item)
          print("\n"+item,"is transferred into",pe.NAME+"'s inventory.")
        elif inven == pe.battleinventory:
          pe.battleinventory.remove(item)
          you.consumeinventory.append(item)
          print("\n"+item,"is transferred back into storage.")
    for x in inven:
      if poo.lower() == x.lower():
        item = x
        if inven == you.weaponinventory:
          pe.equipcatalog(pe.weap,item,1)
        elif inven == you.helminventory:
          pe.equipcatalog(pe.helm,item,2)
        elif inven == you.chestinventory:
          pe.equipcatalog(pe.chest,item,3)
        elif inven == you.bootsinventory:
          pe.equipcatalog(pe.boots,item,4)
        elif inven == you.accessinventory:
          pe.equipcatalog(pe.access,item,5)
        elif inven == you.consumeinventory:
          pe.battleinventory.append(item)
          you.consumeinventory.remove(item)
          print("\n"+item,"is transferred into",pe.NAME+"'s inventory.")
        elif inven == pe.battleinventory:
          pe.battleinventory.remove(item)
          you.consumeinventory.append(item)
          print("\n"+item,"is transferred back into storage.")
        break
  
  def changeequip(self,pe):
    nice = 0
    while nice == 0:
      print("\n"+pe.NAME+"'s Stats:\nHP:",str(round(pe.fHP))+"\nMP:",str(round(pe.fMP))+"\nMRG:",str(round(pe.fMRG))+"\nAT:",str(round(pe.fAT))+"\nDF:",str(round(pe.fDF))+"\nMAT:",str(round(pe.fMAT))+"\nMDF:",str(round(pe.fMDF)),"\nSP:",str(round(pe.fSP))+"\nAC:",str(round(pe.fAC))+"\nEV:",str(round(pe.fEV))+"\nCT:",str(round(pe.fCT))+"\nAPN:",str(round(pe.fAPN))+"\nMPN:",str(round(pe.fMPN)))
      if pe.isomode == True:
        print("ISO:",str(pe.isopoints))
      damn = input("\nWhat do you want to equip?\n(1) Headgear  (2) Bodygear  (3) Lowergear\n(4) Weapon  (5) Accessory  (6) Exit\nAction: ")
      if damn == "1" or damn.lower() == "headgear":
        if len(you.helminventory) == 0 and pe.helm != "":
          pe.equipcatalog(pe.helm,"",2)
        elif len(you.helminventory) == 0:
          print("\nYou have no headgear!")
        else:
          self.eqs(pe,you.helminventory)
      if damn == "2" or damn.lower() == "bodygear":
        if len(you.chestinventory) == 0 and pe.chest != "":
          pe.equipcatalog(pe.chest,"",3)
        elif len(you.chestinventory) == 0:
          print("\nYou have no bodygear!")
        else:
          self.eqs(pe,you.chestinventory)
      if damn == "3" or damn.lower() == "lowergear":
        if len(you.bootsinventory) == 0 and pe.boots != "":
          pe.equipcatalog(pe.boots,"",4)
        elif len(you.bootsinventory) == 0:
          print("\nYou have no lowergear!")
        else:
          self.eqs(pe,you.bootsinventory)
      if damn == "4" or damn.lower() == "weapon":
        if len(you.weaponinventory) == 0 and pe.weap != "":
          pe.equipcatalog(pe.weap,"",1)
        elif len(you.weaponinventory) == 0:
          print("\nYou have no weapons!")
        else:
          self.eqs(pe,you.weaponinventory)
      if damn == "5" or damn.lower() == "accessory":
        if len(you.accessinventory) == 0 and pe.access != "":
          pe.equipcatalog(pe.access,"",5)
        elif len(you.accessinventory) == 0:
          print("\nYou have no accessories!")
        else:
          self.eqs(pe,you.accessinventory)
      if damn == "6" or damn.lower() == "exit":
        nice = 1
      
  def upgrades(self,pe):
    if pe == Ishraq:
      pe.skills.insert(0,"Counter")
    if pe == Julius:
      pe.skills.insert(0,"Rest")
    check = ""
    sa = 0
    print("")
    for x in pe.skills:
      print("("+str(pe.skills.index(x)+1)+")",x)
    it = input(fore.GREY_100 + "Which skill do you want to upgrade? " + style.RESET)
    if it.isdigit() == True and it != "0": 
      if len(pe.skills) > (int(it)-1):
        check = pe.skills[(int(it)-1)]
    if check in pe.skills:
      if check.lower() == "counter":
        print("\nCounter - A passive ability of Ishraq's, where when he is attacked by any melee attack, he has a chance to counter them. The player must type whatever word is displayed with or without capitalization to successfully counter the enemy. Ishraq automatically counters attacks that he dodges.\n\nLevel 1 - 30% chance to counter, redirects 48% physical damage.\nLevel 2 - 35% chance to counter, redirects 51% physical damage.\nLevel 3 - 40% chance to counter, redirects 54% physical damage.\nLevel 4 - 45% chance to counter, redirects 57% physical damage.\nLevel 5 - 50% chance to counter, redirects 60% physical damage.")
        sa = 1
      elif check.lower() == "wild instinct":
        print("\nWild Instinct - Ishraq triggers his amplified human instincts, boosting certain stats(Attack, Speed, Evasion, Critical Chance) by varying amounts, but decreasing others(Magic Attack, Magic Defense, Accuracy) by 20%, all at the cost of 2.5% of his health(HP) per turn. This ability can be turned on and off whenever with no mana cost.\n\nLevel 1 - 15%   AT increase, 35% SP increase, 30% EV and CT increase.\nLevel 2 - 17.5% AT increase, 40% SP increase, 35% EV and CT increase.\nLevel 3 - 20%   AT increase, 45% SP increase, 40% EV and CT increase.\nLevel 4 - 22.5% AT increase, 50% SP increase, 45% EV and CT increase.\nLevel 5 - 25%   AT increase, 55% SP increase, 50% EV and CT increase.")
      elif check.lower() == "smash":
        print("\nSmash - Ishraq encases his entire body in a holographic armor, allowing him to do a barrage of 3 attacks successively using WASD keys. Each key does has a different effect that amplifies the current and remaining attacks. Using W increases critical chance(CT). Using A increases physical attack(AT). Using S increases armor penetration(APN). Using D increases accuracy(AC). Doing certain sequences adds a special effect at the end of all 3 attacks. This ability costs 40 mana to cast, and can critically hit on each separate attack.\n\nLevel 1 - +10%   CT increase on W, 10%   AT increase on A, 20% APN increase on S, 10% AC increase on D, AAA and DDD combo unlocked by default.\nLevel 2 - +12.5% CT increase on W, 12.5% AT increase on A, 30% APN increase on S, 15% AC increase on D, unlocks -WS combo.\nLevel 3 - +15%   CT increase on W, 15%   AT increase on A, 40% APN increase on S, 20% AC increase on D, unlocks WWW combo.\nLevel 4 - +17.5% CT increase on W, 17.5% AT increase on A, 50% APN increase on S, 25% AC increase on D, unlocks SSS combo.\nLevel 5 - +20%   CT increase on W, 20%   AT increase on A, 60% APN increase on S, 30% AC increase on D, unlocks AD- combo.")
      elif check.lower() == "valorous chant":
        print("\nValorous Chant - Ishraq shouts to rally his teammates, fearing enemies and increasing all allied attack, defense, and speed, each boost in order per ally alive(4 for all, 3 for AT&DF, 2 for AT, 1 for fear), none by himself. Fear reduces enemy damage output by 25% and causes them to take 25% more damage. Allied buffs last for 4 of Ishraq's turns. This ability cost 60 mana to cast.\n\nLevel 1 - 20% AT, DF, and SP increase.\nLevel 2 - 25% AT, DF, and SP increase.\nLevel 3 - 30% AT, DF, and SP increase.\nLevel 4 - 35% AT, DF, and SP increase.\nLevel 5 - 40% AT, DF, and SP increase.")
        sa = 1
      elif check.lower() == "immortality":
        print("\nImmortality - Ishraq becomes too angry to die for 3 turns. He also gains lifesteal when activated. This ability costs 80 mana to cast.\n\nLevel 1 - Gain 30% lifesteal.\nLevel 2 - Gain 40% lifesteal.\nLevel 3 - Gain 50% lifesteal.\nLevel 4 - Gain 60% lifesteal.\nLevel 5 - Gain 70% lifesteal.")
      elif check.lower() == "barrier":
        print("\nBarrier - Ishraq puts up a barrier on himself or an ally that nullifies physical damage for some hits. This ability costs 50 mana to cast.\n\nLevel 1 - Barrier takes one hit.\nLevel 2 - Barrier takes two hits.\nLevel 3 - Barrier takes three hits.\nLevel 4 - Barrier takes four hits.\nLevel 5 - Barrier takes five hits.")
      elif check.lower() == "rest":
        print("\nRest - When Julius dies, he is able to recover from death after some time. He can revive as much as he wants, as long as another member is still alive.\n\nLevel 1 - Revives at 10% HP, takes 20 turns to get back up.\nLevel 2 - Revives at 15% HP, takes 19 turns to get back up.\nLevel 3 - Revives at 20% HP, takes 18 turns to get back up.\nLevel 4 - Revives at 25% HP, takes 17 turns to get back up.\nLevel 5 - Revives at 30% HP, takes 16 turns to get back up.")
        sa = 1
      elif check.lower() == "runner's high":
        print("\nRunner's High - Julius experiences the runner's high, becoming immune to slows and increasing his physical attack(AT) and defense(DF) for 25 global turns. This ability costs 25 mana to cast.\n\nLevel 1 - 50% AT and DF increase.\nLevel 2 - 55% AT and DF increase.\nLevel 1 - 60% AT and DF increase.\nLevel 1 - 65% AT and DF increase.\nLevel 1 - 70% AT and DF increase.")
        sa = 1
      elif check.lower() == "shield":
        print("\nShield - Julius shields himself, recovering a percentage of his maximum health and reducing the damage he takes until it's his turn again. This ability costs no mana.\n\nLevel 1 - 10% max HP heal, 40%   damage reduction.\nLevel 2 - 11% max HP heal, 42.5% damage reduction.\nLevel 3 - 12% max HP heal, 45%   damage reduction.\nLevel 4 - 13% max HP heal, 47.5% damage reduction.\nLevel 5 - 14% max HP heal, 50%   damage reduction.")
      elif check.lower() == "tremors":
        print("\nTremors - Julius sends shockwaves through the ground towards the enemies, dealing physical damage to all enemies based on his physical and magic attack. It has a chance to make enemies fall, stunning and slowing them. If they do not fall, they are still slowed. This ability costs 55 mana to cast.\n\nLevel 1 - 70% AT ratio, 100% MAT ratio, 50% chance to knock over enemies.\nLevel 2 - 75% AT ratio, 120% MAT ratio, 55% chance to knock over enemies.\nLevel 3 - 80% AT ratio, 140% MAT ratio, 60% chance to knock over enemies.\nLevel 4 - 85% AT ratio, 160% MAT ratio, 65% chance to knock over enemies.\nLevel 5 - 90% AT ratio, 180% MAT ratio, 70% chance to knock over enemies.")
      elif check.lower() == "isometric drawings":
        print("\nIsometric Drawings - Julius summons the power of isometric drawings by singing, buffing himself or an ally to increase the level of all their skills by 1, and recovering a great amount of their ISO-transformation points. This ability costs 70 mana to cast.\n\nLevel 1 - Recovers 100 ISO-points.\nLevel 2 - Recovers 150 ISO-points.\nLevel 3 - Recovers 200 ISO-points.\nLevel 4 - Recovers 250 ISO-points.\nLevel 5 - Recovers 300 ISO-points.")
      elif check.lower() == "combo":
        print("\nCombo - Julius combos with an ally, being able to do various abilites. This ability costs 100 mana to cast.\n\nSpace Sprint - With Ishraq, Julius sprints to form a circle on the ground that atomizes enemies, dealing their combined physical attack(AT) as magic damage to all enemies.\n\nLevel 1 - 200% combined AT ratio.\nLevel 2 - 210% combined AT ratio.\nLevel 3 - 220% combined AT ratio.\nLevel 4 - 230% combined AT ratio.\nLevel 5 - 240% combined AT ratio.\n\nBaking - With Kelly, Julius bakes ISO-food, healing the party with their combined magic attack(MAT).\n\nLevel 1 - 200% combined MAT ratio.\nLevel 2 - 220% combined MAT ratio.\nLevel 3 - 240% combined MAT ratio.\nLevel 4 - 260% combined MAT ratio.\nLevel 5 - 280% combined MAT ratio.\n\nT-Pose - With Tim, Julius T-pose, dealing their combined physical attack(AT) and magical attack(MAT) to one enemy as physical damage.\n\nLevel 1 - 300% combined AT and MAT ratio.\nLevel 2 - 320% combined AT and MAT ratio.\nLevel 3 - 340% combined AT and MAT ratio.\nLevel 4 - 360% combined AT and MAT ratio.\nLevel 5 - 380% combined AT and MAT ratio.\n\nGrubby Tides - With Daniel, Julius summons the tides of grease and crashes it down on enemies, dealing combined magic damage, reducing their evasion(EV), and poisoning them.\n\nLevel 1 - 200% combined MAT ratio, 100% combined MAT ratio for poison, -20% EV reduction.\nLevel 2 - 210% combined MAT ratio, 105% combined MAT ratio for poison, -30% EV reduction.\nLevel 3 - 220% combined MAT ratio, 110% combined MAT ratio for poison, -40% EV reduction.\nLevel 4 - 230% combined MAT ratio, 115% combined MAT ratio for poison, -50% EV reduction .\nLevel 5 - 240% combined MAT ratio, 120% combined MAT ratio for poison, -60% EV reduction.\n\nThe Best Dancer - With Arwyn, Julius dances, increaseing everyone's armor penetration(APN) and magic penetration(MPN) by their combined speed(SP) for 3 turns.\n\nLevel 1 - APN and MPN increase by 100% Julius's SP and 100% of Arwyn's SP.\nLevel 2 - APN and MPN increase by 105% Julius's SP and 100% of Arwyn's SP.\nLevel 3 - APN and MPN increase by 110% Julius's SP and 100% of Arwyn's SP.\nLevel 4 - APN and MPN increase by 115% Julius's SP and 100% of Arwyn's SP.\nLevel 5 - APN and MPN increase by 120% Julius's SP and 100% of Arwyn's SP.")       
      elif check.lower() == "calligraphy":
        if pe.isomode == False:
          print("\nCalligraphy - Kelly utilizes the power within her magic calligraphy pen to attack enemies with high accuracy magic damage with written spells. This ability costs 20 mana to cast, and can critically hit.")
        else:
          print("\nCalligraphy - Kelly utilizes the power within her magic calligraphy pen to attack enemies with high accuracy magic damage with written spells. This ability costs 20 mana to cast, can critically hit, and generates triple the ISO-points.")
        print("\nLevel 1 - 100% MAT ratio, 200% accuracy.\nLevel 2 - 125% MAT ratio, 250% accuracy.\nLevel 3 - 150% MAT ratio, 300% accuracy.\nLevel 4 - 175% MAT ratio, 350% accuracy.\nLevel 5 - 200% MAT ratio, 400% accuracy.")
        sa = 1
      elif check.lower() == "asmr":
        print("\nASMR - Kelly performs ASMR using her pen-mic, recovering a percentage of her mana(MP) and increasing everyone's mana regeneration(MRG) at a cost of her 20% of her maximum health(HP).\n\nLevel 1 - 30 MP recovery, 200% MRG increase.\nLevel 2 - 35 MP recovery, 250% MRG increase.\nLevel 3 - 40 MP recovery, 300% MRG increase.\nLevel 4 - 45 MP recovery, 350% MRG increase.\nLevel 5 - 50 MP recovery, 400% MRG increase.")
        sa = 1
      elif check.lower() == "pinpoint":
        print("\nPinpoint - Kelly targets a vital on the enemy, striking it devastatingly, dealing bonus true damage based on her physical attack, on top of her normal damage. This also causes the enemy to bleed based on Kelly's accuracy. Bleed reduces enemy speed(SP) and amplfies an attacker's critical chance(CT) by 50%. This ability costs 10 mana to cast, and can critically strike for the physical portion.\n\nLevel 1 - 60%  bonus true damage based on AT, 100% AC ratio for bleed.\nLevel 2 - 70%  bonus true damage based on AT, 120% AC ratio for bleed.\nLevel 3 - 80%  bonus true damage based on AT, 140% AC ratio for bleed.\nLevel 4 - 90%  bonus true damage based on AT, 160% AC ratio for bleed.\nLevel 5 - 100% bonus true damage based on AT, 180% AC ratio for bleed.")
      elif check.lower() == "heal":
        print("\nHeal - Kelly recovers the health(HP) of an ally or herself by her magic attack(MAT) and 10% of their maximum health. This ability costs 60 mana to cast.\n\nLevel 1 - 200%   MAT ratio.\nLevel 2 - 212.5% MAT ratio.\nLevel 3 - 225%   MAT ratio.\nLevel 4 - 237.5% MAT ratio.\nLevel 5 - 250%   MAT ratio.")
      elif check.lower() == "perfect requiem":
        print("\nPerfect Requiem - Kelly performs the Perfect Requiem, taking out her violin to deal magic damage per successful note. The player is prompted to type 10 keys successively to play notes correctly, all under a short time limit. Each successfully landed note will add to the total damage dealt to the enemy. Landing all her notes prepares the Finale, which deals special effects based on her weapon, but by default dealing massive double penetrating magical damage. This ability costs 100 mana to cast, and the Finale portion can critically strike.\n\nLevel 1 - 30% MAT ratio per note for a total of 300%, Finale MAT ratio at 500%.\nLevel 2 - 35% MAT ratio per note for a total of 350%, Finale MAT ratio at 550%.\nLevel 3 - 40% MAT ratio per note for a total of 400%, Finale MAT ratio at 600%.\nLevel 4 - 45% MAT ratio per note for a total of 450%, Finale MAT ratio at 650%.\nLevel 5 - 50% MAT ratio per note for a total of 500%, Finale MAT ratio at 700%.")
      elif check.lower() == "revive":
        print("\nRevive - Kelly elevates a fallen ally, reviving them for a percentage of their max health(HP).\n\nLevel 1 - Brings fallen to 30% max HP.\nLevel 2 - Brings fallen to 35% max HP.\nLevel 3 - Brings fallen to 40% max HP.\nLevel 4 - Brings fallen to 45% max HP.\nLevel 5 - Brings fallen to 50% max HP.")
      elif check.lower() == "dab":
        print("\nDab - Tim dabs on the enemy dealing magic damage based on his physical attack(AT), speed(SP), and accuracy(AC). Dabbing simultaneously on the same enemy causes every dab to deal increasingly more damage by 10%. This ability costs 20 mana to cast.\n\nLevel 1 - 80%  AT ratio, x(1 + 0.5% SP and AC above 100% ratio).\nLevel 2 - 90%  AT ratio, x(1 + 1%   SP and AC above 100% ratio).\nLevel 3 - 100% AT ratio, x(1 + 1.5% SP and AC above 100% ratio).\nLevel 4 - 110% AT ratio, x(1 + 2%   SP and AC above 100% ratio).\nLevel 5 - 120% AT ratio, x(1 + 2.5% SP and AC above 100% ratio).") 
        sa = 1
      elif check.lower() == "quen":
        print("\nQuen - Tim shields himself or an ally and removes all negative effects from them. The shield lasts for 1 hit, and has a maximum threshold of damage it can shield. This ability costs 80 mana to cast.\n\nLevel 1 - Shielding for 400  maximum damage.\nLevel 2 - Shielding for 800  maximum damage.\nLevel 3 - Shielding for 1200 maximum damage.\nLevel 4 - Shielding for 1600 maximum damage.\nLevel 5 - Shielding for 2000 maximum damage.")
        sa = 1
      elif check.lower() == "chronopower":
        print("\nChronopower - Tim ignites his weapon with the essence of time, causing his normal attacks to deal bonus magic damage and stealing the enemy's speed for 3 turns for 3 attacks. This ability costs no mana.\n\nLevel 1 - 100% bonus MAT on hit, 10% SP steal.\nLevel 2 - 120% bonus MAT on hit, 15% SP steal.\nLevel 1 - 140% bonus MAT on hit, 20% SP steal.\nLevel 1 - 160% bonus MAT on hit, 25% SP steal.\nLevel 1 - 180% bonus MAT on hit, 30% SP steal.")
      elif check.lower() == "protobelt":
        print("\nSafety Belt - Tim uses his ISO-belt to shoot missiles at all enemies, dealing magic damage. The belt pulls him to safety, making sure he dodges the next attack on him. This ability costs 35 mana to cast.\n\nLevel 1 - 70%  MAT ratio.\nLevel 2 - 85%  MAT ratio.\nLevel 3 - 100% MAT ratio.\nLevel 4 - 115% MAT ratio.\nLevel 5 - 130% MAT ratio.")
      elif check.lower() == "rubix cube":
        print("\nRubix Cube - Tim throws one of his rubix cubes at the enemies and it explodes, causing all enemies to start dancing for 1 turns. Dancing enemies either hit their allies nonwillingly with a normal attack, or just dance when by themselves. The radius of this bomb increases with its level, increasing its accuracy. This ability costs 75 mana to cast.\n\nLevel 1 - Blast radius at 100% AC.\nLevel 2 - Blast radius at 110% AC.\nLevel 1 - Blast radius at 120% AC.\nLevel 1 - Blast radius at 130% AC.\nLevel 1 - Blast radius at 140% AC.")
      elif check.lower() == "autosentry":
        print("\nAutosentry - Tim sends out his assistant drone that acts as its own ally, with its own health and stats based on all of Tim's base stats. It automatically attacks whoever and charges up a Zap attack that deals magic damage and paralyzes an enemy for 1 turn.\n\nLevel 1 -")
      elif check.lower() == "grubby hands":
        print("\nGrubby Hands - Daniels rubs an enemy with his greasy hands, poisoning them and reducing their evasion. Poison reduces enemy defense(DF) and magic defense(MDF) by a quarter. This ability costs 20 mana to cast.\n\nLevel 1 - 40% MAT ratio for poison, -20% EV reduction.\nLevel 2 - 50% MAT ratio for poison, -30% EV reduction.\nLevel 3 - 60% MAT ratio for poison, -40% EV reduction.\nLevel 4 - 70% MAT ratio for poison, -50% EV reduction.\nLevel 5 - 80% MAT ratio for poison, -60% EV reduction.")
        sa = 1
      elif check.lower() == "taunt":
        print("\nTaunt - Daniel taunts an enemy, forcing them to attack Daniel for 2 turns. He gains more phrases to taunt with the higher level this ability is, and also has special taunts towards certain enemies. This ability costs no mana.\n\nLevel 1 - 50%   chance to successfully taunt.\nLevel 2 - 62.5% chance to successfully taunt.\nLevel 3 - 75%   chance to successfully taunt.\nLevel 4 - 87.5% chance to successfully taunt.\nLevel 5 - 100%  chance to successfully taunt.")
        sa = 1
      elif check.lower() == "knight's vow":
        print("\nKnight's Vow - Daniel binds himself to an ally, taking a percentage of the damage they take for himself as magic damage and increasing their attack(AT) and magic damage(MAT) based on Daniel's max health(HP). Daniel cannot bond himself to more than one ally. This ability costs 60 mana.\n\nLevel 1 - 40% of damage directed to Daniel, allied AT and MAT increased by 2%   of Daniel's HP.\nLevel 2 - 45% of damage directed to Daniel, allied AT and MAT increased by 2.5% of Daniel's HP.\nLevel 1 - 50% of damage directed to Daniel, allied AT and MAT increased by 3%   of Daniel's HP.\nLevel 1 - 55% of damage directed to Daniel, allied AT and MAT increased by 3.5% of Daniel's HP.\nLevel 1 - 60% of damage directed to Daniel, allied AT and MAT increased by 4%   of Daniel's HP.")
      elif check.lower() == "photosynthesis":
        print("\nPhotosynthesis - Daniel generates food in his body, regenerating a percentage of his maximum health(HP) every turn but drastically lowering his physical attack(AT). This ability can be turned on and off whenever with no mana cost.\n\nLevel 1 - 3% max health heal, 80% AT reduction.\nLevel 2 - 4% max health heal, 75% AT reduction.\nLevel 3 - 5% max health heal, 70% AT reduction.\nLevel 4 - 6% max health heal, 65% AT reduction.\nLevel 5 - 7% max health heal, 60% AT reduction.")
      elif check.lower() == "enlargen":
        print("\nEnlargen - Daniel increases in size for 4 turns, gaining damage reduction and increased physical attack(AT) but lowering his evasion(EV) by 50%. His next normal attack causes him to roll all over the enemies, dealing great physical damage. If Daniel shrinks back down before using his roll attack, he cannot use it. This ability costs 80 mana.\n\nLevel 1 - 30% damage reduction, 12.5% AT increase.\nLevel 2 - 35% damage reduction, 25%   AT increase.\nLevel 3 - 40% damage reduction, 37.5% AT increase.\nLevel 4 - 45% damage reduction, 50%   AT increase.\nLevel 5 - 50% damage reduction, 62.5% AT increase.")
      elif check.lower() == "electron":
        print("\nElectron - Daniel turns himself or anyone into an electron, boosting his or their accuracy(AC), evasion(EV), speed(SP), and magic attack(MAT) for 3 turns. This ability costs 100 mana to cast.\n\nLevel 1 - +20% AC increase, +20% EV increase, +10 SP increase, 15% MAT increase.\nLevel 2 - +25% AC increase, +25% EV increase, +15 SP increase, 25% MAT increase.\nLevel 3 - +30% AC increase, +30% EV increase, +20 SP increase, 35% MAT increase.\nLevel 4 - +35% AC increase, +35% EV increase, +25 SP increase, 45% MAT increase.\nLevel 5 - +40% AC increase, +40% EV increase, +30 SP increase, 55% MAT increase.")
      elif check.lower() == "silence":
        print("\nSilence - Arwyn stays shut like a lil' bruh, silencing himself for 3 turns(cannot cast skills). When silenced, Arwyn passively converts his normal attacks to true damage plus some bonus true damage based on his physical attack(AT) and magic attack(MAT). This ability costs no mana, and the converted damage portion can critically strike.\n\nLevel 1 - 50% bonus true damage based on AT and MAT.\nLevel 2 - 55% bonus true damage based on AT and MAT.\nLevel 3 - 60% bonus true damage based on AT and MAT.\nLevel 4 - 65% bonus true damage based on AT and MAT.\nLevel 5 - 70% bonus true damage based on AT and MAT.")
        sa = 1
      elif check.lower() == "cut myself":
        print("\nCut Myself - Arwyn cuts himself, drastically reducing enemy physical defense(DF) and magical defense(MDF) for 3 hits but causing himself to bleed for 6.7% of his maximum health for 3 turns. This ability costs 35 mana to cast.\n\nLevel 1 - 30% DF and MDF reduction.\nLevel 2 - 35% DF and MDF reduction.\nLevel 3 - 40% DF and MDF reduction.\nLevel 4 - 45% DF and MDF reduction.\nLevel 5 - 50% DF and MDF reduction.")
        sa = 1
      elif check.lower() == "gunblade":
        print("\nGunblade - Arwyn shoots and slashes an enemy with his gunblade, dealing hybrid damage and healing for a percentage of the damage dealt. This ability costs 30 mana to cast.\n\nLevel 1 - 120% AT ratio for physical damage, 150% MAT ratio for magical damage, 50% heal for damage dealt.\nLevel 2 - 140% AT ratio for physical damage, 175% MAT ratio for magical damage, 60% heal for damage dealt.\nLevel 3 - 160% AT ratio for physical damage, 200% MAT ratio for magical damage, 70% heal for damage dealt.\nLevel 4 - 180% AT ratio for physical damage, 225% MAT ratio for magical damage, 80% heal for damage dealt.\nLevel 5 - 200% AT ratio for physical damage, 250% MAT ratio for magical damage, 90% heal for damage dealt.")
      elif check.lower() == "spark net":
        print("\nSpark Net - Arwyn conjures a lightning chain that bounces between enemies up to 6 times, dealing magic damage. Each bounce can individually critically strike. However, critical strikes paralyze the enemy instead of dealing more damage. If there is only one enemy, the chain does not bounce, but paralyzes no matter what and deals double damage. This ability costs 50 mana to cast.\n\nLevel 1 - 40% MAT ratio per bounce.\nLevel 2 - 45% MAT ratio per bounce.\nLevel 3 - 50% MAT ratio per bounce.\nLevel 4 - 55% MAT ratio per bounce.\nLevel 5 - 60% MAT ratio per bounce.")
      elif check.lower() == "from the shadows":
        print("\nFrom The Shadows - Arwyn disappears into the shadows, becoming invisible. While invisible, he is untargetable by any attacks except all-target attacks. He can wait up to 3 turns while invisible before using Flashcut on the enemies. Once Arwyn uses Flashcut, he must react successively to up to 6 QTE's to keep continuing his attack. Each successfull QTE will cause Arwyn to Flashcut a random enemy, dealing physical damage. There is a 1.25 second window between each QTE to react to. The shadows also deal magic damage to the flashcutted enemy if the battle is shrouded in Darkness. This ability costs 75 mana to cast, and each Flashcut can critically strike individually and proc on-hit effects.\n\nLevel 1 - 60%  AT and MAT Flashcut ratio, 60%  MAT Shadow ratio.\nLevel 2 - 70%  AT and MAT Flashcut ratio, 70%  MAT Shadow ratio.\nLevel 3 - 80%  AT and MAT Flashcut ratio, 80%  MAT Shadow ratio.\nLevel 4 - 90%  AT and MAT Flashcut ratio, 90%  MAT Shadow ratio.\nLevel 5 - 100% AT and MAT Flashcut ratio, 100% MAT Shadow ratio.")
      elif check.lower() == "darkness":
        print("\nDarkness - Arwyn shrouds the entire battlefield in darkness for 25 turns, reducing every enemy's accuracy(AC) and increasing his critical chance(CT) and critical damage, and his armor penetration(APN) and magic penetration(MPN). While darkness exists in the battlefield, Arwyn's shadows will be able to Flashcut with him. This ability costs 60 mana to cast.\n\nLevel 1 - -20% AC reduction, +15% CT increase, +10% CT damage increase, 30% APN and MPN increase.\nLevel 2 - -30% AC reduction, +20% CT increase, +15% CT damage increase, 40% APN and MPN increase.\nLevel 3 - -40% AC reduction, +25% CT increase, +20% CT damage increase, 50% APN and MPN increase.\nLevel 4 - -50% AC reduction, +30% CT increase, +25% CT damage increase, 60% APN and MPN increase.\nLevel 5 - -60% AC reduction, +35% CT increase, +30% CT damage increase, 70% APN and MPN increase.")
      if sa == 1:
        print("\nThis ability upgrades naturally through leveling up; at levels 10, 20, 30, and 40 respectively.")
      else:
        self.upg(pe,check)
    if pe == Ishraq:
      pe.skills.remove("Counter")
    if pe == Julius:
      pe.skills.remove("Rest")

  def upg(self,pe,skil):
    hi = 0
    if skil.lower() == "wild instinct":
      print("\nAbility Level:",(pe.wild+1),"->",(pe.wild+2))
      hi = pe.wild
    elif skil.lower() == "smash":
      print("\nAbility Level:",(pe.sma+1),"->",(pe.sma+2))
      hi = pe.sma
    elif skil.lower() == "immortality":
      print("\nAbility Level:",(pe.immort+1),"->",(pe.immort+2))
      hi = pe.immort
    elif skil.lower() == "barrier":
      print("\nAbility Level:",(pe.barr+1),"->",(pe.barr+2))
      hi = pe.barr
    elif skil.lower() == "shield":
      print("\nAbility Level:",(pe.shi+1),"->",(pe.shi+2))
      hi = pe.shi
    elif skil.lower() == "tremors":
      print("\nAbility Level:",(pe.trem+1),"->",(pe.trem+2))
      hi = pe.trem
    elif skil.lower() == "isometric drawings":
      print("\nAbility Level:",(pe.isom+1),"->",(pe.isom+2))
      hi = pe.isom
    elif skil.lower() == "combo":
      print("\nAbility Level:",(pe.comb+1),"->",(pe.comb+2))
      hi = pe.comb
    elif skil.lower() == "pinpoint":
      print("\nAbility Level:",(pe.pinp+1),"->",(pe.pinp+2))
      hi = pe.pinp
    elif skil.lower() == "heal":
      print("\nAbility Level:",(pe.bake+1),"->",(pe.bake+2))
      hi = pe.bake
    elif skil.lower() == "perfect requiem":
      print("\nAbility Level:",(pe.perfectr+1),"->",(pe.perfectr+2))
      hi = pe.perfectr
    elif skil.lower() == "revive":
      print("\nAbility Level:",(pe.rev+1),"->",(pe.rev+2))
      hi = pe.rev
    elif skil.lower() == "chronopower":
      print("\nAbility Level:",(pe.chrono+1),"->",(pe.chrono+2))
      hi = pe.chrono
    elif skil.lower() == "protobelt":
      print("\nAbility Level:",(pe.proto+1),"->",(pe.proto+2))
      hi = pe.proto
    elif skil.lower() == "rubix cube":
      print("\nAbility Level:",(pe.rub+1),"->",(pe.rub+2))
      hi = pe.rub
    elif skil.lower() == "autosentry":
      print("\nAbility Level:",(pe.auto+1),"->",(pe.auto+2))
      hi = pe.auto
    elif skil.lower() == "knight's vow":
      print("\nAbility Level:",(pe.knightv+1),"->",(pe.knightv+2))
      hi = pe.knightv
    elif skil.lower() == "photosynthesis":
      print("\nAbility Level:",(pe.obese+1),"->",(pe.obese+2))
      hi = pe.obese
    elif skil.lower() == "enlargen":
      print("\nAbility Level:",(pe.jabb+1),"->",(pe.jabb+2))
      hi = pe.jabb
    elif skil.lower() == "electron":
      print("\nAbility Level:",(pe.electr+1),"->",(pe.electr+2))
      hi = pe.electr
    elif skil.lower() == "gunblade":
      print("\nAbility Level:",(pe.gunb+1),"->",(pe.gunb+2))
      hi = pe.gunb
    elif skil.lower() == "spark net":
      print("\nAbility Level:",(pe.spark+1),"->",(pe.spark+2))
      hi = pe.spark
    elif skil.lower() == "from the shadows":
      print("\nAbility Level:",(pe.fromthes+1),"->",(pe.fromthes+2))
      hi = pe.fromthes
    elif skil.lower() == "darkness":
      print("\nAbility Level:",(pe.dar+1),"->",(pe.dar+2))
      hi = pe.dar
    yer = 0
    good = 0
    ite = "Isometric Drawing"
    if pe == Ishraq:
      ite = "Red " + ite
    elif pe == Kelly:
      ite = "Magenta " + ite
    elif pe == Julius:
      ite = "Green " + ite
    elif pe == Tim:
      ite = "Cyan " + ite
    elif pe == Daniel:
      ite = "Yellow " + ite
    elif pe == Arwyn:
      ite = "Blue " + ite
    if hi == 0:
      ite = "T2 " + ite
    elif hi == 1:
      ite = "T3 " + ite
    elif hi == 2:
      ite = "T4 " + ite
    elif hi == 3:
      ite = "T5 " + ite
    if hi == 4:
      print("\nThis ability cannot be upgraded any further through Isometric Drawings. It can only be pushed farther by either special equipment or Julius's Isometric Drawings ability.")
    else:
      while yer == 0:
        nig = input("\nAre you sure you want to upgrade this ability?\n(1) Yes  (2) No\nResponse: ")
        if nig == "1" or nig.lower() == "yes":
          if ite not in you.isoinventory:
            print("\nYou do not have a",ite+".")
          else:
            good = 1              
          yer = 1
        if nig == "2" or nig.lower() == "no":
          yer = 1
      if good == 1:
        pe.learnskill(skil.title())
        print("\nYou have upgraded",skil.title()+".")
        you.isoinventory.remove(ite)


  def campexit(self):
    global sad
    global nextr
    sad = 0
    if self.RID == 6 or self.RID == 25:
      ro = rd(2)
    if self.RID == 27:
      ro = rd(8)
    if self.RID == 17:
      nah = 0
      while nah == 0:
        yi = input("\nExit where?\n(1) C-Wing Hall Ground Floor  (2) D-Wing Hallway Ground Floor\nAction: ")
        if yi == "1":
          ro = rd(12)
          nah = 1
        if yi == "2":
          ro = rd(10)
          nah = 1
    if self.RID == 4:
      nah = 0
      while nah == 0:
        yi = input("\nExit where?\n(1) F-Wing Hallway 1st Floor  (2) F-Wing Hallway 2nd Floor\nAction: ")
        if yi == "1":
          ro = rd(1)
          nah = 1
        if yi == "2":
          ro = rd(5)
          nah = 1
    if self.RID == 14:
      ro = rd(9)
    if self.RID == 18:
      ro = rd(11)
    if self.RID == 23:
      ro = rd(16)
    if self.RID == 28:
      ro = rd(3)
    if self.RID == 29:
      ro = rd(9)
    if self.RID == 30:
      ro = rd(11)
    nextr = ro.ROOM
    nextro = ro
    preeventcheck()
    if sad == 0:
      time.sleep(1)
      print("\nThe group exits the",self.ROOM+".")
      eventcheck()
      if sad == 0:
        croom.remove(self)
        world.append(self)
        world.remove(nextro)
        croom.append(nextro)
        
  def travel(self,nextroom):
    global sad
    global nextr
    nextr = nextroom.ROOM
    sad = 0
    preeventcheck()
    if sad == 0:
      time.sleep(1)
      print("\n...")
      time.sleep(1)
      print(".....")
      time.sleep(1)
      self.randomencounter()
      if sad == 0:
        if nextroom.TYPE == "Hall":
          print("\nThe group travels to the",nextroom.ROOM+".")
        elif nextroom.TYPE == "Shop" or nextroom.TYPE == "Camp":
          print("\nThe group enters the",nextroom.ROOM+".")
        eventcheck()
        if sad == 0:
          croom.remove(self)
          world.remove(nextroom)
          world.append(self)
          croom.append(nextroom)
  
  def roomtarg(self):
    global sad
    sad = 0
    wop = 0
    go = input(fore.GREY_100 + "Travel where? " + style.RESET) 
    if go.isdigit() == True:
      if len(self.paths) >= int(go) and go !="0":
        self.simple((int(go)-1))
        wop = 1
    for x in world:
      if go.lower() == x.ROOM.lower() and x.ROOM in self.paths:
        self.travel(x)
        wop = 1
    if wop != 1:
      sad = 1

  def simple(self,ints):
    global sad
    sad = 0
    for x in world:
      if x.ROOM in self.paths[ints]:
        self.travel(x)
        break

  def speaktarg(self,types):
    if types == self.people:
      go = input(fore.GREY_100 + "Who do you want to speak to? " + style.RESET)
    elif types == self.objects:
       go = input(fore.GREY_100 + "What do you want to search? " + style.RESET)
    for x in types:
      if go.lower() == x.lower():
        self.dialogue(x)
    if go.isdigit() == True:
      if len(types) >= int(go) and go != "0":
        go = types[(int(go)-1)]
        self.dialogue(go)
    
  def dialogue(self,subject):

    global fightid
    global fightmod

    if self.RID == 6:
      if "All Hail..." in quests:
        if subject == "Julius":
          text("\n*Ishraq approaches Julius*","Ishraq, throwing a hand signal: Yo","Julius, looking up from his non-functional phone: So we gonna find that straight edge or what?","Ishraq, crossing his arms: Whenever you're ready.","Julius, looking back at his phone: I'll follow you out the door once you're good to go.")
          questsys("The Straight Edge","StartM")
          you.team.append(Julius)
          you.teamS.append("Julius")
          self.people.remove(subject)
        if subject == "Edmond":
          text("\n*Ishraq approaches Edmond*","Ishraq, wrapping his arm around Edmond: How's Kelly?","Edmond: She's breathing, so she ain't dead.","Ishraq: Think she needs anything?","Brandon, examining: She has some bruises, and she's bleeding a little. Gotta get her something.","Ishraq, ready to help: I'll head to the F-Wing nurse and find something. You guys coming?","Edmond: I'm coming with you.")
          questsys("The FX-Wing Nurse","StartM")
          supu("Edmond",21)
          for x in you.suppback:  
            you.suppteam.append(x)
            you.suppteamS.append(x.name)
            you.suppback.remove(x)
            you.suppbackS.remove(x.name)
          self.people.remove("Edmond")
          self.people.remove("Brandon")
        if subject == "Brandon":
          text("\n*Ishraq approaches Brandon*","Ishraq, touching Brandon's shoulder: How's Kelly?","Brandon, biting his nails: She's breathing alright.","Ishraq, looking at Edmond: Think she needs anything?","Edmond, looking a little nervous: She has some bruises and cuts. They look kinda bad.","Ishraq, ready to help: I'll head to the F-Wing nurse and find something for her. You guys coming?","Brandon: I'll go with you.")
          supu("Brandon",21)
          for x in you.suppback:  
            you.suppteam.append(x)
            you.suppteamS.append(x.name)
            you.suppback.remove(x)
            you.suppbackS.remove(x.name)
          questsys("The FX-Wing Nurse","StartM")
          self.people.remove("Edmond")
          self.people.remove("Brandon")
        if subject == "Kelly":
          text("\nIshraq, thinking to himself: (Damn it...how could I lose control like that? I'm sorry Kelly. I'll get those medical supplies for you.)")
      
      if "The FX-Wing Nurse" in quests:
        if subject == "Kelly":
          if "Ice Pack" in you.questinventory:
            text("\nIshraq, staring at Kelly resting: Okay, we got an ice pack.","\n*Julius slaps the ice pack on Kelly's head...She comes back to life!*","Kelly, dizzy: Uuhh...what happened?","Ishraq, feeling bad: Kinda threw you across the room accidently...sorry.","Kelly, no hard feelings: Ehh...I don't feel that bad. My head just hurts a bit. I'm fine though.","Ishraq, picking Kelly up: Fine by me, looks like you're ready to get up and going.","Kelly, happy: You got that right!")
            you.team.append(Kelly)
            you.teamS.append("Kelly")
            self.people.remove(subject)
            if "Brandon" not in you.suppteamS and "Brandon" not in you.suppbackS:
              supu("Brandon",21)
            if "Edmond" not in you.suppteamS and "Edmond" not in you.suppbackS:
              supu("Edmond",21)
            questsys("The FX-Wing Nurse","Finish")
            xpg(200)
            you.questinventory.remove("Ice Pack")
            if "Ruler" in you.questinventory:
              eventcheck()
          else:
            text("\nIshraq, staring at Kelly resting: Gotta go to the Nurse's office.")

      if "Showdown" in quests:
        if subject == "Ishraq":
          text("\n*Kelly sneaks up on Ishraq sleeping and gets close to his ear*\n","Kelly: HIIII ISHRAAQQ!!","*Ishraq slowly opens his eyes and sees Kelly staring at him*","Ishraq, seemingly indifferent: That hurt. Why'd you do that?","Kelly, having no fun: I thought you would've jumped out of your seat...you suck.","Ishraq, sticking his finger in the ear Kelly yelled in: I don't get surprised.","Kelly, covering both of her ears: I think my ears are starting to hurt looking at you picking at yours.","Ishraq: Yeah, but your eardrums weren't deliberately blown out like mine.","\n*Kelly suddenly kneels to the ground and clasps her ears*\n","Kelly, in sharp pain: UGHH!! AAGGHH! AAAHHEAA!","Ishraq, crouching down calmly: Hey, what's wrong?","Kelly, muttering out: M--m--my ears! I h-hearr! This t-terrible noise! It's SO LOUD!!!","Ishraq, getting up and panicking: Shit shit, what do we do!?","*Kelly stops writhing in pain and goes quiet--her eyes widen as she stares at the ground*","Ishraq, scared: Kelly? You..okay?","Kelly, slowly turning her head to Ishraq: The auditorium. We need to go to the auditorium.","Julius, confused: What are you saying, girl?","Kelly, frustrated as she clasps her ears again: HIM! He told me to come!")
          if data[15] == 2:
            text("Ishraq, dissapointed: The Fedora Man, right? The guy you didn't even bother telling anyone about.","Kelly, not dealing with it: You n-never asked! PLEASE! He said he'll stop ear-raping if we start going NOW!","Ishraq, helping her up: Let's get you to the auditorium asap.")
          elif data[15] == 1:
            text("Tim: The Fedora Man?","Kelly, nodding through the pain: Mhmm!","Tim, thinking: He must've put something in your ear. Pretty impressive planning.","Ishraq, helping Kelly up: No time to praise this guy, we need to get her to the auditorium asap.")
          elif data[9] == 1:
            text("Ishraq: Who? Wait..","Kelly, hurting again: GuGHHH! I c-can't explain right NOW!","Ishraq, figuring it out: The Fedora guy that Bowers mentioned. He's behind all this, isn't he.","Kelly: Mhm..I jus-t didn't tell you! He tried to kidnap me before all this! And he's still tryin-ng to get me! HE PUT SOMETHING--IN MY EARS!!","Ishraq, helping Kelly up: Let's get you to the auditorium asap.")
          else:
            text("Ishraq: Who?","Kelly, hurting again: GuGHHH! I c-can't explain right NOW!","Ishraq, really confused as he helps Kelly up: Okaay..I guess we have to go to the auditorium.")
          revival(Ishraq,o=True)
          self.people.remove("Ishraq")

      if subject == "David":
        if self.RLV == 1:
          if data[12] == 0:
            text("\n*Ishraq approaches David*","Ishraq, curious: What happened?","David, yelling in frustration: My birthday circuit! I was almost done! It's messed up now!","Ishraq, laughing: David, we're already working on arduino and you're still working on your birthday circuit? What the hell?","David, ordering his wires: Chill, I was almost done.","Ishraq, wanting to help: Yo, just give me your K-maps and I'll wire it for you.","David, determined: NO! I need to do this myself.","Ishraq, proud: Good. If you need help, I'm here.")
            data[12] = 1
          else:
            text("\n*Ishraq approaches David*","Ishraq, checking on David: You good?","David, working hard: Yeah.")
        
        elif self.RLV == 2:
          text("\n*Kelly approaches David*","Kelly: Maybe it's for you?","*David takes the screwdriver...nothing happens*","David, sad: Damn...I thought it was gonna turn into a diamond sword.","Kelly, inviting: Well, you can always still join the fight. Team. Team. Team. Haha!","David, excited: TEAM! TEAM! TEAM!")
          supu("David",21)
          self.people.remove("David")
        
        else:
          text("\n*Kelly approaches David*","Kelly, inviting: Team. Team. Team. Haha!","David, excited: TEAM! TEAM! TEAM!")
          supu("David",21)
          self.people.remove("David")

      if subject == "Metin":
        if self.RLV == 1:
          if data[16] == 1:
            text("\n*Ishraq approaches Metin*","Ishraq, grim: Someone will pay.","Metin, sad: Me and Noah buried him right outside. You can see his grave from any of the windows.")
            if data[9] == 1 or data[15] == 1:
              text("Ishraq, tensed: When I find this Fedora Man, he's dead. I will literally rip him off this Earth.","Metin, getting up: And I'm going to help you with that.")
            else:
              text("Ishraq, tensed: When I find out, who did this, they're dead. They better watch themselves.","Metin, getting up: And I'm going to help you kill him.")
          else:
            text("\n*Ishraq approaches Metin*","Ishraq, excited: Well well well, we got the unit on our side already.","Metin, grinning: We win now.","Ishraq, smiling: We indeed do. You ready to fight?","Metin, getting up: Yes.")      
          supu("Metin",31)
          data[17] = data[17] + 1
          self.people.remove("Metin")
        
        elif self.RLV == 2:
          text("\n*Kelly approaches Metin*","Kelly: You take a try.","*Metin takes the screwdriver...nothing happens*","Metin, venting: Man, I'm always so unlucky!")
          self.people.remove("Metin")

          
      if subject == "Hassan":
        if self.RLV == 1:
          text("\n*Ishraq approaches Hassan*","Ishraq, pumped: You ready to get out there and trash these kids?","Hassan, also pumped: Yeeah, these wired fuckin' be pissin' me off. We fought some on our way down, and god DAMN they're strong!","Ishraq, shrugging: Hey, we've got to get power in numbers to save this school, and you can always help.","Hassan: Ight' bet. I'm about to cook these dudes.")
          supu("Hassan",21)
          self.people.remove("Hassan")
        
        elif self.RLV == 2:
          text("\n*Kelly approaches Hassan*","Kelly: ...","*Hassan snatches the screwdriver...nothing happens*","Hassan: THIS SOME BS!")
          self.people.remove("Hassan")

      if subject == "Noah":
        if self.RLV == 1:
          if data[16] == 1:
            text("\n*Ishraq approaches Noah*","Ishraq, grim: He was a fighter.","Noah, reflecting: Yeah...we used to joke around a lot. We swore we'd fight one day. I didn't think it would be to the death.",)
            if data[9] == 1 or data[15] == 1:
              text("Ishraq, angry: I'm afraid I have to say...you guys never got to fight. That wasn't a fight. It was you two being puppeteered by the Fedora Man. I will take him down. He's messing with the wrong people.","Noah, getting up: For Hassan.")
            else:
              text("Ishraq, angry: I'm afraid I have to say...you guys never got to fight. That wasn't a fight. It was you two being puppeteered by something. I swear I will find out who's the culprit behind this, and I will take him down.","Noah, getting up: For Hassan.")
          else:
            text("\n*Ishraq approaches Noah*","Ishraq, excited: Aahh, we in this.","Noah, pumped: Put me in coach.","Ishraq, giving a hand: Get up and let's go!")      
          supu("Noah",16)
          data[17] = data[17] + 1
          self.people.remove("Noah")
        
        elif self.RLV == 2:
          text("\n*Kelly approaches Noah*","Kelly: Here, you try.","*Noah takes the screwdriver...nothing happens*","Noah: Damn...")
          self.people.remove("Noah")
        
      if self.RLV == 2:
      
        if subject == "Brandon":
          text("\n*Kelly approaches Brandon*","Kelly: This could be for you.","*Brandon takes the screwdriver...nothing happens*","Brandon: It is what it is.")
          self.people.remove("Brandon")
        
        if subject == "Edmond":
          text("\n*Kelly approaches Edmond*","Kelly: You try it.","*Brandon takes the screwdriver...nothing happens*","Edmond: No biggie.")
          self.people.remove("Edmond")
          
        if subject == "Alvaro":
          text("\n*Kelly approaches Alvaro*","Kelly: You try it.","*Alvaro takes the screwdriver...nothing happens*","Alvaro: I didn't think so, haha.")
          self.people.remove("Alvaro")

        if subject == "Octavio":
          text("\n*Kelly approaches Octavio*","Kelly: You try it.","*Octavio takes the screwdriver...nothing happens*","Octavio: No problem.")
          self.people.remove("Octavio")
        
        if subject == "Tim":
          text("\n*Kelly approaches Tim*","Kelly: Heyy Tim~!","Tim, abnormally normally: Hello.","Kelly: Here, maybe it's for you.","\n*Tim takes the screwdriver...it starts to glow!!! He is absorbed into the screwdriver seconds after! The screwdriver's tip creates a laser outline of Tim's reconstructing body! It begins to screw, slowly filling in Tim's form until he is complete!*\n","Tim, ecsatic: Yay, I'm a power ranger!","\n~Tim is a European 10th grade engineering student at the highschool of PCTI. He is a varsity fencer, VEX competitor, and the fastest builder when it comes to engineering a robot. He has a knack for making original puns constantly to the point where it pisses mostly everyone off. He is not afraid to do the unordinary, and does not really care about what others think about him. He is also at the rebel stage of his Christian boyhood.\n","Kelly, glee: Hooray for you! We found our new ISO!","Tim, play bragging: Ah, of course I would be chosen, as I look amazing from all angles.","Kelly, not knowing he was joking: Sure...so you feel any different?","Tim, trying to feel something: Hmm...I feel more energetic?","Kelly, trying to help release Tim's power: Hmm...what's something you wish you could do, but you can't.","Tim, very specific: I want my dabs to telepthically hurt people.","Kelly, a little hesitant to continue: Ummm...maybe you can try it on me?","Tim: I'd be glad to.","*Tim dabs on Kelly*","Kelly, slightly hurt: Ugghh! Wow...it worked.","Tim, surprised: Wait, it did. OH YEAH! TIME TO DAB ON EVERYTHING!",fore.CYAN_1+style.BOLD+"\n~Tim has gained a new ability, Dab! He dabs on an enemy, dealing magic damage based on his physical attack(AT), speed(SP), and accuracy(AC). Dabbing simultaneously on the same enemy causes every dab to deal increasingly more damage.\n"+style.RESET)
          input("Kelly, inching away from him: Okay...you go do that.")
          if "Metin" in self.people:
            self.people.remove("Metin")
          if "Edmond" in self.people:
            self.people.remove("Edmond")
          if "Brandon" in self.people:
            self.people.remove("Brandon")
          if "Noah" in self.people:
            self.people.remove("Noah")
          if "Hassan" in self.people:
            self.people.remove("Hassan")
          if "Alvaro" in self.people:
            self.people.remove("Alvaro")
          if "Octavio" in self.people:
            self.people.remove("Octavio")
          self.RLV = 3
          self.people.remove("Tim")
          revival(Tim,o=True)
          Tim.learnskill("Dab")
          if "Dab" not in Tim.skills:
            Tim.skills.append("Dab")
          Tim.XP = round(((Kelly.XP + Julius.XP + Ishraq.XP)/3)-100)
          Tim.Timlevelup(Tim.XP,Colis=True)

      if subject == "Dylan":
        if self.RLV == 2:
          text("\n*Kelly approaches Dylan*","Kelly: Possibly for you.","*Dylan takes the screwdriver...nothing happens*","Dylan: Whatever","Kelly: You can still help out. You wrestle, right?","Dylan: Yeah, I do.")
          supu("Dylan",16)
          self.people.remove("Dylan")
        
        else:
          text("\n*Kelly approaches Dylan*","Kelly: You can still help out without an ISO. You wrestle, right?","Dylan: Yeah, I do.")
          supu("Dylan",16)
          self.people.remove("Dylan")

      if subject == "Jahir":
        if self.RLV == 2:
          text("\n*Kelly approaches Jahir*","Kelly: Maybe...","*Jahir takes the screwdriver...nothing happens*","Jahir: I ain't think so either.","Kelly: You can always fight with us still.","Jahir: Sure thing.")
          supu("Jahir",14)
          self.people.remove("Jahir")
        
        else:
          text("\n*Kelly approaches Jahir*","Kelly: Do you want to help us fight?","Jahir: Sure thing.")
          supu("Jahir",14)
          self.people.remove("Jahir")

      if subject == "Andrew":
        if self.RLV == 2:
          text("\n*Kelly approaches Andrew*","Kelly: Who knows...","*Andrew takes the screwdriver...nothing happens*","Andrew: Fuck this.","Kelly, careful: Well...you can still help.","Andrew: Fuck everythin'. I'll help alright. Help beat these niggas assses.")
          supu("Andrew",15)
          self.people.remove("Andrew")
      
        else:
          text("\n*Kelly approaches Andrew*","Kelly, careful: You can still help out.","Andrew: I'll help alright. Help beat these niggas assses.")
          supu("Andrew",15)
          self.people.remove("Andrew")
    
      if subject == "Shannae":
        if self.RLV == 2:
          text("\n*Kelly approaches Shannae*","Shannae, shaking her head: No, no, no.","Kelly, confused: What?","Shannae: It definitely isn't me. I don't like fighting.","Kelly, laughing: Hahaha! You can still help us in other ways.","Shannae: Of course.")
          supu("Shannae",21)
          self.people.remove("Shannae")
        
        else:
          text("\n*Kelly approaches Shannae*","Shannae, shaking her head: No, no, no.","Kelly, confused: What?","Shannae: I don't like fighting.","Kelly, laughing: Hahaha! You can still help us in other ways.","Shannae: Of course.")
          supu("Shannae",21)
          self.people.remove("Shannae")
      
      if "Transmission" in quests:
        if subject == "Metin" or subject == "Brandond" or subject == "Noah" or subject == "Edmond":
          if subject == "Metin":
            text("\n*Kelly approaches Metin*","Kelly, planning to link up: Where did the ISOs go?","Metin, turning his head left and right: Where'd you come from?","Kelly, pointing: A rift opened up near the shelves...didn't you notice?","Metin, confirming: Yeah, I thought I did hear something. Didn't think it was you and this other guy..Arwyn?","Arwyn, depressed: Yeah...it's me.","Metin, focusing: Anyways, they went to the technology room in the H-Wing. We're gonna set up reliable comms around the school.","Kelly, praising the course of action: Huh. That's a good thing to do. I guess we'll be heading there now.")
          if subject == "Brandon":
            text("\n*Kelly approaches Brandon*","Kelly, planning to link up: Where did the ISOs go?","Brandon, looking up from Pudup's desk: You're back. When'd you get here?","Kelly, pointing: A rift opened up near the shelves...didn't you notice?","Brandon, turning around: More teleporting, huh? You got Arwyn with you too..","Arwyn, depressed: Yeah...unfortunately.","Brandon, pointing out the door: They're in technology room right now in the H-Wing. We're settin' up comms around the school.","Kelly, praising the course of action: Huh. That's a good thing to do. I guess we'll be heading there now.")
          if subject == "Noah":
            text("\n*Kelly approaches Noah*","Kelly, planning to link up: Where did the ISOs go?","Noah, getting up from excercising: ..Oh shit, you're back. When did you come?","Kelly, pointing: A rift opened up near the shelves...didn't you notice?","Noah, shaking his head: Nah, I was working out. Ay, it's Arwyn. He came with you?","Arwyn, depressed: Yeah...it's me...she dragged me along.","Noah, guiding: Anyways, the guys went to the technology room in the H-Wing. We're setting up a communication system around the school.","Kelly, praising the course of action: Huh. That is a good thing to do. I guess we'll be heading there now.")
          if subject == "Edmond":
            text("\n*Kelly approaches Edmond*","Kelly, planning to link up: Where did the ISOs go?","Edmond, looking up from his chromebook: Ayo, Kelly is back guys. But like, she just came outta nowhere.","Kelly, pointing: A rift opened up near the shelves...didn't you notice?","Edmond, looking back at his chromebook: Nah, I was type busy making these beats...ayo, Arwyn is here too.","Arwyn, depressed: Yeah...it's me.","Edmond, answering: The ISOs went to the tech room in the H-Wing. We gonna set up comms around the school.","Kelly, praising the course of action: Huh. That is a good thing to do. I guess we'll be heading there now.")
          text("\n~Some time earlier back in the technology room...\n","*The room telephone starts to ring...everyone stares at it*","Julius: It's not gonna be me.","Ishraq, joking around for fun: I ain't pickin' that shit up!","Tim, no fear: I will do it.","*Tim picks up the phone.*","Tim, deeply: #Hello~.#","???, seemingly exhilerated: Finally! Someone picks up!","Tim, fucking around: I could never decline a call from you.","???, bullying: GAY! GAY! GAY!","Ishraq, ears darting forward: Wait a minute...that's--! *Ishraq rushes towards the phone and snatches it from Tim!*","Ishraq, earraping: KHALIL!!","Khalil, also earraping: HELLO ISHRAQ. HOW ARE YOU?","Ishraq, yelling: I AM GOOD, YOU?","Khalil, continuing: I AM GOOD, THANK YOU. LISTEN FRIEND. I NEED HELP.","Ishraq, getting a bit serious: Help?","Khalil, struggling: I AM FIGHTING. FIGHTING DR. PARENT. IT IS TIME.","Ishraq, completely understanding: The Fence.","Khalil, boldy: YES. MAIN OFFICE. NOW.","*Khalil hangs up*\n","Ishraq, long awaited: It is time...","Julius, weirded out: Time? Time for what?","Ishraq, preaching: It's time to take down PCTI's most notorious silent killer...ripping holes into kids' sweaters since it was built...The Fence.","Tim, realizing what's going on: OOH! That Fence! The one outside the F-Wing. But like, why take it down now? We're sort of busy dealing with real issues...","Ishraq, believing: Khalil said it's time. It must be done now.","Tim, sidetracking: Well before we go to the main office, let's go drop off these radios at shop.")
          ro = rd(6)
          croom.remove(ro)
          world.append(ro)
          ro = rd(30)
          world.remove(ro)
          croom.append(ro)
          you.reset("Supp")
          for x in you.ph1:
            you.suppteam.append(x)
            you.suppteamS.append(x.name)
          you.ph1 = []
          you.reset("Team")
          revival(Ishraq,o=True)
          revival(Julius,o=True)
          revival(Tim,o=True)
          revival(Daniel,o=True)
          worldfunction()
        
      
    if self.RID == 14:
 
      if "No Talking in The Library" in quests:
        if subject == "Julius":
          text("\nJulius, turning to Ishraq: Yo, wassup?")
          boop = input("\n(1) Found anything?  (2) Where do you think your girlfriend is?\nResponse: ")
          if boop == "1":
            text("\nIshraq: Found anything?","Julius, looking back at the file cabinets he's searching: Nah, just a bunch of papers in these.","Ishraq, rubbing his goatee: Maybe check out that room behind the front desk?","Julius: Yeah, I'ma go there next.")
          elif boop == "2":
            text("\nIshraq: Where do you think your girlfriend is?","Julius, a little worried: Not sure...I've been thinking about it ever since you woke me up.","Ishraq, planting his hand on Julius's shoulder: You'll find her, don't worry.")
        if subject == "Kelly":
          text("\nKelly, still scavenging books: Yeah Ishraq?")
          if data[15] != 1:
            boop = input("\n(1) What are all these books?  (2) Remember anything about your kidnapper?\nResponse: ")
          elif data[0] >=30:
            boop = input("\n(1) What are all these books?  (2) Sup.\nResponse: ")
          else:
            boop = "0"
            text("\nIshraq, looking at all the books Kelly gathered: What are all these books?","Kelly, looking back at Ishraq: I'm stealing books.","Ishraq, raising an eyebrow: For what?","Kelly, staring: To read them?","Ishraq, confused: Read?","Kelly, dumbfounded: Yeah, read. That's what you do with books.","Ishraq, shrugging: Who actually reads? I haven't read a single one of the class books for English. Sparknotes yo.","Kelly, also shrugging: Okay...good luck in English.","Ishraq, smirking: General. Screw Honors or Lang.")
          if boop == "1":
            text("\nIshraq, looking at all the books Kelly gathered: What are all these books?","Kelly, looking back at Ishraq: I'm stealing books.","Ishraq, raising an eyebrow: For what?","Kelly, staring: To read them?","Ishraq, confused: Read?","Kelly, dumbfounded: Yeah, read. That's what you do with books.","Ishraq, shrugging: Who actually reads? I haven't read a single one of the class books for English. Sparknotes yo.","Kelly, also shrugging: Okay...good luck in English.","Ishraq, smirking: General. Screw Honors or Lang.")
          elif boop == "2" and data[15] == 1 and data[0] >= 30:
            text("\nIshraq: Sup.","Kelly, grinning and imitating Ishraq's voice: #Sup.#, Hehe!")
          elif boop == "2" and data[15] == 0:
            text("\nIshraq: Remember anything about your kidnapper?","Kelly, still slightly flustered: Yeah...I do. I guess I'll just tell you now.","Ishraq, raising a brow: Huh?","Kelly, explaining: Basically, I was walking with Daniel. Daniel saw the guy in the trench coat, and started acting all weird. I couldn't tell if Daniel was acting or not. At first, I thought they were friends acting a skit out together for me or something. But this Fedora guy just charged at me, and Daniel got a little serious for a second. Next thing you know, they were fighting!","Ishraq, amused at the weird situation: HaHAHA! What the hell?","Kelly, continuing: So Daniel lost, and then the guy took me.","Ishraq, getting information: Remember how he looks?","Kelly, recalling: Umm...he had a trenchcoat, long and black...and a fedora on his head.")
            if data[9] != 1:
              text("Ishraq, dying: HAHA? A fedora neckbeard!? What is this!?","Kelly, slightly embarrased: Yeah...it was very strange.","Ishraq, giving her a high five: Hey, at least we know what we're up against. A joke, HA!")
            else:
              text("Ishraq, excited: Hey! Richard mentioned that guy! A fedora neckbeard!? He's behind all this?!","Kelly, slightly embarrased: Yeah...it was very strange.","Ishraq, giving her a high five: Hey, at least we know what we're up against. A joke, HA!")
            data[15] = 1
        if subject == "The Librarian":
          text("\nIshraq, thinking to himself: (She's out cold...she'll wake up soon.)")
      
      if subject == "Bookcase A-D":
          text("\nIshraq, reading a book title: Computer Integrated Manufacturing by Marianne Albarez...I swear I know this name.")
      if subject == "Bookcase E-H":
        if "Calligraphy" not in Kelly.skills:
          text("\nIshraq, taking notice of a glowing book: Huh?","*Ishraq takes the book from the shelf and reads the title*","Ishraq: Isometric Drawings by Wycliffe A. Graham! What the hell? Graham wrote this? Or is it that...","*The book starts to rattle and flies out of Ishraq's hands, falling to the ground*","Ishraq, intrigued: Does Graham have something to do with the iso-stones?","*Ishraq tries to pick up the book, but it vibrates violently in his hands*","Ishraq, connecting the pieces: It's the same as when Kelly touched the stone in shop...")
          talk = "1"
          while talk == "1":
            boop = input("\n(1) Kelly!  (2) Julius!\nResponse: ")
            if boop == "1":
              text("\nIshraq, shouting across the room: Kelly!","Kelly, responding: Yeah?","Ishraq: Come take a look at this book.","\n*Kelly walks over to Ishraq*\n","Kelly, tapping Ishraq: What did you find?","Ishraq, pointing at the book at the floor: Look...it's inching towards you.","Kelly, curious: Wow, that's so cool!..It's also called Isometric Drawings by Wycliffe A. Graham...as in Dr. Graham? *Kelly picks up the book*","Ishraq, thinking about it: Yeah, I find it very strange. Dr. Graham never metioned writing a book, and I doubt he would write it on isometric drawings.","Kelly: Then what do you think is going on?","Ishraq, concluding: No idea, but Graham is definitely connected to what's going on.","Kelly, agreeing: Definitely...now let's see what this book is so excited for.","\n*Kelly opens the book, and a magenta light radiates from it. The book drags Kelly into it, enveloping her! The book turns through all of its pages quickly and finally closes. A holographic light shines from the book, and Kelly's body reconstructs in the shape of magenta outlined geometric planes.*\n","Ishraq, not surprised: Well well well, look who's an Iso-wielder now.",fore.MAGENTA_1 + style.BOLD +"Kelly, feeling the power: Oh my god, I feel so alive right now!"+style.RESET,"\n*Julius runs over to see what's going on*","Julius, looking at the magenta aura around Kelly: YOU GOT AN ISO? SHEEESH!","\n*Kelly's calligraphy pen appears before her inside the book*",fore.MAGENTA_1 + style.BOLD + "Kelly, astonished: Hey! This was just in my bookbag!"+ style.RESET,"*Kelly touches the pen and feels its energy*",fore.MAGENTA_1 + style.BOLD + "Kelly, feeling comfort: It's filled with some type of power. I feel it."+style.RESET,style.BOLD + fore.MAGENTA_1 + "\n~Kelly has gained a new ability, Calligraphy! She utilizes the power within her magic calligraphy pen to attack enemies with high accuracy magic damage with written spells!\n" + style.RESET)
              talk = "2"
              data[0] = data[0] + 3
              data[1] = data[1] - 1
            elif boop == "2":
              text("\nIshraq, shouting across the room: Julius!","Julius, shouting back: What?!","Ishraq: Come check this out.","\n*Julius runs over to Ishraq*\n","Julius: Yeah?","Ishraq, looking at the book: Look at that book...shit's moving.","Julius, happy: Hey! It looks like it's comin' to me! Didn't Kelly say that the stone she found was going towards you?","Ishraq, nodding: Yeah, she did. Read the cover though.","Julius, crouching down: Isometric Drawings by Wycliffe A. Graham. As in GRAHAM?! HaHAA!","Ishraq, laughing: Heheh, yeah. I find it kind of weird too.","Julius, memeing: We all already knew Graham is god, so he's probably behind all this.")
              if data[15] == 1:
                text("Ishraq, skeptical: Nah, I don't think he's causing all this...has to be the Fedora Man.")
              else:
                text("Ishraq, taking it into consideration: Maybe, but I doubt it. Graham would never do this.")
              text("\n*Julius tries to pick up the book, but it starts shaking violently*\n","Julius, confused: What gives?","Ishraq, mentioning: Kelly also said when she picked up my Iso, it shook violently in her hands...","Julius, disappointed: Damn.","Ishraq, shouting across the room.: Kelly!","\n*Kelly walks over to Ishraq*\n","Kelly, responding: What?","Ishraq, pointing at the book at the floor: Look...it's inching towards you.","Kelly, curious: Wow, that's so cool!..It's also called Isometric Drawings by Wycliffe A. Graham...as in Dr. Graham?","\n*Kelly picks up the book*\n","Ishraq, confirming: Yeah, it's weird. Me and Julius think he's involved in some way","Kelly, agreeing: Definitely...now let's see what this book is so excited for.","\n*Kelly opens the book, and a magenta light radiates from it. The book drags Kelly into it, enveloping her! The book turns through all of its pages quickly and finally closes. A holographic light shines from the book, and Kelly's body reconstructs in the shape of magenta outlined geometric planes.*\n","Ishraq, not surprised: Well well well, look who's an Iso-wielder now.",fore.MAGENTA_1 + style.BOLD + "Kelly, feeling the power: Oh my god, I feel so alive right now!" + style.RESET,"\n*Kelly's calligraphy pen appears before her inside the book*\n",fore.MAGENTA_1 + style.BOLD + "Kelly, astonished: Hey! This was just in my bookbag!"+ style.RESET,"\n*Kelly touches the pen and feels its energy*\n",fore.MAGENTA_1 + style.BOLD + "Kelly, feeling comfort: It's filled with some type of power. I feel it."+style.RESET,style.BOLD + fore.MAGENTA_1 + back.GREY_100+"\n~Kelly has gained a new ability, Calligraphy! She utilizes the power within her magic calligraphy pen to attack enemies with high accuracy magic damage with written spells!\n" + style.RESET)
              talk = "2"
              data[1] = data[1] + 3
          Kelly.learnskill("Calligraphy")
          text("\nIshraq, suddenly suspecting: Too convenient though. Exactly where you said you think it was, you found your isometric drawing Kelly. Someone's listening to us.",fore.MAGENTA_1 + style.BOLD +"Kelly, shocked: Woah, you're right. This is kind of creepy."+style.RESET,"Julius, taking it different: Creepy? This means I should get mine in the Automotive Building! Let's go!","Ishraq: Yeah.")
        else:
          text("\nIshraq, scratching his head: Hmm...The Great Gatsby by F. Scott Fitzgerald...did I read this?")
      if subject == "Bookcase I-L":
        text("\nIshraq, confused: The Definition of Pushing Buttons by Elpresador? This is in the wrong section.")
      if subject == "Bookcase M-P":
        text("\nIshraq, picking out a book: The Crucible by Arthur Miller...I feel like I've read this before.")
      if subject == "Bookcase Q-T":
        text("\nIshraq: Shakespeare. Wasn't he gay?")
      if subject == "Bookcase W-Z":
        text("\nIshraq: The Webster dictionary. This could be useful...Eh, not worth lugging back to shop.")
      if subject == "Computers":
        text("\nIshraq: Hey, Julius. You think a keyboard would make a good weapon?","Julius, laughing: HaHAA, sure.","Ishraq: Word.")
        additem("Keyboard",1,you.weaponinventory)
        self.objects.remove("Computers")
      if subject == "Front Desk":
        text("\nIshraq, opening the drawers of the front desk: Just some pencils...could be deadly.")
        additem("Pencil",2,you.weaponinventory)
        self.objects.remove("Front Desk")

    if self.RID  == 17:

      if subject == "Snacks Crate":
        if "Daily Checkup" not in quests and "Medical Attention" not in quests:
          text("\nIshraq, searching in the storage unit: There's some boxes here.","Julius, dancing over: Yooo~! These are Doritos! Where's the G-Fuel?","Ishraq, laughing: We're really about to live off of Doritos and Scooby Snacks, haha.")
        else:
          text("\nJulius, searching in the storage unit: Yooo~! These are Doritos!","Julius, dancing over: Yooo~! These are Doritos! Where's the G-Fuel?","Metin: Oh shit, gimme dem' scooby snacks.")
        additem("Blue Doritos",16,you.consumeinventory)
        additem("Scooby Snacks",16,you.consumeinventory)
        self.objects.remove("Snacks Crate")
      
      if subject == "Fuze Crate":
        if "Daily Checkup" not in quests and "Medical Attention" not in quests:
          if "The FX-Wing Nurse" not in quests:
            text("\nKelly, shouting: Guys! I found Ice Tea!","Ishraq, coming over: Aaah. Fuze.","Julius: Brisk is better.","Ishraq, sharing: You know, our school used to give out Brisk. It was too unhealthy or something, so they switched over to Fuze.")
          else:
            text("Noah, stumbling upon: Yo! There's some Ice Tea here!","Ishraq, coming over: Aaah. Fuze.","Julius: Brisk is better.","Ishraq, sharing: You know, our school used to give out Brisk. It was too unhealthy or something, so they switched over to Fuze.")
        else:
          if "The FX-Wing Nurse" not in quests:
            text("\nKelly, shouting: Guys! I found Ice Tea!","Julius, coming over: Nice.")
          else:
            text("Noah, stumbling upon: Yo! There's some Ice Tea here!","Julius, coming over: Nice.")
        additem("Fuze",12,you.consumeinventory)
        self.objects.remove("Fuze Crate")
      
      if subject == "Dead Bodies":
        if "Daily Checkup" not in quests and "Medical Attention" not in quests:
          input("\nIshraq, curious: I'm gonna look at the dead bodies...")
          if "The FX-Wing Nurse" not in quests:
            input("Kelly, gagging: Yeah#! You can do that yourself.")
          text("Metin, joining Ishraq: I wanna see them too...I'm wondering if anyone I know died.","Ishraq, ready: Alright, let's go check them out.","\n*Ishraq and Metin walk over to some corpses*\n","Ishraq, observing closely: Hmm...it seems like they were impaled by something, ya heard?","Metin, crouching down: Yeah...look at this girl tho'.","Ishraq, taking a look: What?","Metin, staring back at a boy's corpse: There's no blood surrounding the girl. She's not fully impaled either. And look! There's no blood where she got impaled! What?!","Ishraq, shook: Holy shit...you're right!","Metin, standing back up: I don't think I know any of these people...wait, I think that's Daniella.","Ishraq: Who's that?","Metin: That's Nicole's best friend.","Ishraq: Espinoza?","Metin: Yeah.","Ishraq: Unforunate.")
        else:
          text("\n*Julius walks over to some corpses*\n","Julius, poking at a kid: These guys are really dead...","Metin, joining Julius: I'm wondering if anyone I know died.","Julius, observing closely: Hmm...these guys were stabbed by something. Big holes in all these kids' bodies.","Metin, crouching down: Yeah...look at this girl tho'.","Julius, taking a look: What?","Metin, staring back at a boy's corpse: There's no blood surrounding the girl. She's not fully impaled either. And look! There's no blood where she got impaled! What?!","Julius, shook: HaHAA~! Nah, something weeeird is going on.","Metin, standing back up: I don't think I know any of these people...wait, I think that's Daniella.","Julius: Who?","Metin: That's Nicole's best friend.","Julius: The medical one?","Metin: Yeah.","Julius: Bruh.")
        self.objects.remove("Dead Bodies")
      
      if subject == "Note":
        if "Daily Checkup" not in quests and "Medical Attention" not in quests:
          text("\nIshraq, noticing a slip of paper on the lunch counter: What's that?","Julius: A paper.","Ishraq, opening it up: Hmm...the ink smells fresh.","\n*Ishraq begins to read the paper aloud*\n",'"I am at school right now. I don’t know if I will survive. My phone is not working. I am being chased by other students. I am hiding here all alone. Everyone is trying to kill me. I tried to approach my friends, but they seemed off. I was scared at first, but I tried to speak to them anyway. As soon as I spoke, they all turned and chased me. I ran for my life. A girl caught up to me. She tackled me to the ground. I thought I was dead. But then, something happened. I felt my back explode full of life...and then suddently the girl on top of me stopped moving. Blood came out of her mouth and all over my face. I was horrified at first. But then this thing pulled the girl off of me. I slowly stood up. I observed the life going away from this girl rapidly. I do not know why, but...I felt good."',"\nJulius: Creeeepyyy.","Ishraq, unsettled: This is something else. I think we should get out of here.","Julius: Word.")
        else:
          text("\nJulius, noticing a slip of paper on the lunch counter: Hmm?","*Julius picks up the note*","Julius, opening it up: This smells fresh.","\n*Julius begins to read the paper aloud*\n",'"I am at school right now. I don’t know if I will survive. My phone is not working. I am being chased by other students. I am hiding here all alone. Everyone is trying to kill me. I tried to approach my friends, but they seemed off. I was scared at first, but I tried to speak to them anyway. As soon as I spoke, they all turned and chased me. I ran for my life. A girl caught up to me. She tackled me to the ground. I thought I was dead. But then, something happened. I felt my back explode full of life...and then suddently the girl on top of me stopped moving. Blood came out of her mouth and all over my face. I was horrified at first. But then this thing pulled the girl off of me. I slowly stood up. I observed the life going away from this girl rapidly. I do not know why, but...I felt good."',"\nJulius: Creeeepyyy.")
        additem("Creepy Note",1,you.questinventory)
        self.objects.remove("Note")
        questsys("Feeling Alone","Finish")
        xpg(100)
        
    if self.RID == 18:

      if "More Than Meets The Eye" in quests:
        if subject == "Julius":
          text("\nIshraq, staring at the car in the middle of the vast room: That looks sus.","Julius, lauging: HaHAA, yeah it does. I'm boutta go check it out.","Ishraq: Careful.")
        if subject == "Kelly":
          text("\nIshraq, intrigued: That whole thing you did with the pen was very interesting. How'd you do that?","Kelly, smiling: Well, some sixth sense was telling me I could use the pen. Then, once I started hacking the lock, I saw the sensors I had to configure so that it would react to my pen to open. So I used the laser-like energy from my pen to alter these sensors.","Ishraq, scratching his head: Wow, okay then. Something is leading us on then. Someone wants us to be here.")
          if data[15] == 1:
            text("Kelly: Probably the Fedora Man.","Ishraq, further confused: Is he giving us the Isometric Drawings then? Does he know about your pen? Is he wiring us right now using these powers?","Kelly, scared: Ishraq, I don't know. Those are some scary thoughts that we should keep in mind.","Ishraq: Yeah...")
        if subject == "Ominous Car":
          text("\n*Julius approaches the car*\n","Julius, opening the door and entering the car: Unlocked...nice!","Ishraq, signaling Julius: Find anything?","Julius, just as he opens the glovebox: Nah not yet, hold up...!","\n*Ishraq observes a green flash emitting from all the car's windows*\n","Ishraq, smirking: Ahh shit, that's another one. Julius, you're an ISO!","*Julius does not reply*","Ishraq, calling from a distance: Julius? You still there?","\n*Ishraq approaches the vehicle. Before he could get to close, the car transforms!*\n","Ishraq, jumping back: HOLY SHIT! IT'S A TRANSFORMER! JULIUS!!","\n*Julius stays quiet as he reads something...*","Ishraq, shouting: GET OUT OF THERE ALREADY!","Kelly, running to Ishraq: Hey, we have to fight this thing!","Ishraq, blood pumping suddenly: Right.","\n*Julius is ejected out of the cockpit of the transformer*\n","Julius, plummeting to the ground: ...!!..Hey...that didn't even hurt?","Ishraq, signaling to Julius: Hey, you alright?","Julius,  visibly frustrated: ...Yeeeaaa.....sssss..MAN...LET'S DESTROY THIS SHIT!")
          input(style.BOLD + fore.GREEN_1 +"\n~Julius has gained a new ability, Shield! It recovers a percentage of his maximum health and reduces the damage he takes until it's his turn again!" + style.RESET)
          bots.team = [Entity("Transformer",1000,30,30,60,0,10,60,100,75,0,15,0,3,"17","Boss")] 
          fightid = 5
          battle(you,bots,Cont=False)
          if victory == 1:
            text("\n*The transformer looms over Julius as it is about to collapse*\n","Ishraq, battle buzzed: JULIUS, MOVE!","Julius, activating his shield: I'm chillin'","Ishraq, unsure of Julius's safety: NO CHILL!!","\n*Ishraq power leaps into the air*\n","Ishraq, thinking to himself: These powers in me...I don't know what they are and what they do...I don't know their limits or mine...but they seem to be connected to me. They're materializing around me...and right now, I need to destroy this thing about to fall on my friend.","\n*A red-holographic casing encloses Ishraq's entire body...the Transformer rapidly falls over!!*\n","Ishraq, believing: BOWERS SMASH!","\n*Ishraq strikes the Transfomer with his right arm, immensely pushing it back! He lands on the ground swiftly, only to rebound immediately into the air again to punch the Transfomer with his left arm! The Transformer smashes against the concrete wall of the spacious garage. Ishraq does one last leap into the air, and smashes both his clenched fist through the Transformer!","Kelly, in awe: Woooow, that was sick.","Julius, just standing there: That was type extra. I wasn't gonna get hurt regardless.","Ishraq, getting out of the destroyed Transformer: Not only am I sweating to death, I'm covered in oil now.","Kelly, laughing: Good thing we have showers in the AC!","Ishraq, laughing: Hehehe, I feel like shit no cap. Can't wait to get home.")
            if you.suppteamS[0] == "Brandon":
              text("Brandon, slightly concerned: Yo. Thing are startin' to type heat up in this place. I think we needa get out of here and get some help.")
            elif you.suppteamS[0] == "Edmond":
              text("Edmond, slightly concerned: Yo. Shit is getting really crazy around here. I think we should get some help from the army or some shit.")
            elif you.suppteamS[0] == "Metin":
              text("Metin, slightly concerned: Yo. Why don't we just leave Tech already? We can call in for some help from like the army.")
            elif you.suppteamS[0] == "Hassan":
              text("Hassan, slightly concerned: Yo. We tryna head out? Cuz I'm not dealing with this shit. The fuckin army can deal with this.")
            else:
              input(you.suppteamS[0]+", slightly concerned: Yo, it's getting dangerous now. I think we should leave school and get some help.")
            text("Ishraq, following: Yeah..I think it is about time we get some help. We need to escape the campus.","Kelly, teasing: Oh, so now you want to leave Ishraq? I thought you wanted to play hero some more.","Ishraq, a little embarrassed: Yeah...I'm done playing around, ya heard?","Kelly, leaning over: Yeah, you're definitely done. We're leaving right now.","Julius, at the exit: Come on, let's go.")
            input(style.BOLD + fore.RED_1 +"\n~Ishraq has gained a new ability, Smash! He encases his entire body in a holographic armor, allowing him to do a barrage of 3 attacks successively. The player uses WASD keys to do attacks with different effects that apply on the same attack and remain for the rest of the attacks. Using W increases critical chance(CT) for the current and remaining attacks. Using A increases physical attack(AT). Using S increases armor penetration(APN). Using D increases accuracy(AC). Doing certain sequences adds a special effect at the end of all 3 attacks." + style.RESET)
            Ishraq.learnskill("Smash")
            self.objects.remove("Ominous Car")
            questsys("More Than Meets The Eye","Finish")
            xpg(100)
            questsys("Don't Trip","StartM")
            self.people = []
            autosave()
            revival(Ishraq)
            revival(Julius)
            revival(Kelly)
            if "Shield" not in Julius.skills:
              Julius.skills.insert(1,"Shield")
            input(style.BOLD+"\nUpon exiting this room, you will begin a deathmarch. A deathmarch is a series of random encounters, sometimes with a boss battle at the end. In main story-based deathmarches, you are healed before embarking, and given a shop to prepare, as you usually have to go through the deathmarch before proceeding any further."+style.RESET)

    if self.RID == 25:

      if "The FX-Wing Nurse" in quests:
        if data[13] == 0:
          if subject == "Julius":
            text("\nIshraq, approaching Julius while still jittery: This is a mess.","Julius, calm: It is what it is...damn this is gonna stink.","Ishraq, planning for the future: We shouldn't leave the body in here. We could use this office.","Julius, not sure: I don't know...this office is kinda far. I think we should just loot this place and bring all the supplies to our shop room.","Ishraq, thinking even farther: How about when we get like a quarter of the school saved? That's like 1,000 kids. This office is a good place.","Julius, kinda getting it: Makes sense. Then where should we put the body?","Ishraq, thinking: Hmm...maybe just leave it outside. Just open the door to where the STEM building is being made.","Julius, laughing: HaHAA~! So were just gonn' throw her there?","Ishraq, smirking: You can do that. I still got shit to look for.","*Julius drags the body outta the room to finish the job*")
            self.people.remove("Julius")
          if subject == "File Cabinet":
            text("\nIshraq, to himself: Kelly got like what...a concussion? Head trauma? A, B, C...concussions.","*Ishraq reads the file*","Ishraq: This is just saying to get rest. Fuck it. I'ma just get Kelly an ice-pack.")
            self.objects.remove("File Cabinet")
            self.objects.append("Fridge")
          if subject == "Storage Closet":
            text("\n*Ishraq turns on the closet light*","Ishraq, saying under his breath: Hella useful stuff...should bring some back to shop.")
            additem("Med-Kit",3,you.consumeinventory)
            self.objects.remove("Storage Closet")
          if subject == "Nurse's Desk":
            text("\nIshraq, looking at the blood on his hands: ...She didn't have her ID either. But her name tag is still on the desk. Nurse Urquizo. A name on my grave.","*Ishraq puts the name tag facing down*")
            self.objects.remove("Nurse's Desk")
          if subject == "Medical Cabinets":
            text("\nIshraq, smiling: Assortments of bandages are kinda satisfying. Time to yeet.","*Ishraq takes some random bandages*","Ishraq, to himself: No point in taking it all if we're gonna use this room.")
            additem("Bandages",10,you.consumeinventory)
            self.objects.remove("Medical Cabinets")
          if subject == "Fridge":
            text("\n*Ishraq opens fridge and takes an ice pack. He wraps it in towel paper*","Ishraq: Gimme gimme.")
            additem("Ice Pack",1,you.questinventory)
            self.objects.remove("Fridge")
          if len(self.objects) == 0 and len(self.people) == 0:
            text("\nIshraq, crossing his arms: Alright, everything is done here. This place is ready for use.","\n~The FX-Wing Nurse has been unlocked. You can heal your health here at anytime.")
            ro = rd(25)
            ro.TYPE = "Nurse"
        if data[13] == 1:
          if subject == "Ishraq":
            text("\n*Julius nudges Ishraq*","Julius, testing if Ishraq was really out: ...That's a shlong..oh god.")
          if subject == "File Cabinet":
            input("\nJulius, to himself: Kelly has a concussion. Da fuck am I looking here for, I need ice~!")
            self.objects.remove("File Cabinet")
            self.objects.append("Fridge")
          if subject == "Fridge":
            text("\n*Julius opens fridge and takes an ice pack. He wraps it in towel paper*","Julius, joking to himself: After I give this to Kelly, she'll accept me as her knight in shining armor, HaHAA~!")
            additem("Ice Pack",1,you.questinventory)
            self.objects.remove("Fridge")
          if subject == "Nurse" and self.TYPE == "Camp":
            text("\n*Julius slaps the nurse*","Julius, rubbing the nurse's face: Hello?","Julius, scratching himself: She's still unconscious.")
            if "Ice Pack" in you.questinventory:
              text("\n*Julius slaps Kelly's ice pack onto the Nurse's head*","*The Nurse awakens*","Julius, celebrating: YES~! HaHAA! I didn't expect that to work. I was just playing around.","The Nurse, drunk: Que diablos? Who are you? Shouldn't you be in class?","Julius, grinning: ~Keloke mamasita~.","The Nurse: Ai dios mio! What kind of dream is this?","Julius, still trying to keep a 'seductive' grin: The best kind.","The Nurse: Boy...I'll give you a chance. You can go back to class, and I will not report you.","Julius, laughing: HaHAA~! I didn't even do anything yet!","The Nurse, looking around: ...was there a fight in here?","Julius, still screwing around: Yer'. You and I played rough together...tsk tsk.","The Nurse, gagging: The hell did you drug me with!? There's no way I would fuck with you!","Julius, done messing around: Okay, okay~! Relax! Haha...okay, so here's what really happened. You were going insane. Me and my friend laying over there had to fight you. Once we knocked you out, you got back to normal. Thing is, you injected this needle into him, and he started spazzing out. Now, he's almost like dead. I need you to help him.","The Nurse, giving Julius an unbelieving stare: You know what? I will check your friend out. But if you don't go back to class in 5 seconds, I'm calling the cops.","Julius, understanding: *Sigh*...alright, let me explain to you everything that's happening right now in this school.")
              input("\n*Julius explains the whole situation*")
              text("\nThe Nurse, serious: I don't know why you're still here or why I haven't done anything, but your stories are entertaining at best. If you're trying to cut class, I suggest you leave right now because I'm not giving you a pass.","Julius, also serious, picking up the syringe: Look at the stuff dripping out of this...its a glowing cyan-ish color. This don't look real right?","The Nurse, glaring at the needle Julius handed to her: Is this the shit you drugged me with?","Julius, grinning: COME ON! Just believe me already, HaHAA! My friend needs help!","*The nurse moves over to Ishraq, evaluating him*","The Nurse, shocked: He's in a state of paralysis! He's awake right now too! Ooh! I don't know how to help him! He needs to go to a doctor right now!","Julius, laughing: HaHAA~! Nurses...","The Nurse, still not chill with Julius: Shut up son. There is no cure for paralysis, but let's get him laying on the bed.","\n*The Nurse and Julius heave Ishraq onto a bed...time passes*","\nJulius, thinking out loud: He's down for good I guess...you said he was awake right?","The Nurse, still helping Ishraq in all ways she could: I've iced his muscles...massaged him for any stimulation...he can't even move his mouth.","*The nurse looks at the sample collected from the syringe*","The Nurse, talking to Julius: Do you know what this stuff is and where it came from?")
              if data[15] == 1:
                text("Julius, bringing up a past thought: Maybe...The Fedora Man, the guy who's trying to take revenge on our school must've dosed you. He probably knew all this was gonna happen.")
              else:
                text("Julius, thinking: Not sure...but something weird is definitely happening. The guy who tried kidnapping this girl I know has to have something to do with this.")
              text("*Heavy banging is heard from the door*","Julius, smirking: Wait here...I'll take care of these zombies.","The Nurse, worried: Wait! Make sure to be well rested before going out there!","\n~The FX-Wing Nurse has been unlocked. You can heal your health here at anytime.")
              self.TYPE = "Nurse"
          elif subject == "Nurse" and self.TYPE == "Nurse":
            if data[14] == 0:
              text("\nThe Nurse, introducing herself: Oh, I forgot to mention, my name is Nurse Urquizo. Be careful out there, and make sure to use whatever you need.","Julius, ready: Thanks!","*Julius takes some medical supplies*")
              additem("Med-Kit",3,you.consumeinventory)
              additem("Bandages",10,you.consumeinventory)
              data[14] = 1
              self.people.remove("Nurse")
              self.people.append("Nurse Urquizo")

      if subject == "Nurse Urquizo":
        if "For the Horde" in quests and self.RLV == 1:
          text("\nNurse Urquizo, worried: The door is locked, right??? I've heard people marching outside...and it sounds like a lot of people.","Kelly, sitting down to take a breather: Whew...this sounds dangerous. Stay safe, Ms. Urquizo.","Nurse Urquizo, eyes widening: No, you children stay safe! Don't do anything reckless like this hijo over there!","Julius, turning around: HaHAA, why you coming at me?","Nurse Urquizo, disgusted: I honestly don't even want you ever in here, but given the circumstances...whatever...children, take what you need.")
          additem("Bandages",6,you.consumeinventory)
          additem("Med-Kit",1,you.consumeinventory)
          self.RLV = 2
        else:
          text("\nNurse Urquizo, welcoming: Make sure to get some rest!")

      if subject == "Nurse" and data[14] == 0 and self.TYPE == "Nurse":
        self.people.remove("Nurse")
        self.people.append("Nurse Urquizo")
        text("\nThe Nurse, welcoming: You're back! I never got to give you my name. I am Nurse Urquizo. Be cafeul out there, and make sure to use whatever you need.","Ishraq, taking some supplies: Thanks for treating me while I was out.","Nurse Urquizo, happy: Always here.")
        additem("Med-Kit",3,you.consumeinventory)
        additem("Bandages",10,you.consumeinventory)
    
    if self.RID == 27:

      if subject == "Kit-Kat":
        text("\nIshraq, opening the wrapper already: Hey, free kit-kat!","*Ishraq shares the kit-kat with the team, healing everyone to full health!")
        self.objects.remove("Kit-Kat")
        for x in you.team:
          revival(x,o=True)
        for x in you.backteam:
          revival(x,o=True)
        for x in you.deadteam:
          revival(x,o=True)

      if "The Straight Edge" in quests:

        if subject == "Ruler":
          text("\n*Ishraq opens up Mrs. Wells's desk drawers, and finds a ruler*","\nIshraq, ready to leave: Got the ruler, let's go Julius.")
          additem("Ruler",1,you.questinventory)
          self.objects.remove("Ruler")

    if self.RID == 28:

      if subject == "Ryca":
        if "Medical Attention" in quests:
          text("\n*Kelly appraoches Ryca*","Kelly, wanting to help: You doing fine? Feeling better?","Ryca, vibing: Yeaah, after those stretches, I think I'm ready to kick some ass.","Kelly, giggling: Hahah, you got this!")
        elif "Daily Checkup" in quests:
          text("\n*Kelly appraoches Ryca*","Kelly, chilling: Heyy Ryca","Ryca, vibing: Just thinking of some attacks I could do when I find some wired, ya know?","Kelly, giggling: Hahah, you go!")
          if "Unknown Object" in self.objects:
            input("\nRyca, pointing towards: By the way, we found some weird thing emitting a glowing pink light in here. You might wanna take a look.")

      if subject == "Alex":
        if "Medical Attention" in quests:
          text("\n*Kelly approaches Alex*","Kelly, making fun of: You resting well Mr. Normal?","Alex, insulted: I-I'm not normal. And yes.","Kelly, teasing: Okay Mr. Normal! Hehee!")
        elif "Daily Checkup" in quests:
          text("\n*Kelly approaches Alex*","Kelly, making fun of: Look at Mr. Normal doing well.","Alex, insulted: I-I'm not normal.","Kelly, teasing: Okay Mr. Normal! Hehee!")
        
      if subject == "Didar":
        if "Medical Attention" in quests:
          text("\n*Kelly approaches Didar*","Kelly, concerned: I think I hit you a little too hard while we were fighting, are you okay?","Didar, stepping up: Yes, I am. Where's Ishraq anyways?","Kelly, reminded of him: Oh, that bozo is sleeping still. I'm so gonna scream in his ear when I get back.")
        elif "Daily Checkup" in quests:
          text("\n*Kelly approaches Didar*","Kelly, greeting: Hey Didar, I never really met you, but I've heard about you from Kathleen!...and Daniel.","Didar, stepping up: Daniel talks about me?","Kelly, disgusted at the thought: Yeah...he's really crazy about you.","Didar, informing: Yeah, he does talk to me a lot. When me and the other medical students were scouting, we saw him at the auditorium. He was just standing there...","Kelly, intrigued: Interesting...thank you for the information.","Didar, wondering: Where's Ishraq anyways?","Kelly, reminded of him: Oh, that bozo is sleeping still. I'm so gonna scream in his ear when I get back.")
          data[25] = 1
      if subject == "Unknown Object":
        text("\nKelly, shocked: Wooah, what's this doing here?")
        additem("T2 Magenta Isometric Drawing",1,you.isoinventory)
        self.objects.remove("Unknown Object")

    if self.RID == 29:

      if subject == "Tim's Bookbag":
        input("\nTim: Found it! Hey, what's this!?")
        additem("T2 Cyan Isometric Drawing",1,you.isoinventory)
        additem("Calculator",1,you.accessinventory)
        additem("Bible",1,you.accessinventory)
        self.objects.remove("Tim's Bookbag")
    
    if self.RID == 30:
      if "Transmission" in quests:

        if subject == "Box #1":
          text("\nIshraq: A chromebook repair kit? Useless to be honest. Still takin' it.")
          additem("Repair Kit",you.accessinventory)
          self.objects.remove("Box #1")
        
        if subject == "Box #2":
          text("\nIshraq: Well, would ya' look at that.")
          additem("T2 Yellow Isometric Drawing",you.isoinventory)
          self.objects.remove("Box #2")

        if subject == "Box #3":
          text("\nIshraq, finding something: This looks like a radio kit...*Ishraq walks over to Daniel with the box*","Ishraq, giving the box to Daniel: I think this might be a box.","Daniel, glancing at the contents: Mmm, yeah! I can defintely work with this.","\nTim, thinking it over: It's great we found this kit and all, but we really only need one solid way of communicating. We got three ideas on it. The first was to set up a radio broadcast with receivers in safe havens where students are. We got the kit for that. The second was walkie-talkies, which I'm not sure we will find here. I perosnally think they're more robust and simpler. The third was to get control of the announcement speakers in each room, which would make the radio broadcast we're gonna set up useless.\n","Daniel, really wanting to set up the broadcast: But we can set the radio where we want it to be and use it from where we want. The announcement speakers are in the main office! That's too far from shop!","Ishraq: The announcement speakers are convenient though...and not at the same time.","Tim, accepting Daniel's idea: Eh, the announcement speakers are in a far spot to use safely. I guess we should set up our own system. But, walkie-talkies are just completely better than all this.","Ishraq: Well, if we find them, we'll use them, but in the mean time this is our plan.","\n~The team goes on and on discussing their ideas on setting up a reliable way of communication...meanwhile, in a dark room only lit by a vast amount of bright monitors...\n")
          self.objects.remove("Box #3")
          ro = rd(30)
          croom.remove(ro)
          world.append(ro)
          ro = rd(31)
          world.remove(ro)
          croom.append(ro)
          eventcheck()
        
        if subject == "Julius":
          text("\nJulius, idle: Need anything from me?")
          if data[23] != "":
            boop = input("\n(1) Find anything?  (2) The Fedora Man... \nResponse: ")
            if boop == "1":
              text("\nIshraq: Find anything?","Julius, slowly turning to Ishraq: Do it look like I even know what we're doing here, HaHAA~!")
            if boop == "2":
              text("\nIshraq: The Fedora Man...he talks as if he knew you.","Julius, pausing: ...Strange. I'm not even sure myself if I know him or not.","Ishraq, gaslighting: He called you a pussy, whatchu' gonna do about it?","Julius, abnormally serious: I don't know..")
          else:
            text("\nIshraq: Find anything?","Julius, slowly turning to Ishraq: Do it look like I even know what we're doing here, HaHAA~!")
          
        if subject == "Tim":
          text("\nTim, ripping through boxes: Ishraaaq.")
          if data[23] == "":
            text("\nIshraq, wondering if Tim saw: Did you see Arwyn at the auditorium?","Tim: Yeah...he was with the Fedora Man.","Ishraq, worried: He was wired too...")
          else:
            text("\nIshraq, relieved: You had me convinced you were dead back at the auditorium.","Tim, feeling complimented: I always knew I was good at acting. By the way, you saw Arwyn at the auditorium?","Ishraq, excited to hear about: No? He was there?!","Tim: Yeah, he came in with the Fedora Man and left with him...I think he was wired.")
        
        if subject == "Daniel":
          text("\nDaniel, searching: Yo.")
          if data[23] == "":
            if data[24] == 1:
              text("Ishraq, feeling bad: Yo. Sorry.","Daniel, understanding what he was apologizing for: What are you saying sorry to me for? You better beg Kelly for forgiveness.","Ishraq, not taking him seriously: Yeah, I sure will.")
            else:
              text("Ishraq, feeling bad: Yo. Sorry.","Daniel: Why are you saying sorry to me?","Ishraq: I didn't save your queen.","Daniel, taking the opportunity: That's alright. Only me, her true knight in shining armor, can save her.")
          else:
            text("\nIshraq, skeptical: It's nothing, huh?","Daniel: What?","Ishraq: That's what you told me in the auditorium. What bothered you back there?","Daniel, not trusting himself: I don't know. I just had a memory. A good one too, hehe...but I don't know if it actually happened, that's all.","Ishraq, willing to believe: Maybe something from when you were wired? You clearly remembered me failing to save Kelly, haha.","Daniel, eyes widening: Yeah...YES!","Ishraq: What?","Daniel: Aaah. I'll tell you later.")

    if self.RID == 31:
      if "Transmission" in quests:
        
        if subject == "???":
          text("\nKelly, calling out: Hello-?","*The person doesn't say anything*","Kelly, noticing their eyes: You're...not wired.","???, bluntly: Don't talk to me.","Kelly, confused: What are you doing here?...*The person does not respond*...Come on! Say something!","???, sighing: Aaah. Why did it have do be you here.","Kelly, somewhat insulted: Excuse me?","???: Nevermind. Just shut up.","Kelly, getting a better look: You're...you're Arwyn. From shop!","Arwyn, depressed: And now she recognizes me, great. Just leave me alone.","Kelly, irritated: Why are you being like this?","Arwyn, dryly: What am I supposed to be like?","Kelly, annoyed: I don't know, maybe like a normal person? You're acting very wired for someone who isn't.","Arwyn, confused: What does that even mean?","Kelly, explaining: We call the people who are mind-controlled by the Fedora guy 'Wired'.","Arwyn, understanding: Oh. That's what you mean.","Kelly, repeating herself: So like, what are you doing here?! Why are you here?!","Arwyn, painfully: I just wanna go home and play League.","Kelly, stomping: Answer me!","Arwyn, remembering: Aaaah--The Fedora guy. He doesn't know I'm not wired.","Kelly, shocked: How?!","Arwyn, shrugging: I don't know. He just assumed I was.","Kelly, kind of excited: B-but the earrape attack from the loudspeakers! It was supposed to wire you!","Arwyn, cool: I guess it didn't.","Kelly, really happy: This is great! Come on, let's get out of here together!","Arwyn, refusing: No. Screw you.","Kelly, taken aback: W-what?","Arwyn, insulting: You're annoying.","Kelly, astonished: Is this a joke or something?!","Arwyn, plainly: Nah.","Kelly, really frustrated: Why did it have do be you here.","Arwyn, looking around: There's no exit out of this cellar anyways.","\n*Kelly takes out her calligraphy pen...she cuts the bars of her cell using its laser!...a cut-out piece of the bar starts to emit a Blue Isometric Drawing...*","Kelly, getting out of the closet-sized cell: Well. At least that maniac up there won't be cumming all over me...hey, wait a second.. *Kelly picks up the bar*, Arwyn..this has to be for you!","Arwyn, curious: What is it?","Kelly, rushing over to him and handing it over: It's an ISO! Dr. Graham wants you to have it!","\n*The bar instantly starts to wrap around Arwyn as soon as Kelly hands it to him, locking him up before shrinking him into a small shining blue light! His body begins to reconstruct plane by plane until he is completed to be the next ISO!*\n",fore.DODGER_BLUE_1+style.BOLD +"Arwyn, gaining some happiness: That was...quite interesting. I feel better.."+style.RESET,fore.DODGER_BLUE_1+"\nArwyn has gained a passive ability! When silenced, his normal attacks deal true damage plus bonus true damage based on his physical and magical attack.")
          text("\n*A rift opens up before Kelly and Arwyn!*\n","Kelly, hopeful: An exit?","Arwyn, curious: One way to find out. *Arwyn jumps in, vanishing!*","Kelly, jumping in as well: Whatever!","\n*Kelly and Arwyn find themselves in unknown territory...*\n","Kelly, taking a look around: Wait. This is Times Square. In New York! YES! WE MADE IT OUT!! But how? I thought only PCTI was in the Realm Between...","Arwyn, trying to catch up: What are you talking about?","Kelly, explaining quickly: We were stuck in PCTI when we were there...there was no way out of the campus..but now we're here.","Arwyn, gravely: So you're saying...there was no way of going home?","Kelly, vigorously: Yes! There was no way of going home!","Arwyn, dying inside: T-that means...no League.","Kelly, a little confused but going with it: Yeah...no League.","\n*Six prominent figures suddenly surround Kelly and Arwyn out of the blue...*\n","Obama, gloriously: Let's get this show on the road fellas'.","Kennedy, rubbing his forehead: We must stay open minded, my fellow Americans. But we will fight if we must.","Lincoln, towering over everyone with his hat: The party war ENDS here.","Trump, with great presense: When the looting starts, the shooting starts.","Sanders, about to die anyways: I will keep fighting--*cough*--for the weak.","Musk, scratching his head: I just wanna live on the Moon.","Kelly, turning 360: What..the fuck.","All Prominent Figures: Join us! Together we will destroy all opposition!")
          start = time.time()        
          elapsed = 0               
          while elapsed < 6:
            print("\nYou have",round(6-elapsed),"seconds to make a decision")
            boop = input("(1) Democrats  (2) Republicans  (3) Independent\nResponse: ")
            elapsed = time.time() - start
            if boop == "1" or boop == "2" or boop == "3":
              break
          if boop != "1" and boop != "2" and boop != "3":
            boop = str(random.randint(1,3))
          if boop == "1":
            input("\nObama, getting ready to dunk: You made the right choice.")
            bots.team = [Entity("Trump",300,30,20,40,30,40,50,100,100,5,0,10,3,"17","Male Boss"),Entity("Lincoln",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss"),Entity("Sanders",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss"),Entity("Musk",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss")] 
          if boop == "2":
            input("\nTrump, rising: We will make America great again!")
            bots.team = [Entity("Obama",300,30,20,40,30,40,50,100,100,5,0,10,3,"17","Male Boss"),Entity("Kennedy",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss"),Entity("Sanders",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss"),Entity("Musk",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss")] 
          if boop == "3":
            input(style.BOLD+"\nSanders, reviving with surreal strength: I will fight on forever."+style.RESET)
            bots.team = [Entity("Obama",300,30,20,40,30,40,50,100,100,5,0,10,3,"17","Male Boss"),Entity("Kennedy",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss"),Entity("Trump",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss"),Entity("Lincoln",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss")] 
          fightid = 9
          battle(you,bots,Cont=False)
          if victory == 1:
            text("Kelly, totally lost: Okay, seriously, where are we?")
            if boop == "1":
              text("Obama, wondering: What? Is this not your universe?","Arwyn: Not our universe?","Kennedy, figuring it out: Aaah. Their universe isn't technologically advanced yet.","*Another rift opens up!*","Obama, guiding: Seems like a tear to your universe is fluctuating here. You should take it now before you're stuck here.")
            if boop == "2":
              text("Trump, swearing he figured it out: You guys are defintely from China!","Kelly, offended: Umm...","Lincoln, figuring it out: No, they're not from here at all. As in, this universe.","Arwyn: This universe?","Trump, understanding: Ah, they're from a slow universe. How'd they even get here then?","*Another rift opens up!*","Lincoln, guiding: Seems like a tear to your universe is fluctuating here. You should take it now before you're stuck here.")
            if boop == "3":
              text("Musk, confirming his suspisions: I knew it. You guys seem foreign.","Kelly, a little offended: Foreign?","Musk, explaining: As in, not from this universe.","Arwyn: Not this universe?","*Another rift opens up!*","Musk, guiding: Seems like a tear to your universe is fluctuating here. You should take it now before you're stuck here.")
            text("Arwyn, not caring: Does League exist in this universe?","Kelly, grabbing Arwyn and jumping through the rift: Goodbye!","Arwyn, struggling: WAIT!","\n*Arwyn and Kelly land in the Engineering Shop room.*\n","Arwyn, visibly frustrated: Why are you so strong?","Kelly, sticking her tongue out: Cuz' I have an ISO! You do too, but you haven't used it much.","Arwyn, sour: Why is somone like you an ISO.","Kelly, ignoring: The other ISOs aren't here...let's find out where they went.")
            ro = rd(31)
            croom.remove(ro)
            world.append(ro)
            ro = rd(6)
            world.remove(ro)
            croom.append(ro)
            wee = ""
            for x in you.ph1:
              if x.name == "Metin":
                wee = wee + "1"
              if x.name == "Brandon":
                wee = wee + "2"
              if x.name == "Noah":
                wee = wee + "3"
              if x.name == "Edmond":
                wee = wee + "4"
            if "1" not in wee:
              ro.people.append("Metin")
            elif "2" not in wee:
              ro.people.append("Brandon")
            elif "3" not in wee:
              ro.people.append("Noah")
            elif "4" not in wee:
              ro.people.append("Edmond")
            worldfunction()


  
  def randomencounter(self):
    global weight
    global fightid
    global fightmod
    tis = random.randint(1,100)
    if tis <= self.ENC:
      ag = random.randint(1,100)
      print("!!!")
      dam = input("\nEnemies approach!\n(1) Fight  (2) Run\nAction: ")
      wee = 0
      while wee == 0:
        if dam == "1" or dam.lower() == "fight":
          randomweight("Mobs","Freshman",5,"Sophomore",4,"Junior",1,"Senior",2)
          enemygenerator(random.choice(weight),1)
          if ag <= 75:
            enemygenerator(random.choice(weight),2)
          if ag <= 50:
            enemygenerator(random.choice(weight),3)
          if ag <= 25:
            enemygenerator(random.choice(weight),4)
          if ag <= 10:
            enemygenerator(random.choice(weight),5)
          fightid = 0
          fightmod = 0
          battle(you,bots,Cont=False)
          wee = 1
        elif dam == "2" or dam.lower() == "run":
          time.sleep(0.5)
          if random.randint(1,100) > 50:
            print("\n*The team runs from the battle.*")
          else:
            print("\n*The team fails to escape!*")
            randomweight("Mobs","Freshman",5,"Sophomore",4,"Junior",1,"Senior",2)
            enemygenerator(random.choice(weight),1)
            if ag <= 75:
              enemygenerator(random.choice(weight),2)
            if ag <= 50:
              enemygenerator(random.choice(weight),3)
            if ag <= 25:
              enemygenerator(random.choice(weight),4)
            if ag <= 10:
              enemygenerator(random.choice(weight),5)
            fightid = 0
            fightmod = 0
            battle(you,bots,Cont=False)
          wee = 1

  def deathmarch(self,steps,spc=""):
    if spc == "nig":
      print("NIG")
    else:
      time.sleep(1)
      print("\nThe march begins...\n")
      time.sleep(1)
    for x in range(steps):
      print("\n...")
      time.sleep(1)
      print("...")
      time.sleep(1)
      print("...")
      time.sleep(1)
      self.randomencounter()
    if spc == "Edge":
      text("\n*The team reaches the fence behind the T-Building*\n","Ishraq, quickly climbing over the fence: I can go. You guys can hold out here.","Kelly, totally not for it: Yeah, I'm not staying here.","Ishraq: But can you even climb this?","Kelly, staring at the top of the fence: ...No","Julius, volunteering: I should go. I won't gas out like you Ishraq.","Ishraq: True. You can reach the police station nearby pretty quickly.","\n*Ishraq turns away from the group, and almost slips*\n","Ishraq, balancing: Woooa, almost fell....wait. Guys. Something's really off.","Kelly, scared: What do you mean?","Ishraq, staring down: I'm staring into the void. There is no ground. It's just black.","Julius, weirded out: Whatchu mean bro?","Ishraq, staring out into the distance: There's nowhere to go.","\n*Two students approach the team*\n","Julius, ready to fight: We got company.","Ishraq, leaping over the fence: Yo, it's Alvaro and Octavio. Let's free them.")
      bots.team = [Entity("Alvaro",300,30,20,40,30,40,50,100,100,5,0,10,3,"17","Male Boss"),Entity("Octavio",400,30,30,50,0,20,55,100,100,5,10,0,3,"18","Male Boss")] 
      battle(you,bots,Cont=False)

class Support:
  def __init__(self,name,cd):
    self.name = name
    self.cd = cd   #cooldown
    self.ccd = 0   #current cooldown
    self.scd = 0   #saved cooldown

  def use(self):
    self.ccd = self.cd

  def supporttimers(self):

    if self.ccd > 0:
      self.ccd = self.ccd - 1
      if self.ccd == 0:
        time.sleep(0.5)
        print("\n"+self.name,"is ready!")

def supu(name,cd,sk=False):
  if sk == False:
    print("\n"+name,"has been unlocked as a support character!")
  you.suppback.append(Support(name,cd))
  you.suppbackS.append(name)

def teamskill():
  global Ishraq
  global Kelly
  global Julius
  global Tim
  global Daniel
  global Arwyn
  for x in you.team:
    x.wild = Ishraq.wild
    x.sma = Ishraq.wild
    x.valo = Ishraq.wild
    x.immort = Ishraq.wild
    x.barr = Ishraq.wild
    x.fromthes = Arwyn.fromthes
    x.run = Julius.run
    x.res = Julius.res
    x.shi = Julius.shi
    x.trem = Julius.trem
    x.isom = Julius.isom
    x.comb = Julius.comb
    x.callig = Kelly.callig
    x.asm = Kelly.asm
    x.pinp = Kelly.pinp
    x.bake = Kelly.bake
    x.perfectr = Kelly.perfectr
    x.rev = Kelly.rev
    x.grub = Daniel.grub
    x.taun = Daniel.taun
    x.knightv = Daniel.knightv
    x.obese = Daniel.obese
    x.jabb = Daniel.jabb  
    x.electr = Daniel.electr
    x.silen = Arwyn.silen
    x.cutm = Arwyn.cutm
    x.gunb = Arwyn.gunb
    x.spark = Arwyn.spark
    x.dar = Arwyn.dar
    x.da = Tim.da
    x.que = Tim.que
    x.chrono = Tim.chrono
    x.proto = Tim.proto
    x.rub = Tim.rub
  for x in you.backteam:
    x.wild = Ishraq.wild
    x.sma = Ishraq.wild
    x.valo = Ishraq.wild
    x.immort = Ishraq.wild
    x.barr = Ishraq.wild
    x.fromthes = Arwyn.fromthes
    x.run = Julius.run
    x.res = Julius.res
    x.shi = Julius.shi
    x.trem = Julius.trem
    x.isom = Julius.isom
    x.comb = Julius.comb
    x.callig = Kelly.callig
    x.asm = Kelly.asm
    x.pinp = Kelly.pinp
    x.bake = Kelly.bake
    x.perfectr = Kelly.perfectr
    x.rev = Kelly.rev
    x.grub = Daniel.grub
    x.taun = Daniel.taun
    x.knightv = Daniel.knightv
    x.obese = Daniel.obese
    x.jabb = Daniel.jabb  
    x.electr = Daniel.electr
    x.silen = Arwyn.silen
    x.cutm = Arwyn.cutm
    x.gunb = Arwyn.gunb
    x.spark = Arwyn.spark
    x.dar = Arwyn.dar
    x.da = Tim.da
    x.que = Tim.que
    x.chrono = Tim.chrono
    x.proto = Tim.proto
    x.rub = Tim.rub

def additem(item,amount,storage):
  for x in range(amount):
    storage.append(item)
  print("\n"+str(amount)+"x",item,"was added into your inventory.")

def wimple(ints,direct,bat=False):
  global sad
  sad = 0
  if direct == "Team":
    for x in you.backteam:
      if x.NAME in you.backteamS[ints]:
        quickswitch(x,direct,bat)
        break
  elif direct == "Backteam":
    for x in you.team:
      if x.NAME in you.teamS[ints]:
        quickswitch(x,direct,bat)
        break
  elif direct == "Supp Team":
    for x in you.suppback:
      if x.name in you.suppbackS[ints]:
        quickswitch(x,direct,bat)
        break
  elif direct == "Res":
    for x in you.suppteam:
      if x.name in you.suppteamS[ints]:
        quickswitch(x,direct,bat)
        break

def guestswitch(bat=False):
  global sad
  sad = 0
  wop = 0
  if len(you.suppteam) < 3 and len(you.suppback) > 0:
    while len(you.suppteam) < 3:
      print("\nSupport Team:")
      print(you.suppteamS)
      print("\nReserve Team:")
      print(you.suppbackS)
      come = input("\nType a name or an appropriate number to insert a member into the team: ") 
      if come.isdigit() == True and come != "0":
        if len(you.suppback) >= int(come):
          wimple((int(come)-1),"Supp Team",bat)
          wop = 1
      for x in you.suppback:
        if come.lower() == x.name.lower() and x.name in you.suppbackS:
          quickswitch(x,"Supp Team",bat)
          wop = 1
      if wop != 1:
        sad = 1
  elif len(you.suppteam) == 3 and len(you.suppback) > 0:
    nudes = 0
    while nudes == 0:
      print("\nReserve Team:")
      print(you.suppbackS)
      wow = input("\nChoose someone from the reserve team to put in the team: ") 
      if wow.isdigit() == True and wow != "0":
        if len(you.suppback) >= int(wow):
          wimple((int(wow)-1),"Supp Team",bat)
          wop = 1
      for x in you.suppback:
        if wow.lower() == x.name.lower() and x.name in you.suppbackS:
          quickswitch(x,"Supp Team",bat)
          wop = 1
      if wop != 1:
        continue
      else:
        nudes = 1
    while nudes == 1: #~
      wop = 0
      print("\nSupport Team:")
      print(you.suppteamS)
      wow = input("\nChoose someone from the team to put in the reserve team: ") 
      if wow.isdigit() == True and wow != "0":
        if len(you.suppteam) >= int(wow):
          wimple((int(wow)-1),"Res",bat)
          wop = 1
      for x in you.suppteam:
        if wow.lower() == x.name.lower() and x.name in you.suppteamS:
          quickswitch(x,"Res",bat)
          wop = 1
      if wop != 1:
        continue
      else:
        nudes = 2
  elif len(you.suppteam) < 3 and len(you.suppback) == 0:
    print("\nSupport Team:")
    print(you.suppteamS)
    print("\nYou do not have enough members to switch anyone out.")


def teamswitch(bat=False):
  global sad
  sad = 0
  wop = 0
  if len(you.team) < 4 and len(you.backteam) > 0:
    while len(you.team) < 4:
      print("\nTeam:")
      print(you.teamS)
      print("\nReserve Team:")
      print(you.backteamS)
      come = input("\nType a name or an appropriate number to insert a member into the team: ") 
      if come.isdigit() == True and come != "0":
        if len(you.backteam) >= int(come):
          wimple((int(come)-1),"Team",bat)
          wop = 1
      for x in you.backteam:
        if come.lower() == x.NAME.lower() and x.NAME in you.backteamS:
          quickswitch(x,"Team",bat)
          wop = 1
      if wop != 1:
        sad = 1
  elif len(you.team) == 4 and len(you.backteam) > 0:
    nudes = 0
    while nudes == 0:
      print("\nReserve Team:")
      print(you.backteamS)
      wow = input("\nChoose someone from the reserve team to put in the team: ") 
      if wow.isdigit() == True and wow != "0":
        if len(you.backteam) >= int(wow):
          wimple((int(wow)-1),"Team",bat)
          wop = 1
      for x in you.backteam:
        if wow.lower() == x.NAME.lower() and x.NAME in you.backteamS:
          quickswitch(x,"Team",bat)
          wop = 1
      if wop != 1:
        continue
      else:
        nudes = 1
    while nudes == 1:
      wop = 0
      print("\nTeam:")
      print(you.teamS)
      wow = input("\nChoose someone from the team to put in the reserve team: ") 
      if wow.isdigit() == True:
        if len(you.team) >= int(wow):
          wimple((int(wow)-1),"Backteam",bat)
          wop = 1
      for x in you.team:
        if wow.lower() == x.NAME.lower() and x.NAME in you.teamS:
          quickswitch(x,"Backteam",bat)
          wop = 1
      if wop != 1:
        continue
      else:
        nudes = 2
  elif len(you.team) <= 4 and len(you.backteam) == 0:
    print("\nTeam:")
    print(you.teamS)
    print("\nYou do not have enough members to switch anyone out.")
    
def forceswitch(ally,bat=False):
  if ally in you.team:
    quickswitch(ally,"Force",bat)
    if len(you.backteam) > 0:
      teamswitch(bat)
  elif ally in you.backteam:
    you.backteam.remove(ally)
    you.backteamS.remove(ally.NAME)
  elif ally in you.deadteam:
    you.deadteam.remove(ally)
    you.deadteamS.remove(ally.NAME)

def quickswitch(pers,direction,bat=False):
  if direction == "Team":
    you.backteam.remove(pers)
    you.backteamS.remove(pers.NAME)
    you.team.append(pers)
    you.teamS.append(pers.NAME)
    print("\n"+pers.NAME,"is placed in the party!")
    if bat == True:
      you.teamID.append(pers.ID)
  if direction == "Backteam":
    you.team.remove(pers)
    you.teamS.remove(pers.NAME)
    you.backteam.append(pers)
    you.backteamS.append(pers.NAME)
    print("\n"+pers.NAME,"is removed from the party!")
  if direction == "Force":
    you.team.remove(pers)
    you.teamS.remove(pers.NAME)
    if bat == True:
      you.teamID.remove(pers.ID)
    print("\n"+pers.NAME,"is unavailable!")
  if direction == "In":
    you.team.append(pers)
    you.teamS.append(pers.NAME)
    print("\n"+pers.NAME,"is placed in the party!")
  if direction == "Supp Team":
    you.suppback.remove(pers)
    you.suppbackS.remove(pers.name)
    you.suppteam.append(pers)
    you.suppteamS.append(pers.name)
    print("\n"+pers.name,"is placed in the party!")
  if direction == "Res":
    you.suppback.append(pers)
    you.suppbackS.append(pers.name)
    you.suppteam.remove(pers)
    you.suppteamS.remove(pers.name)
    print("\n"+pers.name,"is removed from the party!")


def revival(ally,MID=False,o=False):
  ally.cHP = ally.fHP
  ally.cMP = ally.fMP
  if ally in you.deadteam:
    you.deadteam.remove(ally)
    you.deadteamS.remove(ally.NAME)
    if len(you.team) >= 4:
      you.backteam.append(ally)
      you.backteamS.append(ally.NAME)
    else:
      you.team.append(ally)
      you.teamS.append(ally.NAME)
  elif ally not in you.deadteam and ally not in you.team and ally not in you.backteam:
    if len(you.team) >= 4:
      you.backteam.append(ally)
      you.backteamS.append(ally.NAME)
    else:
      you.team.append(ally)
      you.teamS.append(ally.NAME)
  if MID == False:
    ally.purge("Death",you,bots,op=o)
  else:
    ally.purge("Death",you,bots,mid=True,op=o)

def questsys(quest,soc):
  if soc == "StartS":
    quests.append(quest)
    input("\nYou started the side quest |"+quest+"|")
  elif soc == "StartM":
    quests.insert(0,quest)
    input("\nYou started the main quest |"+quest+"|")
  elif soc == "Finish":
    quests.remove(quest)
    input("\n|"+quest+"| quest complete!")
    qcomp.append(quest)

def questcatalog(): #print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
  print(style.BOLD+"\n-Quests-"+style.RESET)
  for x in quests:
    if x == "All Hail...":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Head to the FX-Wing Engineering Shop Room to check on your classmates.")
    if x == "The FX-Wing Nurse":
      if "Ice Pack" not in you.questinventory:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Go to the FX-Wing Nurse's office to get medical supplies for Kelly and everyone.")
      else:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Attend to Kelly back at Shop.")
    if x == "The Straight Edge":
      if "Ruler" not in you.questinventory:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Go to Mrs. Wells's room in the 2nd floor of the FX-Wing to find a ruler.")
      else:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Return to Shop and use the ruler to draw some Isometric Drawings.")
    if x == "No Talking in The Library":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Check out the libraries in the school to try and find an Isometric Drawing. There is two, each located in the F-Wing and C-Wing.")
    if x == "More Than Meets The Eye":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Investigate the Automotive Building to try and find an Isometric Drawing.")
    if x == "Don't Trip":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Escape PCTI.")
    if x == "For the Horde":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Regroup at Shop.")
    if x == "Daily Checkup":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Check on the Medical Shop in the D-Wing.")
    if x == "Medical Attention":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Scout out the Medical Shop in the D-Wing.")
    if x == "Sign Language":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Find Tim's bookbag in the last place he remembers being, his ASL room in the C-Wing.")
    if x == "Showdown":
      if data[23] != "":
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Rush to the Auditorium.")
      elif data[25] == 0:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Wake up Ishraq at Shop.")
      else:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Wake up Ishraq at Shop, or go to the Auditorium.")
    if x == "Transmission":
      ro = rd(11)
      if "Technology Room" not in ro.paths:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"After a great loss, regroup at Shop and decide the next course of action.")
      elif "Technology Room" in ro.paths:
        print(style.BOLD+"\n"+x+":\n"+style.RESET,"Scavenge the Technology Room in the H-Wing Ground Floor to find radios.")
      #print(style.BOLD+"\n"+x+":\n"+style.RESET,"Link up with Khalil in the Main Office located in the C-Wing, or go to Shop and drop off the scavenged radio-tech.")
    if x == "The Asylum":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "Ghosts of the Future":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "Simple, Really":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "STEM":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "Color Coded":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "The Things We Would Do":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "Open The Gym":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "The First Key":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "The Wicked Witch":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"")
    if x == "Feeling Alone":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Scavenge food from the cafeterias.")
    if x == "The Teacher and The Student":
      print(style.BOLD+"\n"+x+":\n"+style.RESET,"Visit Dr. Graham's room in the F-Wing Hallway 2nd floor.")




def text(yes1,yes2="",yes3="",yes4="",yes5="",yes6="",yes7="",yes8="",yes9="",yes10="",yes11="",yes12="",yes13="",yes14="",yes15="",yes16="",yes17="",yes18="",yes19="",yes20="",yes21="",yes22=""):
  input("\n"+yes1)
  if yes2 != "":
    input("\n"+yes2)
  if yes3 != "":
    input("\n"+yes3)
  if yes4 != "":
    input("\n"+yes4)
  if yes5 != "":
    input("\n"+yes5)
  if yes6 != "":
    input("\n"+yes6)
  if yes7 != "":
    input("\n"+yes7)
  if yes8 != "":
    input("\n"+yes8)
  if yes9 != "":
    input("\n"+yes9)
  if yes10 != "":
    input("\n"+yes10)
  if yes11 != "":
    input("\n"+yes11)
  if yes12 != "":
    input("\n"+yes12)
  if yes13 != "":
    input("\n"+yes13)
  if yes14 != "":
    input("\n"+yes14)
  if yes15 !="":
    input("\n"+yes15)
  if yes16 !="":
    input("\n"+yes16)
  if yes17 !="":
    input("\n"+yes17)
  if yes18 !="":
    input("\n"+yes18)
  if yes19 !="":
    input("\n"+yes19)
  if yes20 !="":
    input("\n"+yes20)
  if yes21 !="":
    input("\n"+yes21)
  if yes22 !="":
    input("\n"+yes22)

def battle(p1,p2,Cont=None,Mid=None):
  global bots
  global sad
  global fightmod
  global fightid
  global victory
  global allfighters
  global lastat
  global player1
  global player2
  winc = False
  victory = 0
  battleinit()
  if Mid == True:
    for x in p1.team: 
      x.midbattlesave()
    for x in p1.backteam:
      x.midbattlesave()
    p1.cteam = []
    p1.cbackteam = []
    p1.cdeadteam = []
    p1.csuppteam = []
    p1.csuppback = []
    for x in p1.team:
      p1.cteam.append(x)
    for x in p1.backteam:
      p1.cbackteam.append(x)
    for x in p1.deadteam:
      p1.cdeadteam.append(x)
    for x in p1.suppteam:
      p1.csuppteam.append(x)
    for x in p1.suppback:
      p1.csuppback.append(x)
  for x in p2.team:
    p2.teamC.append(x)
  for x in p2.backteam:
    p2.backteamC.append(x)
  for x in p2.deadteam:
    p2.deadteamC.append(x)
  while winc == False:
    alliesgofirst = True
    lastat = ""
    turn = ""
    previous = ""
    turnstack = 0
    allfighters = []
    player1 = p1
    player2 = p2
    player1.teamID = []
    player2.teamID = []
    for x in player1.team:
      allfighters.append(x)
      player1.teamID.append(x.ID)
    for x in player2.team:
      allfighters.append(x)
      player2.teamID.append(x.ID)
    for x in player1.backteam:
      allfighters.append(x)
    for x in player1.deadteam:
      allfighters.append(x)
      x.resttimer = 21 - x.res
    for x in player2.backteam:
      allfighters.append(x)
    for x in player2.deadteam:
      allfighters.append(x)
    for x in allfighters:
      x.turncount = 0    
    for x in player1.team:#~
      if Mid == True:
        x.purge("Death",player1,player2,mid=True)
      else:
        x.purge("Death",player1,player2)
      x.purge("Map Reset",player1,player2)
    for x in player2.team:
      x.purge("Death",player2,player1)
      x.purge("Map Reset",player2,player1)
    for x in player1.suppteam:
      x.ccd = 0
    prebattleevent(player1,player2)
    while victory == 0:
      battleevent(player1,player2)
      battlespeed = []
      checka = len(player1.team)
      for y in range(checka):
        for x in player1.team:
          if x.cHP <= 0:
            x.purge("Death",player1,player2)
            player1.team.remove(x)
            if x.ID in player1.teamID:
              player1.teamID.remove(x.ID)
            if x.NAME in player1.teamS:
              player1.teamS.remove(x.NAME)
            player1.deadteam.append(x)
            player1.deadteamS.append(x.NAME)
      if len(player1.team) < 4 and len(player1.backteam) > 0:
        teamswitch(bat=True)
      if len(player1.team) == 0 and len(player1.backteam) == 0:
        break
      for x in player1.deadteam:
        if x.re == True:
          x.resttimer = x.resttimer - 1
          if x.resttimer == 0:
            x.cHP = round((0.10+(0.05*x.res))*x.fHP)
            if len(player1.team) < 4:
              player1.team.append(x)
              player1.teamS.append(x.NAME)
              player1.teamID.append(x.ID)
            else:
              player1.backteam.append(x)
              player1.backteamS.append(x.NAME)
            player1.deadteam.remove(x)
            player1.deadteamS.remove(x.NAME)
            time.sleep(0.5)
            print("\n"+x.NAME,"gets back up!")
            x.resttimer = 21 - (x.res)
      checke = len(player2.team)
      for y in range(checke):
        for x in player2.team:
          if x.cHP <= 0:
            x.purge("Death",player2,player1)
            player2.team.remove(x)
            if x.ID in player2.teamID:
              player2.teamID.remove(x.ID)
            if x.NAME in player2.teamS:
              player2.teamS.remove(x.NAME)
            player2.deadteam.append(x)
            player2.deadteamS.append(x.NAME)
      if len(player2.team) < 5 and len(player2.backteam) > 0:
        bruh = player2.backteam[0]
        bruhN = player2.backteamS[0]
        player2.backteam.remove(bruh)
        player2.backteamS.remove(bruhN)
        player2.team.append(bruh)
        player2.teamS.append(bruhN)
        player2.teamID.append(bruh.ID)
        print("\n"+bruh.NAME,"moves up to fight!")
      if len(player2.team) == 0 and len(player2.backteam) == 0:
        break
      for x in allfighters:
        if x in player1.team:
          x.globaltimers()
          x.currentstats(player1,player2)
        if x in player2.team:
          x.globaltimers()
          x.currentstats(player2,player1)
      for x in allfighters:
        if x in player1.team or x in player1.backteam or x in player1.deadteam:
          x.maptimers(player1,player2)
        if x in player2.team or x in player2.backteam or x in player2.deadteam:
          x.maptimers(player2,player1)
      for x in player1.suppteam:
        x.supporttimers()
      battlespeed = []
      for x in player1.team:
        if x.NAME in player1.teamS or x.invis > 0 and x.cSP > 0:
          for number in range(x.cSP):
            battlespeed.append(x.ID)
      if alliesgofirst == False:
        for x in player2.team:
          if x.NAME in player2.teamS or x.invis > 0 and x.cSP > 0:
            for number in range(x.cSP):
              battlespeed.append(x.ID)
      elif alliesgofirst == True:
        alliesgofirst = False
      for x in allfighters:
        if previous != "":
          x.deturn = x.deturn + 1
          if previous == x.ID:
            x.deturn = 0
          news = 0
          if x.deturn >=10:
            news = ((5+(1*x.deturn))*battlespeed.count(x.ID))
          else:
            news = ((1+(0.5*x.deturn))*battlespeed.count(x.ID))
          newss = round(news-battlespeed.count(x.ID))
          for t in range(newss):
            battlespeed.append(x.ID)
          if previous == x.ID and turnstack < 2:
            spamred = round((1-((0.5)**(turnstack+1)))*battlespeed.count(turn))
            for z in range(spamred):
              battlespeed.remove(turn)
          elif previous == x.ID and turnstack == 2:
            turnstack = 0
            x.deturn = -1
            y = battlespeed.count(x.ID)
            for t in range(y):
              battlespeed.remove(x.ID)
      turn = random.choice(battlespeed)
      if turn == previous:
        turnstack = turnstack + 1
      if turn != previous and previous != "":
        turnstack = 0
      previous = turn
      for x in player1.team:
        if turn == x.ID:
          x.onturntimers(player1,player2)
          if x.cHP > 0:
            for y in player1.team:
              y.currentstats(player1,player2)
            for y in player2.team:
              y.currentstats(player2,player1)
            if x.invis > 0:
              x.invis = x.invis - 1
              if x.invis == 0:
                x.instant = True
              x.stuns()
              x.fromtheshadows(player1,player2)
            else:
              x.stuns()
              x.allyattacksys(player1,player2)
            x.Isopower(player1)
      for x in player2.team:
        if turn == x.ID:
          x.onturntimers(player2,player1)
          if x.cHP > 0:
            for y in player2.team:
              y.currentstats(player1,player2)
            for y in player1.team:
              y.currentstats(player2,player1)
            x.stuns()
            x.AIdetector()
    if len(player2.team) == 0 and len(player1.team) > 0:
      rewards("Battle")
      winc = True
      victory = 1
      bots = Player()
    elif len(player1.team) == 0 or (len(player1.team) == 0 and len(player2.team) == 0):
      if Cont == False:
        time.sleep(1)
        input("\nYou died...")
        poop = 2
        while poop == 2:
          redux = input("\n(1) Restart Fight  (2) Continue from Last Checkpoint\nResponse: ")
          if redux == "1":
            if Mid == True:
              savereset("Mid")
            else:
              savereset()
            battlerestart()
            poop = 1
          elif redux == "2":
            data = []
            for x in dataC:
              data.append(x)
            savereset()
            sad = 1
            winc = True
            poop = 1
            bots = Player()
        if redux == "1":
          continue
      if Cont == True:
        winc = True
    fightid = 0

def battleinit():
  bots.teamS = []
  bots.backteamS = []
  for x in bots.team:
    x.genderset()
    bots.teamS.append(x.NAME)
  for x in bots.backteam:
    x.genderset()
    bots.backteamS.append(x.NAME)

def prebattleevent(p1,p2):
  global fightmod
  global fightid
  if fightid == 2:
    Ishraq.learnskill("Wild Instinct")
    Ishraq.WI = True
    Ishraq.wild = 4
    forceswitch(Kelly,True)
    print("\nIshraq instantly taps into his wild instincts, increasing his attack, speed, evasion, and critical chance, but reducing his magic attack, magic defense, and accuracy! His body starts to damage itself!",fore.YELLOW_1 + style.BOLD+"(NO NEED TO ACTIVATE SKILL!!!)"+style.RESET)
  if fightid == 3:
    Ishraq.WI = True
    Ishraq.wild = 4
  if fightid == 4:
    for x in range(4):
      Julius.battleinventory.append("Bandages")
      Ishraq.battleinventory.append("Bandages")
    Julius.learnskill("Runner's High")
    Julius.run = 0
  if fightid == 5:
    Julius.learnskill("Shield")
    Julius.shi = 0
  if fightid == 7:
    Kelly.learnskill("ASMR")
    Kelly.asm = 0


def battleevent(p1,p2):
  global allfighters
  global dif
  global fightmod
  global fightid

  for x in allfighters:
    if x.NAME == "The Soul of Kelly":
      sett = x.cHP
      quotes = ["Rebirth.","Life will continue on.","I am The Bringer of Life.","Life cycles through me."]
      for y in p1.backteam:
        y.setHP = y.cHP
      for y in p1.team:
        if y.cHP > y.setHP:
          x.cHP = x.cHP + (y.cHP-y.setHP)
          if x.cHP > x.fHP:
            x.cHP = x.fHP
        y.setHP = y.cHP
      if sett < x.cHP:
        kel = random.choice(quotes)
        time.sleep(1)
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"\nThe Soul of Kelly: "+kel+style.RESET)
        time.sleep(0.5)
        print("\n"+x.NAME,"is healed through the health generated from allies, healing for",fore.MEDIUM_SPRING_GREEN+str(x.cHP-sett)+style.RESET,"health! She has",x.cHP,"health now!")
      if (x.cHP <= 0.5*x.fHP) and x.tw2 == 0:
        time.sleep(1)
        sett = x.cHP
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"\nThe Soul of Kelly: God give me power..."+style.RESET)
        x.cHP = x.cHP + round(0.25*x.fHP*x.healmod)
        time.sleep(0.5)
        print("\n"+x.NAME,"calls upon higher powers to heal",x.GEN[1]+"self for",fore.MEDIUM_SPRING_GREEN+ str(x.cHP-sett)+style.RESET,"health!",x.GEN[2].capitalize(),"has",x.cHP,"health now!")
        time.sleep(1)
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"\nThe Soul of Kelly: You're all fired."+style.RESET)
        time.sleep(0.5)
        print("\n"+x.NAME,"unleashes the true power of the Isometric Drawings, increasing her power to the highest caliber!")
        x.ISOmode = True
        x.tw2 = 1
      if (x.cHP <= 0.25*x.fHP) and x.tw3 == 0:
        time.sleep(1)
        sett = x.cHP
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"\nThe Soul of Kelly: I see the light..."+style.RESET)
        x.cHP = x.cHP + round(0.25*x.fHP*x.healmod)
        time.sleep(1)
        print("\n"+x.NAME,"calls upon higher powers to heal",x.GEN[1]+"self for",fore.MEDIUM_SPRING_GREEN+ str(x.cHP-sett)+style.RESET,"health!",x.GEN[2].capitalize(),"has",x.cHP,"health now!")
        x.tw3 = 1
      if x.cHP <= 0 and x.tw4 == 0:
        time.sleep(1)
        x.cHP = x.fHP
        if dif == "1":
          x.invis = 6
        elif dif == "2":
          x.invis = 10
        elif dif == "3":
          x.invis = 15
        elif dif == "4":
          x.invis = 30
        elif dif == "5":
          x.invis = 99999
        if x.revealed <= 0:
          p2.teamS.remove(x.NAME)
          p2.teamID.remove(x.ID)
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"\nThe Soul of Kelly: I..."+style.RESET)
        time.sleep(1)
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"The Soul of Kelly: Am..."+style.RESET)
        time.sleep(1)
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"The Soul of Kelly: Immortal."+style.RESET)
        time.sleep(0.5)
        print("\n"+x.NAME,"revives herself completely, fully restoring her health!\n")
        time.sleep(1)
        print(fore.GREY_0 + back.MAGENTA_1 + style.BOLD+"The Soul of Kelly: Light."+style.RESET)
        time.sleep(0.5)
        print("\n"+x.NAME,"becomes light, rendering her invisible to the naked eye!")
        x.tw4 = 1

    if (x.immortal > 0 or x.emmortal > 0) and x.cHP <=0:
      time.sleep(1)
      print("\n"+x.NAME,"gets back up!")
      x.cHP = 1

    if x.NAME == "Julius" and x.ISOmode == True:
      if x.cHP <=0:
        x.ISOmode = False
        x.cHP = x.fHP
        x.isoboost = 6
        x.isoboostL = 1
        x.runhigh = 26
        time.sleep(1)
        print("\n"+x.NAME,"embraces his eternal will, standing back up to fight! He is fully powered-up by the runner's high and the isometric drawings!")
        x.Isopower(p1,EW=True)

    if x.NAME == "Mr. Pudup":
      x.stunimmune = [1,9999]

  if "Kelly" in p2.teamS and Kelly not in p2.team and "Amira" not in p2.teamS:
    p2.team.append(Kelly)

  if "Origins-N" in quests:
    print("\n(Press enter to continue)")
    input("\nYou're about to enter a battle.") 
    print("You will see a command list that looks like this")
    print(fore.YELLOW_1 + "\nIt's Daniels's turn." + style.RESET,"\nAttack, Skills, Items, Recover, or Check? ")
    input("\nTo interact with this command list, you can either type the commands or use corresponding numbers to what order they're in, such as 1 for attack, 2 for skills, etc.")
    tutorial = True
    while tutorial == True:
      s = input("\nWhat would you like to know about?\n(1) Attack (2) Skills (3) Items (4) Recover (5) Check (6) Support (7) I'm ready\nResponse: ")
      if s.lower() == "attack" or s == "1":
        input("\nThe attack command is the normal way to deal damage for all allies and enemies. There are two types of damage outputs, physical and magical. The attack command usually deals physical damage. The damage it deals is directly the value of attack(AT) a character has. When multiple enemies are present, you will be prompted to choose who to attack. A number must be used to target whomever. An enemy will fall and not be able to fight once their health points(HP) reach 0. Attacking also restores your mana points(MP) directly proportional to your mana regeneration(MRG)")
        continue
      if s.lower() == "skills" or s == "2":
        input("\nThe skill command lets you do many different things. Different skills can deal damage, strengthen your allies, or even cause enemies to hit each other! Allies all have different skills, and most skills cost some of your mana points(MP). Numbers or names of skills can be used to use them, but targeting an enemy needs a number.")
        continue
      if s.lower() == "items" or s == "3":
        input("\nThe items command allows you to use various different items to assist you in battle. An ally can only hold up to 4 items in battle. Numbers or names can be used to use whatever.")
        continue
      if s.lower() == "recover" or s == "4":
        input("\nThe recover command allows you to recover some of your mana points(MP) dependent on your mana regeneration(MRG). It restores double the amount attacking does, and is useful if you want to skip a turn in battle for any reason.")
        continue
      if s.lower() == "check" or s == "5":
        input("\nThe check command lets you check allied or enemy stats. These stats are the following:\n\nHP - Health Points that allow you to keep fighting\nMP - Mana points that let you cast skills\nAT - Attack that increases your physical damage\nDF - Defense that gives you damage reduction against physical damage\nMAT - Magic Attack that increases your magical damage\nMDF - Magic Defense that gives you damage reduction against magical damage\nSP - Speed that increases your chances of going the next turn\nAC - Accuracy that lets you hit opponents\nEV - Evasion that lets you dodge enemy attacks\nCT - Critical Chance to deal extra damage on certain attacks\nAPN - Armor Penetration that reduces enemy Defense on physical attacks\nMPN - Magic Penetration that reduces enemy Magic Defense on magical attacks\nMRG - Mana Regeneration that recovers your mana")
        continue
      if s.lower() == "support" or s == "6":
        input("\nThe support command allows you to call assistance from the 4000 students in PCTI. You can assign up to three support fighters into your team that all have their individual skills, some having special skills with certain main allies. Their skills can be used without wasting a turn, and go on cooldown for a number of total turns in battle.")
      if s.lower() == "i'm ready" or s == "7": 
        tutorial = False
        quests.remove("Origins-N")
        break 
  if "All Hail.." in quests:
    if fightid == 1:
      if Ishraq.cHP <= round(0.5*Ishraq.fHP) and Kelly not in p1.team and fightmod == 1:
        p1.team.append(Kelly)
        p1.teamS.append("Kelly")
        p1.teamID.append(Kelly.ID)
        allfighters.append(Kelly)
        time.sleep(0.4)
        print("\nKelly: I'm here Ishraq!")
      elif fightmod == 3:
        Ishraq.Q1B = 1
    
  if "The FX-Wing Nurse" in quests:
    if fightid == 4 and data[13] == 1 and Julius.cHP < Julius.fHP and Ishraq not in p1.team:
      text("\n*Ishraq charges through the fight*","Ishraq, pumped up: YOU THOUGHT I WAS GONNA LET YOU ONLY FIGHT?!","Julius, grinning: Ayy~! Come on, we got this!")
      revival(Ishraq)
      p1.teamID.append(Ishraq.ID)
      allfighters.append(Ishraq)

  if "The Straight Edge" in quests:
    if fightid == 6:
      for x in p2.team:
        x.confused = 99

  if "For the Horde" in quests:
    if fightid == 7 and fightmod == 1:
      if len(p1.team) == 1:
        if p1.team[0].cHP <= 0:
          text("\nBrandon, standing back: Ishraq...you gotta get back up.","Metin, a little worried: Kelly's out for the count...this is not looking good.","David, hopeful: Julius needs a minute...he'll get better soon.","\n*Ishraq's vision dims and his eyes struggle to stay open*\n","Ishraq, quietly: Shit...","Noah, hyping up: YOU GOT THIS MAN, YOU'RE THE GOAT!")
          if data[16] == 0:
            input("Hassan: WORD! THIS LIGHTWORK FOR YOU!")
          text("Metin: Ishraq boutta clutch the 1v20! EASY.","Ishraq, trying to raise his back off the floor but failing: Guys...you need to fight.","Metin, ready: I've been waiting for you to say that since the start.","Ishraq, eyes widening: Y-you need...you all need to fight...","David, teaming: TEAM! TEAM! TEAM! LET'S ALL TEAM ON THESE CLOWNS!","Ishraq, slowly losing consciousness: You guys...all can fight. It doesn't matter if they're wired. You guys are all strong...","David, looking at Ishraq shockingly: ISHRAQ! DON'T LET UP NOW! YOU'RE STRONGER THAN THAT!","\n*Some classmates begin to engage in combat with other wired*\n","Ishraq, listening to the battle and thinking to himself: ...This is not going to end well...I need to get up. *Ishraq forces his eyes open to stay awake*","Metin: THEY'RE ALL ON ME, WHAT ARE YA ALL DOING!!!??","Alvaro: They're too strong! I can't do anything!","*Ishraq slowly stands up from the ground*","Ishraq, with some energy: We need...we all need to fight!","\n*As David fights a wired, he notices Ishraq stand up...he makes direct eye contact with him. Ishraq stares into his eyes. David's mouth moves, but Ishraq cannot hear it. But he knew what he said.*","Ishraq, building up: Team. Team. Team. Team! Team! Team! TEAM! TEAM!! TEEAAAM!!! EVERYONE READY?! BULLDOGS ON THREE! ONE, TWO, THREE!!!","Everyone: BULLDOGS!!!!!","Ishraq, vibrating: WE CAN DO THIS!!")
          input(style.BOLD + fore.RED_1 +"\n~Ishraq has gained a new ability, Valorous Chant! He shouts to rally his teammates, fearing enemies and increasing all allied attack, defense, and speed, each boost in order per ally alive(4 for all effects, 3 for AT&DF&Fear, 2 for AT&Fear, himself for Fear)." + style.RESET)
          text("\n*The ground begins to shake...Julius gets up!*","Julius, laughing: HaHAA~! Now I'm pumped...these goons aren't getting passed me.","*Julius plants his fists into the ground, sending a shockwave towards the enemies, knocking nearly all of them over!*")
          input(style.BOLD+fore.GREEN_1+"\n~Julius has gained a new ability, Tremors! He sends shockwaves through the ground towards the enemies, dealing physical damage to all enemies based on his physical and magic attack. It has a chance to make enemies fall, stunning them. If they do not fall, they are slowed."+style.RESET)
          revival(Ishraq)
          Ishraq.learnskill("Valorous Chant")
          Ishraq.valo = 0
          if Ishraq.ID not in p1.teamID:
            p1.teamID.append(Ishraq.ID)
            allfighters.append(Ishraq)
          revival(Julius)
          Julius.learnskill("Tremors")
          Julius.trem = 0
          if Julius.ID not in p1.teamID:
            p1.teamID.append(Julius.ID)
            allfighters.append(Julius)
          for x in you.suppteam:
            if x.name == "Brandon":
              nig = Entity("Brandon",110,10,16,35,0,30,55,120,100,5,0,0,2,"50","Male")
              nig.learnskill("Groot Root")
            if x.name == "Edmond":
              nig = Entity("Edmond",90,10,20,25,0,45,60,100,120,8,0,0,2,"51","Male")
              nig.learnskill("Chill Vibes")
              nig.learnskill("Mixtape")
            if x.name == "David":
              nig = Entity("David",105,10,18,30,0,35,60,100,110,10,0,0,2,"52","Male")
              nig.learnskill("Team")
            if x.name == "Metin":
              nig = Entity("Metin",125,10,25,50,0,10,40,110,90,5,0,0,2,"53","Male")
              nig.learnskill("Bear")
            if x.name == "Noah":
              nig = Entity("Noah",95,10,17,30,0,40,55,120,120,7,0,0,2,"54","Male")
              nig.learnskill("Boxing Combo")
              nig.learnskill("Gaze")
            if x.name == "Hassan":
              nig = Entity("Hassan",115,10,18,35,0,25,60,110,100,8,0,0,2,"55","Male")
              nig.learnskill("Buckets")
            if x.name == "Alvaro":
              nig = Entity("Alvaro",85,10,14,25,0,40,45,100,100,6,0,0,2,"56","Male")
              nig.learnskill("Accurate Strike")
            if x.name == "Octavio":
              nig = Entity("Octavio",100,10,16,30,0,30,50,110,100,5,0,0,2,"57","Male")
              nig.learnskill("Cripple")
            you.backteam.append(nig)
            you.backteamS.append(x.name)
          for x in you.suppback:
            if x.name == "Brandon":
              nig = Entity("Brandon",110,10,16,35,0,30,55,120,100,5,0,0,2,"50","Male")
              nig.learnskill("Groot Root")
            if x.name == "Edmond":
              nig = Entity("Edmond",90,10,20,25,0,45,60,100,120,8,0,0,2,"51","Male")
              nig.learnskill("Chill Vibes")
              nig.learnskill("Mixtape")
            if x.name == "David":
              nig = Entity("David",105,10,18,30,0,35,60,100,110,10,0,0,2,"52","Male")
              nig.learnskill("Team")
            if x.name == "Metin":
              nig = Entity("Metin",125,10,25,50,0,10,40,110,90,5,0,0,2,"53","Male")
              nig.learnskill("Bear")
            if x.name == "Noah":
              nig = Entity("Noah",95,10,17,30,0,40,55,120,120,7,0,0,2,"54","Male")
              nig.learnskill("Boxing Combo")
              nig.learnskill("Gaze")
            if x.name == "Hassan":
              nig = Entity("Hassan",115,10,18,35,0,25,60,110,100,8,0,0,2,"55","Male")
              nig.learnskill("Buckets")
            if x.name == "Alvaro":
              nig = Entity("Alvaro",85,10,14,25,0,40,45,100,100,6,0,0,2,"56","Male")
              nig.learnskill("Accurate Strike")
            if x.name == "Octavio":
              nig = Entity("Octavio",100,10,16,30,0,30,50,110,100,5,0,0,2,"57","Male")
              nig.learnskill("Cripple")
            you.backteam.append(nig)
            you.backteamS.append(x.name)
          for x in you.backteam:
            allfighters.append(x)
            x.genderset()
          you.reset("Supp")
          fightmod = 2
    if fightmod == 2 and fightid == 7:
      if "Tremors" not in Julius.skills:
        Julius.skills.append("Tremors")

  if "Medical Attention" in quests:
    if fightid == 8:
      for x in p2.team:
        if x.NAME == "Bed" and x.cHP <=0:
          time.sleep(0.5)
          print("\nTim breaks free, joining the battle!")
          revival(Tim)
          if Tim.ID not in p1.teamID:
            p1.teamID.append(Tim.ID)
            allfighters.append(Tim)

  if "Transmission" in quests:
    if fightid == 9 and (fightmod == 1 or fightmod == 2 or fightmod == 3):
      if len(p2.team) == 1:
        if p2.team[0].cHP <= round(0.3*p2.team[0].HP):
          time.sleep(0.5)
           text("Kelly, totally lost: Okay, seriously, where are we?")
            if boop == "2":
              text("Trump, swearing he figured it out: You guys are defintely from China!","Kelly, offended: Umm...","Lincoln, figuring it out: No, they're not from here at all. As in, this universe.","Arwyn: This universe?","Trump, understanding: Ah, they're from a slow universe. How'd they even get here then?","*Another rift opens up!*","Lincoln, guiding: Seems like a tear to your universe is fluctuating here. You should take it now before you're stuck here.")
            if boop == "3":
              text("Musk, confirming his suspisions: I knew it. You guys seem foreign.","Kelly, a little offended: Foreign?","Musk, explaining: As in, not from this universe.","Arwyn: Not this universe?","*Another rift opens up!*","Musk, guiding: Seems like a tear to your universe is fluctuating here. You should take it now before you're stuck here.")
            text("Arwyn, not caring: Does League exist in this universe?","Kelly, grabbing Arwyn and jumping through the rift: Goodbye!","Arwyn, struggling: WAIT!","\n*Arwyn and Kelly land in the Engineering Shop room.*\n","Arwyn, visibly frustrated: Why are you so strong?","Kelly, sticking her tongue out: Cuz' I have an ISO! You do too, but you haven't used it much.","Arwyn, sour: Why is somone like you an ISO.","Kelly, ignoring: The other ISOs aren't here...let's find out where they went.")
          text("\n*A rift opens up on the battlefield*\n","Kelly, alerting Arwyn: HEY! It's looks like the same portal that got us here!")
          if fightmod == 1:
            text("Obama, understanding: I knew ya'll weren't from our universe.","Arwyn: Not our universe?","Kennedy, figuring it out: Aaah. Their universe isn't technologically advanced yet.","Obama, explaining: Seems like a tear to your universe is fluctuating here. You should take it now before you're stuck here forever.","*Kelly")
          if fightmod == 2:
            text("")
          if fightmod == 3:
            text("")
          Kelly.cMP = Kelly.fMP
          Kelly.learnskill("Perfect Requiem")
          Kelly.perfectr = 0
          fightmod = 4

              

def worldfunction():
  interupt = 0
  while interupt == 0:
    for x in croom:
      x.interface()

def battlerestart():
  for x in bots.team:
    x.saverest(bots,you)
  for x in bots.backteam:
    x.saverest(bots,you)
  for x in bots.deadteam:
    x.saverest(bots,you)
  bots.team = []
  bots.teamS = []
  bots.backteam = []
  bots.backteamS = []
  bots.deadteam = []
  bots.deadteamS = []
  for x in bots.teamC:
    bots.team.append(x)
    bots.teamS.append(x.NAME)
  for x in bots.backteamC:
    bots.backteam.append(x)
    bots.backteamS.append(x.NAME)
  for x in bots.deadteamC:
    bots.deadteam.append(x)
    bots.deadteamS.append(x.NAME)
  

def enemygenerator(enemy,position):
  global ename
  global gHP
  global gMP
  global gAT
  global gDF
  global gMAT
  global gMDF
  global gSP
  global gAC
  global gEV
  global gCT
  global gAPN
  global gMPN
  global gMRG
  global gGEN
  ename = enemy
  genders = ["Male","Female"]
  lvs = (Ishraq.LV+Kelly.LV+Julius.LV+Tim.LV+Daniel.LV+Arwyn.LV)
  if enemy == "Freshman":
    gHP = round(random.randint(6,18)*(1+((19/240)*lvs)))
    gMP = 0
    gAT = round(random.randint(3,7)*(1+((6.5/240)*lvs)))
    gDF = round(random.randint(10,15)*(1+((2/240)*lvs)))
    gMAT = 0
    gMDF = round(random.randint(0,5)*(1+((2/240)*lvs)))
    gSP = random.randint(25,35)
    gAC = random.randint(85,110)
    gEV = random.randint(85,110)
    gCT = random.randint(0,4)
    gAPN = 0
    gMPN = 0
    gMRG = 0
    gGEN = random.choice(genders)
    infernalmobs(ename)
  elif enemy == "Sophomore":
    gHP = round(random.randint(10,20)*(1+((19/240)*lvs)))
    gMP = 0
    gAT = round(random.randint(4,9)*(1+((6.5/240)*lvs)))
    gDF = round(random.randint(13,19)*(1+((2/240)*lvs)))
    gMAT = 0
    gMDF = round(random.randint(5,10)*(1+((2/240)*lvs)))
    gSP = random.randint(30,35)
    gAC = random.randint(90,115)
    gEV = random.randint(85,110)
    gCT = random.randint(1,5)
    gAPN = random.randint(0,2)
    gMPN = 0
    gMRG = 0
    gGEN = random.choice(genders)
    infernalmobs(ename)
  elif enemy == "Junior":
    gHP = round(random.randint(12,25)*(1+((19/240)*lvs)))
    gMP = 0
    gAT = round(random.randint(5,10)*(1+((6.5/240)*lvs)))
    gDF = round(random.randint(15,25)*(1+((2/240)*lvs)))
    gMAT = 0
    gMDF = round(random.randint(10,15)*(1+((2/240)*lvs)))
    gSP = random.randint(35,40)
    gAC = random.randint(90,120)
    gEV = random.randint(90,110)
    gCT = random.randint(2,6)
    gAPN = random.randint(0,5)
    gMPN = 0
    gMRG = 0
    gGEN = random.choice(genders)
    infernalmobs(ename)
  elif enemy == "Senior":
    gHP = round(random.randint(15,30)*(1+((19/240)*lvs))) #x20
    gMP = 0
    gAT = round(random.randint(6,12)*(1+((6.5/240)*lvs)))  #x7.5
    gDF = round(random.randint(20,30)*(1+((2/240)*lvs))) #x3
    gMAT = 0
    gMDF = round(random.randint(40,45)*(1+((2/240)*lvs)))  #x3
    gSP = random.randint(40,45) 
    gAC = random.randint(90,120)
    gEV = random.randint(95,115)
    gCT = random.randint(2,6)
    gAPN = random.randint(0,10)
    gMPN = 0
    gMRG = 0
    gGEN = random.choice(genders)
    infernalmobs(ename)
  bots.team.append(Entity(ename,gHP,gMP,gAT,gDF,gMAT,gMDF,gSP,gAC,gEV,gCT,gAPN,gMPN,gMRG,str(position+16),gGEN))


def infernalmobs(name):
  global ename
  global gHP
  global gMP
  global gAT
  global gDF
  global gMAT
  global gMDF
  global gSP
  global gAC
  global gEV
  global gCT
  global gAPN
  global gMPN
  global gMRG
  global gGEN
  global inferno
  if name == "Freshman":
    randomweight("Infernal","",5,"Fat ",3,"Skinny ",4,"Stupid ",2,"Nerdy ",4)
  elif name == "Sophomore":
    randomweight("Infernal","",5,"Fat ",3,"Skinny ",4,"Stupid ",2,"Nerdy ",4)
  elif name == "Junior":
    randomweight("Infernal","",5,"Fat ",3,"Skinny ",4,"Stupid ",2,"Nerdy ",4)
  elif name == "Senior":
    randomweight("Infernal","",5,"Fat ",3,"Skinny ",4,"Stupid ",2,"Nerdy ",4)
  woah = random.choice(inferno)
  if woah != "":
    ename = woah + name
  if "Fat" in ename:
    gHP = round(2*gHP)
    gSP = round(gSP/2)
    gDF = round(2*gDF)
    gEV = round(gEV/2)
  elif "Skinny" in ename:
    gHP = round(0.75*gHP)
    gEV = round(1.25*gEV)
  elif "Stupid" in ename:
    gMAT = round(gMAT/2)
    gMDF = round(gMDF/2)
    gAT = round(gAT*2)
    gDF = round(gDF*2)
  elif "Nerdy" in ename:
    gMAT = round(gMAT*2)
    gMDF = round(gMDF*2)
    gAT = round(gAT/2)
    gDF = round(gDF/2)

def randomweight(types,enem1,enem1w,enem2="",enem2w=0,enem3="",enem3w=0,enem4="",enem4w=0,enem5="",enem5w=0): 
  global weight
  global inferno
  if types == "Mobs":
    weight = []
    for x in range(enem1w):
      weight.append(enem1)
    if enem2 != "":
      for x in range(enem2w):
        weight.append(enem2)
    if enem3 != "":
      for x in range(enem3w):
        weight.append(enem3)
    if enem4 != "":
      for x in range(enem4w):
        weight.append(enem4)
    if enem5 != "":
      for x in range(enem5w):
        weight.append(enem5)
  if types == "Infernal":
    inferno = []
    for x in range(enem1w):
      inferno.append(enem1)
    if enem2 != "":
      for x in range(enem2w):
        inferno.append(enem2)
    if enem3 != "":
      for x in range(enem3w):
        inferno.append(enem3)
    if enem4 != "":
      for x in range(enem4w):
        inferno.append(enem4)
    if enem5 != "":
      for x in range(enem5w):
        inferno.append(enem5)

def rewards(questorbattle,quest=""):
  tot = 0 
  mon = 0
  ni = you.money
  if questorbattle == "Battle":
    for x in bots.deadteam:
      if x.NAME == "Richard":
        tot = tot + 50
      if x.NAME == "Amira":
        tot = tot + 5000
      if x.NAME == "Ryca":
        tot = tot + 50
      if "Nurse" in x.NAME:
        tot = tot + 50
      if "Freshman" in x.NAME:
        tot = tot + 3
        mon = mon + round((random.randint(1,100)/100),2)
      if "Sophomore" in x.NAME:
        tot = tot + 6
        mon = mon + round((random.randint(5,150)/100),2)
      if "Junior" in x.NAME:
        tot = tot + 10
        mon = mon + round((random.randint(10,200)/100),2)
      if "Senior" in x.NAME:
        tot = tot + 15
        mon = mon + round((random.randint(25,500)/100),2)
    xpg(tot)
    you.money = round((you.money + mon),2)
    ree = round((you.money-ni),2)
    if mon > 0:
      print("\nThe group finds "+"${:,.2f}".format(ree)+"! They now have "+"${:,.2f}".format(you.money),"in total!")
  

def xpg(amount):
  ish = Ishraq.XP
  kel = Kelly.XP
  jul = Julius.XP
  dan = Daniel.XP
  tim = Tim.XP
  arw = Arwyn.XP
  print("")
  for x in you.team:
    x.XP = x.XP + amount
  for x in you.backteam:
    x.XP = x.XP + round(amount/2)
  for x in you.deadteam:
    x.XP = x.XP + round(amount/4)
  print("")
  if ish != Ishraq.XP:
    Ishraq.Ishraqlevelup(Ishraq.XP-ish)
  if kel != Kelly.XP:
    Kelly.Kellylevelup(Kelly.XP-kel)
  if jul != Julius.XP:
    Julius.Juliuslevelup(Julius.XP-jul)
  if dan != Daniel.XP:
    Daniel.Daniellevelup(Daniel.XP-dan)
  if tim != Tim.XP:
    Tim.Timlevelup(Tim.XP-tim)
  if arw != Arwyn.XP:
    Arwyn.Arwynlevelup(Arwyn.XP-arw)

def save(load,fi):
  global world
  global data
  global croom
  global quests
  global qcomp
  global Ishraq
  global Julius
  global Kelly
  global Daniel
  global Tim
  global Arwyn
  global you
  re = "saves" + str(fi) +".txt"
  if load == "save":
    os.remove(re)
    with open(re, 'wb') as f:
      pickle.dump([you,world,croom,Ishraq,Julius,Kelly,Daniel,Tim,Arwyn,croom,data,quests,qcomp], f, protocol=2)
  if load == "load":
    with open(re, 'rb') as f:
      you,world,croom,Ishraq,Julius,Kelly,Daniel,Tim,Arwyn,croom,data,quests,qcomp = pickle.load(f)
      you.team = []
      you.backteam = []
      you.deadteam = []
      for x in you.teamS:
        if x == "Ishraq":
          you.team.append(Ishraq)  
        elif x == "Daniel":
          you.team.append(Daniel)
        elif x == "Tim":
          you.team.append(Tim)
        elif x == "Julius" or x == "Ian":
          you.team.append(Julius)
        elif x == "Kelly":
          you.team.append(Kelly)
        elif x == "Arwyn":
          you.team.append(Arwyn)
      for x in you.backteamS:
        if x == "Ishraq":
          you.backteam.append(Ishraq)  
        elif x == "Daniel":
          you.backteam.append(Daniel)
        elif x == "Tim":
          you.backteam.append(Tim)
        elif x == "Julius" or x == "Ian":
          you.backteam.append(Julius)
        elif x == "Kelly":
          you.backteam.append(Kelly)
        elif x == "Arwyn":
          you.backteam.append(Arwyn)
      for x in you.deadteamS:
        if x == "Ishraq":
          you.deadteam.append(Ishraq)  
        elif x == "Daniel":
          you.deadteam.append(Daniel)
        elif x == "Tim":
          you.deadteam.append(Tim)
        elif x == "Julius" or x == "Ian":
          you.deadteam.append(Julius)
        elif x == "Kelly":
          you.deadteam.append(Kelly)
        elif x == "Arwyn":
          you.deadteam.append(Arwyn)

def autosave():
  Ishraq.savedstats()
  Julius.savedstats()
  Arwyn.savedstats()
  Tim.savedstats()
  Daniel.savedstats()
  Kelly.savedstats()
  you.teamC = []
  you.deadteamC = []
  you.backteamC = []
  you.suppteamC = []
  you.suppbackC = []
  dataC = []
  for x in you.team:
    you.teamC.append(x)
  for x in you.deadteam:
    you.deadteamC.append(x)
  for x in you.backteam:
    you.backteamC.append(x)
  for x in you.suppteam:
    you.suppteamC.append(x)
  for x in you.suppback:
    you.suppbackC.append(x)
  for x in data:
    dataC.append(x)

def savereset(Con=""):
  if Con == "Mid":
    Ishraq.saverest(you,bots,"Mid")
    Kelly.saverest(you,bots,"Mid")
    Julius.saverest(you,bots,"Mid")
    Arwyn.saverest(you,bots,"Mid")
    Tim.saverest(you,bots,"Mid")
    Daniel.saverest(you,bots,"Mid")
  else:
    Ishraq.saverest(you,bots)
    Kelly.saverest(you,bots)
    Julius.saverest(you,bots)
    Arwyn.saverest(you,bots)
    Tim.saverest(you,bots)
    Daniel.saverest(you,bots)
  you.team = []
  you.teamS = []
  you.deadteam = []
  you.deadteamS = []
  you.backteam = []
  you.backteamS = []
  you.suppteam = []
  you.suppteamS = []
  you.suppback = []
  you.suppbackS = []
  if Con =="Mid":
    for x in you.cteam:
      you.team.append(x)
      you.teamS.append(x.NAME)
    for x in you.cdeadteam:
      you.deadteam.append(x)
      you.deadteamS.append(x.NAME)
    for x in you.cbackteam:
      you.backteam.append(x)
      you.backteamS.append(x.NAME)
    for x in you.csuppteam:
      you.suppteam.append(x)
      you.suppteamS.append(x.name)
    for x in you.csuppback:
      you.suppback.append(x)
      you.suppbackS.append(x.name)
  else:
    for x in you.teamC:
      you.team.append(x)
      you.teamS.append(x.NAME)
    for x in you.deadteamC:
      you.deadteam.append(x)
      you.deadteamS.append(x.NAME)
    for x in you.backteamC:
      you.backteam.append(x)
      you.backteamS.append(x.NAME)
    for x in you.suppteamC:
      you.suppteam.append(x)
      you.suppteamS.append(x.name)
    for x in you.suppbackC:
      you.suppback.append(x)
      you.suppbackS.append(x.name)

def preeventcheck():
  global sad
  global nextr
  global fightmod
  global fightid
  global victory
#------------------------------------------------------------------------------------
  if "All Hail..." in quests:
    if croom[0].RID == 1:
      if nextr == "D-Wing Hallway 1st Floor":
        if data[10] == 0:
          time.sleep(1)
          text("\nKelly, curious: Ishraq, why do you wanna go to the D-Wing?","Ishraq, worried: Didn't you hear that? I think someone might be in trouble.","Kelly, foreboding: You sure you wanna go? We might get attacked.")
          talk = "1"
          while talk =="1":
            dec = input("\n(1) Yes  (2) No\nResponse: ")
            if dec == "1":
              input("\nIshraq, fearless: Yeah, let's go.")
              break
            elif dec =="2":
              input("\nIshraq, nervous: On second thought, let's head to shop.")
              sad = 1
              break
        elif data[10] == 1:
          time.sleep(0.5)
          print("\nKelly: It's too dangerous to go back! We'll go later if we can!")
          time.sleep(0.5)
          sad = 1
        elif data[10] == 2:
          time.sleep(0.5)
          print("\nKelly: We can hang out at the Medical shop later, we need to go to our shop first.")
          time.sleep(0.5)
          sad = 1
      elif nextr == "F-Wing Media Center":
        time.sleep(0.5)
        print("\nKelly: Let's go to our shop room first.")
        time.sleep(0.5)
        sad = 1
      elif nextr == "F-Wing Hallway 2nd Floor":
        time.sleep(0.5)
        print("\nKelly: Pretty sure we'll get to shop faster if we just stay on the 1st floor.")
        time.sleep(0.5)
        sad = 1
    elif croom[0].RID == 2: 
      if nextr == "F-Wing Hallway 1st Floor":
        time.sleep(0.5)
        print("\nKelly: Why do you wanna turn back? Let's go already.")
        time.sleep(0.5)
        sad = 1
      if nextr == "H-Wing Complex 1st Floor":
        time.sleep(0.5)
        print("\nKelly: Ishraq, the bridge is the last place we wanna go.")
        time.sleep(0.5)
        sad = 1
      if nextr == "FX-Wing Hallway 2nd Floor":
        time.sleep(0.5)
        print("\nKelly: Shop is downstairs, not upstairs...are you drunk?")
        time.sleep(0.5)
        sad = 1
      if nextr == "FX-Wing Nurse's Office":
        time.sleep(0.5)
        print("\nKelly: We're pretty hurt, but we'll go to the nurse later.")
        time.sleep(0.5)
        sad = 1
    elif croom[0].RID == 6:
      if len(croom[0].people) > 2:
        time.sleep(0.5)
        print("\nIshraq, thinking to himself: (I should talk to everyone first.)")
        time.sleep(0.5)
        sad = 1
      else:
        if "Brandon" in you.suppteamS:
          time.sleep(0.5)
          text("\nIshraq, opening the door: Let's head out.","Brandon, walking over: Followin'","Julius, having fun with stereotypes: How we gonna leave these two kids alone? They're gonna jank everything in here, haHAA!","Edmond, with a slight smile: I might honestly take Miller's hall passes.","Brandon, already outside: Let's go already.","Ishraq, looking at Julius: Alright, we should check my calc room for a ruler, bound to have one.","Julius, pointing up: It's upstairs right?","Ishraq, bringing up different objectives: Yeah, Mrs. Wells's classroom, or we could go to the nurse's office down the hall.")
        elif "Edmond" in you.suppteamS:
          text("\nIshraq: Let's head out.","Edmond, walking over: Followin'","Julius, making fun of Brandon's height and appearence: How we gonna leave Groot with David? He can't help David if he can't speak, haHAA!","Brandon, laughing: That's whack.","Julius: I am groot!","Edmond, already outside: Let's go already.","Ishraq, looking at Julius: Alright, we should check my calc room for a ruler, bound to have one.","Julius, pointing up: It's upstairs right?","Ishraq, bringing up different objectives: Yeah, Mrs. Wells's classroom, or we could go to the nurse's office down the hall.")
        xpg(100)
        questsys("All Hail...","Finish")
        Julius.learnskill("Rest")
        ro = rd(8)
        ro.paths.append("Mrs. Wells's Classroom")
#------------------------------------------------------------------------------------   
  if "The FX-Wing Nurse" in quests:
    ro = rd(25)
    if ro in croom and ro.TYPE == "Camp":
      time.sleep(0.5)
      if data[13] == 0:
        print("\nIshraq: Need something for Kelly before we go.")
      else:
        print("\nJulius: Ishraq and Kelly still need my help.")
      time.sleep(0.5)
      sad = 1
#------------------------------------------------------------------------------------ 
  if "No Talking in The Library" in quests:
    ro = rd(14)
    if ro in croom and nextr == "C-Wing Hall 1st Floor" and "Calligraphy" not in Kelly.skills:
      time.sleep(0.5)
      print("\nIshraq: We're not finished searching here yet.")
      time.sleep(0.5)
      sad = 1
    elif ro in croom and nextr == "C-Wing Hall 1st Floor" and "Calligraphy" in Kelly.skills:
      questsys("No Talking in The Library","Finish")
      xpg(200)
      ro.people = []
#------------------------------------------------------------------------------------ 
  if "The FX-Wing Nurse" in quests or "The Straight Edge" in quests:
    if nextr == "D-Wing Hallway 1st Floor": 
      time.sleep(0.5)
      if "The FX-Wing Nurse" not in quests:
        print("\nKelly: Ishraq, Mrs. Wells's room is upstairs in the FX...and look, the bridge is guarded by students. Why do you wanna go?")
      else:
        print("\nJulius: Ishraq, there's too many people across the bridge, we can't take em'.")
      time.sleep(0.5)
      sad = 1
    if nextr == "H-Wing Complex 1st Floor":
      time.sleep(0.5)
      if "The FX-Wing Nurse" not in quests:
        print("\nKelly: Ishraq, Mrs. Wells's room is upstairs...and don't you see those students across the bridge? Suicide mission much?")
      else:
         print("\nJulius: Ishraq, we can't just travel right now, we need to go to the nurse.")
      time.sleep(0.5)
      sad = 1
#------------------------------------------------------------------------------------   
  if data[17] == 2:
    time.sleep(1)
    text("\nMetin, grabbing Ishraq: Yo, is there any food here?")
    if data[16] == 0:
      text("Hassan: Word, I'm hungry. We need some food from the cafe.")
    else:
      text("Ishraq, reminded of his hunger: Uuuh...nope, there's no food.")
    text("Noah, yawning: Ooghh...we should make a stop by the cafe Ishrish.","Ishraq, a bit hungry himself: Yeah, we'll go loot the cafe.")
    questsys("Feeling Alone","StartS")
    data[17] = 3
#------------------------------------------------------------------------------------
  if nextr == "F-Wing Media Center" and data[20] == 0:
    time.sleep(0.5)
    print("\nIshraq: It's locked...")
    if "No Talking in The Library" in quests:
      time.sleep(0.25)
      print("Kelly: Let's check the C-Wing Library then.")
    time.sleep(0.5)
    sad = 1
#------------------------------------------------------------------------------------
  if "More Than Meets The Eye" in quests:
    if nextr == "Automotive Building" and "No Talking in The Library" not in qcomp:
      text("\nIshraq, opening the doors to the outside: I've never been to the automotive building.","Kelly, going out first: I don't think anyone of us have.","\n*The group goes down the outdoor stairwell to the Automotive building*","\nIshraq, looking at the glaring red lock: We need a teacher's ID...","Julius, scratching his head: Damn it...I guess we should go to the Media Center first.")
      data[21] = 1
      sad = 1
    elif nextr == "Automotive Building" and "No Talking in The Library" in qcomp:
      if data[21] == 0:
        text("\nIshraq, opening the doors to the outside: I've never been to the automotive building.","Kelly, going out first: I don't think anyone of us have.")
      text("\n*The group goes down the outdoor stairwell to the Automotive building*","\nIshraq, looking at the glaring red lock: We need a teacher's ID...damn it, we should've grabbed the Librarian's.","Kelly, approaching the lock: Hey, let me try something.","\n*Kelly takes out her calligraphy pen*\n","Kelly, explaining: I feel this power inside this pen...its light can physically and emotionally alter things. I think I can recalibrate the lock's system with the pen so it reacts to its light.","Ishraq, confused: What makes you think any of that?","Kelly, also confused: I don't know...I just know it's going to work. The Iso in me...it's telling me.","Ishraq, with belief: Alright, give it a shot.","\n*Kelly successfully hacks the lock*\n","Julius, impressed: Wow, that was cool.","Ishraq, opening the door: No time to waste, let's find that Iso for you Julius.","Julius: Yezir.")
      ro = rd(18)
      ro.objects = ["Ominous Car"]
      ro.people = ["Julius","Kelly"]
#------------------------------------------------------------------------------------
  if "Don't Trip" in quests:
    yikes = input("\nStart the deathmarch?\n(1) Yes  (2) No\nAction: ")
    if yikes == "1" or yikes.lower() == "yes":
      ro = rd(18)
      ro.ENC = 80
      ro.deathmarch(9,"Edge")
      if victory == 1:
        text("\n*Alvaro and Octavio regain their senses*\n","Ishraq: You guys alright?","Alvaro, waking up: What's going on?","Kelly, interceding: I got this Ishraq.","\n*Kelly explains everything*\n","Octavio, crazed out: This really is like an anime!","Julius: Word.","Ishraq, slightly grinning: I guess...and yeah, there's no where to go. We're stuck in Tech it seems.","Kelly, looking out: I can sort of see where the world is missing from here...so now what?","Ishraq: We should go back to shop. Gather as much as people as we can. We need to take this school back.","Alvaro: Agreed. If anyone's gonna lead, it has to be you Ishraq.","Ishraq, intrigued: Why do you say that? Hegheh.","Alvaro, praising: You took down The Fence. You're like the rep of the Engineering shop.","Kelly, jealous: Umm, are you sure about that?","Alvaro, putting aside: Well like...you're Kelly. And Ishraq is Ishraq.","Julius: Yeah, Ishraq is GOAT status Kelly, sorry.","Kelly: Yeah, whatever. I'm clearly the representative though. GPA, NASA Hunch...yeah.","Julius, vibing: Ight, but can you code games like Ishraq?","Ishraq, laughing: Hahaha, Kelly just quit it. I'm more popular with the boys.","Kelly, annoyed: Whatever.","\n*The group travels back to the Automotive Building*\n")
        supu("Alvaro",11)
        supu("Octavio",11)
        questsys("Don't Trip","Finish")
        questsys("For the Horde","StartM")
    elif yikes == "2" or yikes.lower() == "no":
      sad = 1
#------------------------------------------------------------------------------------
  if "Daily Checkup" in quests or "Medical Attention" in quests:
    ro = rd(6)
    if ro.RLV != 3:
      input("\nKelly, taking a step back: I should really find out if this ISO belongs to anyone in here.")
      sad = 1
    ro = rd(28)
    if ro.RLV == 2:
      text("\nJulius, asking Kelly: So what are we gonna do now?","Kelly, thinking: Hmm...I dunno yet. We could go to shop rooms and start freeing students. But I really want to go back to shop so I can wake that bozo up.","Julius, letting Kelly lead: You do whatever, we stick together.","Tim, suggesting: Ah, you know what. I'm missing my backpack. The last place I remember being before I was wired was in my ASL room. Can we stop by there?","Kelly: Yeah, sure Tim. But where is it?","Tim: It's right around the corner in the C-Wing.")
      if "Daily Checkup" in quests:
        questsys("Daily Checkup","Finish")
      elif "Medical Attention" in quests:
        questsys("Medical Attention","Finish")
      questsys("Sign Language","StartM")
      ro.RLV = 3
      ro = rd(9)
      ro.paths.append("ASL Room")
#------------------------------------------------------------------------------------
  if "Sign Language" in quests:
    if nextr == "F-Wing Hallway 1st Floor":
      time.sleep(0.5)
      print("\nTim: My ASL room is in the C-Wing.")
      sad = 1
      time.sleep(0.5)
    if nextr == "FX-Wing Hallway 1st Floor":
      time.sleep(0.5)
      print("\nTim: Shop later, first my ASL room, which is in the C-Wing.")
      sad = 1
      time.sleep(0.5)
    if croom[0].RID == 29:
      text("\nKelly, curious: I didn't know you took sign language Tim. Are you good at it?","Tim, laughing: Haha, no. I do know quite a bit. Like this is how you say 'I love you.'","*Tim signs the phrase, and a yellow spark starts to orbit around Kelly*","Kelly, looking down frantically: UUUHH, what is this!!??","Tim, startled from her anxiousness: UMMM, I DON'T KNOW.","Kelly, breaking down: I'M GONNA DIE!","Tim, attempting to slap her: No, you're not gonn--!! What?","\n*As Tim tried to slap her, his force was completely rejected and Kelly's body did not move an inch--The yellow spark dissipates!*\n","Kelly, taking Tim's hand off her face: Don't touch me.","Tim, backing off: Okayyy...I think I might've signed you some sort of barrier...",fore.CYAN_1+style.BOLD+"\n~Tim has gained a new ability, Quen! He shields himself or an ally and removes all negative effects from them. The shield lasts for 1 hit, and has a max threshold of shielding.\n"+style.RESET,"Kelly, devilishy grinning: A barrier, huh? I expect you'll be using it on me only...or I might just not heal you~","Tim, slightly defeated: Ew.","Julius, insisting: Alright, let's quickly get back to shop.")
      Tim.learnskill("Quen")
      questsys("Sign Language","Finish")
      data[23] = ""
      questsys("Showdown","StartM")
      xpg(50)
      ro = rd(6)
      ro.people.append("Ishraq")
#------------------------------------------------------------------------------------
  if "Transmission" in quests:
    if croom[0].RID == 23 and croom[0].RLV == 1:
      text("\n*The formerly wired students begin to wake back up!*\n","Kenny, dazed: Ughh..W-where am I? This is the auditorium..","Matvey, in visible disgusted confusion: I was in the bathroom...taking a shit...","Daniel, in shock: No...","Daniel suddenly gets up and charges at Ishraq! Ishraq is shoved, but he catches himself before he falls!*","Ishraq, not expecting that: Hey, what was that for?")
      if data[24] == 1:
        text("Daniel, furious: YOU!! YOU HURT HER!!","Ishraq, mad confused: What?","Daniel, spitting all over Ishraq: YOU JUST COULDN'T GIVE HER UP TO THE FEDORA GUY, HUH?! INSTEAD, YOU DECIDE TO BE A WHITE-KNIGHT AND END UP CAUSING HER MORE PAIN!!","Ishraq, astounded: Wait, you remember?!","Daniel, punching a seat: OF COURSE I DO!!","Ishraq, laughing his ass off: HEHAHA!! YOU'RE ACTING LIKE YOU WOULDN'T HAVE DONE THE SAME THING!","Daniel, bloodshot as he grabs Ishraq's shirt: If you ever hurt her ever again...I'm coming for you.","Ishraq, dying: BRUUUUHH, I didn't even hurt Kelly directly! Relax buddy!","Daniel, letting go of him: I'll make sure you don't. I'll stick real close, friend.","Ishraq, shrugging: Okay buddy.","\n~Daniel is a Dominican Peruvian 10th grade engineering student at the highschool of PCTI. He is a VEX competitor, and one of the two students, the only in engineering, to get a 5 on the AP Physics exam. He is infatuated with learning and helping others, but is anything but a saint. He loves to bully people for the sheer entertainment of it, but also finds it funny to get bullied. He has no shame whatsoever, being able to do absolutely wild things.")
      else:
        if data[23] != "":
          text("Daniel, furious: YOU!! YOU DIDN'T SAVE HER!!","Ishraq, astounded: Wait, how do you know that?! You were wired!!","Daniel, punching a seat: OF COURSE I REMEMBER!!","Ishraq, laughing his ass off: HEHAHA!! HOW?!","Daniel, visibly disturbed: I will always remember every moment I see my queen...every...every moment.","Ishraq, dying: BRUUUUH, this is crazy! Of course you would be able to do that!","Daniel, looking down: I remember...","Ishraq, concerned: You okay friend?","Daniel, deciding to hide it: It's nothing. Anyways, I'll make sure I save her. I'll do what you couldnt.","Ishraq, shrugging: Okay buddy.","\n~Daniel is a Dominican Peruvian 10th grade engineering student at the highschool of PCTI. He is a VEX competitor, and one of the two students, the only in engineering, to get a 5 on the AP Physics exam. He is infatuated with learning and helping others, but is anything but a saint. He loves to bully people for the sheer entertainment of it, but also finds it funny to get bullied. He has no shame whatsoever, being able to do absolutely wild things.")
        else:
          text("Daniel, furious: YOU!! YOU DIDN'T SAVE HER!!","Ishraq, astounded: Wait, how do you know that?! You were wired!!","Daniel, punching a seat: OF COURSE I REMEMBER!!","Ishraq, laughing his ass off: HEHAHA!! HOW?!","Daniel, like a soldier on duty: I will always remember every moment I see my queen...every word she speaks...everything.","Ishraq, dying: BRUUUUH, this is crazy! Of course you would be able to do that!","Daniel, looking down at Ishraq: I'll make sure I save her. I'll do what you couldn't.","Ishraq, shrugging: Okay buddy.","\n~Daniel is a Dominican Peruvian 10th grade engineering student at the highschool of PCTI. He is a VEX competitor, and one of the two students, the only in engineering, to get a 5 on the AP Physics exam. He is infatuated with learning and helping others, but is anything but a saint. He loves to bully people for the sheer entertainment of it, but also finds it funny to get bullied. He has no shame whatsoever, being able to do absolutely wild things.")
      croom[0].RLV = 2
      revival(Daniel,o=True)
      Daniel.XP = round(((Kelly.XP + Julius.XP + Ishraq.XP + Tim.XP)/4)-100)
      Daniel.Daniellevelup(Daniel.XP,Colis=True)
      Daniel.learnskill("Taunt")
#------------------------------------------------------------------------------------
  if data[22] == 0 and nextr == "Cafe 1":
    input("\nIshraq, confused: All the doors are locked...")
    sad = 1
      
def eventcheck():
  global sad
  global nextr
  global fightmod
  global fightid
  global victory
  global fi
  global dif
  victory = 0
  #------------------------------------------------------------------------------------
  if "Origins" in quests and croom[0].RID == 0:
    time.sleep(1)
    print("\n(Press enter to continue the dialogue)")
    time.sleep(1)
    text("\nDisclaimer: Some of the dialogues in this game are meant to be satirical and unnatural. These exaggerated dialogues do not represent any of the characters in real-life.","\n~It was a normal day at the school of PCTI, commonly referred to as Tech. Daniel was walking with his fellow engineering student, Kelly, through the hallways of Tech. On their way to their next class together, a man approached them, alarming Daniel.","\nDaniel, bombastically: You dare stand in the way of none other than the great Kelly, and I, Daniel!?","???, irreverently: Oh, I'm sorry. You see...I can't proceed, as you're blocking the entire hallway with that frame of yours.","Daniel, trying to hold in a laugh: BHGFHHGH..!! You should watch your mouth...my calibur of expertise is far above anyone's inferior intellect.","???, cheering: Ah! A fellow man of culture I see! You have such a lovely mistress walking beside you! *Blows kisses*","Daniel, suddenly serious: Yes, but she is only mine to behold...so you better back off!","Kelly, confused and weirded out: What are you even saying?","???, aggressively: *Lunges to grope Kelly*, SHE SHALL BE MINE FOR THE TAKING!!","Kelly: *Shrieks*","Daniel, hero-like: *Pushes the man away from Kelly*, NO! I WILL STOP YOU RIGHT HERE! LET THIS BE A DUEL BETWEEN US MEN!","???, with the cool-guy tone: *Tips Fedora*, So be it then.")
    print("\nDaniel begins his duel the The Fedora Man!\n")
    Daniel.HP = 800
    Daniel.cHP = 800
    Daniel.AT = 100
    Daniel.DF = 80
    Daniel.MAT = 120
    Daniel.MDF = 80
    Daniel.CT = 20
    Daniel.MRG = 10
    bots.team = [Entity("The Fedora Man",1300,0,100,40,0,40,50,100,115,6,0,0,0,"17","Male")]
    battle(you,bots,Cont=True)
    time.sleep(2)
    if Daniel.cHP <=0:
      text("\nDaniel, defeated: Please...stay away from her","???, smirking: The better man deserves the woman...she's mine now.","Daniel, desperate: No...no..NO! I can't let you do that!","*Daniel lunges at the man, knocking his fedora off*","*The man turns around and looks at Daniel*","*Daniel gasps in shock*","Daniel, astonished: No..it can't be! There's no way!","???, revengeful: I'll be taking her with me, and the end will approach all of you...you and everyone you know at this god forsaken school!","*Daniel watches as the man opens up a teleportation rift, and walks away with Kelly in hand, fainting as he watched them go*")
    else:
      text("\nDaniel, victoriously: ...The better man deserves the woman...you lost, she's rightfully mine.","???, smirking whilst on the ground: ..You think you've won..cute.","Daniel, dominatingly: Ha! Pathetic. Learn your place worm!","???, anime: You're already dead.","Daniel, confused: What?","*Daniel falls to the ground*","Daniel, holding his chest: What...did you do..?","???, cool-guy tone: Never underestimate the power of a complete chad.","Daniel, dramatically: No...it can't be!","???, revengeful: You lose. I'll be taking her with me, and the end will approach all of you...you and everyone you know at this god forsaken school!","*Daniel watches as the man opens up a teleportation rift, and walks away with Kelly in hand, fainting as he watched them go*")
    if Daniel in you.deadteam:
      you.deadteam.remove(Daniel)
      you.deadteamS.remove(Daniel.NAME)
    Daniel.HP = 45
    Daniel.cHP = 45
    Daniel.cMP = 100
    Daniel.AT = 8
    Daniel.DF = 15
    Daniel.MAT = 15
    Daniel.MDF = 5
    Daniel.CT = 6
    Daniel.MRG = 3
    print(style.BOLD + fore.RED_1 + style.BLINK + "\nPCTI Lockdown" + style.RESET)
    time.sleep(1)
    input(fore.GREY_100 + "\nSome general information you should know before you play, this game a turn-based strategy RPG game. Your decisions throughout the game will affect how your game pans out. Some decisions will even be timed. If you ever run into trouble, you will always be able to access the help section once you reach a certain early point in the game. That's all, have fun." + style.RESET)
    ro = rd(0)
    croom.remove(ro)
    world.append(ro)
    ro = rd(1)
    world.remove(ro)
    croom.append(ro)
    quests.append("All Hail..")
    eventcheck()
#--------------------------------------------------------------------------------------------------
  if "All Hail.." in quests and croom[0].RID == 1:
    if "Origins" in quests:
      quests.remove("Origins")
    you.team = [Ishraq]
    you.teamS = ["Ishraq"]
    print("\n???, suddenly: Wake up.")
    time.sleep(1)
    speak = input("???, in a concerned tone: Can you talk? ")
    if speak == "":
      print("Ishraq, drunk: ...*grunts*")
      time.sleep(0.5)
      input("*??? slaps Ishraq*")
      input("Ishraq, confused: ..What the..?")
    else:
      print("Ishraq:", speak)
    time.sleep(0.5)
    text("\n~Ishraq is a Bengali Peruvian 10th grade engineering student at the highschool of PCTI. He is a varsity track mid-distance sprinter, fencer, and VEX competitor. He is very adept at expressing his rage and care towards people, shouting loudly, procrastinating, and making new friends of all kinds. He believes everyone has the potential to do great things, looking beyond faults. His extroversion makes him a popular figure, but also puts off others.","\n???, content: Well, it seems you can.","???, seriously: Listen...we've been in this janitor's closet for an hour now. People all over the school seem to be mind controlled! I don't know if you're gonna believe this, but just listen.", "???, directly: Some guy tried kidnapping me, and he opened some portal doing so. I tried fighting him as he pulled me into it and I somehow managed to get separated from him. I landed here in the F-Wing and out of nowhere...this noise shrieked all over the school! It was so loud...it made me fall. It lasted for a bit, but once it was over, I looked around.", "???, frightened: No one got out of any classroom, except you. You were trying to eat your phone...I tapped your shoulder, and you just died. I looked into your classroom, and everyone was demonically standing straight." "???, expressively: It was so scary...I was gonna run but I heard footsteps coming from across the hall. I quickly dragged you into this closet so they didn't see you, and we've been here ever since.")
    talk = "2"
    while talk == "2":
      meet = input("\n(1) Who are you again?   (2) I'M THE CONDUCTOR OF THE POOP TRAIN!!\n(3) Oh word?\nType the corresponding number to enter a response: ")
      if meet == "1":
        text("\nIshraq, genuinely trying to clarify: Who are you again?","Kelly, a little surprised: Ummm...Ishraq, it's me, Kelly? The noise must've hit you hard.","\n~Kelly is a Korean 10th grade engineering student at the highschool of PCTI. She is 3rd in class ranking among 894 students in the 10th grade, a SkillsUSA officer, and placed 2nd in State for FBLA. She has obsessive oragnization tendencies that lead her to be good at managing things...and people. Under her hard outlook, she is quite the whimsical character who loves to experience new things.")
        talk = "1"
        while talk == "1":
          meet = input("\n(1) Word.   (2) Oh, HI KELLY!\nResponse: ")
          if meet =="1":
            text("\nIshraq, straight-up: Word. I don't even remember coming to school...I smell like laundry detergent now.","Kelly, panicking: You've been laying here for an hour! Do you know how heavy you are?! This is insane..how are we gonna get out!?")
            talk = "2"
            while talk == "2":
              meet = input("\n(1) I'm only 130 pounds.   (2) Relax. I've been lifting.\nResponse: ")
              if meet =="1":
                text("\nIshraq, blunt: I'm only 130 pounds.","Kelly, concerned at Ishraq's frivolous attitude: Ishraq, this really isn't the time.","???, loudly: *Step*,*Step*,*Step*","Ishraq, just noticing: Oh shit, this person's standing right in front of the door.","Kelly, quietly: Shh.","Ishraq, adrenaline rushing to him: ...!","*CRASH*","*Ishraq is ripped out of the closet*","Kelly, crying out loud : ISHRAQ!","Ishraq, a little unnerved: AAAGH SHIT!! YO! BOWERS GOT DUMB-STRENGTH RIGHT NOW!")
                fightmod = 1
                print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
                talk = "3"
                break
              elif meet =="2":
                text("\nIshraq, flippantly: Relax. I've been lifting. I'll square up with anyone.","Kelly, not laughing: You're gonna die. Don't do anything stupid.","Ishraq: It's a joke...!","*CRASH*","*Ishraq is ripped out of the closet*","Kelly, crying out loud: ISHRAQ!","Ishraq, a little unnerved: AAAGH SHIT!! YO! BOWERS GOT DUMB-STRENGTH RIGHT NOW!")
                print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
                fightmod = 1
                talk = "3"
                break
          elif meet == "2":
            data[0] = data[0] + 1
            text("\nIshraq, using his normal loud greetings: Oh, HI KELLY!","Kelly, shocked at Ishraq's stupidity: SHHHH!! They're still around I think!","Ishraq, adrenaline rushing to him: ...!","*CRASH*","*Ishraq is ripped out of the closet*","Kelly, crying out loud: ISHRAQ!","Ishraq, a little unnerved: AAAGH SHIT!! YO! BOWERS GOT DUMB-STRENGTH RIGHT NOW!",)
            fightmod = 1
            print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
            talk = "3"
            break
      elif meet == "2":
        text("\nIshraq, with a little brain damage: I'M THE CONDUCTOR OF THE POOP TRAIN!!","Kelly, creeped out: ...Umm, okay. Don't you recognize me? Kelly? No? There's something wrong with you, and it was probably best to leave you out in the hallway.","\n~Kelly is a Korean 10th grade engineering student at the highschool of PCTI. She is 3rd in class ranking among 894 students in the 10th grade, a SkillsUSA officer, and placed 2nd in State for FBLA. She has obsessive oragnization tendencies that lead her to be good at managing things...and people. Under her hard outlook, she is quite the whimsical character who loves to experience new things.")
        data[0] = data[0] - 3
        talk = "1"
        while talk =="1":
          meet = input("\n(1) Chill, I'm good.   (2) GREEEEEEEN!\nResponse: ")
          if meet == "1":
            input("\nIshraq, back to his senses: Chill, I'm good.")
            time.sleep(1)
            data[0] = data[0] + 2
            text("Kelly, concerned with Ishraq's frivolous attitude: Oh, wow, seriously though, this isn't the time to be stupid.","Ishraq, bluntly: Honestly, I dont't...!","*CRASH*","*Ishraq is ripped out of the closet*","Kelly, crying out loud: ISHRAQ!","Ishraq, a little unnerved: Ishraq: AAAGH SHIT!! YO! BOWERS GOT DUMB-STRENGTH RIGHT NOW!")
            fightmod = 1
            print("\nIshraq begins his duel with the mind controlled Richard!\n")
            talk = "3"
            break
          elif meet == "2":
            data[0] = data[0] - 2
            text("\nIshraq, extremely loud: GREEEEEEEN!","Kelly, ready to run:...I think I'll just slowly get up and...!","*CRASH*","*Ishraq is ripped out of the closet*","Kelly, a little thrown off: Ishraq?","Ishraq, spouting random words: ICICLES POOP MAYONNAISE AT TACOBELL!","???, confused: #What?#","Ishraq, making some type of connection: THE STAGES OF THE CELL CYCLE! WHAT DON'T YOU GET?!","Kelly, evaluating the situation: Oh my god, that's Richard. His eyes are pale!","Ishraq, confused: Richard? No no, Richard is more...uuuh..green?","Richard, annoyed: #Shut up, I'm bringing you in!#","Ishraq: REEEEEEEEEEEE!",)
            fightmod = 2
            print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
            talk = "3"
            break
      elif meet =="3":
        text("\nIshraq, casually: Oh word?","???, shocked and panicking: Word? WORD?! Word...that's it? This stuff doesn't happen everyday! Our phones aren't working. I tried emergency calling with your phone and mine, but nothing happened. What are we gonna do!?")
        talk = "1"
        while talk == "1":
          meet = input("\n(1) Let's wait.  (2) Who are you again?\nResponse: ")
          if meet == "1":
            text("\nIshraq, calmly: Let's wait.","???, still panicking: We can't wait! We're gonna eventually starve, or some creep is gonna find us!")
            talk = "2"
            while talk == "2":
              meet = input("\n(1) Relax.   (2) Can I have my phone back?\nResponse: ")
              if meet == "1":
                text("\nIshraq, still calm: Relax.","???, more panic: Are you delusional Ishraq? How are we supposed to relax...WHEN WE'RE GONNA DIE?!","Ishraq, subtly realizing: Oh, it's you Kelly. Sorry, I was a bit drunk. Thanks for waking me up with your yelling.","\n~Kelly is a Korean 10th grade engineering student at the highschool of PCTI. She is 3rd in class ranking among 894 students in the 10th grade, a SkillsUSA officer, and placed 2nd in State for FBLA. She has obsessive oragnization tendencies that lead her to be good at managing things...and people. Under her hard outlook, she is quite the whimsical character who loves to experience new things.\n","Kelly, calming down: ...No, you're right. Yelling won't do us good, I should really...!","*CRASH*","*Kelly is ripped out of the closet*","Ishraq, dumbfounded: HOLY SHIT! KELLY!","*Ishraq leaps into the hallway, finding Kelly laying on the ground*","Ishraq, nervous: Hey, are you good?","Kelly: ...","Ishraq, enraged: Someone's boutta get their ass merked.","*Ishraq turns around*""Ishraq, ready to swing: Richard Bowers, eh? I'll assume you didn't do that by choice. I'm still gonna merk your ass.")
                fightmod = 3
                print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
                talk = "3"
                break
              elif meet == "2":
                data[0] = data[0] + 2
                text("\nIshraq, breaking the ice: Can I have my phone back?","???, calming down a little: ...Here I guess. Your lock screen is funny.","Ishraq, subtly realizing: Hehe...didn't realize it was you Kelly. I was still recovering from that noise.","\n~Kelly is a Korean 10th grade engineering student at the highschool of PCTI. She is 3rd in class ranking among 894 students in the 10th grade, a SkillsUSA officer, and placed 2nd in State for FBLA. She has obsessive oragnization tendencies that lead her to be good at managing things...and people. Under her hard outlook, she is quite the whimsical character who loves to experience new things.\n","Kelly, easing up: Glad you're back...!","*CRASH*","*Kelly is ripped out of the closet*","Ishraq, dumbfounded: HOLY SHIT! KELLY!","*Ishraq leaps into the hallway, finding Kelly laying on the ground*","Ishraq, nervous: Hey, are you good?","Kelly: ...","Ishraq, enraged: Someone's boutta get their ass merked.","*Ishraq turns around*","Ishraq, ready to swing: Richard Bowers, eh? I'll assume you didn't do that by choice. I'm still gonna merk your ass.")
                print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
                fightmod = 3
                talk = "3"
                break
          elif meet == "2":
            text("\nIshraq, genuinely trying to clarify : Who are you again?","Kelly, a little surprised: Ummm...Ishraq, it's me, Kelly? The noise must've hit you hard.","\n~Kelly is a Korean 10th grade engineering student at the highschool of PCTI. She is 3rd in class ranking among 894 students in the 10th grade, a SkillsUSA officer, and placed 2nd in State for FBLA. She has obsessive oragnization tendencies that lead her to be good at managing things...and people. Under her hard outlook, she is quite the whimsical character who loves to experience new things.\n","Ishraq, agreeingly: Yeah, it did...its wearing off though.","Kelly, trying to make sense of Ishraq's attitude: Makes sense why you were so careless about what's happening right now.","Ishraq, correcting Kelly: Nah, it wore off by then.","Kelly, shocked: Wow...!","*CRASH*","*Kelly is ripped out of the closet*","Ishraq, dumbfounded: HOLY SHIT! KELLY!","*Ishraq leaps into the hallway, finding Kelly laying on the ground*","Ishraq, nervous: Hey, are you good?","Kelly: ...","Ishraq, enraged: Someone's boutta get their ass merked.","*Ishraq turns around*","Ishraq, ready to swing: Richard, eh? I'll assume you didn't do that by choice. I'm still gonna merk your ass.")
            fightmod = 3
            print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
            talk = "3"
            break
    fightid = 1
    if fightmod == 1 or fightmod == 3:
      bots.team = [Entity("Richard",100,0,7,50,0,0,45,85,100,0,0,0,0,"17","Male")]
      battle(you,bots,Cont=True)
    if fightmod == 2:
      bots.team = [Entity("Richard",75,0,7,50,0,0,40,60,100,0,0,0,0,"17","Male")]
      battle(you,bots,Cont=True)
    if victory == 0:
      time.sleep(2)
      text("\nRichard, in a distorted voice: #I'll be taking you back to The Fedora Man, Kelly.#","Ishraq, losing sense: ...Who...the heck is...The Fedora Man?","Richard: #None of your concern.#")
      time.sleep(1)
      text("\n*An electric bolt from a ceiling light smites Richard, releasing Kelly from his grasp*","\nIshraq: " + style.BOLD + "YES." + style.RESET)
      if fightmod == 1:
        input("*Kelly recovers from the ground*")
      victory = 1
      data[9] = 1
    if victory == 1:
      time.sleep(2)
      if fightmod == 2:
        text("\nIshraq, bloodthirsty: Sum light. Who's next?","Kelly, frightened: Umm...are you okay now? Is the weird stuff out of your system?")
        talk = "1"
        while talk == "1":
          boop = input("\n(1) Fuck you mean lil bruh?  (2) Yeah, I'm good.\nResponse: ")
          if boop == "1":
            data[0] = data[0] - 10
            text("\nIshraq: Fuck you mean lil bruh?","Kelly, disappointed: ...I'm gonna assume you got a bit more insensitive...","Ishraq, mockingly: Stay...sucking...me.","Kelly, putting her hand over her mouth: Ew, you're gross.","Ishraq: I already nutted...and you're still sucking.","Kelly, not taking it: I'm done with you. We can go our own ways.")
            talk = "2"
            while talk == "2":
              boop = input("\n(1) BEGONE THOT!  (2) Sorry, I wasn't thinking straight!\nResponse: ")
              if boop == "1":
                text("\nIshraq, with his extremely loud voice: BE-GONE THOT!","\n*Kelly ignores and leaves Ishraq, trailing off down into the FX hallway. It was the last time they met. Ishraq soon was brought under control by an unknown force. His eyes turned pale, and he became just like Richard. Whatever happened at PCTI was never found out, and The Fedora Man had gotten what he wanted. That ends the story of PCTI Lockdown...")
                sys.exit()
              if boop == "2":
                data[0] = data[0] + 3
                text("\nIshraq, realizing his rude behavior: Sorry, I wasn't thinking straight!","Kelly, petty: ...Still not forgiving you. I never thought you would ever say things like that.","Ishraq, confused: It wasn't me though.","Kelly, speaking her heart: But it was you. It's in you.","Ishraq, weirded out a little: Okay I guess...so what now?","Kelly: There's something wrong with Richard...I don't think this school is safe right now. Do you think everyone's being controlled like this?","Ishraq, thinking it over: Maybe, you said the noise shreaked all over school...maybe through the announcements.","Kelly, impressed: Yeah, that makes sense...wow! Wait! That must mean our shop-peoples are in danger! We have to go help them quick!","Ishraq, ready: Alright, let's go!")
                talk = "3"
          elif boop == "2":
            data[0] = data[0] + 1
            text("\nIshraq, calmly: Yeah, I'm good.","Kelly, glad: That's good. Now we can actually talk and figure things out.","Ishraq: So what now?","Kelly, thinking: Richard was able to rip you out of the closet...there's obviously something wrong with him.","Ishraq: Agreed.","Kelly, concluding: And there's probably more people just like Richard around, so we need to get out of here fast.","Ishraq, disagreeing: Nah, not yet. We need to help people.","Kelly, in a reluctant tone: I guess...do you think everyone's being controlled like this?","Ishraq, thinking it over: Maybe, you said the noise shreaked all over school...maybe through the announcements.","Kelly, impressed: Yeah, that makes sense...wow! Wait! That must mean our shop-peoples are in danger! We have to go help them quick!","Ishraq, ready: Alright, let's go!")
            time.sleep(1)
            talk = "3"
      else:
        if fightmod == 1:
          text("\nKelly, observing Richard's unconscious body: Oh my god, what's wrong with him?","Ishraq, shrugging: I don't know...seems like somethings controlling him, at the same time, making him way stronger.","Kelly, looking at Ishraq: This is getting too dangerous...we need to get out of here before we die!","Ishraq, with a questioning tone: What about Richard? Didn't you say you came through a portal?","Kelly, with self-interest: We can't be sure if Richard is still being controlled, and yeah, I did.")
        if fightmod == 3:
          text("\nIshraq, a little worried: Yo, Kelly. Kelly. Kelly. Come on, I know you're not dead...","Kelly, regaining consciousness: ...Ishraq? What happened?","Ishraq, trying to make sense: What seems to be a mind controlled Richard ripped you out of our hiding spot, and I just beat his ass.","Kelly, recovering: Damn...I feel bruised. How'd he rip me out through a door..? Ugh, we need to get out of here quick. This is dangeorus!","Ishraq, determined: Hold on...Richard stuck his hand through it, something's making everyone abnormal. We gotta get to the center of this...didn't you say you came through a portal?","Kelly: Yeah.")
        text("Ishraq, acting as if familiar with the impossible: I think we just found ourselves caught in a sci-fi, or an anime.","Kelly, thinking she figured it out: ...or this could be a really weird dream of mine. Goodbye Ishraq from dream world...I'll make sure to jot this down in my journal. *Closes her eyes, trying to wake up*","Ishraq, after a few seconds: Still here.","Kelly, taking charge: This doesn't make sense. It's 6th period right now. We should go to our shop class and see if everyone is fine.")
        talk = "1"
        while talk == "1":
          boop = input("\n(1) Sure, it's a start.  (2) You mentioned a guy trying to kidnap you.\nResponse: ")
          if boop == "1":
            text("\nIshraq: Sure, it's a start. We need to find out what's going on.")
            talk = "3"
            time.sleep(1)
          elif boop == "2":
            text("\nIshraq, curious: You mentioned a guy trying to kidnap you. What was the deal with that?","Kelly, a little annoyed: I told you already, some guy tried kidnapping me into some portal and I managed to get separated from him. Then I suddenly woke up in the F-Wing, even though I was in the intersection to the FX-Wing...right? Can we go to shop already?","Ishraq, feeling Kelly was hiding something: Where were you going before you got kidnappped?","Kelly, annoyed: I was going to SHOP.")
            start = time.time()        
            elapsed = 0               
            while elapsed < 10:
              print("\nYou have",round(10-elapsed),"seconds to make a decision")
              boop = input("(1) *Go to Kelly's shop class*  (2) *Probe further*\nResponse: ")
              elapsed = time.time() - start
              if boop == "1" or boop == "2":
                break
            if boop == "2" and elapsed < 10:
              text("\nIshraq, to himself in his head: Why is she so pissed?","Ishraq, inquiring further: Okay, but how did this guy who tried kidnapping you even look?","Kelly, explaining carefully: He had this...fedora on his head. He was wearing a long black trenchcoat. He didn't attack me immediately...umm..he actually....")
              if data[9] == 1:
                input("Ishraq, happy to make a connection: Hey, Richard mentioned a guy called The Fedora Man.")
              else:
                input("Ishraq: He what?")
              text("Kelly, stopping herself: You know, the whole situation was very strange, and I don't feel comfortable talking about it.","Ishraq, not dealing with it: Don't give me that bullshit. I don't care if you're comfortable or not, you're in danger. Hell, we're all in danger. We're dealing with freaking a guy who makes portals, mind controlled Richard and probably the entire school, and tried kidnapping you. Just tell me.","Kelly, giving up: Fine. I was walking with Daniel. Daniel saw the guy in the trench coat, and started acting all weird. I couldn't tell if Daniel was acting or not. At first, I thought they were friends acting a skit out together for me or something. But this Fedora guy just charged at me, and Daniel got a little serious for a second. Next thing you know, they were fighting!","Ishraq, amused at the weird situation: HaHAHA! What the hell?","Kelly, slightly flustered: I don't know why I didn't want to tell you...I was embarrassed to be honest.","Ishraq, bluntly: So, Daniel white-knighted you.","Kelly, awkwardly: Well, he did protect me...","Ishraq, grinning: Yo, I can't wait to bully this kid.")
              if fightmod == 3:
                text("Kelly, angry: What do you mean? You did the same thing. The right thing. Any decent person would try to help their friend.","Ishraq, cynically: Weren't you the one trying to get outta here before helping your friends?","Kelly, aggressively: First off, I don't care about Richard, Second, you showed me that I should help my friends right now, so why aren't we at shop already?!","Ishraq, trying to ease the tension: Alright, alright, let's go.")
                data[0] = data[0] - 3
              if fightmod == 1:
                text("Kelly, with a defending tone: Why though? Sure, he was acting weird, but it was pretty brave.","Ishraq, slightly jealous: I guess.","Kelly: ...Let's just go to shop already")
              data[15] = 1
            else:
              text("\nIshraq, to himself in his head: She's pissed for no reason.","Ishraq, trying to ease the awkward tension: Okay, then we'll go to SHOP.","Kelly, content: Yes, we will.")
            talk = "3"
            time.sleep(1)
    Ishraq.Q1B = 0
    quests.remove("All Hail..")
    quests.append("All Hail...")
    revival(Ishraq,o=True)
    revival(Kelly,o=True)
    input("\n*Noises are heard from the D-Wing*")
    time.sleep(0.5)
#-------------------------------------------------------------------------------------------------------
  if "All Hail..." in quests:
    if nextr == "D-Wing Hallway 1st Floor" and croom[0].RID == 1:
      text("\n*Ishraq and Kelly cross the F-Wing Bridge, reaching the D-Wing. Upon reaching the three way intersection between the C-Wing, D-Wing, and the bridge, the lights in the school shut out.","\nKelly, scared: WHAT THE HELL??! Oh my god, I'm done.","Ishraq, laughing: Yeeaah~, we should've went to shop, heheh.","*The lights flash back on*","Kelly: Uuuh, we're surrounded on all sides Ishraq.","Ishraq: Saykali, Sese, and Satya...these med students yo.","Kelly: Get ready!! They're closing in!")
      print("\nThe three medical students begin to attack Kelly and Ishraq!\n")
      bots.team = [Entity("Alex",60,0,5,20,0,0,35,120,100,1,0,0,0,"17","Male"),Entity("Satya",45,0,8,10,0,0,40,100,120,2,0,0,0,"18","Male"),Entity("Ryca",40,10,4,20,15,0,30,100,100,50,0,0,0,"19","Female Heal")]
      battle(you,bots,Cont=True)
      if victory == 1:
        time.sleep(1.5)
        text("\nIshraq, picking up Alex: You three alright?","Alex, recovering: ...Woah..what happened?","Ishraq, tired: Long story short, eveyone's being mind controlled right now, and it seems knocking people out cures them. You guys attacked us.","Satya, trying to make sense: You mean the entire school is under some trance? Isn't it dangerous to stick around?","Kelly, talking fast: Definitely, but some other weird stuff happened and we need to figure out what's going on.","Ryca, scared: Well, where should we go?","Kelly, suggesting: We planned on going to our shop room,","Ryca, figuring it out: Alright...as you and Ishraq go there, me and these dudes will stay at our shop..we'll try to save some people if we can.","Ishraq, signaling them off: Good luck. We're off.","\n*Ishraq and Kelly travel back to the F-Wing*")
        data[10] = 2
      else:
        time.sleep(1)
        text("\nIshraq, tired: Damn...they're tough! Come on Kelly, let's dip!","Kelly, running already: Way ahead of you!","*\nIshraq and Kelly retreat back to the F-Wing*")
        data[10] = 1
      sad = 1
      revival(Ishraq,o=True)
      revival(Kelly,o=True)
    if nextr == "F-Wing Engineering Shop Room":
      text("\nIshraq, trying to open the unlocked door: The door is locked, but the light is green, so it should be able to open","Kelly, noticing the light as well: Strange...should we try breaking in or..?!","*The door opens*","Ishraq, dying on the inside: Uuuuhh, hello?","Kelly, also dying: They're sooo welcoming us.","Ishraq: Should we enter?")
      talk = "1"
      while talk == "1":
        bruh = input("\n(1) YER!  (2) No way!\nResponse: ")
        if bruh == "1":
          data[0] = data[0] + 5
          text("\nKelly: YER!","Ishraq: YEERR!","???: YEEERRR!","Kelly, eyes widening: ...that sounded like Julius!","Ishraq, excited: Julius is fine then, let's meet him inside!","Kelly, grabbing Ishraq: Wait!..Fine.","*Ishraq and Kelly enter their shop room*","Ishraq, scanning the student tables: There's no one here.","Kelly, pointing: Ishraq! Your left! Their eyes are pale!","Ishraq, accepting death: Aaaand we're fucked.","*Someone shuts the door*","Kelly: Ishraq, Julius just came in! HE JUST LOCKED US IN!","Ishraq, shouting: Kelly! Distract him as much as you can!","Kelly, panicking: Distract?! What do you mean distract?!")
          talk = "2"
        elif bruh == "2":
          data[0] = data[0] - 1
          text("\nKelly, scared: No way!","Ishraq, acting like the door opening wasn't creepy: Why not?","Kelly, giving Ishraq a You-Serious? face: You're joking, right? This is like those traps in those horror movies.","Ishraq, trying to use common-sense: Well, this isn't a horror movie.","Kelly, using more common-sense: Yeah, it's worse...this is real life.","Ishraq, yolo: Who cares, let's just go.","*Ishraq and Kelly enter their shop room*","Ishraq, scanning the student tables: There's no one here.","Kelly, pointing: Ishraq! Your left! Their eyes are pale!","Ishraq, accepting death: Aaaand we're fucked.","*Someone shuts the door*","Kelly: Ishraq, Julius just came in! HE JUST LOCKED US IN!","Ishraq, shouting: Kelly! Distract him as much as you can!","Kelly, panicking: Distract?! What do you mean distract?!")
          talk = "2"
        while talk =="2":
          bruh = input("\n(1) Just do something!  (2) You know...girl things!\nResponse: ")
          if bruh == "1":
            text("\nIshraq, tensing up: Just do something!","Kelly, letting her body talk: Uuuh, Julius...*punches Julius as hard as she can*","Julius: ...","Kelly, surprised at herself: Haha..HA! I punched him! ...!","*Julius gets up from the ground, sweeping Kelly and smoothly grabbing her before she falls*","Julius, singing: Isometric...Isometric...ISOMETRIC DRAAAAWWWIIINGS!","*Julius starts to dance with her*","Ishraq, laughing a bit: That's good enough? Well, no going back now, save my friends or die trying.","David, flapping his arm against his chest like a sword as if he was playing Minecraft: TEAM! TEAM! TEAM!","Edmond, screaming at David: TEEAAAAM!","Brandon, announcing to the world: I...AM...GROOOOOOT!\n")
            talk == "3"
            break
          elif bruh == "2":
            text("\nIshraq, talking as if Kelly knew what he meant: You know...girl things!","Kelly, not knowing whether to be disgusted or not: Girl things? What does that even mean?","Ishraq, recalling: Remember when Daniel leaned over the table and moved his boobs up and down to get gummy bears from Julius? Try that!","Kelly, trying to stay serious: I can't do that!","Ishraq, being serious: Just do it!","Kelly, looking down: No, I literally can't do that!","Ishraq: Why?!","Kelly, raging: You're an asshole!","Ishraq, confused: What do you mean?!","*Julius sweeps Kelly and smoothly grabs her before she falls to the ground*","Julius, singing: Isometric...Isometric...ISOMETRIC DRAAAAWWWIIINGS!","*Julius starts to dance with her*","Ishraq, laughing a bit: That's good enough? Well, no going back now, save my friends or die trying.","David, flapping his arm against his chest like a sword as if he was playing Minecraft: TEAM! TEAM! TEAM!","Edmond, screaming at David: TEEAAAAM!","Brandon, announcing to the world: I...AM...GROOOOOOT!\n")
            data[0] = data[0] - 5
            data[1] = data[1] + 2
            talk == "3"
            break
      you.team = [Ishraq]
      you.teamS = ["Ishraq"]
      bots.team = [Entity("Brandon",120,0,20,40,0,0,50,100,100,0,0,0,0,"17","Male"),Entity("David",100,0,24,30,0,0,50,100,50,0,0,0,0,"18","Male"),Entity("Edmond",110,0,22,36,0,0,50,100,100,0,0,0,0,"19","Male")]
      battle(you,bots,Cont=True)
      time.sleep(1)
      if Ishraq.cHP > 0:
        text("\nDavid: Yo, this dude hacking!","Edmond: Word.","Brandon: Turn them shits off!","Ishraq: I'm sorry, the dude playing right now learned how to read this code!","David: Well...act like your getting your ass beat right now.","Ishraq: I'll try I guess.","*Ishraq falls...*")
      text("\nIshraq, losing consciousness: Kelly...fight..","Kelly, terrified: ISHRAQ!","*Something on Mr. Pudup's desk begins to glow red, Mr.Pudup being Ishraq's and Kelly's 9th grade engineering teacher, but only Ishraq's 10th grade teacher*","Kelly, puzzled: It's projecting an isometric drawing..?","*Julius tries grabbing Kelly to resume dancing, but she bolts for the drawing*","*The piece of metal began to vibrate intensely in her hands, hurting her*","Kelly, thinking to herself: Whooah, ow! What even is this? It's projecting a red holographic isometric drawing...","*Julius jerks Kelly back to him, and she drops the device*","Kelly, desperate: No no no!","*In a last attempt, Kelly kicks the device, and it lands near Ishraq*","\n*The object begins wrapping itself upon Ishraq, completely covering his body in an unknown metal! The metal compresses his body, briefly turning him into a small shining red light! His body reconstructs from red outlined geometric planes! After the reconstruction, the object sends out a final pulse of energy, weakening everyone else in the room!*\n",)
      input(style.BOLD + fore.RED_1 +"~Ishraq has gained a new ability, Wild Instinct! He triggers his amplified human instincts to increase his attack, speed, evasion, and critical strike chance! However, it reduces his accuracy, magic attack, magic defense, and damages his body!\n" + style.RESET)
      input(fore.RED_1 + style.BOLD + "Ishraq, looking at his hands: What is this feeling? This feels like pre-track season! OH YEAH, LET'S FIGHT!!" + style.RESET)
      revival(Ishraq)
      bots.team = [Entity("Brandon",60,0,10,20,0,0,25,100,50,0,0,0,0,"17","Male"),Entity("David",50,0,12,15,0,0,25,100,50,0,0,0,0,"18","Male"),Entity("Edmond",55,0,11,18,0,0,25,100,50,0,0,0,0,"19","Male")]
      fightid = 2
      battle(you,bots,Cont=False)
      if victory == 1:
        time.sleep(1)
        text("\n*Julius lets go of Kelly*","Kelly: Ishraq! Let's finish him!")
        revival(Kelly)
        bots.team = [Entity("Julius",70,10,10,20,0,0,50,100,50,0,0,0,0,"17","Male Boss")]
        fightid = 3
        battle(you,bots,Cont=False,Mid=True)
        if victory == 1:
          time.sleep(1)
          text("\nIshraq, cramping: *Huff*...Shit!","*Julius lunges at Ishraq*","*Ishraq dodges instinctively, causing Julius to plant into the ground*","*Kelly jumps onto Ishraq, attempting to take him down*","*Ishraq throws her off of him into the computers in the back*","Ishraq, realizing what he did: FUCK! I need to relax...relax.","*Ishraq cools down*","*Brandon, David, and Edmond slowly regain consciousness*","Ishraq, happy to see his friends: You guys good?","David, raising his arm: Uugh...te..teaam?","Ishraq, flapping his arm across his chest: Team. Team. Team.","Edmond, dizzy: What the hell... even happen Ishraq?","Brandon, joyfully laughing yet worried: Word, who broke those 2 computers? Ms. Miller gonna sue us.","Edmond: Facts.","David: Why is Kelly just laying near those computers though. Did someone throw her? Is she dead?","Edmond: She dead.")
          talk = "1"
          while talk == "1":
            butt = input("\n(1) *Explain what happened*  (2) Ms. Miller attacked me.\n(3) I threw her.  (4) Kelly's dead.\nResponse: ")
            if butt == "1":
              if data [15] == 1:
                text("\nIshraq, taking a long breath: Alright, where do I begin...Kelly was walking with Daniel not long ago. Some guy walks up to them, and starts fighting Daniel..","David, interrupting: He had his wood sword though, right?","Ishraq, grinning: I don't know, hopefully. Then, the guy showed Daniel up, and kidnapped Kelly. Here's where it gets funny. The guy opens up a portal, and takes her to some other dimension..","Brandon, not smiling: Ishraq, you're playin' too much. We're actually in serious trouble right now if someone sees this.","Ishraq, understanding why Brandon didn't believe anything he just said: I'll show you something that'll make you believe me..*Ishraq taps into his wild instincts, begining to emanate a red aura*, does this explain anything?","Edmond, in disbelief: WOAH?! What kinda roids is...?","Ishraq, explaining: Something I found in this dimension, cuz we're actually all in the portal with Kelly. I think everyone at tech is. Kelly fought the guy and got separated from him, but she ended up in the F-Wing after entering the portal. She saw everyone standing straight as hell, except me. She found me drunk, and we ended up coming here to see if anyone was alright. We found ya'll then, and you people attacked us.","David, goofing around: Damn, you beat us though...right?","Ishraq, excited to talk about it: You guys legit jumped my ass, but then I got that weird red aura somehow. It was weird. I felt like I disappeared for a moment. I was in some red space just floating. Then I came back and went ape shit.","Brandon, happy: Good thing you survived man. What should we do now though?","Ishraq, looking at Julius on the floor: We should really check on Kelly and Julius.","Edmond, running: I'll check on Kelly.","Brandon, walking: I will too.","Ishraq, nudging David: Let's go help Julius, David.","David, following: With you.","\n*Ishraq and David walk to Julius*\n","David, being serious: Yo, Julius. Wake up. Ms. Miller's not in the room, you can help me with my birthday circuit.","Ishraq, stating: Word, it's your chance David.","David, looks back at the table he sits at: Wait, where's my circuit, it's not on my table anym...NOO! *David runs off*")
              else:
                text("\nIshraq, taking a long breath: Alright, where do I begin...Kelly said she was kidnapped by some guy who can make portals...","David, interrupting: Nether Portals?","Ishraq, grinning: Yes, like Minecraft...here's where it gets funny. The guy opens up a portal, and takes her to some other dimension..","Brandon, not smiling: Ishraq, you're playin' too much. We're actually in serious trouble right now if someone sees this.","Ishraq, understanding why Brandon didn't believe anything he just said: I'll show you something that'll make you believe me..*Ishraq taps into his wild instincts, begining to emanate a red aura*, does this explain anything?","Edmond, in disbelief: WOAH?! What kinda roids is...?","Ishraq, explaining: Something I found in this dimension, cuz we're actually all in the portal with Kelly. I think everyone at tech is. Kelly fought the guy and got separated from him, but she ended up in the F-Wing after entering the portal. She saw everyone standing straight as hell, except me. She found me drunk, and we ended up coming here to see if anyone was alright. We found ya'll then, and you people attacked us.","David, goofing around: Damn, you beat us though...right?","Ishraq, excited to talk about it: You guys legit jumped my ass, but then I got that weird red aura somehow. It was weird. I felt like I disappeared for a moment. I was in some red space just floating. Then I came back and went ape shit.","Brandon, happy: Good thing you survived man. What should we do now though?","Ishraq, looking at Julius on the floor: We should really check on Kelly and Julius.","Edmond, running: I'll check on Kelly.","Brandon, walking: I will too.","Ishraq, nudging David: Let's go help Julius, David.","David, following: With you.","*Ishraq and David walk to Julius*","David, being serious: Yo, Julius. Wake up. Ms. Miller's not in the room, you can help me with my birthday circuit.","Ishraq, stating: Word, it's your chance David.","David, looks back at the table he sits at: Wait, where's my circuit, it's not on my table anym...NOO!","*David runs off*")
              text("Ishraq, nudging Julius: Julius, come on. You're strong.","Julius, fidgeting: ...!","Ishraq: Hm..?","Julius, quietly whispering: Tupac is alive.","Ishraq, smiling: I know he is.","\n~Julius is a Uruguayan 10th grade engineering student at the highschool of PCTI. He is a varsity track distance runner prodigy. He is undeniably strong and has limitless stamina, boasting a vulgar and humorous attitude. He is quite popular around the school, and is not known to be truly hated by anyone.","\n*Ishraq helps Julius up*","Julius, looking around the room: My head is spinning...where is everyone?","Ishraq: No idea, but I'll fill you in.","*Ishraq fills Julius in on all the events up to now*","Julius, stroking his chin: I wanna know where to find some isometric drawings, cuz it sounds like we're gonna need them if we're up against an entire school.","Ishraq: Agreed.","Julius, looking at Ishraq in the eye: We could try drawing them, and see if they start glowing.","Ishraq, scanning the room again: You know where Miller put the straight edges?","Julius: No.","Ishraq, trying to grasp his ID lanyard: I got my 8th ID yesterday, I should have it with me...where's my ID..?","Julius, laughing: HaHAA! I got my ID, we chillin...wait, where's my ID?","Ishraq, shouting: YO DOES ANYONE HAVE THEIR ID?","Brandon, confused: I just had mine..","Edmond, creeped out: Same, but it's gone.","Ishraq, throwing his arms to the side with his hands open: What the hell? Where's the metersticks?")
              text("Edmond, checking where the metersticks are usually: They're not here.","Ishraq, in disbelief: There's legit no straight edges in the room.","Julius, suggesting: We'll just find one in another room.","Ishraq, sitting down on a chair: Aight, let's just chill for now though.")
              ro = rd(6)
              ro.people.append("Julius")
              ro.people.append("Edmond")
              ro.people.append("Brandon")
              ro.people.append("David")
              ro.people.append("Kelly")
              if "Wild Instinct" not in Ishraq.skills:
                Ishraq.skills.insert(0,"Wild Instinct")
              Ishraq.wild = 0
              time.sleep(1.5)
              talk = "2"
              break
            elif butt == "2":
              text("\nIshraq, swiping his shoulders: Ms. Miller attacked me.","Brandon, not believing Ishraq: Where is she right now then?","Ishraq, smirking: I'm jus' playin'.")
            elif butt == "3":
              text("\nIshraq, blank face: I threw her.","David, mouth gaping in shock: You threw Kelly?","Ishraq, trying to keep a straight face conflicted between laughing and being serious: Yup. I threw her.")
            elif butt == "4":
              text("\nIshraq, concerned: Kelly's dead","Edmond, scared: No way, stop playin'.","Ishraq, very concerned: I'm actually not sure if she's fine or not.")
#-------------------------------------------------------------------------------------------------------
  if "The FX-Wing Nurse" in quests and data[18] == 0:
    ro = rd(25)
    if nextr == "FX-Wing Nurse's Office":
      text("\nJulius, walking into the office slowly: The lights are off...power went out here.","*Lights flickering*","Ishraq, not moving: This ain't even a joke anymore. Why everything gotta be like a horror movie?","Julius, putting his arm across Ishraq's chest: Shhh...you hear that? I think some bitch is crying.","*Julius and Ishraq trying to listen more*","Ishraq, wide-eyed: Oh damn, someone is. Or something...","Julius, reminiscing: Aahh, this feels like finding the Witch in Left 4 Dead.","Ishraq, laughing in despair: Haha...we're dead.","Julius, serious: So, rock papers for whoever checks the cubicle?","Ishraq, picking his nose: Sure...ready?")
      talk = "1"
      jc = ["Rock","Paper","Scissors"]
      jm = random.choice(jc)
      while talk == "1":
        boop = input("\n(1) Rock  (2) Paper\n(3) Scissors\nResponse: ")
        if boop == "1":
          if jm == "Scissors":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, smirking: I'm IshROCK!","Julius, facepalming: Yeah, I have no idea why I chose scissors. You always fucking pick rock.")
          if jm == "Paper":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, sad: Bruh, everyone knows my strategy already.","Julius, laughing: HaHAA~! You always be picking rock, Ishraq.")
          if jm == "Rock":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, proud: A fellow rock user I see...","Julius, waiting: Again?")
          talk = "2"
        if boop == "2":
          if jm == "Scissors":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, sad: I barely even use paper...","Julius, laughing: HaHAA~! I had a feeling you were gonna switch it up. You always doing rock, and you thought I was gonna do paper, so you did scissors, but I actually did scissors. 1000 IQ.")
          if jm == "Paper":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, confused: What kinda people both use paper first? Everyone uses rock or scissors, hehe.","Julius, laughing: HaHAA~! Word!")
          if jm == "Rock":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, smirking: Lady luck is smiling.","Julius, facepalming: Yeah, on you! I was gonna do paper as well!")
          talk = "2"
        if boop == "3":
          if jm == "Scissors":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, indifferent: Scissors tie.","Julius, waiting: Again?")
          if jm == "Paper":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, smirking: You thought I was gonna do rock, but the switch up~!","Julius, grinning: Thas' smart. I like that.")
          if jm == "Rock":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, facepalming: Why'd I not choose rock? You even chose rock...","Julius, laughing: HaHAA~! I don't know, you tell me.")
          talk = "2"
      text("\n*Something shrieks from the cubicle*","Ishraq, crying on this inside: Yeah...screw the game, let's just leave.","Julius, ready to dip: Yeah, screw Kelly.","*The cubicle is knocked down, revealing a bloody nurse. The nurse charges at the students*","Ishraq, thoughts running through his mind: Fight...fight...if you can't run, fight...","Julius, already outside the office: What are ya doin'? MOVE!","Ishraq, adrenaline rushing through his veins: NO, WE HAVE TO FIGHT!","Julius, rushing back to help: Fucking hell!")
      bots.team = [Entity("The Nurse",250,10,10,0,20,0,70,80,130,20,0,0,0,"17","Female Boss")]
      battle(you,bots,Cont=False)
      if victory == 1:
        text("\n*The nurse grabs a scissor from a desk, charging Julius*","Julius, running: OOOOHHH SHIT!!","*Ishraq lunges at the nurse, slamming her away from Julius, dropping the scissors on the floor*","*The nurse picks up a syringe, and relentlessly charges at Ishraq*")
        start = time.time()        
        elapsed = 0               
        while elapsed < 6:
          print("\nYou have",round(6-elapsed),"seconds to make a decision")
          boop = input("(1) *Pick up the scissors*  (2) *Kick the scissors away*\nResponse: ")
          elapsed = time.time() - start
          if boop == "1" or boop == "2":
            break
        if boop != "1" and boop != "2":
          boop = str(random.randint(1,2))
        if boop == "1":
          text("\n*Ishraq picks up the scissors*","Ishraq, wildly charging at the Nurse: mpGH...aRUAAAAH!","*Ishraq stabs the nurse through the neck...The nurse falls to the ground, spewing blood*","Ishraq, vibrating: FUCK!","Julius, at a loss of words: Man...I don't know...","Ishraq, hands trembling: There's blood all over my hands. I just killed someone.","Julius, trying to keep himself and Ishraq calm: Don't worry, don't worry, bro, like...we were in danger. You had to.","Ishraq, enraged at himself: NO! I DIDN'T! I could've knocked her out! Easy!","Julius, making excuses for Ishraq: Bro, you saw that needle. Who knows what's in that injection.","Ishraq, praying: ...I'm not afraid of anything. But killing someone? It doesn't feel right, and I've always had this feeling that I would be afraid to do it.","Julius, poking the Nurse's butt: Stop thinking about it...let's just hide the body. Remove that freaking scissor too.","Ishraq, scared: Hell no.","Julius, dying on the inside: Aight, I'll take care of the body, you go look for stuff for Kelly.")
          data[13] = 0
          ro = rd(25)
          ro.people = ["Julius"]
          ro.objects = ["File Cabinet","Storage Closet","Nurse's Desk","Medical Cabinets"]
        if boop == "2":
          text("\n*Ishraq kicks the scissors away*","*The nurse injects the syringe into Ishraq*","Ishraq, vibrating as his left arm feels numb: FUCK!","*Julius tackles the nurse...Ishraq takes the syringe out of his arm*","Ishraq, heavily breathing: Juliuuus! Chokehold her!","*Julius pins the nurse into a chokehold...The nurse passes out*","*Ishraq sits on the ground and leans against a wall near the exit of the room.*","Julius, quickly coming to Ishraq's side: You okayy~?! That was fuckin' wild.","Ishraq, shaking everywhere: Is this what a seizure feels like?","Julius, concerned: God damn...who knows what was in that needle.","Ishraq, voice giving out: Maybe...the nurse can..help.","Julius, worried: Yo Ishraq...you're spazzing out like crazy. Like you need some medical attention right now more than Kelly does.","Ishraq, eyes going up: Yeah...my body...can't move!","Julius, ready to run to shop: I'ma go get everyone! We need to figure something out!","Ishraq, with all his power: WAIT! It's...too dangerous! Just find something...in the room! Wake the...nurse up...","*Ishraq's body flails and suddenly fails. It's motionless now*")
          forceswitch(Ishraq)
          data[13] = 1
          ro = rd(25)
          ro.people = ["Ishraq","Nurse"]
          ro.objects = ["File Cabinet"]
    elif ro.TYPE == "Nurse":
      if data[13] == 0:
        text("\n*Ishraq looks down the hallway, seeing Julius running*","Ishraq, shouting: YO! WHAT'S HAPPENIN'?","Julius, approaching: GO! THESE PEOPLE HAVE BEEN CHASING ME ALL OVER THE SCHOOL!!","Ishraq, getting ready to run: HOW MANY?","Julius, reaching Ishraq: A LOT!","*Ishraq starts running alongside Julius*","Ishraq, casually: You know I can't run for long. Distance is terrible.","*A horde of students halt Julius and Ishraq's run*","Ishraq, already panting: Damn it...we're surrounded.","Julius, not backing down: If it's a fight, it's a fight.","Ishraq, back to back with Julius: Let's do this.")
      elif data[13] == 1:
        text("\n*Julius kicks the door open*","Julius, whippin' it: Oooh~! Ya'll not ready for my mixtape.","*Julius looks up, seeing 10 wired students surrounding him*","Julius, shocked: OH SHIT!...Well...peace!","*Julius dips, running through the crowd...the crowd chases him*","Julius, running smoothly: They can't run forever. I'll lap them through this entire school if I have to.","\n~Julius makes a full 2 miles around the entire school, out-manuevering hundreds of wired students","\nJulius, starting to break a sweat: Phew...that was a good run. I'm back at the nurse's office...","*Students start to surround Julius from all sides, some coming out of the ceiling*","Julius, desperately laughing: Damn...guess they can run forever...I have to fight...","*The students charge Julius*")
      revival(Julius,o=True)
      print("")
      input(style.BOLD + fore.GREEN_1 +"~Julius has gained a new ability, Runner's High! It increases his attack and defense, and makes him immune to slows for a period of time!" + style.RESET)
      bots.team = [Entity("Miguel",65,0,10,50,0,0,20,80,80,0,10,0,0,"17","Male"),Entity("Yairre",55,0,8,30,0,0,25,100,100,0,0,0,0,"18","Female"),Entity("Marlin",40,0,7,30,0,0,25,100,110,0,0,0,0,"19","Male"),Entity("Emily",35,0,7,35,0,0,20,110,100,0,0,0,0,"20","Female"),Entity("Ihsas",55,0,9,45,0,0,20,100,100,0,0,0,0,"21","Male")]
      fightid = 4
      battle(you,bots,Cont=False)
      if victory == 1:
        time.sleep(0.5)
        print("\nThe next 5 students attack!")
        time.sleep(0.5)
        bots.team = [Entity("Isabella",30,0,8,0,0,0,35,120,160,30,0,0,0,"17","Female"),Entity("Micheal",25,0,6,30,0,0,25,100,90,0,0,0,0,"18","Male"),Entity("Melanie",40,0,6,40,0,0,20,100,80,0,0,0,0,"19","Female"),Entity("Josh",35,0,7,35,0,0,25,100,100,0,0,0,0,"20","Male"),Entity("Rachelle",45,0,6,45,0,0,20,100,80,0,0,0,0,"21","Female")]
        battle(you,bots,Cont=False,Mid=True)
        if victory == 1:
          text("\nIshraq, exhausted: God damn...too much people.","*The students regain consciousness and the situation is explained to them*","Ishraq, delegating: Alright, so band into groups, take over classrooms, save more students. This is how we're gonna fight.","*The students move out*","Ishraq, looking back at an exhausted Julius: So you're finally down, eh?","Julius, getting back up: You thought!","Ishraq, smirking: We're playing like one of those conquest games now, but we're gonna take this school over.","Julius, hopping back up: Sure, let's get moving.")
          for x in world:
            if x.RID == 1:
              x.ENC = 80
            elif x.RID == 2:
              x.ENC = 65
            elif x.RID == 3:
              x.ENC = 55
            elif x.RID == 5:
              x.ENC = 60
            elif x.RID == 8:
              x.ENC = 65
          data[18] = 1
          if "Runner's High" not in Julius.skills:
            Julius.skills.insert(0,"Runner's High")
          Julius.run = 0
          if "Ishraq" in ro.people:
            ro.people.remove("Ishraq")
#-------------------------------------------------------------------------------------------------------
  if "The Straight Edge" in quests:
    if nextr == "Mrs. Wells's Classroom" and data[19] == 0:
      text("\nIshraq, kicking the door open: MRS. WELLS?","\n*Three students are fighting in the classroom*\n","Ishraq, alert: HEY, Julius! That's Metin, Hassan, and Noah! ","Julius, indifferent: Who?","Ishraq, getting ready to fight: They're in our shop, we gotta stop them!","Julius, a little hesitant: We could just let them fight too...they're clearly wired.","Ishraq, taking interest: Wired?","Julius, looking for convenience: Mind-controlled. Just call em' wired.","Ishraq, agreeing: Sounds good.","Julius, ready to work with Ishraq: So what do you wanna do? Fight or let them fight?")
      start = time.time()        
      elapsed = 0               
      while elapsed < 10:
        print("\nYou have",round(10-elapsed),"seconds to make a decision")
        boop = input("(1) Fight  (2) Watch\nResponse: ")
        elapsed = time.time() - start
        if boop == "1" or boop == "2":
            break
      if boop != "1" and boop != "2":
        boop = str(random.randint(1,2))
      if boop == "1":
        bots.team = [Entity("Metin",160,0,15,60,0,0,30,100,80,0,10,0,0,"17","Male"),Entity("Hassan",130,0,12,35,0,0,45,100,100,0,0,0,0,"18","Male"),Entity("Noah",120,0,13,30,0,0,40,100,110,0,0,0,0,"19","Male")]
        fightid = 6
        battle(you,bots,Cont=False)
        if victory == 1:
          text("\n*Hassan gets back up and charges Noah*","\nHassan, angry: #I HATE YOU, SO ANNOYING#","Noah, getting up in stance: #FUCK YOU NIGGA#","\n*Hassan is about to make contact with Noah, when Metin explodes from below them*","Metin, about to end everyone: AAGGHHGH!","*Metin grabs Noah and Hassan's heads and bangs them together*","\nIshraq, amazed: God damn. They okay?","Metin, regaining clarity: I didn't go too hard I think. But then again, I don't even know my own strength.","Ishraq: You should be powering down soon. Whatever was screwing with your head is gone.","Metin, understandingly: You're right...but it felt good.","Ishraq, concerned: What do you mean?","Metin, trying to explain: I felt...like I lost my reason. My path. But I didn't care. Because the way it made me physically feel was so good.","Julius, trying to conclude: So this wired thing makes you feel so good that you don't care about your free will.","Noah, waking up: Somethin' like that...man my head hurts.","Hassan, also waking up: It's cuz yo' hard ass head! Bro, I'm hungry.","Ishraq, picking Hassan and Noah up: Alright, go to shop and we'll meet ya'll there once were done doing what we need to.")
          ro = rd(27)
          ro.objects = ["Ruler","Kit-Kat"]
          data[19] = 1
          ro = rd(6)
          ro.people.append("Metin")
          ro.people.append("Noah")
          ro.people.append("Hassan")
      elif boop == "2":
        text("\n*The three boys exchange many attacks. Hassan charges Noah*","\nHassan, angry: #I HATE YOU, SO ANNOYING#","Noah, in stance: #FUCK YOU NIGGA#","\n*Hassan is about to make contact with Noah, when Metin explodes from below them*","Metin, about to end everyone: AAGGHHGH!","*Metin grabs Noah and Hassan's heads and smashes them together*","\nIshraq, itching to jump in: GOD DAMN! THEY'RE NOT OKAY!","Metin, regaining clarity: ...I didn't go too hard I think. But then again, I don't even know my own strength.","Ishraq, checking pulses: Bro...Hassan's dead.","Metin, shocked: WHAT?!","Ishraq, shocked: METIN! YOU KILLED HASSAN!","Metin, scared: WHAT?!","Ishraq, angry at himself: MAN! I KNEW I SHOULD'VE JUMPED IN!","Metin, confused: Bro, what's going on...is this a dream?")
        data[16] = 1
        if data[15] == 1:
          text("Ishraq, directing his anger: This is the Fedora Man's fault.","Julius, curious: Who?","Ishraq, ready to kill: He's the guy behind this shit I think. He tried kidnapping Kelly earlier, and now everyone's brainwashed...has to be him.","*\nNoah wakes up*","Metin, still confused: Okay, but what is going on?","Ishraq, explaining: Okay, everyone at tech is under some trance, and we're tryna figure out what's going on. There was this guy who tried kidnapping Kelly and he can make portals...")
        elif data[9] == 1:
          text("Ishraq, thinking about it: This might be connected to the Fedora Man.","Julius, curious: Who?","Ishraq, keeping it in mind: He's this guy Bowers mentioned him.","*\nNoah wakes up*","Metin, still confused: Okay, but what is going on?","Ishraq, explaining: Okay, everyone at tech is under some trance...and we're tryna find out what's going on.")
        else:
          text("Ishraq, frustrated: No it's not...I don't even know what's going on.is going on in this place...","*\nNoah wakes up*","Metin, still confused: Okay, but why were we just fighting?","Ishraq, explaining: Okay, everyone at tech is under some trance, and we're tryna figure out what's going on.")
        text("Noah, drunk: My head hurts...yo were we just fighting?","Metin, figuring things out: Alright, so were in a apocalyptic version of our school.","Ishraq, liking that: Yeah. Alright we're gonna go do what we need to do, you two head down to shop. We got people there.","Metin, picking up Hassan's body: Gotchu sexy.")
        ro = rd(27)
        ro.objects = ["Ruler","Kit-Kat"]
        data[19] = 1
        ro = rd(6)
        ro.people.append("Metin")
        ro.people.append("Noah")
    if nextr == "F-Wing Engineering Shop Room" and "Ruler" in you.questinventory:
      if "The FX-Wing Nurse" in qcomp:
        text("\n*Julius slaps the ruler onto the table*","\nIshraq, looking at Kelly: Alright, do your thing.","Kelly, stretching: You want me to draw some isometric drawings?","Julius, laughing: HaHAA...of course.","Kelly, a little doubtful: Don't think this is going to work, but I'll try...","\n*Kelly draws a perfect isometric drawing of a random block*","\nIshraq, staring at the drawing: Now what?","Julius: We stare.","\n*A couple minutes pass*","\nJulius, shrugging: Okay, this is stupid.","Ishraq, reassuring: Nothing's stupid anymore. An idea is an idea. Good job Julius.","Julius: Thanks I guess.","Kelly, confused: Wait...you guys went through all that work to find a ruler?","Ishraq, thinking he missed something: Yeah...why?","Kelly, pulling something out from inside her hoodie: I have my ID right here.","\n*Everyone looks at each other*\n","Julius, confused: None of us have our IDs.","Ishraq: Yup...you're the only one who has it.","Brandon: That's type sus.","Edmond: Word.","Ishraq, changing the topic: Anyways, we should try looking for more isometric drawings.")
        questsys("The Straight Edge","Finish")
        xpg(200)
        you.questinventory.remove("Ruler")
        you.weaponinventory.append("Ruler")
        text("\nIshraq, concluding: Hmm...maybe the isometric drawings are in random places around the school. Right Kelly?","Kelly, agreeing: Yeah, like I found that stone randomly on Pudup's table. It was there by sheer coincidence. I didn't expect it to do what it did to you...","Ishraq, trying to make a connection: Was there anything else about the stone?","Kelly, thinking back on it: Well, it was displaying a holographic red colored isometric drawing from it...and when I picked it up, it was shaking violently. It sort of hurt, and when I dropped it, I kind of saw like gravitate towards you. So I kicked it.","Ishraq, making a hypothesis: Okay, so it was naturally attracted to me. So, where do you guys feel natural in perhaps.","Julius, stumped: I feel natural everywhere.","Kelly, also a little skeptical: I feel the most natural here in shop.","Ishraq, quickly thinking of something else: Well, how about where the hell do you guys just think you would find an isometric drawing stone?","Kelly, without a doubt: The library.","Julius, a little unsure: Maybe the automotive building? Just seems like it would have one.","Ishraq, ready: It's settled then, we're going to those places.")
        questsys("No Talking in The Library","StartM")
        questsys("More Than Meets The Eye","StartM")
      elif "The FX-Wing Nurse" not in qcomp and "Ice Pack" not in you.questinventory:
        text("\nJulius, reminding Ishraq: We need to go to the nurse for Kelly. She's got the best handwriting.","Ishraq: Agreed.")
#---------------------------------------------------------------------------------------------
  if "No Talking in The Library" in quests:
    if nextr == "C-Wing Media Center":
      text("\nIshraq, looking around: ...Alright, I guess we split up and sear...!!!","Kelly, putting her hand over Ishraq's mouth: Look!","\n*A tall and ghastly figure turns around*\n","The Librarian: THERE IS NO TALKING IN THE LIBRARY!!!","Julius, taken aback: Wooah...this technically a media center tho'.","The Librarian, screaming: WHERE IS YOUR ID'S!!!??","Ishraq, unphased: She's wired.")
      if data[13] == 0:
        text("Julius, looking at Ishraq: Don't do it again sir!","Ishraq, shaking his head: No more killing.")
      else:
        text("Julius, looking at Ishraq: We have to fight her then.","Ishraq, nodding: Let's do this.")
      print("\nThe Librarian engages onto the team!")
      bots.team = [Entity("The Librarian",750,30,22,40,40,100,70,150,95,10,0,10,0,"17","Female Boss")]
      battle(you,bots,Cont=False)
      if victory == 1:
        time.sleep(1)
        text("\nIshraq, panting: Toughest one yet.","Kelly, falling to the ground: Yeah...I mean that's the first wired that can levitate and throw books at you.","Julius, stretching: Alright, let's search for that stone.")
        ro = rd(14)
        ro.people = ["Kelly","Julius","The Librarian"]
        ro.objects = ["Bookcase A-D","Bookcase E-H","Bookcase I-L","Bookcase M-P","Bookcase Q-T","Bookcase W-Z","Computers","Front Desk"]
#---------------------------------------------------------------------------------------------
  if "For the Horde" in quests:
    if nextr == "F-Wing Engineering Shop Room":
      text("\nKelly, relieved: Aaah, finally back in a room full of non-wired people. I already feel cozy and safe...*Kelly checks her cubby*, hey this is my ASMR mini-mic! I've been looking for this!","\n*Kelly begins to make ASMR noises because she wants to...everyone just stares at her*\n","Kelly, stopping: What?","Everyone: No...keep going.","Everyone: Wait, what??","Kelly, happy: You guys like it that much?? Yay!","Ishraq, relaxed and confused: I don't know about ya'll...but it feels like she's hypnotizing us...","Metin: That's because I think she is...I feel so relaxed now.","Kelly, giddy: What do you guys mean?!","Julius, agreeing: Your mic...it's so soothing...and I'm not an ASMR type of person..I think your ISO is causing it.","Kelly, realizing: Oooh, maybe you're right.","*Kelly's ASMR microphone suddenly mixes with her calligraphy pen, becoming one!*",fore.MAGENTA_1+"\n~Kelly has gained a new ability, ASMR! She can perform ASMR in battle, recovering a percentage of her mana(MP) and increasing everyone's mana regeneration(MRG) at a cost of her health(HP)!\n"+style.RESET,"Ishraq, trying to turn on Mr. Pudup's computer: Shit...there's no electricity.","Julius, not fretting: Don't worry about that, this school has back up generators I heard.","Ishraq: We need them up and running...our chromebooks will run out of charge, ya heard?","Julius, confused: What are we gonna use chromebooks for?","Ishraq, also confused: ...communication maybe??? We still have no internet...DAMN IT!","Julius: Phones aren't working either...something is blocking radio signals.")
      talk = "1"
      while talk == "1":
        bruh = input("\n(1) *Take a headcount*  (2) *Take a nap*\nResponse: ")
        if bruh == "1":
          data[0] = data[0] + 5
          text("\nIshraq, taking a headcount: I was gonna make an excell sheet for organization. Guess I'll use paper. Ight', rolecall time. Julius.","Julius: Yer.","Ishraq: Kelly.","Kelly: Heyyy!","Ishraq: Brandon.","Brandon: Yo yo.","Ishraq: DAVID.","David: TEAM!","Ishraq: Edmond.","Edmond: I'm stil chillin'","Ishraq: METIN.","Metin: HI.","Ishraq: Noah.","Noah: Here bro.")
          if data[16] == 0:
            text("Ishraq: Hassan.","Hassan: PRESENT!")
          text("Ishraq: Alvaro.","Alvaro: I'm still alive.","Ishraq: Octavio.","Octavio: Here.","Ishraq, checking everyone off: We're all here. The only person missing that we've found so far is Richard.","Julius: Good, HaHAA!","Metin: Damn. You really gonna do Richard like that?","Julius, laughing: Yeaaah! Nobody wants that school shooter in here, HaHAA!","\n*Everyone looks at each other in reluctant agreement...Loud marching is heard from a distance*\n","Ishraq, with a sixth sense: No good. Something is coming. Towards us.")
          talk = "2"
        elif bruh == "2":
          data[1] = data[1] + 5
          text("\nIshraq, pulling a chair out: Well, time to take a nap. Wake me up when ya need me.","Kelly, shrugging: I guess we could rest...but there's so much stuff to do.","Ishraq, looking up at Kelly: I only slept for 4 hours today and I still haven't taken my nap in school. Don't worry, I'll guard the room.","Kelly, compliant: Okay, that's fine. Alright everyone, I think we should all work on gathering necessities for survival. That means we should make consistent runs to the cafeteria.","Julius, jumping in: Me, Brandon, Edmond, and David can take care of that.")
          if data[10] == 1:
            text("Kelly, thinking about other students: Me and Ishraq ran into some medical students a while ago...we weren't able to beat them, so they're most likely still wired. We could always check on them.")
          elif data[10] == 2:
            text("Kelly, thinking about other students: Me and Ishraq ran into some medical students a while ago...we were able to beat them, and Ishraq told them to take over their shop after they became un-wired. I don't know if they did, but we could always go chck on them.")
          else:
            text("Kelly, wondering: I wonder if anyone else was not wired like me and Ishraq...we should really check other shop rooms.")
          text("Metin: Agreed.","\n*Loud marching is heard from a distance*\n","Ishraq, instantly waking up: No good. Something is coming. Towards us.")
          talk = "2"
      text("Kelly, shaking: Wooah...what's going on???","Alvaro: It's the sound of marching in unison...ROTC kids maybe.","\n*The shop door starts to get rammed*\n","Brandon, jumping a little: !!...Uuuh. Guys. They're at our door already.")
      text("Ishraq, getting to the front-line: Stay back, let the ISO's fight first.","Metin, listening: Sounds like a lot of people...easily more than 20.","Ishraq: Shit.","\n*The door is slammed again, close to breaking open!*\n","Kelly, observing from the window: Someone is being carried out there!","\n*The door breaks open! Wired rush into the room, carrying someone in!*\n","Ishraq, staggered: They got Tim! But...his eyes are white! He's wired!","Julius, as he knocks out a wired: He's their commander, HaHAA!","Ishraq, throwing a wired into a pile of others: Of course Tim had to be a ring leader!","\n*Tim is lowered down from the people carrying him like a king*\n","Tim: #This seems like a suitable place to be my castle.#","Ishraq: God damn it, now he's trying to colonize us.","Tim: #Come soldiers, we will destroy all resistance here and claim this place as ours!#","Kelly, zapping wired with her pen: They're coming in full force!!! Get ready everyone!!")
      bots.team = [Entity("Tim",1000,100,30,30,0,70,60,100,110,0,0,0,20,"17","Male Boss"),Entity("Jahir",200,30,20,40,10,20,40,100,100,10,0,0,0,"18","Male"),Entity("Andrew",175,30,25,30,30,10,45,100,110,0,0,0,0,"19","Male"),Entity("Dylan",225,30,30,50,0,40,45,110,100,0,10,0,0,"20","Female"),Entity("Shannae",200,30,15,40,40,60,35,110,100,10,0,10,0,"21","Female")]
      bots.backteam = [Entity("Yanelly",210,30,10,30,10,50,30,110,100,0,0,0,0,"22","Female"),Entity("Destiny",180,30,19,20,10,70,40,100,100,40,10,0,0,"23","Female"),Entity("Manuel",190,30,20,50,10,10,35,100,100,5,0,0,0,"24","Male"),Entity("Emely",150,30,12,30,10,20,60,100,120,10,0,0,0,"25","Female"),Entity("Matthew",180,30,17,40,10,40,40,110,100,6,0,0,0,"26","Male"),Entity("Brianna",165,30,16,30,10,20,40,100,120,10,0,0,0,"27","Female"),Entity("Lesly",230,30,40,40,10,20,25,120,100,4,20,0,0,"28","Female"),Entity("Stephanie",140,30,24,20,10,20,45,105,105,7,0,0,0,"29","Female"),Entity("Tony",240,30,30,50,10,0,40,100,100,8,0,0,0,"30","Male"),Entity("Keshvi",130,30,10,20,10,100,30,100,100,20,0,0,0,"31","Female"),Entity("Kobe",180,33,24,45,10,30,50,120,100,5,0,0,0,"32","Male"),Entity("Antonio",210,30,25,30,10,30,45,110,100,10,0,0,0,"33","Male"),Entity("Tahmid",200,30,16,55,10,20,35,110,100,6,0,0,0,"34","Male")]
      fightid = 7
      fightmod = 1
      battle(you,bots,Cont=True)
      if victory == 1:
        text("\nIshraq, ecstatic: YES!!! WE DID IT!...","*Ishraq tips over and falls to the ground face-first*","*More marching is head outside*","Metin, huffing: We already...took out their ringleader...what gives?","Brandon, laying down: They don't care. We're doomed.","Metin, making a plan: Alright...you all hide in the closets. I'll take the rest of them on.","Noah, placing his hand on Metin's shoulder: No sacrifices today brother...you've saved someone in your lifetime already.","Metin, flattered: You just can't stop bringing it up, huh? Well, too bad the Heimlich maneuver isn't saving you or anyone in this room. So go hide.","Noah, shaking his head left and right: Nah, I'm not giving up these gloves.","Metin, too tired: Have it your way, guess we're all dead.","\n*Wired approach the Engineering Shop Room...Ishraq begins to glow...the Wired enter the room, no students are able to fight...a pulse releases from Ishraq's body, knocking every non-ISO organism out!*\n")
      else:
        text("\nBrandon, on the ground: We can't win...we're doomed.","Metin, huffing: You guys retreat...to the back of the room! I'll take them all on!","Noah, staying beside Metin: No sacrifices today! You've save someone in your liftime already!","Metin, smiling: Well, too bad the Heimlich maneuver isn't saving you or anyone in this room. I'll hold them off! You guys regain your energy and get the hell out of here!","Noah, prepared to fight: Nah, I'm not giving up these gloves.","Metin, respectful: Fine, we'll fight together. Everyone else, just run!","\n*More wired approach the Engineering Shop Room...Ishraq begins to glow...the Wired enter the room, students still fighting the previous wave...a pulse releases from Ishraq's body, knocking every non-ISO organism out!*\n")
      time.sleep(1)
      print("...")
      time.sleep(1)
      print(".....")
      time.sleep(1)
      print("???: ......")
      time.sleep(1)
      print("???: Awaken.")
      time.sleep(1)
      text("*Ishraq looks around...he is in the ISO-space once again, the same red-space he went in when he was reconstructed as an ISO.*","Ishraq, testing if he could talk: Yo.","???: I hope you are okay, Mr. Ahmed.")
      if victory == 1:
        input("Ishraq, disorientated: Huh...where am I?")
      else:
        text("Ishraq, disorientated: Are...they still fighting?","???: Do not worry. Your friends are all safe. I helped a bit.")
      text("\n*Dr. Graham appears before Ishraq...Ishraq is no longer free floating in the red-space, but now is standing in it.*\n","Ishraq, relieved: Dr. Graham! What are you doing in...my womb...?","Dr. Graham: Yes, this is your second womb. Where you were reconstructed and born again as an Isometric Wielder.","Ishraq, intrigued: An Isometric Wielder...what does that mean?","Dr. Graham: You are of equal dimensions. In this world, there exist dimensions of space in which things exist in. Existence as you know it exists in the 3rd dimension. What if I told you there are 10 dimensions?","Ishraq, confused: I don't know what you're on about Doctor.","Dr. Graham: That is okay Mr. Ahmed, I am here to answer your questions. Shoot.")
      talk = "1"
      t1 = 0
      t2 = 0
      t3 = 0
      t4 = 0
      t5 = 0
      t6 = 0
      t7 = 0
      t8 = 0
      while talk == "1":
        if t1 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(X) I have no questions.\nResponse: ")
        elif t2 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(3) Source of Power?  (X) I have no more questions.\nResponse: ")
        elif t3 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(3) Source of Power?  (4) These powers seem connected to me personally...\n(X) I have no more questions.\nResponse: ")
        elif t4 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(3) Source of Power?  (4) These powers seem connected to me personally...\n(5) What exactly am I equalizing?  (X) I have no more questions.\nResponse: ")
        elif t5 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(3) Source of Power?  (4) These powers seem connected to me personally...\n(5) What exactly am I equalizing?  (6) Why would someone want to kidnap Kelly?\n(X) I have no more questions.\nResponse: ")
        elif t6 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(3) Source of Power?  (4) These powers seem connected to me personally...\n(5) What exactly am I equalizing?  (6) Why would someone want to kidnap Kelly?\n(7) How come you don't stop the Fedora Man?  (X) I have no more questions.\nResponse: ")
        elif t7 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(3) Source of Power?  (4) These powers seem connected to me personally...\n(5) What exactly am I equalizing?  (6) Why would someone want to kidnap Kelly?\n(7) How come you don't stop the Fedora Man?  (8) Who esle is an ISO?\n(X) I have no more questions.\nResponse: ")
        elif t8 == 0:
          bruh = input("\n(1) Why's it so comfortable here?  (2) 10 dimensions?\n(3) Source of Power?  (4) These powers seem connected to me personally...\n(5) What exactly am I equalizing?  (6) Why would someone want to kidnap Kelly?\n(7) How come you don't stop the Fedora Man?  (8) Who esle is an ISO?\n(9) What's the end plan?  (X) I have no more questions.\nResponse: ")
        if bruh == "1":
          text("\nIshraq, laying down as if he was going to bed: It's so comfortable in here...","Dr. Graham: This is your Isometric Drawing. It exists in every dimension at the same time. It is the source of your power.")
          t1 = 1
        if bruh == "2":
          text("\nIshraq, confused: I don't know...10 dimensions doesn't seem right.","Dr. Graham: Well, living in the 3D realm your entire life, you cannot possibly comprehend too much beyond it.")
        if bruh == "3" and t1 == 1:
          text("\nIshraq, trying to stay awake: Why is it a source of power?...How?","Dr. Graham: In existing in all dimensions, you act as an equalizer. Any threat to a dimension from another dimension, you are able to equalize. It is a small gift from me to you to help you fight.","Ishraq, shocked: Wait, you gave me these powers?!","Dr. Graham: Correct.")
          t2 = 1
        if bruh == "4" and t2 == 1:
          text("\nIshraq, noticing: These powers seem connected to me...same for Kelly and maybe Julius.","Dr.Graham: Your Isometric Drawing materializes at your will. It will shape after you as a person and what you want the most to best accomadate your way of equalizing the world.")
          t3 = 1
        if bruh == "5" and t3 == 1:
          input("\nIshraq, confused: What exactly am I equalizing?")
          if data[15] == 1:
            input("Dr. Graham, frowning: As you should know by now, there is a man who poses a threat to the entire universe right now. He is using powers from the 6th dimension to terrorize the 3rd dimension. You know him as the Fedora Man.")
          elif data[9] == 1:
            text("Dr. Graham, frowning: As you should know by now, there is a man who poses a threat to the entire universe right now. He is using powers from the 6th dimension to terrorize the 3rd dimension. You know him as the Fedora Man. Mr. Bowers mentioned him when you fought.")
            data[15] = 2
            data[0] = data[0] - 2
          else:
            text("Dr. Graham, frowning: There is a man who poses a threat to the entire universe right now. He is using powers from the 6th dimension to terrorize the 3rd dimension. He has a fedora on his head and wears a black trenchcoat. Let us call him The Fedora Man.")
            data[15] = 2
            data[0] = data[0] - 2
          text("Ishraq, shocked: What the hell?!","Dr. Graham: He comes from the future. He has time-travelled to our time to kidnap Ms. Cha and bring her to his time.")
          t4 = 1
        if bruh == "6" and t4 == 1:
          text("\nIshraq, weirded out: Why would someone want to time-nap Kelly?","Dr. Graham, shrugging: I am not sure. Nonetheless, I will assist you in any I can. Just go to my room and someone will be waiting for you.")
          t5 = 1
        if bruh == "7" and t5 == 1:
          text("\nIshraq, curious: Wait...how come you don't just stop the Fedora Man yourself?","\nDr. Graham, smiling: Hahaha...you are in the Realm Between and I am not. You exists right now in a rift between the present and one point in the future. Before the Fedora Man could escape to the future, I froze time in the 3rd dimension so that the portal to the future would close. I then went to investigate what damage he had done. Ms. Cha was already in the Realm Between falling in the void, but the Fedora Man was frozen in our time. I could not enter the Realm as I had to stay outside the rift to keep the present time frozen. So I cut out our campus from our world and inserted it into the Realm Between to save Ms. Cha.\n","Ishraq, understanding: Ah, I see. So you want us to take him down from the inside so you can safely unfreeze time and get us out of here.","Dr. Graham: Spot on.")
          t6 = 1
        if bruh == "8" and t6 == 1:
          text("\nIshraq, wondering: Who else is an ISO?","Dr. Graham: Currently only you three. I cannot simply hand them out to everyone...the amount of power I can transfer is limited since I am using the rest keeping time frozen. I will deliver it whenever I see someone fit. I will know since I too exist in all dimensions just like you, Ms. Cha, and Mr. Pallero.")
          t7 = 1
        if bruh == "9" and t7 == 1:
          text("\nIshraq, suddenly serious: So what's the end plan to all of this?","Dr. Graham, grim: That is up to you, Mr. Ahmed. We cannot let the Fedora Man escape with Kelly into the future. I have faith that you will find a way to stop him, as you are one of my AP students. Am I right or am I right?")
          t8 = 1
          start = time.time()        
          elapsed = 0               
          while elapsed < 6:
            print("\nYou have",round(6-elapsed),"seconds to make a decision")
            boop = input("(1) Do I kill him?  (2) I have no more questions.\nResponse: ")
            elapsed = time.time() - start
            if boop == "1" or boop == "2":
              break
          if boop != "1" and boop != "2":
            boop = "2"
          if boop == "1":
            input("\nIshraq: Do I have to kill him?")
            if data[13] == 0:
              input("Dr. Graham: I cannot answer...you have blood on your hands already. Be careful Mr. Ahmed. Anyways, do not forget to vitit my room.")
            else:
              input("Dr. Graham: I cannot answer...you will find a way in due time. Anyways, do not forget to visit my room.")
            input("Ishraq: I won't forget.")
            if t8 == 1:
              input("Dr. Graham: You had a lot of questions. I appreciate your inquisition. Knowledge is power, and I am glad you pursue it. As a token, I think I can bump up your strength a bit.")
              additem("T2 Red Isometric Drawing",1,you.isoinventory)
              input("\nDr. Graham: I wish you well on this journey. Do not forget to visit my room.")
            else:
              input("Dr. Graham: I wish you well on this journey. Do not forget to visit my room.")
            talk = "2"
          else:
            bruh = "x"
        if bruh.lower() == "x":
          if t1 == 0:
            text("\nIshraq: I have no questions.","Dr. Graham: Are you sure?","Ishraq, sure: Yes.","Dr. Graham: Very well. Do not forget to visit my room.")
          else:
            input("\nIshraq: I have no more questions.")
            if t8 == 1:
              input("Dr. Graham: You had a lot of questions. I appreciate your inquisition. Knowledge is power, and I am glad you pursue it. As a token, I think I can bump up your strength a bit.")
              additem("T2 Red Isometric Drawing",1,you.isoinventory)
            input("\nDr. Graham: I wish you well on this journey. Do not forget to visit my room.")
          talk = "2"
      text("\n*Ishraq wakes up inside his shop room...he looks around to see everyone recovering.*\n","Julius, announcing: Yo! Ishraq is awake~!","*Kelly walks over to Ishraq*","Kelly, lending a hand: You okay?","Ishraq, grabbing her hand to pull himself up: Yeah...I just had some sort of vision, ya heard?","Kelly: Hmm?","\n*Ishraq explains to Kelly and everyone his encounter with Dr. Graham*\n","Julius, excited: YOOO! I ALWAYS KNEW DR. G WAS SOME SORT OF GOD!","Ishraq, laughing: Hahaha! Word. So is everyone alright?","Kelly, looking over at everyone: Yeah...I'm attending to everyone. We're working with the nurse right now. No one is seriously injured.","Ishraq, relieved: Good...do I get to sleep now?","Kelly, laughing: Haha...I don't think so. While you were out, we decided to go check on the medical shop. You're coming with us.","Ishraq, sighing: Haaah...I'm gonna knock out sooner or later. Do you guys REALLY need me? You and Julius are strong enough to deal with some wired, right?","Julius, leniant: Let the man rest. We need him juiced up for the rest of the day.","Ishraq, sitting back down: Thank you Julius...wait a second, what's in my pocket?","\n*Ishraq shuffles into his pocket and pulls out a screwdriver*\n","Ishraq, delirious: Huhawhat? When the hell did I find this?","*The screwdriver emits a Cyan Isometric Drawing from it*","Kelly, excited: Ooooh! Dr. Graham sent another ISO!","Ishraq, glad as he rests his eyes: Yeah...time to find out who for. Here Kelly. I'm finally gonna nap now.","*Ishraq gives Kelly the screwdriver*")
      questsys("For the Horde","Finish")
      you.reset("Team")
      autosave()
      revival(Ishraq)
      revival(Kelly)
      revival(Julius)
      forceswitch(Ishraq)
      boo = 0
      for x in bots.deadteam:
        boo = boo + 30
      xpg(boo)
      if data[10] == 2:
        questsys("Daily Checkup","StartM")
      else:
        questsys("Medical Attention","StartM")
      ro = rd(3)
      ro.paths.append("Medical Shop Room")     
      bots.reset("Team")
      if "ASMR" not in Kelly.skills:
        Kelly.skills.insert(1,"ASMR")
      if "Valorous Chant" not in Ishraq.skills:
        Ishraq.skills.insert(2,"Valorous Chant")
      if "Tremors" not in Julius.skills:
        Julius.skills.insert(2,"Tremors")
      ro = rd(6)
      if data[16] == 0:
        ro.people = ["Brandon","Edmond","David","Metin","Noah","Hassan","Alvaro","Octavio","Tim","Dylan","Jahir","Andrew","Shannae"]
      else:
        ro.people = ["Brandon","Edmond","David","Metin","Noah","Alvaro","Octavio","Tim","Dylan","Jahir","Andrew","Shannae"]
      if "Metin" not in you.suppbackS:
        supu("Metin",31,sk=True)
      if "Noah" not in you.suppbackS:
        supu("Noah",16,sk=True)
      if "Hassan" not in you.suppbackS and data[16] == 0:
        supu("Hassan",21,sk=True)
      ro.RLV = 2
#---------------------------------------------------------------------------------------------
  if "Feeling Alone" in quests:
    ro = rd(17)
    if nextr == "Cafe 2" and ro.RLV == 1:
      if "Daily Checkup" not in quests and "Medical Attention" not in quests:
        text("\n*Everyone surveys the room*\n","Ishraq, at a loss of words: Holy...","Metin, unsure: What...?","Noah, looking away: I don't think I want food anymore.","Kelly, nauseous: Can we leave please?","Ishraq, alert: There could be something dangerous in here...maybe we should leave.")
        if "The FX-Wing Nurse" not in quests:
          text("Kelly, scared: These kids were all massacred! There's blood everywhere!","Ishraq, calming her: Don't worry. If we stay close to each other, we will not die here.")
        else:
          text("Noah, taking another peak: There's blood everywhere...this is crazy.","Ishraq, shocked: I've never seen anything like this before...this is different.")
        text("Metin, skeptical: I count...14 bodies scattered around the room...and they seem like they were together. Yet they're all dead.","Ishraq, trying to sense anything: Other than the bodies...I'm not feeling any sense of danger in here. Come on, let's get the food.","Julius, agreeing: We'll do a quick run and back.","Kelly, sticking close: Fine...")
      else:
        text("\n*Everyone surveys the room*\n","Julius, disgusted: Ooooh...this ain't pretty.","Metin, unsure: What...?","Noah, looking away: I don't think I want food anymore.","Kelly, nauseous: Can we leave please?","Julius, covering his nose: I haven't smelt anything like this before...bleuugh.","Kelly, scared: These kids were all massacred! There's blood everywhere!","Julius, taking a step forward: We need to get food. Come on.","Metin, skeptical: I count...14 bodies scattered around the room...and they seem like they were together. Yet they're all dead.","Julius, shivering: Yeah...they were probably all wired too. Some crazy shit probably did this.")
      ro.RLV = 2
      ro.objects = ["Snacks Crate","Fuze Crate","Dead Bodies","Note"]
#---------------------------------------------------------------------------------------------
  if "Medical Attention" in quests:
    ro = rd(28)
    if nextr == "Medical Shop Room" and ro.RLV == 1:
      text("Tim, entering the room first: Infiltration time!","Julius, following up: This room is giving me bad vibes already. There better not be another witch crying in here","Tim, interested: Another witch?","Julius: Me and Ishraq had a run in with some crying wired woman back in the Nurse's office...","Tim: She probably needed some medical attention.")
      if data[13] == 0:
        input("Julius, thinking back to her death: Well, she definitely did get it.")
      else:
        input("Julius, happily: We helped her out.")
      text("Kelly, sneaking inside: ..Anything in here?","Julius, putting his arm out to signal a stop: Wait...you here that? From the back of the room.","Kelly: Sounds like wired..they're doing something.","Tim, pushing past Julius: Let's go say hi!","Julius, not stopping him: Okay, you do you.","\n*Tim rolls his eyes back so they are completely white and approaches the wired by himself*\n")
      text("Tim, exaggertingly: HEY EVERYONE!! HOW ARE YA' DOING TODAY?","*Wired turn around to look at Tim*","??? #1: #Who the hell is this guy?#","??? #2: #I don't know him.#","??? #3: #Is he supposed to be here?#","??? #4: #No clue. Are you injured strange guy?#")
      talk = "2"
      while talk == "2":
        bruh = input("\n(1) Yes.  (2) No.\nResponse: ")
        if bruh == "1":
          text("Tim, acting: Aaghh, yes I am.","??? #5: Get him on a bed.","\n*Tim is escorted to a resting bed by the group of wired...they lock him in place*\n","Tim, regretful: Umm...what's going on?","??? #3: #You are probably going to get transfered to the Computer Repair shop to get re-wired. You are exhibiting signs of free will, which means the fight you were involved in must have almost un-wired you. The fact that you are here instead of assaulting Graham's group is a sign.#","Tim, sweating nervously: That's great and all, but what's up with the restraints?","??? #3: #That is just a normal procedure we go through here. This is the Recuperation Center. People who are re-wired are transferred here to be facilitated and restrained. Conscious movement impairs the wiring and healing process. Move around too much and you will malfunction and be disobedient to The God.#","Tim, swallowing: Th-The God?!","??? #1, taking a closer look at Tim: #He does not recognize The God...how can he still be wired?#","Tim, smug: Because I'm not. I actually something way better and cooler. I am an ISO!","\n*All the wired stop doing what they're doing*\n","??? #1: #He's apart of Graham's group! He tricked us!#","??? #2: #HAHAA! He got himself caught! What an idiot!#","Kelly, nudging Julius: Tim just willingly gave himself in...is he stupid?","Julius, shrugging: I don't know...but it seems like his cover is blown. Let's go break this dude out!")
          fightmod = 2
        if bruh == "2":
          text("Tim, reassuring: No, I am not, thanks for asking. What are you guys doing here?","??? #5: #What do you mean? This is the Recuperation Center. What's your position?#","Tim, bombastically: I lead the assault on the enemy's base!","??? #2: #Oh, he was on assault duty. They failed the attack though...#","??? #3: #It's great you made it out of there without getting de-wired. The Computer Repair shop already has there hands full rewiring some students.#","Tim, trying to figure out what's going on: Why do we need to recover again?","??? #5: #Not you. The students that are re-wired take time to adjust here. If they retain their intellect, which you clearly didn't, we delegate them to positions other than assault.#","Tim, shook and saddened: Damn...I can't believe I just got roasted by a wired.","??? #1, suspiscious: #You say that as if you're not wired.#","Tim, smug: Because I'm not. I'm actually something way better and cooler. I am an ISO!","\n*All the wired stop doing what they're doing*\n","??? #1: #He's apart of Graham's group now! We have to stop him!#","Kelly, nudging Julius: I think Tim is in trouble. We should go to him.","Julius, excited: Fighting time!")
          fightmod = 1
        fightid = 8
      if fightmod == 1:
        bots.team = [Entity("Alex",200,10,25,50,0,35,45,120,100,5,0,0,2,"18","Male"),Entity("Satya",180,10,28,40,0,0,50,100,120,8,10,0,2,"19","Male"),Entity("Ryca",150,20,18,30,35,70,40,110,110,50,0,0,0,"20","Female Heal"),Entity("Didar",130,10,16,20,50,100,40,100,110,3,0,0,0,"21","Male Heal"),Entity("Taric A.",250,0,26,45,0,35,60,100,100,9,0,0,0,"22","Male")]     
        battle(you,bots,Cont=False)
      if fightmod == 2:
        forceswitch(Tim)
        bots.team = [Entity("Bed",100,0,0,20,0,0,0,0,50,0,0,0,0,"17","Male"),Entity("Alex",200,10,25,50,0,35,45,120,100,5,0,0,2,"18","Male"),Entity("Satya",180,10,28,40,0,0,50,100,120,8,10,0,2,"19","Male"),Entity("Ryca",150,20,18,30,35,70,40,110,110,50,0,0,0,"20","Female"),Entity("Didar",130,10,16,20,50,100,40,100,110,3,0,0,0,"21","Male"),Entity("Taric A.",250,0,26,45,0,35,60,100,100,9,0,0,0,"22","Male")]      
        battle(you,bots,Cont=False)
      if victory == 1:
        if fightmod == 1:
          text("Tim, flexing: Ooh yeah, nothing can stop the Tim!","Julius, laughing: HaHAA~! You weird weird.")
        elif fightmod == 2:
          text("Julius, slapping Tim's back: YOU! Are craazy! HaHAA~!","Tim, flexing: I had everything under control~")
        text("Kelly, skipping towards Ryca: Are you okay?","*\nThe medical students regain concsiousness\n*","Ryca, jumping up: Yeah, I'm good...sheeee, I need to stretch out.","Kelly, joining Ryca in her stretching: I'm so happy to see you safe, let me fill everyone in on what's going on.","*Kelly explains everything*","Alex, normally: So we will try to take over this shop.","Kelly, nodding: Yeah, there's a lot of people in medical, almost quadruple the amount in engineering. Stick close and pick off students one by one till you guys can amass an army.","Taric A., stretching his calves: Lightwork.","Kelly, a little worried: You guys have any weapons?","Satya: We've got our anatomy textbooks. They're heavy as fuck. Our shop textbooks are heavy too.","Kelly, intrigued: Anatomy, huh. Let me see your books.","\n*Satya hands over his textbooks to Kelly*\n","Kelly, skimming through it: I just thought of a great tactic for fighting. I can learn about the human body and its weaknesses from this book...",style.BOLD + fore.MAGENTA_1 + "\n~Kelly has gained a new ability, Pinpoint! She targets a vital on the enemy, striking it devastatingly, dealing bonus true damage based on her physical attack, on top of her normal damage. This also causes the enemy to bleed based on Kelly's accuracy.\n"+style.RESET,"Ryca, innovating: Not only that, you can learn about health in general from our shop textbook. It might be useful with all that fighting you're going to do with the other ISOs.","Kelly, really interested with ideas floating in her head: Yeah...I really can. I can't wait to read through all this. We all do need to stay healthy.",style.BOLD + fore.MAGENTA_1 +"\n~Kelly has gained a new ability, Heal! She recovers the health(HP) of an ally or herself by her magic attack(MAT) and a percentage of their maximum health.\n"+style.RESET)
        Kelly.learnskill("Pinpoint")
        Kelly.learnskill("Heal")
        text("Ryca, fired up: Let's take back this school guys! *Ryca looks to Kelly* What will you do now?","Kelly, looking up: I dunno...I think we could just invade every shop and free a group of students like we did in here. We can spread the cure to wiring like a disease.","Ryca, in support: That sounds like a great idea.")
        ro.RLV = 2
        ro.people = ["Ryca","Alex","Didar"]
  if "Daily Checkup" in quests:
    ro = rd(28)
    if nextr == "Medical Shop Room" and ro.RLV == 1:
      text("Tim, entering the room first: Infiltration time!","Julius, following up: This room is giving me bad vibes already. There better not be another witch crying in here","Tim, interested: Another witch?","Julius: Me and Ishraq had a run in with some crying wired woman back in the Nurse's office...","Tim: She probably needed some medical attention.")
      if data[13] == 0:
        input("Julius, thinking back to her death: Well, she definitely did get it.")
      else:
        input("Julius, happily: We helped her out.")
      text("Kelly, sneaking inside: Is there anyone in here?","Julius, putting his arm out to signal a stop: Wait...you here that? From the back of the room.","Kelly, suddenly excited after listening: HEY! People are talking over there! It sounds like normal people too! Let's go!","Tim, pushing past Julius: I WILL SAY HI FIRST!","Julius, shrugging: Okayy~","\n*Tim shoves Kelly out of the way and approaches the students first*\n","Tim, exaggertingly: HEY EVERYONE!! HOW ARE YA' DOING TODAY?","Ryca, jumpscared: HHAHAAGH~! WHO ARE YOU!? EVERYONE JUMP HIM!","Tim, taking a step back: WAIT! I'm not wired! I AM TIM!","Alex, chilled: Oh, I know this guy. I had geometry with him.","Didar: Yeah me too.","Ryca, still ready to kick ass: HEY TIM. YOU DON'T DO THAT HERE.","Tim, trolling: Do what?","*Kelly flys in, jump kicking Tim to the ground*","Kelly, enraged: THAT'S FOR PUSHING ME TO THE GROUND ASSHOLE! *Kelly looks over to Ryca* Heyy! I'm so glad to see you safe! You, Alex, and Satya were able to camp out here!","Ryca, glad: Yeah, we stuck together and found Didar and Taric in here. They were still zombies, so we waited for an oppurtunity to pick them off when they were alone. After we did that, we just locked the door to this room and holed up in here. We're planning on hunting other medical students slowly one at a time to eventually gather an army.")
      text("Kelly, in support: Brilliant plan! But like it sounds quite dangerous...you guys need things to fight with. These zombies that us engineering students call wired are no joke. Your shop is also huge compared to ours, there being like quadruple the amount of kids in your shop.","Taric A., stretching his calves: I think there's like 200 people in our shop, lightwork.","Satya: We can fight with our anatomy textbooks. They're pretty much lethal given how fucking heavy they are. Our shop textbooks are heavy too.","Kelly, intrigued: Anatomy, huh. Let me see your books.","\n*Satya hands over his textbooks to Kelly*\n","Kelly, skimming through it: I just thought of a great tactic for fighting. I can learn about the human body and its weaknesses from this book...",style.BOLD + fore.MAGENTA_1 + "\n~Kelly has gained a new ability, Pinpoint! She targets a vital on the enemy, striking it devastatingly, dealing bonus true damage based on her physical attack, on top of her normal damage. This also causes the enemy to bleed based on Kelly's accuracy.\n"+style.RESET)
      text("Ryca, innovating: Not only that, you can learn about health in general from our shop textbook. It might be useful with all that fighting you're going to do with the other ISOs.","Kelly, really interested with ideas floating in her head: Yeah...I really can. I can't wait to read through all this. We all do need to stay healthy.",style.BOLD + fore.MAGENTA_1 +"\n~Kelly has gained a new ability, Heal! She recovers the health(HP) of an ally or herself by her magic attack(MAT) and a percentage of their maximum health.\n"+style.RESET)
      Kelly.learnskill("Pinpoint")
      Kelly.learnskill("Heal")
      text("Ryca, fired up: Let's take back this school guys! *Ryca looks to Kelly* What will you do now?","Kelly, looking up: I dunno...I think we could just invade every shop and free a group of students. If we free groups like yours, they can slowly work towards freeing people in their respective shops. We can spread the cure to wiring like a disease.","Ryca, totally for it: That sounds like a great idea.")
      ro.RLV = 2
      ro.people = ["Ryca","Alex","Didar"]
      ro.objects = ["Unknown Object"]
#--------------------------------------------------------------------------------------------------
  if "Sign Language" in quests:
    if nextr == "ASL Room":
      text("\n*Everyone stares at something that should obviously not be in the room*\n","Tim, ecstatic: IT'S A BIG ROCK! THE PIONEERS USED TO RIDE THESE BABIES!","Julius, in awe as he points: Wooow look, there's something yellow glowing in the hole.","Kelly, getting closer as she observes the hole cut out at the top of the column-shaped rock: There's a symbol..the yellow light is emitting a symbol. Of what, I have no clue.","Tim, sure: Another ISO maybe? They're clearly color-coded, and we don't have a Yellow ISO yet.","Kelly, leaning towards Tim's idea: Perhaps, but this is way too big to be an ISO. It's like 8 to 9 feet. It's decently chonky too.","*Tim walks up to the rock and touches it*","Tim, not feeling anything: Hmm...I guess I'm not supposed to have two ISOs. Welp, I guess I'll look for my bookbag.","\n*Tim quickly scans the room from where he's standing and does not see his bag--he then assumes a kneeling position near the rock to scan the floor--!!!--He is suddenly imbued with an unknown power! The yellow light fades away from the rock.*\n","Tim, confused as he is energized suddenly: Guys..I think I'm the yellow ISO..WOW!","Kelly, scratching her head: Are you sure?? You didn't enter a yellow-space, did you?","Tim, turning to her: I did not! Which means I am probably not the Yellow ISO.","Julius, ready to leave: Ight~Let's just get back to shop before some freaky shit happpens to Tim.")
      ro = rd(29)
      ro.objects = ["Tim's Bookbag"]
#--------------------------------------------------------------------------------------------------
  if "Showdown" in quests:
    if nextr == "Auditorium" and data[23] == "":
      ro = rd(6)
      if "Ishraq" in ro.people:
        text("\nKelly, pointing out as the team hides behind chairs: Something's going on here. Look at the stage.","Julius, counting: ..there's 4 wired just standing there. Think we can take em'?","Kelly, bravely: Probably. It'd be easier with Ishraq. Do you want to go get him?")
        talk = "1"
        while talk == "1":
          bruh = input("\n(1) Yes  (2) No\nResponse: ")
          if bruh.lower() == "yes" or bruh == "1":
            input("\nJulius, sneaking out of the auditorium: Yeah, let's go wake that dude up.")
            sad = 1
            talk = "2"
          elif bruh.lower() == "no" or bruh == "2":
            text("\nJulius, relaxed: Naahh, who needs that dude? We got these guys, lightwork.","Tim, waiting for a signal: So when can I go in?","Julius, shrugging: You do you.","\n*Tim reveals himself and sprints down the left aisle*\n","Tim, jumping onto the stage: FIGHT ME STRANGE PEOPLE!! HEY, WAIT!! THESE GUYS ARE FROM OUR SHOP!!","Kelly, slowly following Tim: Yeahh, they are. That's Matvey, Kenny...and?","Julius: This guy is Lacselles, but this other guy?","Tim: Dereck, I have him in shop with Ishraq.","Kelly, puzzled: They aren't hearing us, and we're right next to them. They're like..deactivated or something.","*Tim punches Dereck...all the wired activate!*","Tim, happy: There!","Kelly, tired: Really Tim?","Dereck: #What was that for?#","Kenny: #It's THEM. But how?#","Lascelles: #Well, they're here already, let's just fight!#")
            bots.team = [Entity("Kenny",300,10,26,50,0,40,45,110,100,5,0,0,2,"18","Male"),Entity("Lascelles",300,10,30,55,0,40,40,100,100,7,0,0,2,"19","Male"),Entity("Matvey",260,10,25,45,0,60,45,120,100,10,0,0,2,"20","Male"),Entity("Dereck",225,10,22,40,0,50,40,100,130,4,0,0,2,"21","Male")]
            battle(you,bots,Cont=True)
            if victory == 1:
              text("\nKenny, falling: #Y-you weren't suppo---# *Kenny knocks out*","Kelly, kicking his body: What are they on about?","Tim, inferring: I think we were supposed to come here later. This was set up for us.")
              if data[15] == 0:
                input("\nKelly, sitting on Kenny: Well, that's too bad. Sucks for the guy who set us up.")
              elif data[15] == 1 or data[15] == 2:
                input("\nKelly, sitting on Kenny: Well, that's too bad. Sucks for the Fedora Man.")
              input("\n*A portal opens up in the center of the stage!! In walks The Fedora Man with two other wired!!! He walks out and looks at the bodies on the ground...*\n")
            else:
              text("\nKelly, falling backwards: They're tough...","Julius, jumping back: Yeah..looks like we did need our man Ishraq.",bots.team[0].NAME+": #Do not let them escape!#","\n*A portal opens up in the center of the stage!! In walks The Fedora Man with two other wired!!!*\n")
            text("The Fedora Man, mouth open: Yes...this might be it!!","Kelly, getting up: This might be what? The day you die?! Come on guys, let's kill this loser right now!","Julius, into it: Damn, she's feisty right now, HaHAA~!","The Fedora Man, glaring at Kelly: Kill me you said? You couldn't even do that in ten years of time! *He begins walking towards Kelly menacingly*","Kelly, standing her ground: I'm not scared of you.","*The Fedora Man grasps Kelly's neck with his musty hand*","The Fedora Man, grinning: Ooh, your skin is softer than ever before..","Kelly, getting really creeped out: Let-t go!!","The Fedora Man, lifting her by the neck: Little girl, we're going to have so much fun together! Soon!","Tim, charging at the Fedora Man: I WILL DEFEAT YOOOOUU!!!---","*The Fedora Man lets go of Kelly and rocks Tim, instantly incapacitating him!*","Julius, shook as he's taking a step back: Wooah.","The Fedora Man, grinning: Hughagh~! Go run off Julius, you're good at that!","Kelly, crawling away: No no no, you're not taking me with you!","The Fedora Man, stomping towards Kelly: We'll see, little girl! HUGHAHGAHG!","\n*Ishraq, suddenly waking up*\n","Ishraq, staring deeply: ...They're in trouble.")
            data[23] = "0"
            if "Kenny" in bots.team:
              data[23] = data[23] + "1"
            if "Lascelles" in bots.team:
              data[23] = data[23] + "2"
            if "Matvey" in bots.team:
              data[23] = data[23] + "3"
            if "Dereck" in bots.team:
              data[23] = data[23] + "4"
            you.reset("Team")
            you.team = [Ishraq]
            you.teamS  = ["Ishraq"]
            for x in you.suppteam:
              you.ph1.append(x)
            you.suppteam = []
            you.suppteamS = []
            ro = rd(16)
            croom.remove(ro)
            world.append(ro)
            ro = rd(6)
            world.remove(ro)
            croom.append(ro)
            ro.people.remove("Ishraq")
            talk = "2"
            worldfunction()
      else:
        text("\nIshraq, noticing the stage: There's wired waiting for us.","Tim, waiting for a signal: So when can I go in?","Ishraq, resting his arm around Tim's shoulder and pointing: Take a look. These wired are from our shop. That's Daniel in the middle. Matvey and Dereck on the right. Kenny and Lascelles on the left.","Julius, grinning: Yoo~! It's big man Lascell'!","Kelly, careful: They're not moving at all...they seem like--deactivated or something?","Tim, reckless: One way to find out!","\n*Tim sprints down the left aisle*\n","Tim, jumping onto the stage: FIGHT ME PEOPLE FROM SHOP!!","*The wired wake up*","Lascelles: #They have arrived.#","Daniel, instantly noticing in the background: #She is here!#","Tim, praising himself: I, the sexy Timothy Mercurio, am here too.","*The team reaches Tim*","Lascelles: #They are engaging. Prepare for battle.#")
        bots.team = [Entity("Daniel",375,100,20,90,40,50,35,110,90,4,0,0,2,"18","Male"),Entity("Kenny",300,10,26,50,0,40,45,110,100,5,0,0,2,"19","Male"),Entity("Lascelles",300,10,30,55,0,40,40,100,100,7,0,0,2,"20","Male"),Entity("Matvey",260,10,25,45,0,60,45,120,100,10,0,0,2,"21","Male"),Entity("Dereck",225,10,22,40,0,50,40,100,130,4,0,0,2,"22","Male")]
        battle(you,bots,Cont=False)
        if victory == 1:
          text("\nDaniel, falling: #D-damn it, we fail---# *Kenny knocks out*","Kelly, kicking his body: Of course you failed. You weren't gonna beat us.")
          if data[15] == 2 or data[15] == 1 or data[9] == 1:
            text("Ishraq, curious: So the Fedora Man wanted us to come here? What for? To beat up these guys?","Kelly, sitting on Daniel: I guess so. He probably thought I was gonna lose here! What a joke!")
          else:
            text("Ishraq, curious: So who told you to come here? What's even going on?","Kelly, sitting on Daniel and getting ready to explain: So there's this guy who wears a fedora and a black trenchcoat who tried kidnapping me when we were still in the real world. Him and Daniel right here got into a fight. Daniel lost badly and this guy opened up a portal and threw me into it. Next thing you know, everything else happened.","Ishraq, eyes widened: This just got even weirder.")
          text("\n*A portal opens up in the center of the stage!! In walks The Fedora Man with one other wired!!!*\n","The Fedora Man, grinning: You made it here. *He notices Kelly sitting on Daniel*","Ishraq, unnerved: He's real. Great.","The Fedora Man, licking his lips: We're going to have so much fun together Kelly..ooohgh I can't wait for you to sit on me like that.","Julius, turning around weirded out: Ooh, this guy is weird weird, HaHAA~!","Ishraq, laughing but unsure: Hehah, she's not going to sit on you. Wait. That came out weird--she ain't going nowhere with you.","*Kelly drops to the ground and starts to clasp her ears again*","The Fedora Man, laughing: Hughahgh~! Oh, really? It hurts more the closer I am to her by the way.","Kelly, screaming: ST-STOOP!! THIS!","The Fedora man, stopping the earrape: Of course I'll stop. Just come with me. *The Fedora Man starts stomping towards Kelly mencaingly...he's stopped by Ishraq's arm!*","Ishraq, glaring: ...")
          start = time.time()        
          elapsed = 0               
          while elapsed < 6:
            print("\nYou have",round(6-elapsed),"seconds to make a decision")
            boop = input("(1) Let him take Kelly  (2) Don't give Kelly up\nResponse: ")
            elapsed = time.time() - start
            if boop == "1" or boop == "2":
              break
          if boop != "1" and boop != "2":
            boop = "1"
          if boop == "1":
            text("Ishraq, stunned: ...","The Fedora Man, throwing Ishraq's arm away from him: That's right! Do nothing! Useless as always! HUGHAHHGHA! *The Fedora Man walks over to Kelly, Ishraq standing aside.*","Julius, itching to engage: Hey hey, what are you gonna do to her?!","The Fedora Man, with an awful stare: WHAT ELSE??! HUGHAHHHGH! *The Fedora Man picks up Kelly over his shoulder...Kelly and Ishraq meet eyes as she's being carried away.*","Kelly, muttering: I'll be fine...","The Fedora Man, snarky: Get up Daniel. You have a job to finish.","\n*Daniel gets up!*","Daniel, looking at the other fallen wired: #IT'S DIN DIN TIME!#","*Daniel eats the other wired students and grows in size, gaining tremendous strength!*","The Fedora Man, amused as he opens a portal: I'm not wasting my precious time fighting a vermin like you. This big guy will do that. Anyways, me and Kelly have a date scheduled for later. Bye bye buddy!","\n*The Fedora Man opens a portal and exits with Kelly and one other wired!","Ishraq, noticing: Wait, that was Arwyn...","Tim, focusing: Hey, we gotta fight Daniel, let's go!")
            fightmod = 1
          elif boop == "2":
            data[0] = data[0] + 10
            data[2] = data[2] - 10
            fightmod = 2
            text("\nIshraq, rage building up: You're fighting me! NOW!","Kelly, clasping her ears again: No no no no!! PLEASE! DON'T START AGAIN!!","The Fedora Man, looking down at Ishraq: You heard her.","Ishraq, trying to clothesline The Fedora Man but to no avail: ...! What the hell?!","The Fedora Man, unmovable: I will destroy you eventually Ishraq, don't be so hasty. But first, I want to destroy her. Inside and out.","Kelly, shrieking: AAAAAAAGHHHH!!! STOOPP! STOOPP!","Tim, crumbling: Ishraq! We can't win this!","Ishraq, looking back at Kelly: Her ears are bleeding...","The Fedora Man, breathing on Ishraq: I can keep going! I'm enjoying this!","Ishraq, pulling himself away from him: Fucking shit. Just quit doing whatever the fuck you're doing already!","The Fedora Man, stopping: Good. *The Fedora Man walks over to Kelly, Ishraq standing aside.*","Julius, itching to engage: Hey hey, what are you gonna do to her?!","The Fedora Man, with an awful stare: WHAT ELSE??! HUGHAHHHGH! *The Fedora Man picks up Kelly over his shoulder...Kelly and Ishraq meet eyes as she's being carried away.*","Kelly, whimpering: It's okay...","The Fedora Man, snarky: Get up Daniel. You have a job to finish.")
            text("\n*Daniel gets up!*","Daniel, rebelling: #UGHH-GHH!! Y-YOU HURT..THE Q-QUEEN!!#","*Daniel charges at The Fedora Man, disobeying him! However, his attack is futile!*","The Fedora Man, admiring: Yes, that's it. Endorse that feeling of consciousness, you wired. You'll soon be fully aware. *The Fedora Man kicks Daniel away, knocking him back a great distance!*","Daniel: #Urghh--I-I am sorry!#","The Fedora Man, smiling as he opens a portal: Don't be. Anyways, I'm not wasting my precious time fighting a vermin like you. This big guy will do that. Also, me and Kelly have a date scheduled for later.","\n*The Fedora Man opens a portal and exits with Kelly and one other wired!\n","Ishraq, noticing: Wait, that was Arwyn...","Daniel, looking at the other fallen wired: #IT'S DIN DIN TIME!#","\n*Daniel eats the other wired students and grows in size, gaining tremendous strength!*","Tim, focusing: Hey, we gotta fight Daniel, let's go!")
          forceswitch(Kelly)
          if fightmod == 1:
            bots.team = [Entity("Mega Daniel",925,300,30,200,50,50,30,150,50,5,0,0,3,"18","Male")]
            battle(you,bots,Cont=False,Mid=True)
          elif fightmod == 2:
            bots.team = [Entity("Mega Daniel",740,300,30,200,50,50,30,150,50,5,0,0,3,"18","Male")]
            battle(you,bots,Cont=False,Mid=True)
          if victory == 1:
            text("*Daniel approaches Tim slowly whilst injured*","Tim, closing out: With all this crazy time and space stuff going on, I really wanna be able to do that stuff to. Do you know how I'm gonna do it?","Ishraq: Enlighten me.","Tim, smirking: I'm gonna become the fastest man alive, so fast no one can even see me dabbing.","*A cyan-ish aura appears around Tim's hands and he finishes off Daniel! Daniel visibly falls slowly to the ground. Tim does an incredibly fast dab on him afterwards!*",fore.CYAN_1+style.BOLD+"\n~Tim has gained a new ability, Chronopower! He ignites his weapon with the essence of time, causing his normal attacks to deal bonus magic damage and stealing the enemy's speed for 3 turns for 3 attacks.\n"+style.RESET,"Ishraq, falling on his back: What a...fight.","Tim, kneeling near Ishraq: We'll get Kelly back, no sweat. But then again, who needs her anyways?")
            if boop == "1":
              text("Ishraq, reflecting: I didn't even try to stop him.","Tim, serious: I'm pretty sure everyone in the room knew that none of us could. It's honestly better you didn't do anything stupid.","Ishraq, turning to Tim in confusion: You of all people saying this...","Tim, laughing: Haha, I'm confident and cocky with these ISO powers, but I'm not retarded.")
            else:
              text("Ishraq, reflecting: He didn't even budge. I literally could not push his neck with all my strength.","Tim, sighing of relief: Yeah...that Fedora guy is crazy. In all ways.")
              data[24] = 1
            text("Julius, a little lost: Damn...so what do we even do now? We just lost an ISO.","Ishraq, also lost: This really sucks. I guess we're heading back to shop. Though, let's wait for these guys we knocked out to wake back up.")
          questsys("Showdown","Finish")
          xpg(300)
          Tim.learnskill("Chronopower")
          questsys("Transmission","StartM")
          ro = rd(6)
          peep = ["Kenny","Lascelles","Matvey","Dereck"]
          ro.people.extend(peep)
          if "Chronopower" not in Tim.skills:
            Tim.skills.append("Chronopower")
    if nextr == "Auditorium" and "0" in data[23]:
      revival(Julius,o=True)
      revival(Tim,o=True)
      text("\nIshraq, noticing the stage: I knew they were here. *Ishraq rushes onto the stage*","The Fedora Man, with a beaten Kelly directly below him curled on the ground: I was waiting for you.","Ishraq, vibrating as he looks around: Y-you did all this? Where's Julius?!","The Fedora Man, cracking up: GHAUGHAHHAHA! HE RAN OFF LIKE THE PUSSY HE IS! HE KNOWS STRENGTH WHEN HE SEES IT UNLIKE YYOOOOU! GHAUHGAA!","Ishraq, walking past the Fedora Man and kneeling near Tim: Tim...you fought well.","The Fedora Man: Fought well? He didn't last a second!! HAGH!","Ishraq, noticing now: Kelly...KELLY!! WHAT! DID! YOU! DO!?","The Fedora Man, turning to Ishraq while unzipped: WHAT DO YOU THINK I DID?! HUGAHAHHA!","Ishraq, ENRAGED: YOUU SICK BASTAAARRRRD!! YOU'RE DONE!!!!","The Fedora Man, amused as he opens a portal: I'm not wasting my precious time fighting a vermin like you. My wired will do that. Anyways, me and Kelly have a date scheduled for later. Bye bye buddy!","\n*The Fedora Man opens a portal and exits with Kelly and one other wired! Ishraq attempts to chase but fails!*\n","Ishraq, screaming: HAAAAAAAAAAAAAAAAAAAGHH! WHO WANTS TO DIE?!","Julius, making an appearance: Yo~! You good dude?","Ishraq, viciously: HE TOOK KELLY AND KILLED TIM, JULIUS! COME ON, LET'S GO!","Tim, springing back up to help fight wired: Naw Ishraq, I was acting dead. I didn't wanna make you think we could fight that guy.","Ishraq, frustrated: WHY!? WOULD YOU DO THAT!?","Julius and Tim, in unison: We wouldn't win!","Ishraq, unstable but noticing: FUUCCCK!...!!LOOK WHO IT IS, IT'S WIRED DANIEL!!")
      you.reset("Supp")
      for x in you.ph1:
        you.suppteam.append(x)
        you.suppteamS.append(x.name)
      bots.team = [Entity("Daniel",375,100,20,90,40,50,35,110,90,4,0,0,2,"18","Male")]
      if "1" in data[23]:
        bots.team.append(Entity("Kenny",300,10,26,50,0,40,45,110,100,5,0,0,2,"19","Male"))
      if "2" in data[23]:
        bots.team.append(Entity("Lascelles",300,10,30,55,0,40,40,100,100,7,0,0,2,"20","Male"))
      if "3" in data[23]:
        bots.team.append(Entity("Matvey",260,10,25,45,0,60,45,120,100,10,0,0,2,"21","Male"))
      if "4" in data[23]:
        bots.team.append(Entity("Dereck",225,10,22,40,0,50,40,100,130,4,0,0,2,"22","Male"))
      battle(you,bots,Cont=False)
      if victory == 1:
        DHP = 475
        text("\n*Daniel gets back up!*","Daniel: #IT'S DIN DIN TIME!#")
        if data[23] == "0":
          input("*Daniel grows in size, gaining strength!*")
        else:
          input("*Daniel eats the other wired students and grows in size, gaining tremendous strength!*")
          if "1" in data[23]:
            DHP = DHP + 125
          if "2" in data[23]:
            DHP = DHP + 125
          if "3" in data[23]:
            DHP = DHP + 105
          if "4" in data[23]:
            DHP = DHP + 95
        bots.team = [Entity("Mega Daniel",DHP,300,30,200,50,50,30,150,50,5,0,0,3,"18","Male")]
        battle(you,bots,Cont=False,Mid=True)
        if victory == 1:
          text("*Daniel approaches Tim slowly whilst injured*","Tim, closing out: With all this crazy time and space stuff going on, I really wanna be able to do that stuff to. Do you know how I'm gonna do it?","Ishraq: Enlighten me.","Tim, smirking: I'm gonna become the fastest man alive, so fast no one can even see me dabbing.","*A cyan-ish aura appears around Tim's hands and he finishes off Daniel! Daniel visibly falls slowly to the ground. Tim does an incredibly fast dab on him afterwards!*",fore.CYAN_1+style.BOLD+"\n~Tim has gained a new ability, Chronopower! He ignites his weapon with the essence of time, causing his normal attacks to deal bonus magic damage and stealing the enemy's speed for 3 turns for 3 attacks.\n"+style.RESET,"Ishraq, falling on his back: What a...fight.","Tim, kneeling near Ishraq: We'll get Kelly back, no sweat. But then again, who needs her anyways?","Ishraq, no longer angry: Yeah, I know. I just got caught up in the moment. Especially after I thought you died. I can't believe Kelly got raped. It's crazy.","Tim, shrugging: It happens, even by people who don't have powers that can bend time and space. So not surprised.","Ishraq, not sure how to feel: I guess. I still saw the guy's penis. Straight up.","Julius, dying: Wghh-WHAT!! HaHAA~! That nigga flashed you!","Ishraq, getting up: I know. Well. I guess it's time to head back. Though, let's wait for these guys we knocked out to wake back up.")
          questsys("Showdown","Finish")
          xpg(300)
          Tim.learnskill("Chronopower")
          questsys("Transmission","StartM")
          ro = rd(6)
          peep = ["Kenny","Lascelles","Matvey","Dereck"]
          ro.people.extend(peep)
          you.ph1 = []
          if "Chronopower" not in Tim.skills:
            Tim.skills.append("Chronopower")
#--------------------------------------------------------------------------------------------------
  if "Transmission" in quests:
    if nextr == "F-Wing Engineering Shop Room":
      ro = rd(6)
      if ro.RLV == 3:
        text("\nIshraq, slumping on a chair: Maaaan. What the hell do we do now?","Daniel, already ready to leave: We search.","Julius, ready to chill: Eh. We're not finding that guy. Let him do his business with Kelly.","Daniel, rushing up to Julius and grabbing his neck with his musty hands: Listen here buddy. She's probably out there right now crying for help. Can you truly call yourself a man if you sit here and do nothing?","Julius, grossed out: Getchyo' crusty ass hands off me you weirdo!","Daniel, pulling away: Ridiculous. I'll go out to find her on my own if you lazy faggots won't.","Tim, bidding him farewell: When you die Daniel, you die! Don't forget that on your quest!","Daniel, sneering: I don't need to remember that...cuz' I can't die.","Ishraq, laughing: Hehaha, good luck my friend.")
        if data[24] == 1:
          input("\nDaniel, mockingly: Oh look, he's no longer interested in saving Kelly now that his cock is flacid.")
          if data[0] >= 40:
            input("\n\nIshraq, in complete disagreement: What?! Stop twisting shit in your head, I just tried to save her because she's my friend.")
          else:
            input("Ishraq, in complete disagreement: What?! Stop twisting shit in your head, I just tried to save her because I know her.")
        else:
          text("\nDaniel, mockingly: Oh look, now the slacker is getting complacent. Get up, will you?! You already failed once, doesn't that bother you?!")
          if data[23] == "":
            text("\nIshraq, angered: What could I have done there? He was killing her! Also, I'm not gonna go out of my way to save Kelly. We're trying to save everyone in this school.","Daniel, catching Ishraq off guard: Kelly is apart of everyone, no?")
          else:
            text("\nIshraq, angered: I couldn't get to him fast enough, I get it. But I'm not gonna go out of my way to save Kelly. We're trying to save everyone in this school.","Daniel, catching Ishraq off guard: Kelly is apart of everyone, no?")
        text("\n*Daniel walks to the door of the shop room*\n","Daniel, serious: Come with me. We will find her.","Ishraq, wanting to go but trying to act cool: Dude, you're a whole clown.","Daniel, straight-faced: I don't care. Kelly is in danger.","Ishraq, sweating: ...Y-you're right. We shouldn''t be sitting on our asses right now. We need to think of something.","\n*Ishraq gets up from his sit and gathers the team around a table*\n","Ishraq, just trying to make an idea: Soo...we're up against a guy that can teleport. Where to, we have no idea. He has to be in the school campus. So we either search every god damn room in this place, or we could try something different.","Tim, throwing in: Hmm, maybe we can do something at the Technology Room.","Ishraq, intrigued: Whatchu thinkin'?","Tim, taking out his phone: There's no service or internet. We need to set up some form of communication. If we could've communicated in the first place, finding Kelly would be plain simple.","Daniel, excited: Yeah, we can set up a radio broadcast network amongst rooms that we know other students are in, like the medical shop!","Tim: Yeah, this way we can always communicate with each other. It would also be useful to gain access to walkie-talkies and the announcement loudspeakers.","Ishraq, having some knowledge: Loudspeaker controls are in the main office...but I think we should go the H-Wing first to get our hands on some radio-tech in the Technology room.","Daniel, down for it: Agreed. This is going to be fun.")
        ro.RLV = 4
        ro = rd(11)
        ro.paths.append("Technology Room")
    if nextr == "Technology Room":
      ro = rd(30)
      if ro.RLV == 1:
        text("Ishraq, being cautious: Proceed quietly. This room ain't that big, we can clear it easily.","Tim, sneaking around: ...Seems clear. No wired anywhere.","Ishraq, signaling: Alright, Daniel, get the door. ","*Daniel locks the door, the team is safe inside the Techonlogy room.*","Tim, entering a storage closet: Alright, there's hella boxes in here. A ton of unopened tech.","Julius: Yeah, our tax dollars go here.","Daniel, slightly conflicted: It's not a waste, but schools do waste money on things that become outdated. Though, the old stuff ain't even bad at all.","Ishraq, trying to turn on a computer: Not working...damn it, forgot that there's no electricity. We really need to get those backup generators up. Without them, nothing in this school is gonna work. Even the water fountains.","Julius: Yeah, we just need to figure out where that is.","Ishraq, rubbing his chin: I have an idea of where it is. It's actually right out the door outside the Automotive Building I think. You know that huge underground garage?","Julius: Yeah, the road sinks down into it. It's usually closed though.","Ishraq: I think that's where all the school's inner-working are facilitated at. Like it's water-works, electricity, and stuff.","Tim: Yeah, it could be. I think they store food there to.","Daniel, starting to open boxes: Alright, but let's first look for some radios.")
        ro.RLV = 2
        ro.objects = ["Box #1","Box #2","Box #3"]
        ro.people = ["Julius","Tim","Daniel"]
    if croom[0].RID == 31:
      text("\nKelly, slowly opening her eyes: W-where...am I?","*Kelly looks around...it seems she is in a cell...the floor is cold and moist...the air in the room is musty.*","Kelly, touching her face: What is this? Ew! It's slimy.","*Kelly tries to see what it is, but can't in the dark room...she rubs it all off, but now it is on her hands. She rubs her hands on the floor to get rid of the sticky slimy substance.*","Kelly, really grossed out: What was that?","*The Fedora Man hears Kelly, and quickly rolls his chair towards her cell*")
      if data[23] == "":
        if data[24] == 1:
          text("\nThe Fedora Man, regretful: You p-passed out for a moment there. I am so sorry Kelly. I am soo sooo sorry. Please forgive me.","Kelly, head buzzing: Ugghh--you.","The Fedora Man, wide-eyed: Please please PLEASE forgive me for hurting you!","Kelly, bewildered: What the heck is happening right now..?","The Fedora Man, grabbing the cell bars: I wiped the blood off your face! It was Ishraq's fault!","Kelly, astonished: Are you serious right now? YOU did this to me!!","The Fedora Man, bending the cell bars slightly open: WHAT DID YOU SAY YOU FUCKING WHORE?!","Kelly, aghast: I-I didn't mean it--!","The Fedora Man, enraged: I DIDN'T DO ANYTHING!! IT WAS THAT! DISGUSTING! LOSER! ISHRAAAQ!","Kelly, submissively: Okay, okay! It was Ishraq's fault!")
        else:
          text("\nThe Fedora Man, concerned: You p-passed out for a moment there.","Kelly, head buzzing: Ugghh--you.","The Fedora Man, innocently: Why do you sound repulsed?","Kelly, astonished: Are you serious right now? You've been hurting me physically with your stupid ear attacks!","The Fedora Man, regretful: I am so sorry Kelly. I am soo sooo sorry. Please forgive me. There was no other way I could get you and those brutes to where I wanted to.","Kelly, not dealing with it: Oh, there was plenty of other damn ways!","The Fedora Man, grabbing the cell bars: Please. PLEASE! Forgive me!!","Kelly, spitting towards him: You're a maniac if you think you deserve forgiveness!","The Fedora Man, bending the cell bars slightly open: WHAT DID YOU SAY YOU FUCKING WHORE?!","Kelly, aghast: I-I didn't mean it--!","The Fedora Man, enraged: I DIDN'T DO ANYTHING WRONG, YOU HEAR ME!! IT'S ALL ISHRAQ'S FAULT!! OKAY!?","Kelly, submissively: Okay, okay! It's Ishraq's fault!...?")
        text("The Fedora Man, relieved: Aaaah! You understand now. Great! Well! Did you like the treat I left you?","Kelly, muttering: W-what t-treat?","The Fedora Man, nonchalantly: I nutted on your face. I'm sorry, I just couldn't hold back! Your beauty is just...too striking, I really had to! Forgive me, little girl. But umm..how did it taste?","Kelly, at a loss of words: I...I...","The Fedora Man, eagerly waiting: Yes, yes!","Kelly, pleasing him: I f-forgive you.","The Fedora Man, jumpy: Thank you! Anyways, I just wanna talk to you. Is that okay?","Kelly, trying to get by: Y-yes.")
      else:
        text("\nThe Fedora Man, ecsatic: KELLY~! How are you, little girl?","Kelly, head buzzing: Ugghh--you. I-I can't remember.","The Fedora Man, fear instilling: You don't remember, huh? I remember clearly! @I'm not scared of you!@-you said! HUGHAHGHAH!","Kelly, terrified: Oh...no no no..NO!! W-what..did you..doo---?","The Fedora Man, unzipping his pants: I really wanted to beat you down. I would've of, but you sort of passed out after I hit you once. And then this mean guy right here was hungry~! HGUAHHHG!","Kelly, tears streaming down her face: ...Please don't do it again...","The Fedora Man, teaching her: As long as you don't cross the line, I won't EVER lay a finger on you. But what you said about not being afraid really ticked me off! ","Kelly, not finding the words: I--I...I'm sorry.","The Fedora Man, happy: Good girl! Did you like the treat I left you?","Kelly, muttering: W-what t-treat?","The Fedora Man, nonchalantly: I nutted on your face. I'm sorry, I just couldn't hold back! Your beauty is just...too striking, I really had to! Forgive me, little girl. But umm..how did it taste?","Kelly, lost: I f-forgive you.","The Fedora Man, jumpy: Thank you! Anyways, I just wanna talk to you. Is that okay?","Kelly, submissively: Y-yes.")
      text("\nThe Fedora Man, bragging: Well, I want you to listen to my problems. You see, I could kill all your friends at any time. Ishraq, Julius, Tim, all of them! But without them, I really can't escape this place. You see, I need them to get stronger. A lot stronger. Your teacher, Dr. Graham, knows how powerful I am. I need to convince him into thinking I'm dead. That's where your friends come in. They need to be strong enough to 'kill' me. That way, the second Graham unfreezes time in the present, I can escape with you into the future.","Kelly, carefully: W-what will you do then...what do I have to do with this!?","The Fedora Man, trying to be charming: You, my dear, are destined to be my true love.","Kelly, taken aback disgusted: WHAT?!","\nThe Fedora Man, rambling: I know your future, and it's with me. We once lived happy together in our mansion worth millions of dollars...but one day. One. Day. You, my beloved, we're kidnapped by disgusting sewer rats! They put a price. A PRICE! ON YOU! YOU ARE SOMETHING OF IMMEASURABLE COST! AND THEY HAD THE NERVE!!! AND THAT STUPID UGLY DUMB LOSER ISHRAQ WAS AMONG THEM!","Kelly, trembling: W-what are you..even saying?","The Fedora Man, not even hearing Kelly: Oh, and the money they wanted from me...even though you are worth more than the sun...it left me penniless. I gave them everything. My life. That's what he always wanted from me. My life. And that's what he got. For you, I gave it to that vermin. And so they gave me the address of where they left you...a-and...and...you were there. In a body bag. Dyed crimson from your blood. I opened it up and looked at your beaten face. I kissed it over and over again, but you didn't respond. Kelly, don't you see!? YOU DIED!","Kelly, her heart sinking: Why...","The Fedora Man, angry: WHY? HOW COULD THEY EVER RESIST YOUR BEAUTY? THEY BEAT YOU, RAPED YOU, AND KILLED YOU! ABSOLUTELY NO RESPECT FOR WOMEN!")
      start = time.time()        
      elapsed = 0               
      while elapsed < 8:
        print("\nYou have",round(8-elapsed),"seconds to make a decision")
        boop = input("(1) How did you not protect me?  (2) Why don't you kill Ishraq right now?\nResponse: ")
        elapsed = time.time() - start
        if boop == "1" or boop == "2":
          break
      if boop != "1" and boop != "2":
        boop = str(random.randint(1,2))
      if data[23] == "":
        text("\nKelly, getting a gold of herself and thinking in her head: Kelly...relax. You will make it out of this. You are strong. And this guy? He's a total nutcase! Come on Kelly, you have to get something out of this guy!")
      else:
        input("\nKelly, getting a hold of herself and thinking in her head: Kelly...relax. You will make it out of this. You are strong...way stronger than this rapist...but this guy. He's crazy and delusional! Does he not realize he also has beaten and raped me? Come on Kelly, you have to get something out of this guy.")
      if boop == "1":
        text("\nKelly, pouting: How did you not protect me?","The Fedora Man, stumbling: Umm...okay. I got involved with Ishraq a long time ago. He eventually joined a gang that targeted Asian beauties like yourself. See, this guy was dirt poor scum. Me on the other hand, I was filthy rich and respected amongst the one percent. Ishraq was so jealous of me that he spent the rest of his days trying to ruin my life. His attempts at doing anything were futile though, as I just bested him in anything and everything. But one day, he found out about you, my dear little girl. He learned that you were my wife. Keep in mind, I had plenty of girlfriends before I married you, but I stayed loyal to only you once we met.","Kelly, weirded out: Okay...","The Fedora Man, continuing: Ishraq targeted my weaknesses and the weak like the pathetic worm he is. He forced me to do whatever he willed using you to threaten me!","Kelly, thinking to herself: He didn't even answer my question...he's just gloating. Something's wrong with his story.")
      if boop == "2":
        text("\nKelly, doubting The Fedora Man's story: Why don't you kill Ishraq right now? The other ISO's can easily fake your death. You hate him, don't you? Go kill him!","The Fedora Man, nervous: Umm...I can't.","Kelly, figuring out he's lying: Come on big boy. He killed me, right? Do it for me.","The Fedora Man, insisting: I really can't! If I do, I'll be stuck here forever!","Kelly, pouting: Awww~does it really matter though? I'm already dead in your time.","The Fedora Man, attracted: Well...yeah. That's why I'm bringing you, my true love, to my time. I plan to live on with you once again.","Kelly, winking: That's awfully selfish of you. We'll meet in the future some day.","The Fedora Man, growing annoyed: Okay, okay! I can't kill Ishraq yet because it might destroy the future in drastic ways.","Kelly, thinking to herself: He was nervous...and he's sweating. Something's wrong with his story.")
      text("\nThe Fedora Man, offering his hand: Anyways, my dear, are you willing to help me escape with you back into the future?")
      start = time.time()        
      elapsed = 0               
      while elapsed < 6:
        print("\nYou have",round(6-elapsed),"seconds to make a decision")
        boop = input("(1) Of course~!  (2) No.\nResponse: ")
        elapsed = time.time() - start
        if boop == "1" or boop == "2":
          break
      if boop != "1" and boop != "2":
        boop = str(random.randint(1,2))
      if boop == "1":
        text("\nKelly, cutely: Of course I will~!","The Fedora Man, getting shy: O-oh, thank you. Just to let you know, all you have to do is help your friends get stronger by any means necessary.")
        start = time.time()        
        elapsed = 0               
        while elapsed < 7:
          print("\nYou have",round(7-elapsed),"seconds to make a decision")
          boop = input("(1) Tease him.  (2) Leave him be.\nResponse: ")
          elapsed = time.time() - start
          if boop == "1" or boop == "2":
            break
        if boop != "1" and boop != "2":
          boop = str(random.randint(1,2))
        if boop == "1":
          text("\nKelly, egging him on: Yeah, yeah, I know. But what can I do to help you~?","The Fedora Man, face getting red: Wwhah...","Kelly, teasing: Oh come on. Quit acting like you're new to this. We were partners, right?","The Fedora Man, rushing over to her and grasping her shoulders: WEEEEGHHH~! DO YOU WANT TO HAVE SEX RIGHT NOW??!!!","Kelly, immediately regretting her actions: GET AWAY!! YOU'RE HURTING ME!!","The Fedora Man, jerking himself away from her: Oh, oh, oh. I'm so sorry, please don't leave! Please..","Kelly, aghast: What is...wrong with you?!","The Fedora Man, pleading: I'm sorry! I just...thought you wanted-","Kelly, cutting him off: I don't want anything! Especially from--*Kelly cuts herself off*","Kelly, thinking in her head: I need to be really careful not to make fun of this guy.","The Fedora Man, wide-eyed: From what?","Kelly, quickly: Not from..just especially not in here! I hate dark rooms!","The Fedora Man, learning: Oh! I'll remember that!")
      if boop == "2":
        text("\nKelly, eyes sharpening: No. I will not help you.","The Fedora Man, raising an eyebrow: Hmm? What will you do then?")
        start = time.time()        
        elapsed = 0               
        while elapsed < 7:
          print("\nYou have",round(7-elapsed),"seconds to make a decision")
          boop = input("(1) I will stop you.  (2) I'm going to kill Ishraq.\nResponse: ")
          elapsed = time.time() - start
          if boop == "1" or boop == "2":
            break
        if boop != "1" and boop != "2":
          boop = str(random.randint(1,2))
        if boop == "1":
          text("\nKelly, squinting with hatred: I will stop you.","The Fedora Man, suddenly hurt: W-why?","Kelly, glaring: I don't trust you one bit.","The Fedora Man, getting a hold: No matter...you'll help me regardless. And then I'll show you why you should trust me! I am a good and strong man!")
        if boop == "2":
          text("\nKelly, deviously smiling: Hmph. I'm going to kill Ishraq. That way I don't die in the future!","The Fedora Man, tilting his head: Umm..what makes you think you could do that?","Kelly, getting annoyed: What do you mean by that?","The Fedora Man, condescendingly: Well, you're worst than me in all ways. And the Ishraq right here and now is already becoming a menace. Soon enough, he'll need an entire army or a genius like me to take him down. And guess what? You're neither of them.","Kelly, feeling down: W-whatever! I'll stop him somehow!","The Fedora Man, shrugging: Good luck, little girl.")
      text("\nKelly, tired and thinking to herself: Is he finally done? Is he gonna let me go or something? He wants me to help the other ISOs get stronger...","The Fedora Man, predictably: Well, off you go back to your friends. Just exit through this door right here.","*The Fedora Man opens her cell up and points towards the exit...Kelly gets up off the floor and carefully walks towards the door.*","Kelly, glad: Finall---!!","*The Fedora Man flips a lever, opening up a trapdoor below where Kelly is standing! Kelly falls into another extremely cramped cell in a dimly lit room!*","Kelly, panicking: NO! NO! NO! YOU'RE NOT GOING TO KEEP ME IN HERE!","The Fedora Man, horny: Oooh~! This is perfect! From here, I can masturbate on you all I want! Be prepared! Your next meal is in an hour!! HUGGHAHGH!!","Kelly, screaming in terror: AAAAAAAAAAAAAAAEEEEGHH!!!!","The Fedora Man, glee: Yes! I'll make sure you're scared of me until the day you die! That way you will always listen... *The Fedora Man closes the trapdoor, locking Kelly in!*","Kelly, kneeling in defeat: God...please. Help me.\n")
      time.sleep(1)
      print("...")
      time.sleep(1)
      print("...")
      time.sleep(1)
      print("...")
      time.sleep(1)
      text("\nDr. Graham, inside of Kelly's head: Don't give up!","Kelly, sobbing but so happy: Dr. Graham! W-what do I even do?","Dr. Graham, giving hope: Ms. Cha. You are one of the most brightest students in this entire school. Just like all my students, you are capable. Capable of doing the impossible! But you! You can go beyond impossible! Don't ever doubt your talent and don't ever let anyone control your life! This Fedora Man? Easier than any of the problems you do in my class.","Kelly, still broken: I don't know Doctor...I don't know if I can deal with this guy.","Dr. Graham, youngly: It's okay if you don't know! That's why we learn! In time, you will learn what a strong lady you are.","Kelly, cheering up: Y-you really think so? You really think I'm strong?","Dr. Graham, wrapping up: I don't think. I know. I cannot stay here with you any longer Ms. Cha. Every word I speak, I use a tiny fraction of my power. I use too much of it, and time can unfreeze for just a femtosecond...and then things will start to get strange. Farewell.","Kelly, to herself: Hmm...maybe God does exist...! Wait a minute, someone is watching me..")
      you.reset("Team")
      revival(Kelly,o=True)
      revival(Arwyn,o=True)
      Arwyn.XP = round(((Tim.XP + Kelly.XP + Julius.XP + Ishraq.XP + Daniel.XP)/5)-100)
      Arwyn.Arwynlevelup(Arwyn.XP,Colis=True)
      for x in you.suppteam:
        you.ph1.append(x)       
      you.suppteam = []
      you.suppteamS = []
      ro = rd(31)
      ro.people.append("???")
      worldfunction()
#--------------------------------------------------------------------------------------------------
    
      
#--------------------------------------------------------------------------------------------------
  if nextr == "Auditorium" and "Final Showdown" in quests and croom[0].RID == 16:
    time.sleep(1)
    text("\nAmira: It's about time you all came...finally here to take away my gift? The only thing I have left?","Ishraq: Don't you get it!? The Fedora Man is using your ass to take us out!","Kelly: He's not your friend just because he gave you these powers! And we're not your enemies for trying to stop you!","Amira: I get it...only you six get to be extraordinary and powerful...no one else can!","Daniel: Guys, be careful, the power's getting to her head, aaghaha!!","Amira: The power has gotten to all of your heads!","Kelly: You're honestly beyond help.","Amira: Funny you say that Kelly. I thank you for your cooperation in advance!","Kelly: What do you me...!?","*Kelly is paralyzed and dragged towards Amira by her tethers*","Amira: Your powers are now mine...prepare for The End, haters.","Arwyn: Yes! Kelly is finally gone!","Daniel: MY QUEEN!! I'M COMING FOR YOU!")
    bots.team = [Entity("Amira",10000,0,500,100,500,100,60,100,100,1,1,1,0,"17","Female"),Entity("Kelly",1500,0,0,0,0,0,0,0,0,0,0,0,0,"18","Female"),Entity("Jackie",2000,0,0,0,0,0,0,0,0,0,0,0,0,"19","Female"),Entity("Abby",2500,0,0,0,0,0,0,0,0,0,0,0,0,"20","Female"),Entity("Meryem",1000,0,0,0,0,0,0,0,0,0,0,0,0,"21","Female")]
    bots[0].AmiraUP()
    battle(you,bots,Cont=False)
#---------------------------------------------------------------------------------------------
  

def rd(ID):
  for x in world:
    if x.RID == ID:
      ro = x
      return ro
  for x in croom:
    if x.RID == ID:
      ro = x
      return ro

you = Player()
bots = Player()
quests = []
qcomp = []
world = []
croom = []
data = [30,35,50,40,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
dataC = [30,35,50,40,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nextr = 0
victory = 0

yes = 0
while yes == 0:
  yuh = "saves"
  rwe = input("\n(1) New Game  (2) Load Game\nResponse: ")
  if rwe == "1":
    yes = 1
  if rwe == "2":
    nig = input("\nChoose a file:\n(1)  (2)  (3)  (4)  (5)\nFile: ")
    if nig.isdigit() == True and nig != "0":
      if int(nig) < 6:
        yuh = yuh + nig +".txt"          
      filesize = os.path.getsize(yuh)
      if filesize > 0:
        save("load",int(nig))
        worldfunction()
      else:
        print("\nThere is no save data on this file!")
    
  

world.append(World("Boss Battle Demo","Demo",-1,0))
world.append(World("Graham's Mind","Start",0,0))
world.append(World("F-Wing Hallway 1st Floor","Hall",1,0)) #80
world.append(World("FX-Wing Hallway 1st Floor","Hall",2,0)) #65
world.append(World("D-Wing Hallway 1st Floor","Hall",3,0)) #55
world.append(World("F-Wing Media Center","Camp",4,0))
world.append(World("F-Wing Hallway 2nd Floor","Hall",5,0)) #60
world.append(World("F-Wing Engineering Shop Room","Shop",6,0))
world.append(World("H-Wing Complex 1st Floor","Hall",7,45))
world.append(World("FX-Wing Hallway 2nd Floor","Hall",8,0)) ##65
world.append(World("C-Wing Hall 1st Floor","Hall",9,75))
world.append(World("D-Wing Hallway Ground Floor","Hall",10,40))
world.append(World("H-Wing Complex Ground Floor","Hall",11,50))
world.append(World("C-Wing Hall Ground Floor","Hall",12,35))
world.append(World("Main Office","Camp",13,0))
world.append(World("C-Wing Media Center","Camp",14,0))
world.append(World("B-Wing Hallway 1st Floor","Hall",15,40))
world.append(World("Main Lobby","Hall",16,60))
world.append(World("Cafe 2","Camp",17,0))
world.append(World("Automotive Building","Camp",18,0))
world.append(World("B-Wing Hallway Ground Floor","Hall",19,20))
world.append(World("Cafe 1","Camp",20,0))
world.append(World("C-Wing Nurse's Office","Camp",21,0))
world.append(World("Gymnasium","Camp",22,0))
world.append(World("Auditorium","Camp",23,0))
world.append(World("A-Wing Hallway","Hall",24,20))
world.append(World("FX-Wing Nurse's Office","Camp",25,0))
world.append(World("DB-Wing Sector","Hall",26,20))
world.append(World("Mrs. Wells's Classroom","Camp",27,0))
world.append(World("Medical Shop Room","Camp",28,0))
world.append(World("ASL Room","Camp",29,0))
world.append(World("Technology Room","Camp",30,0))
world.append(World("The Fedora Man's Lair","Lair",31,0))


for x in world:
  x.initroutes()

Ishraq = Entity("Ishraq",50,100,12,25,0,10,55,100,100,5,0,0,2,"1","Male")
Ishraq.helm = "Glasses"
Ishraq.chest = "Track Warm-Up"
Ishraq.boots = "Jays"
Ishraq.weap = ""
Ishraq.access = ""
Ishraq.genderset()
Kelly = Entity("Kelly",30,100,7,10,7,25,35,110,110,15,5,5,4,"2","Female")
Kelly.helm = "Hairband"
Kelly.chest = "School Uniform"
Kelly.boots = "Flats"
Kelly.weap = "Pen"
Kelly.access = "Agenda"
Kelly.genderset()
Julius = Entity("Julius",55,100,11,15,0,20,45,100,100,4,0,0,1,"3","Male")
Julius.helm = ""
Julius.chest = "Track Warm-Up"
Julius.boots = "Roshes"
Julius.weap = "Track Baton"
Julius.access = ""
Julius.genderset()
Daniel = Entity("Daniel",45,100,8,15,15,5,30,100,100,6,0,0,3,"4","Male")
Daniel.helm = "Glasses"
Daniel.chest = "School Uniform"
Daniel.boots = "Sneakers"
Daniel.weap = ""
Daniel.access = ""
Daniel.genderset()
Tim = Entity("Tim",40,100,9,12,10,25,50,100,100,7,0,0,2,"5","Male")
Tim.helm = "Glasses"
Tim.chest = "School Uniform"
Tim.boots = "Sneakers"
Tim.weap = "Slingshot"
Tim.access = ""
Tim.genderset()
Arwyn = Entity("Arwyn",35,100,10,5,5,15,35,100,100,10,0,0,4,"6","Male")
Arwyn.helm = "Glasses"
Arwyn.chest = "School Uniform"
Arwyn.boots = "Vans"
Arwyn.weap = "Scissors"
Arwyn.access = ""
Arwyn.genderset()
Ishraq.learnskill("Counter")
Daniel.learnskill("Grubby Hands")
Daniel.addbattleitem("Chips")
ro = rd(0)
world.remove(ro)
croom.append(ro)
you.team = [Daniel]
you.teamS = ["Daniel"]

worldfunction()