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
print(style.BOLD+"|"+style.RESET+"| |")

#Add Calligraphy accuracy effect
#Update Tremors to crit
#Update Isometric Drawings to cancel effects after death and update for SHah/Amira

class Player:
  def __init__(self):
    self.team = []
    self.teamS = []
    self.backteam = []
    self.backteamS = []
    self.deadteam = []
    self.deadteamS = []
    self.teamC = []
    self.backteamC = []
    self.deadteamC = []
    self.cteam = []
    self.cbackteam = []
    self.cdeadteam = []
    self.teamID = []
    self.supportteam = []
    self.supportteamS = []
    self.supportback = []
    self.consumeinventory = []
    self.helminventory = []
    self.chestinventory = []
    self.bootsinventory = []
    self.weaponinventory = []
    self.accessinventory = []
    self.isoinventory = []
    self.questinventory = []

class Entity:
  def __init__(self,NAME,HP,MP,AT,DF,MAT,MDF,SP,AC,EV,CT,APN,MPN,MRG,ID,GEN): 
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
    self.GEN = GEN
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
    self.head = ""
    self.body = ""
    self.lower = ""
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
    self.ak = -1
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
    self.hat = False
    self.hate = -1
    self.hatelis = []
    self.suc = -1
    self.powers = -1
    self.telep = -1
    self.mimi = -1
    self.desp = -1
    self.lifesteal = 0 #Positive Effects
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
    self.chronot = 0
    self.quenshield = False
    self.tension = 0
    self.chadwalked = 0
    self.chadlist = []
    self.duel = []
    self.duelt = 0
    self.hater = 0
    self.surge = 0
    self.teth = []
    self.tethered = []
    self.ptelepath = 0
    self.telepath = 0
    self.mimicm = 0
    self.mimit = 0
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
    self.greased = [0]
    self.deturn = 0
    #Stuns
    self.stunned = False
    self.stunimmune = False
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
    #Quest-Specific Buffs
    self.Q1B = 0 #Richard fight Enraged Ishraq 2x attack boost
    self.cry = 0 #Nurse cry timer
    #Mob Essentials
    self.turncount = 0
    self.setHP = 0
    self.tw1 = 0
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
    for x in self.Sbattleinventory:
      self.battleinventory.append(x)

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

  def Ishraqlevelup(self):
    global Colis
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
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()

  def Daniellevelup(self):
    global Colis
    broom = self.LV
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
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()

  def Juliuslevelup(self):
    global Colis
    broom = self.LV
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
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()

  def Kellylevelup(self):
    global Colis
    broom = self.LV
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
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()

  def Timlevelup(self):
    global Colis
    broom = self.LV
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
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()

  def Arwynlevelup(self):
    global Colis
    broom = self.LV
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
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()
  
  def Shahlevelup(self):
    global Colis
    broom = self.LV
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(5,5,3,3,0,0,0,0,0,0,0,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(10,5,3,2,0,0,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(10,5,3,3,0,0,0,0,0,0,0,0,0)
    if self.XP >=500 and self.LV == 4: 
      self.LV = self.LV + 1 
      self.levelstatup(20,5,3,2,5,5,0,0,5,0,0,0,0)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(15,5,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,3,3,3,1,0,0,0,0,0,0)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(15,5,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,3,3,3,3,0,0,5,2,0,0,0)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,3,5,3,3,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(25,5,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(25,5,3,4,3,3,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(25,5,3,4,3,3,0,0,5,0,0,0,0)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,3,4,3,3,1,0,0,0,0,0,0)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(30,5,5,4,3,3,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,4,4,3,3,0,0,0,0,0,0,0)
    if self.XP >=12300 and self.LV == 18: 
      self.LV = self.LV + 1 
      self.levelstatup(30,5,6,4,3,3,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.levelstatup(30,5,5,4,3,3,0,5,0,2,0,0,1)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,5,4,0,3,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,5,4,0,3,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,5,4,0,3,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,5,4,0,3,1,0,0,0,0,0,0)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,5,3,0,3,0,0,0,0,5,0,1)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,5,3,0,3,0,0,0,0,0,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,5,3,0,3,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(60,5,5,3,0,3,0,0,0,0,0,0,0)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(50,5,5,3,0,3,0,0,0,0,0,0,0)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,5,5,0,3,0,0,0,2,0,5,1)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(75,0,5,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(75,0,5,4,0,0,1,0,0,0,0,0,0)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(75,0,5,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(75,0,5,4,0,0,0,0,0,0,0,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,5,4,0,0,0,0,0,0,0,0,1)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,5,3,1,0,0,0,0,0,0,0,0)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,5,2,1,0,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(50,0,5,3,1,0,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(100,0,5,2,1,0,0,0,0,0,0,0,0)
    if broom != self.LV:
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()

  def Amiralevelup(self):
    global Colis
    broom = self.LV
    if self.XP >=50 and self.LV == 1:
      self.LV = self.LV + 1
      self.levelstatup(10,10,4,4,4,4,0,0,0,0,0,0,0)
    if self.XP >=150 and self.LV == 2:
      self.LV = self.LV + 1   
      self.levelstatup(10,10,4,4,4,4,0,0,0,0,0,0,0)
    if self.XP >=300 and self.LV == 3:
      self.LV = self.LV + 1 
      self.levelstatup(10,10,4,4,4,4,0,0,0,1,0,0,1)
    if self.XP >=500 and self.LV == 4: 
      self.LV = self.LV + 1 
      self.levelstatup(10,10,4,4,4,4,0,0,0,0,0,0,0)
    if self.XP >=750 and self.LV == 5:
      self.LV = self.LV + 1
      self.levelstatup(10,10,4,4,4,4,0,0,0,0,0,0,0)
    if self.XP >=1050 and self.LV == 6:
      self.LV = self.LV + 1 
      self.levelstatup(15,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=1400 and self.LV == 7:
      self.LV = self.LV + 1 
      self.levelstatup(15,10,2,2,2,2,1,0,0,1,0,0,1)
    if self.XP >=1800 and self.LV == 8:
      self.LV = self.LV + 1 
      self.levelstatup(15,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=2300 and self.LV == 9:
      self.LV = self.LV + 1 
      self.levelstatup(15,10,2,2,2,2,0,0,0,0,3,3,0)
    if self.XP >=2900 and self.LV == 10:
      self.LV = self.LV + 1 
      self.levelstatup(15,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=3600 and self.LV == 11:
      self.LV = self.LV + 1
      self.levelstatup(25,10,2,2,2,2,0,0,0,1,0,0,1)
    if self.XP >=4400 and self.LV == 12:
      self.LV = self.LV + 1 
      self.levelstatup(20,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=5300 and self.LV == 13:
      self.LV = self.LV + 1
      self.levelstatup(20,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=6300 and self.LV == 14:
      self.LV = self.LV + 1 
      self.levelstatup(20,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=7500 and self.LV == 15:
      self.LV = self.LV + 1 
      self.levelstatup(20,10,2,2,2,2,1,0,0,1,0,0,1)
    if self.XP >=8900 and self.LV == 16:
      self.LV = self.LV + 1
      self.levelstatup(20,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=10500 and self.LV == 17:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=12300 and self.LV == 18: 
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=14300 and self.LV == 19:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,2,2,2,0,0,0,1,2,2,1)
    if self.XP >=16550 and self.LV == 20:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=19050 and self.LV == 21:
      self.LV = self.LV + 1 
      self.levelstatup(40,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=21800 and self.LV == 22:
      self.LV = self.LV + 1 
      self.levelstatup(75,10,2,2,2,2,0,0,0,0,0,0,0)  
    if self.XP >=24800 and self.LV == 23:
      self.LV = self.LV + 1 
      self.levelstatup(75,10,2,2,2,2,1,0,0,1,0,0,1)
    if self.XP >=28050 and self.LV == 24:
      self.LV = self.LV + 1 
      self.levelstatup(75,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=31550 and self.LV == 25:
      self.LV = self.LV + 1 
      self.levelstatup(75,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=35300 and self.LV == 26:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,2,2,2,0,0,0,0,0,0,0)
    if self.XP >=39300 and self.LV == 27:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,1,1,1,1,0,0,0,1,0,0,1)
    if self.XP >=43550 and self.LV == 28:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,1,1,1,1,0,0,0,0,0,0,0)
    if self.XP >=48050 and self.LV == 29:
      self.LV = self.LV + 1 
      self.levelstatup(50,20,1,1,1,1,0,0,0,0,3,3,0)
    if self.XP >=52800 and self.LV == 30:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=57800 and self.LV == 31:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,3,3,3,3,1,0,0,1,0,0,1)
    if self.XP >=63050 and self.LV == 32:
      self.LV = self.LV + 1
      self.levelstatup(50,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=68550 and self.LV == 33:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=74300 and self.LV == 34:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,3,3,3,3,0,0,0,0,0,0,0)
    if self.XP >=80300 and self.LV == 35:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,1,1,1,1,0,0,0,1,0,0,1)
    if self.XP >=86550 and self.LV == 36:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,1,1,1,1,0,0,0,0,0,0,0)
    if self.XP >=93100 and self.LV == 37:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,1,1,1,1,0,0,0,0,0,0,0)
    if self.XP >=100000 and self.LV == 38:
      self.LV = self.LV + 1 
      self.levelstatup(50,10,2,2,2,2,0,0,0,0,0,0,0)
    if broom != self.LV:
      self.cHP = self.HP
      self.cMP = self.MP
      levelgap = self.LV-broom
      if Colis != True:
        for x in range(levelgap):
          broom = broom + 1
          print("")
          print(self.NAME,"levels up to level",str(broom)+"!")
          input()

  def Isopower(self,al,EW=False):
    if EW == True:
      self.skills.insert(0,"Runner's High")
      self.shi = self.shi - 3
      self.ISOmode = False
    else:
      if self.ISOmode == True:
        if self.cHP > 0:
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
            if self.cHP > 0:
              al.teamS.remove(self.NAME)
              self.NAME = "Daniel"
              al.teamS.append(self.NAME)
            self.skills.insert(4,"Enlargen")
            self.skills.remove("Grubby Tides")
            self.skills.insert(0,"Grubby Hands")
            self.jabb = self.jabb - 3
          if self.NAME == "Taco Lord":
            if self.cHP > 0:
              al.teamS.remove(self.NAME)
              self.NAME = "Tim"
              al.teamS.append(self.NAME)
            self.skills.remove("Taco Tuesday")
            self.da = self.da - 3
          if self.NAME == "Arwyn":
            self.fromthes = self.fromthes - 3
          if self.NAME == "Amira":
            self.powers = self.powers - 3
            self.mimit = 0
          if self.NAME == "Shad":
            if self.cHP > 0:
              al.teamS.remove(self.NAME)
              self.NAME = "Shah"
              al.teamS.append(self.NAME)
            self.armw = self.armw - 3
            self.skills.remove("Sick Pump")
            self.skills.insert(0,"Progressive Overload")
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
    if skillname == "From the Shadows":
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
    if skillname == "Protobelt":
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

    #Normal effect

    if self.chronot > 0:
      for x in enemy.team:
        if self in x.chronoslow:
          self.pSP = self.pSP * (0.9-(0.05*x.chrono))
    
    if len(self.chronoslow) > 0:
      boost = 0
      for x in self.chronoslow:
        if x.chronot > 0:
          boost = boost + ((0.1+(0.05*self.chrono))*x.SP)
        else:
          self.chronoslow.remove(x)
      self.fSP = self.fSP + boost

    #if len(self.teth) > 0:
      #split = (0.1+(0.05*self.powers))
      #people = len(self.teth)
      #dsplit = split/people
      #for x in self.teth:
       # self.fAT = self.fAT + (dsplit*x.AT)
       # self.fMAT = self.fMAT + (dsplit*x.MAT)

   # if len(self.tethered) > 0:
      #split = (0.1+(0.05*self.tethered[0].powers))
      #people = len(self.tethered[0].teth)
      #dsplit = split/people
      #self.pAT = self.pAT * (1-dsplit)
      #self.pMAT = self.pMAT * (1-dsplit)

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
        self.pAT = self.pAT * (1-dsplit)
        self.pMAT = self.pMAT * (1-dsplit)
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
      self.pSP = self.pSP *0.75

    if self.poisont >0:   #On Turn Debuff
      self.pDF = self.pDF *0.75
      self.pMDF = self.pMDF* 0.75

    if self.fear > 0:
      self.dmgreduct = self.dmgreduct * 1.25
      self.pAT = self.pAT * 0.75
      self.pMAT = self.pMAT * 0.75

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
        self.pAT = self.pAT * 1.55
        self.pDF = self.pDF * 1.55
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
      elif self.NAME == "Shah":
        self.pMAT = self.pMAT * 1.2
        self.pDF = self.pDF * 1.5
        self.pMDF = self.pMDF * 1.4
        self.pSP = self.pSP * 1.2
        self.pAPN = self.pAPN * 1.5
        self.pAC = self.pAC * 1.2
      elif self.NAME == "Amira":
        self.pAT = self.pAT * 1.1
        self.pMAT = self.pMAT * 1.1
        self.dmgreduct = self.dmgreduct * 0.8
        self.pEV = self.pEV * 1.5
        self.pCT = self.pCT * 1.5
        self.pMRG = self.pMRG * 2
        self.pMPN = self.pMPN * 2

    if self.WI == True:    #Permanent Passive
      self.pAT = self.pAT * (1.15 + (0.025*self.wild))
      self.pSP = self.pSP * (1.35 + (0.05*self.wild))
      self.fEV = self.fEV + (30 + (5*self.wild))
      self.fCT = self.fCT + (30 + (5*self.wild))
      self.pMAT = self.pMAT * 0.8 
      self.pMDF = self.pMDF * 0.8
      self.fAC = self.fAC - 20

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

    if self.pbarrier > 0:   #On hit buff
      self.fDF = self.fDF + 100000
      self.pDF = self.pDF * 100
      
    if self.manaflow[0] > 0:   #On turn buff 
      self.pMRG = self.pMRG * (2 + (0.5*self.manaflow[1].asm))

    if self.runhigh > 0:    #Global buff
      self.pAT = self.pAT * (1.3+(0.05*self.run))
      self.pDF = self.pDF * (1.4+(0.05*self.run))
      
    if self.tremsl > 0:    #Global debuff
      self.pSP = self.pSP * 0.5

    if self.greased[0] > 0:    #On hit debuff   
      self.fEV = self.fEV - (20+(5*self.greased[1].grub))

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
      self.pEV = self.pEV * 100
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
      self.fAT = self.fAT + ((0.02+(0.005*self.bonded[1].knightv))*self.bonded[1].HP)
      self.fMAT = self.fMAT + ((0.02+(0.005*self.bonded[1].knightv))*self.bonded[1].HP)

    if self.tension > 0:
      self.pAT = self.pAT * ((1.5+(0.05*self.progo))+((0.5+(0.05*self.progo))*self.tension))
      if self.tension >= 3:
        self.pAC = self.pAC * (1.6 + (0.1*self.progo))
        self.fAPN = self.fAPN + (50 + (12.5*self.progo))

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

    for x in ally.team: 
      if len(x.chadlist) > 0:
        if self in x.chadlist:
          if self == x.chadlist[0]:
            self.fCT = self.fCT + (40 + (12.5*self.chad))
          else:
            self.fCT = self.fCT + 40
          self.CTdmg = self.CTdmg + (0.1 + ((0.15/4)*self.chad))

    if self.Q1B > 0:
      self.pAT = self.pAT*2

    if self.giantess > 0:
      self.pAT = self.pAT * 4
      self.fEV = self.fEV - 100
      self.pMAT = self.pMAT * 0.25

    if self.NAME == "Amira" and self.ID !="8":
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
      if self.cHP <= (0.2*self.HP):
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
              x.cHP = x.HP
          for x in player2.deadteam:
            x.cHP = x.HP
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

    if self.talkEN > 0:
      self.fEV = self.fEV + 100000
      self.pEV = self.pEV * 100
    
    if self.candyAC > 0:
      self.pAC = self.pAC * 0
    
    if self.cry > 0:
      self.fEV = self.fEV - 40
      self.fSP = self.fSP - 15
    
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

    if self.rages[0] >0:
      self.rages[0] = self.rages[0] - 1
      if self.rages[0] == 0:
        time.sleep(0.5)
        print("\nThe flames cease to rage across the battlefield!")
        for x in allfighters:
          x.rages = [0]
          x.burnt = 0

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

      if self.NAME == "Amira" and self.resil == 1 and self.ID !="8":
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
        dmg = round(2*self.cMAT)
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
        dmg = round(2*self.cMAT)
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

      if self in ene.hatelis and ene.hat == True:
        ene.cAPN = round(ene.cAPN/(1.4+(0.4*ene.hate)))
        ene.cMPN = round(ene.cMPN/(1.4+(0.4*ene.hate)))
        
  def prehiteffects(self,ene):
    global sett
    global player1
    global player2

    if ene.hat == True: 
      self.hater = 2
      if self not in ene.hatelis:
        ene.hatelis.append(self)
      ene.cMP = ene.cMP + ene.cMRG
      if ene.cMP > ene.MP:
        ene.cMP = ene.MP

    if self.hat == True and ene in self.hatelis:
      self.cAPN = round(self.cAPN * (1.4+(0.4*self.hate)))
      self.cMPN = round(self.cMPN * (1.4+(0.4*self.hate)))

    if (len(self.duel) >0 and ene not in self.duel) or (len(ene.duel)>0 and self not in ene.duel):
      self.cAT = 0
      self.cMAT = 0
    
    if (len(self.duel) > 0 and ene in self.duel) or (len(self.duel)<=0 and len(ene.duel) <=0):
      if self in player1.team:
        self.currentstats(player1,player2)
        ene.currentstats(player2,player1)
      elif self in player2.team:
        self.currentstats(player2,player1)
        ene.currentstats(player1,player2)
      
  def onhittimersoffense(self,ene,timer,mr=""):
    global sett
    global player1
    global player2

    if self.lifesteal > 0:
      if (sett-ene.cHP) >0 and round(self.lifesteal*(sett-ene.cHP)) >0:
        butt = self.cHP 
        self.cHP = self.cHP + round(self.lifesteal*(sett-ene.cHP))
        if self.cHP > self.HP:
          self.cHP = self.HP
        time.sleep(timer)
        print("\n" + self.NAME,"heals for",fore.MEDIUM_SPRING_GREEN + str(self.cHP-butt) + style.RESET,"health! They now have",self.cHP,"health!")

    if self.chronotime > 0:
      self.prehiteffects(ene)
      sett = ene.cHP
      if ene.cHP >0:
        dmg = round((1+(0.2*self.chrono))*self.cMAT)
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
        dmg = round((0.6+(0.1*self.fromthes))*self.cMAT)
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
          if ene.cHP <= 0:     
            ene.purge("Death",player1,player2)
            player1.team.remove(ene)
            player1.teamID.remove(ene.ID)
            player1.teamS.remove(ene.NAME)
            player1.deadteam.append(ene)
            player1.deadteamS.append(ene.NAME)
          else:
            ene.currentstats(player1,player2)
        elif ene in player2.team:
          if ene.cHP <= 0: 
            ene.purge("Death",player2,player1)
            player2.team.remove(ene)
            player2.teamID.remove(ene.ID)
            player2.teamS.remove(ene.NAME)
            player2.deadteam.append(ene)
            player2.deadteamS.append(ene.NAME)
          else:
            ene.currentstats(player2,player1)

    if self.mvolley == 3:
      self.mvolley = 0
      time.sleep(timer)
      print("\n"+self.NAME+"'s accumulated power discharges three balls of light!")
      for x in range(3):
        for y in player1.team:
          if y.cHP <= 0:
            y.purge("Death",player1,player2)
            player1.team.remove(y)
            player1.teamID.remove(y.ID)
            player1.teamS.remove(y.NAME)
            player1.deadteam.append(y)
            player1.deadteamS.append(y.NAME)
          else:
            y.currentstats(player1,player2)
        time.sleep(timer/4)
        if len(player1.team) > 0:
          targ = random.choice(player1.team)
          if len(self.duel) > 0:
            if self.duel[1] in player1.team:
              targ = self.duel[1]
          elif len(self.taunted) > 0:
            if self.taunted[1] in player1.team:
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
          dmg = round((1.5+(0.25*self.telep))*self.cMAT)
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
        dmg = round((1.5+(0.25*self.telep))*self.cMAT)
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

    if self.WI == True:
      sett = self.cHP
      self.cHP = self.cHP - round(0.025*self.HP)
      time.sleep(0.2)
      if self.cHP <=0:
        self.WI = False
        self.cHP = 1
        print("\n"+self.NAME,"loses",(sett-self.cHP),"health from his wild instincts! He is at critical health, exiting wild instinct!")
      else:
        print("\n"+self.NAME,"loses",(sett-self.cHP),"health from his wild instincts! He has",self.cHP,"health now!")

    if self.immortal > 0:
      self.immortal = self.immortal - 1
      if self.immortal == 0:
        time.sleep(0.5)
        print("\n" + self.NAME,"is mortal again!")

    if self.OB == True:
      sett = self.cHP
      self.cHP = self.cHP + round((0.03+(0.01*self.obese))*self.HP)
      if self.cHP > self.HP:
        self.cHP = self.HP
      time.sleep(0.3)
      print("\n" +self.NAME+ "'s self-sustainability heals him for",fore.MEDIUM_SPRING_GREEN + str(self.cHP-sett) + style.RESET,"health! He has",self.cHP,"health now!")

    if self.scirc > 0:
      self.scirc = self.scirc - 1
      if self.scirc == 1:
        print("\n"+self.NAME,"is about to short circuit!")
      if self.scirc == 0:
        self.cHP = 0
        print("\n"+self.NAME,"short circuits and dies!")

    if self.burnt > 0:
      sett = self.cHP
      if len(self.rages) > 1:
        if self.rages[1] in enemy.team:
          self.burnd = self.burnd + ((0.1*(22-self.rages[1].rages[0]))*self.rages[1].cMAT)
      self.cHP = self.cHP - round(self.burnd * (1-(self.cMDF/(self.cMDF+100))))
      if len(self.rages) > 1:
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
        if self.rages[0] > 0 and self.burnt <=0 and self.rages[1] != self:
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

    if self.chadwalked > 0:
      self.chadwalked = self.chadwalked - 1
      if self.chadwalked == 0:
        time.sleep(0.5)
        print("\nThe battle is no longer affected by the chadness of",self.NAME+".")
        self.chadlist = []

    if self.duelt > 0:
      self.duelt = self.duelt - 1
      if self.duelt == 0:
        time.sleep(0.2)
        print("\n"+self.NAME,"exits his arm-wrestling match!")
        for x in allfighters:
          if len(x.duel) > 0:
            if self == x.duel[1]:
              x.duel = []
        self.duel = []

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
        print("\n"+self.NAME,"turns back to his normal self, exiting Enlargen!")
        if self.jabbaroll > 0:
          self.jabbaroll = 0

    if self.knightb > 0:
      self.knightb = self.knightb - 1
      if self.knightb == 0:
        time.sleep(0.3)
        print("\n" + self.NAME,"is unbinded from his ally!")
        for x in ally.team:
          if len(x.bonded) > 0:
            if self == x.bonded[1]:
              x.bonded = []

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
        print("\n"+self.NAME+"'s tethers release from all enemies!")
        self.teth = []
        for x in enemy.team:
          if self in x.tethered:
            x.tethered.remove(self)

    if self.giantess > 0:
      self.giantess = self.giantess - 1
      if self.giantess == 0:
        time.sleep(0.3)
        print("\n" + self.NAME,"is back to her normal size!")

    if self.candyAC > 0:
      self.candyAC = self.candyAC - 1
      if self.candyAC == 0:
        time.sleep(0.2)
        print("\n"+self.NAME+"'s accuracy is no longer being reduced by the chocolate bar!")

  def stuns(self):
    global bad
    self.stunned = False
    if self.stunimmune == 1:
      if self.dance > 0 or self.sparkstun > 0 or self.tremstun >0 or self.rooted > 0:
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
        allf = allfighters
        for x in allf:
          if x.cHP <= 0:
            allf.remove(x)
          if x.invis > 0 and x.cHP >0 and x in allf:
            allf.remove(x)
        att = random.choice(allf)
        print("\n"+self.NAME,"is dancing uncontrollably, attacking a random target!")
        self.attack(att)
      elif self.confused > 0:
        time.sleep(0.5)
        self.confused = self.confused - 1
        self.stunned = True
        allf = allfighters
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
                for x in enemy.team:
                  if x.ID in enemy.teamID and x.invis <=0:
                    self.zanslash(x)
            if bad == False:
              uga = 1
        self.stunned = True
        
        
  def currentstats(self,ally,enemy):
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
    self.CTdmg = 2
    self.pAPN = 1.00
    self.pMPN = 1.00
    self.pMRG = 1.00
    self.lifesteal = 0
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
    global CI
    global lastat
    self.tensionattack = True
    self.prehiteffects(enemy)
    CI = False
    redat = (.48+(0.03*enemy.counte))*self.cAT
    pat = (1-(.48+(0.03*enemy.counte)))*self.cAT
    sett = enemy.cHP
    selfsett = self.cHP
    self.cMP = self.cMP + self.cMRG
    if self.cMP > self.MP:
      self.cMP = self.MP 
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
        enemy.specialdodgecases(self,0.5,"Physical Melee")
      else:
        time.sleep(1)
        if enemy.NAME == "Note Packet":
          print("\n"+self.NAME,"picks up the Note Packet!")
          enemy.cHP = 0
        else:
          if random.randint(1,100) <= self.cCT:
            if enemy.coun == True:
              enemy.counter(self) 
            if CI == True and self.cDF <=0:
              self.cHP = self.cHP - round(self.CTdmg*redat*self.dmgreduct)
              if self.cHP >0:            
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-self.cHP) + style.RESET,"critical damage!",self.NAME,"has",self.cHP,"health remaining!")
              else:
                self.cHP = 1
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-self.cHP) + style.RESET,"critical damage!",self.NAME,"is at critical health!")
              time.sleep(0.5)
            elif CI == True and self.cDF > 0:
              self.cHP = self.cHP - round(self.dmgreduct*self.CTdmg*(redat * (1-((self.cDF)/(self.cDF+100)))))
              if self.cHP > 0:
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-self.cHP) + style.RESET,"critical damage!",self.NAME,"has",self.cHP,"health remaining!")
              else:
                self.cHP = 1
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-self.cHP) + style.RESET,"critical damage!",self.NAME,"is at critical health!")
              time.sleep(0.5)
            if CI == True:
              dmg = round(self.CTdmg*pat)
              enemy.defense(self,"Physical",dmg)       
            else: 
              dmg = round(self.CTdmg*self.cAT)
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
            if enemy.coun == True:
              enemy.counter(self) 
            if CI == True and self.cDF <=0:
              self.cHP = self.cHP - round(redat*self.dmgreduct)
              if self.cHP > 0:
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-self.cHP) + style.RESET,"damage!",self.NAME,"has",self.cHP,"health remaining!")
              else:
                self.cHP = 1
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-self.cHP) + style.RESET,"damage!",self.NAME,"is at critical health!")
              time.sleep(0.5)
            elif CI == True and self.cDF >0:
              self.cHP = self.cHP - round(self.dmgreduct * redat * (1-((self.cDF)/(self.cDF+100))))
              if self.cHP > 0:
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-self.cHP) + style.RESET,"damage!",self.NAME,"has",self.cHP,"health remaining!")
              else:
                self.cHP = 1
                print("\n" + enemy.NAME, "counters",self.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-self.cHP) + style.RESET,"damage!",self.NAME,"is at critical health!")
              time.sleep(0.5)
            if CI == True:
              dmg = round(pat)
              enemy.defense(self,"Physical",dmg)   
            else: 
              dmg = round(self.cAT)
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

  def specialdodgecases(self,enemy,timer,mr=""):
    global sett
    global player1
    global player2

    if self.coun == True:
      redat = (.48+(0.03*self.counte))*enemy.cAT
      selfsett = enemy.cHP
      time.sleep(timer)
      if random.randint(1,100) <= enemy.cCT:
        if enemy.cDF <=0:
          enemy.cHP = enemy.cHP - round(enemy.CTdmg*redat*enemy.dmgreduct)
          if enemy.cHP >0:            
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            enemy.cHP = 1
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"is at critical health!")
        elif enemy.cDF >0:
          enemy.cHP = enemy.cHP - round(enemy.dmgreduct*enemy.CTdmg*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
          if enemy.cHP > 0:
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            enemy.cHP = 1
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + style.BOLD + str(selfsett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"is at critical health!")
      else:
        if enemy.cDF <=0:
          enemy.cHP = enemy.cHP - round(redat*enemy.dmgreduct)
          if enemy.cHP >0:            
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            enemy.cHP = 1
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")
        elif enemy.cDF >0:
          enemy.cHP = enemy.cHP - round(enemy.dmgreduct*enemy.CTdmg*(redat * (1-((enemy.cDF)/(enemy.cDF+100)))))
          if enemy.cHP > 0:
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            enemy.cHP = 1
            print("\n" + self.NAME, "counters",enemy.NAME +", redirecting",fore.ORANGE_1 + str(selfsett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"is at critical health!")

    if self.NAME == "Amira" and self.ID != "8":
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

    if self.NAME == "Amira" and self.cHP <= round(0.2*self.HP) and self.ID != "8":
      self.onhittimersdefense(enemy,timer)
     
    if self.safety > 0:
      self.safety = self.safety - 1

    if enemy.tension > 0 and enemy.tensionattack == True:
      enemy.tensionattack = False
      enemy.tension = 0
      time.sleep(timer)
      print("\n"+enemy.NAME,"releases all tension!")

    if self.hater > 0 and enemy.hat == True:
      enemy.cAPN = round(enemy.cAPN/(1.4+(0.4*enemy.hate)))
      enemy.cMPN = round(enemy.cMPN/(1.4+(0.4*enemy.hate)))

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
          print(fore.SKY_BLUE_1+"\nIt's",self.NAME+"'s turn." + style.RESET)
        else:
          print("\nIt's",self.NAME+"'s turn.")
        if self.isomode == True and self.isopoints >= 100 and self.ISOmode == False:
          fight = input(fore.GREY_100 + "Attack, Skills, Items, Recover, Check, Support, or Transform? " + style.RESET)
        else:
          fight = input(fore.GREY_100 + "Attack, Skills, Items, Recover, Check, or Support? " + style.RESET)
        if fight == "1" or fight.lower() == "attack":
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
                  if x.ID in enemy.teamID and x.invis <=0:
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
                  if x.ID in enemy.teamID and x.invis <=0:
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
          self.inventorysystem(self,ally,enemy)
          if bad == True:
            continue
          seq = 1
        elif fight == "4" or fight.lower() == "recover":
          buttsss = self.cMP
          time.sleep(1)
          self.cMP = self.cMP + (2*self.cMRG)
          if self.cMP > self.MP:
            self.cMP = self.MP 
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
              self.immortal = 4
              self.counte = self.counte + 3
              self.enragev = 1 + (1-(self.cHP/self.HP))
            elif self.NAME == "Julius":
              if self.NAME == "Julius":
                input(fore.GREEN_1+"\nJulius: Iso...Iso..."+style.RESET)
                input(fore.GREEN_1+style.BOLD +"Julius: ISOOOMETRIC DRRAAAA-AWWWIINGSS!!"+style.RESET)
              else:
                input(fore.GREEN_1+"\nIan: Minecraft?"+style.RESET)
                input(fore.GREEN_1+style.BOLD +"Ian: MMMIIIIINNNNEEECRAAAFTTT!!!"+style.RESET)
              sett = self.cHP
              self.cHP = self.cHP + round(0.2*self.HP)
              self.skills.remove("Runner's High")
              self.runhigh = 0
              self.shi = self.shi + 3
              if self.cHP > self.HP:
                self.cHP = self.HP
            elif self.NAME == "Kelly":
              input(fore.MAGENTA_1 + "\nKelly: Excuse me?"+style.RESET)
              input(fore.MAGENTA_1 + style.BOLD +"Kelly: I'm grading you."+style.RESET)
              self.perfectr = self.perfectr + 3
              self.skills.remove("Heal")
              self.skills.insert(3,"Omniheal")
              sett = self.cMP
              self.cMP = self.cMP + round(0.4*self.MP)
              if self.cMP > self.MP:
                self.cMP = self.MP
            elif self.NAME == "Daniel":
              input(fore.YELLOW_1 + "\nDaniel: I..."+style.RESET)
              input(fore.YELLOW_1 +style.BOLD+ "Daniel: LIKE MEN!!!"+style.RESET)
              self.skills.remove("Enlargen")
              self.skills.remove("Grubby Hands")
              self.skills.insert(0,"Grubby Tides")
              self.thehut = (self.isopoints/100)+1
              self.jabbaroll = 1
              for x in enemy.team:
                if x.fear <4:
                  x.fear = 4
            elif self.NAME == "Tim":
              input(fore.CYAN_1 + "\nTim: It's raining tacos...!!!"+style.RESET)
              input(fore.CYAN_1 + style.BOLD + "Taco Lord: FROM OUTTAA THE SKIES! TACOS..DON'T NEED TO ASK WHY!!"+style.RESET)
              ally.teamS.remove("Tim")
              ally.teamS.append("Taco Lord")
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
                x.dark = 16
            elif self.NAME == "Shah":
              input(fore.ORANGE_RED_1+"\nShah: Awggh, yeah.")
              input(style.BOLD+"Shad: Just got back from the gym."+style.RESET)
              self.armw = self.armw + 3
              self.skills.remove("Progressive Overload")
              self.skills.insert(0,"Sick Pump")
              ally.teamS.remove("Shah")
              ally.teamS.append("Shad")
              self.NAME = "Shad"
              if self.tension == 3:
                self.tension = 4
              elif self.tension < 3:
                self.tension = 3
            elif self.NAME == "Amira":
              input(fore.SKY_BLUE_1+"\nAmira: Haters only make me stronger."+style.RESET)
              input(fore.SKY_BLUE_1+style.BOLD+"Amira: Farewell."+style.RESET)
              self.powers = self.powers + 3
              self.mimit = 1
              for x in enemy.team:
                x.hater = 2
                if x not in self.hatelis:
                  self.hatelis.append(x)
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
            if self.NAME == "Shad":
              if self.tension == 3:
                print("\n"+self.NAME,"does a sick pump, tension boosting to max!")
              else:
                print("\n"+self.NAME,"does the most chad pump, tension boosting beyond max!")
            if self.NAME == "Amira":
              print("\n"+self.NAME,"declares everyone as her haters, applying the haters debuff to all enemies!")
            self.ISOmode = True
            for x in ally.team:
              x.currentstats(ally,enemy)
            for x in enemy.team:
              x.currentstats(enemy,ally)
              

  def check(self,ally):
    print("\n"+ally.NAME+"'s Current Stats:\nHP:",str(ally.cHP)+"/"+str(ally.HP)+"\nMP:",str(ally.cMP)+"/"+str(ally.MP)+"\nMRG:",str(ally.cMRG)+"\nAT:",str(ally.cAT)+"\nDF:",str(ally.cDF)+"\nMAT:",str(ally.cMAT)+"\nMDF:",str(ally.cMDF),"\nSP:",str(ally.cSP)+"\nAC:",str(ally.cAC)+"\nEV:",str(ally.cEV)+"\nCT:",str(ally.cCT)+"\nAPN:",str(ally.cAPN)+"\nMPN:",str(ally.cMPN))
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
              if x.ID in enemy.teamID and x.invis <=0:
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
    elif skill == "From the Shadows":
      self.allyskillscost("From the Shadows",75,"Ultra")
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
          self.target(self.revive,ally.deadteam,ally.teamS,al=ally)
    elif skill == "Runner's High":
      self.allyskillscost("Runner's High",30,"Basic")
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
                self.dab(x)
    elif skill == "Protobelt":
      self.allyskillscost("Protobelt",35,"Mega")
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
      self.allyskillscost("Chronopower",30,"Mega")
      if bad != True:
        self.chronopower()
    elif skill == "Rubix Cube":
      self.allyskillscost("Rubix Cube",75,"Ultra")
      if bad != True:
        self.rubixcube(enemy)
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
                if x.ID in enemy.teamID and x.invis <=0:
                  self.mimic(x,ally,enemy)
        else:
          bad = True
      else:
        self.mimic(al=ally,targ=enemy)
    elif skill == "Desperation":
      self.allyskillscost("Desperation",50,"Mega")
      if bad != True:
        self.desperation(ally,enemy)
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
              if x.ID in enemy.teamID and x.invis <=0:
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
      self.lastattack = skill
      lastat = skill
  
  def allyskillscost(self,skill,cost,level):
    global bad
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
        if cost > round(self.MP*(0.5-(0.05*self.mimi))):
          if self.cMP < cost:
            print("\n" + self.NAME, "does not have enough mana! She needs",cost,"mana to cast!")
            bad = True
        elif cost < round(self.MP*(0.5-(0.05*self.mimi))):
          if self.cMP < round(self.MP*(0.5-(0.05*self.mimi))):
            print("\n" + self.NAME, "does not have enough mana! She needs",round(self.MP*(0.5-(0.05*self.mimi))),"mana to cast!")
            bad = True
    else:
      if self.cMP < cost:
        if self.NAME == "Kelly":
          print("\n" + self.NAME, "does not have enough mana! She needs",cost,"mana to cast!")
        else:
          print("\n" + self.NAME, "does not have enough mana! He needs",cost,"mana to cast!")
        bad = True

  def inventorysystem(self,targ,tea,ene):
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
          self.itemcatalog(check,targ,tea,ene)
          wop = 1
      for x in self.battleinventory:
        if it.lower() == x.lower():
          self.itemcatalog(x,targ,tea,ene) 
          wop = 1
    if wop == 0:
      bad = True

  def equipcatalog(self,item1,item2,sec):
    #dHP = stat[0]
    #dMP = stat[1]
    #dMRG = stat[2]
    #dAT = stat[3]
    #dDF = stat[4]
    #dMAT = stat[5]
    #dMDF = stat[6]
    #dSP = stat[7]
    #dAC = stat[8]
    #dEV = stat[9]
    #dCT = stat[10]
    #dAPN = stat[11]
    #dMPN = stat[12]
    no = 0
    stat = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    eff = ""

    if item1 == "Pencil":   #Weapons
      stat[3] = stat[3] - 1
      stat[10] = stat[10] - 2
      stat[11] = stat[11] - 2
    elif item1 == "Ruler":
      stat[3] = stat[3] - 3
      stat[2] = stat[2] - 1
    elif item1 == "Keyboard":
      stat[3] = stat[3] - 4

    if item2 == "Pencil":   #Weapons
      stat[3] = stat[3] + 1
      stat[10] = stat[10] + 2
      stat[11] = stat[11] + 2
    elif item2 == "Ruler":
      stat[3] = stat[3] + 3
      stat[2] = stat[2] + 1
    elif item2 == "Keyboard":
      stat[3] = stat[3] + 4
    if item2 != "":
      print("\nStat Changes from equipping",item2+":")
    else:
      print("\nStat Changes from de-equipping",item1+":")
    if stat[0] != 0:
      print("HP:",self.HP,"->",(self.HP+stat[0]))
    if stat[1] != 0:
      print("MP:",self.MP,"->",(self.MP+stat[1]))
    if stat[2] != 0:
      print("MRG:",self.MRG,"->",(self.MRG+stat[2]))
    if stat[3] != 0:
      print("AT:",self.AT,"->",(self.AT+stat[3]))
    if stat[4] != 0:
      print("DF:",self.DF,"->",(self.DF+stat[4]))
    if stat[5] != 0:
      print("MAT:",self.MAT,"->",(self.MAT+stat[5]))
    if stat[6] != 0:
      print("MDF:",self.MDF,"->",(self.MDF+stat[6]))
    if stat[7] != 0:
      print("SP:",self.SP,"->",(self.SP+stat[7]))
    if stat[8] != 0:
      print("AC:",self.AC,"->",(self.AC+stat[8]))
    if stat[9] != 0:
      print("EV:",self.EV,"->",(self.EV+stat[9]))
    if stat[10] != 0:
      print("CT:",self.CT,"->",(self.CT+stat[10]))
    if stat[11] != 0:
      print("APN:",self.APN,"->",(self.APN+stat[11]))
    if stat[12] != 0:
      print("MPN:",self.MPN,"->",(self.MPN+stat[12]))
    if eff != "":
      print("\n"+eff)
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
        self.HP = self.HP + stat[0]
        self.MP = self.MP + stat[1]
        self.MRG = self.MRG + stat[2]
        self.AT = self.AT + stat[3]
        self.DF = self.DF + stat[4]
        self.MAT = self.MAT + stat[5]
        self.MDF = self.MDF + stat[6]
        self.SP = self.SP + stat[7]
        self.AC = self.AC + stat[8]
        self.EV = self.EV + stat[9]
        self.CT = self.CT + stat[10]
        self.APN = self.APN + stat[11]
        self.MPN = self.MPN + stat[12]
        if item2 != "":
          sec.remove(item2)
        if item1 != "":
          sec.append(item1)
        if sec == you.weaponinventory:
          self.weap = item2
        elif sec == you.helminventory:
          self.head = item2
        elif sec == you.chestinventory:
          self.body = item2
        elif sec == you.bootsinventory:
          self.lower = item2
        elif sec == you.accessinventory:
          self.access = item2
        no = 1
      if choi == "2" or choi.lower() == "no":
        no = 1
    

  def addbattleitem(self,Item):
    self.battleinventory.append(Item)

  def itemcatalog(self,item,targ,tea,ene):
    if item == "Chips":
      sett = targ.cHP
      targ.cHP = targ.cHP + 10
      if targ.cHP > targ.HP:
        targ.cHP = targ.HP
      time.sleep(1)
      print("\n"+targ.NAME,"eats chips, recovering",fore.MEDIUM_SPRING_GREEN+str(targ.cHP-sett)+style.RESET,"health!",targ.NAME,"has",targ.cHP,"health now!")
    if item == "Taco":
      sett = targ.cHP
      targ.cHP = targ.cHP + round(0.25*self.HP)
      if targ.cHP > targ.HP:
        targ.cHP = targ.HP
      targ.purge("Cleanse",tea,ene)
      time.sleep(1)
      print("\n"+targ.NAME,"eats Tim's taco, recovering",fore.MEDIUM_SPRING_GREEN+str(targ.cHP-sett)+style.RESET,"health and cleansing them!",targ.NAME,"has",targ.cHP,"health now!")
    if item == "Bandages":
      sett = targ.cHP
      targ.cHP = targ.cHP + 10
      if targ.cHP > targ.HP:
        targ.cHP = targ.HP
      time.sleep(1)
      print("\n"+targ.NAME,"wraps themselves with bandages, recovering",fore.MEDIUM_SPRING_GREEN+str(targ.cHP-sett)+style.RESET,"health!",targ.NAME,"has",targ.cHP,"health now!")
    if item == "Med-Kit":
      sett = targ.cHP
      targ.cHP = targ.cHP + 40
      if targ.cHP > targ.HP:
        targ.cHP = targ.HP
      time.sleep(1)
      print("\n"+targ.NAME,"uses a med-kit, recovering",fore.MEDIUM_SPRING_GREEN+str(targ.cHP-sett)+style.RESET,"health!",targ.NAME,"has",targ.cHP,"health now!")
    self.battleinventory.remove(item)


  def supportsystem(self,ally,enemy):
    global bad
    global player1
    wop = 0
    bad = False
    if len(player1.supportteam) == 0:
      print("\nYou do not have any support allies!")
    else:
      print("")
      print(player1.supportteamS)
      it = input(fore.GREY_100 + "Call who? " + style.RESET)
      if it.isdigit() == True and it != "0":
        if len(player1.supportteam) > (int(it)-1):
          check = player1.supportteam[(int(it)-1)]
          self.supportcatalog(check,ally,enemy)
          wop = 1
      for x in player1.supportteam:
        if it.lower() == x.name.lower():
          self.supportcatalog(x,ally,enemy) 
          wop = 1
    if wop == 0:
      bad = True

  def supportcatalog(self,per,ally,enemy):
    global bad

    if per.name == "Brandon":
      if per.ccd > 0:
        print("\nBrandon is on cooldown!")
        bad = True
      else:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.brandonroot,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to root!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and x.invis <=0:
                self.brandonroot(x)
    
    elif per.name == "Edmond":
      if per.ccd > 0:
        print("\nEdmond is on cooldown!")
        bad = True
      else:
        if len(enemy.teamS) > 1:
          print("")
          print(enemy.teamS)
          self.target(self.edmondattack,enemy.team,enemy.teamID)
        else:
          if len(enemy.teamS) == 0:
            print("\There is no one to attack!")
            bad = True
          else:
            for x in enemy.team:
              if x.ID in enemy.teamID and x.invis <=0:
                self.edmondattack(x)
          
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
  
  def brandonroot(self,enemy):
    time.sleep(1)
    brandAC = 100 + round((100/240)*self.supportscale())
    diff = enemy.cEV - brandAC
    if random.randint(1,100) <= diff:
      print("\nBrandon erupts the roots in the ground, but",enemy.NAME,"dodges the roots!")
    else:
      print("\nBrandon erupts the roots in the ground, rooting",enemy.NAME+"!")
      enemy.rooted = 1
    
  def edmondattack(self,enemy):
    global sett
    time.sleep(1)
    diff = enemy.cEV - 100
    ejAT = 11 + round((109/240)*self.supportscale())
    ejAPN = round((50/240)*self.supportscale())
    if random.randint(1,100) <= diff:
      print("\nEdmond attacks, but", enemy.NAME, "dodges!")
      enemy.specialdodgecases(self,0.5,"Physical Support")
    else:
      sett = enemy.cHP
      dmg = round(ejAT*enemy.dmgreduct)
      enemy.defense(self,"Physical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\nEdmond attacks", enemy.NAME +  ", but deals no damage!")
        else:
          print("\nEdmond attacks", enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        print("\nEdmond attacks", enemy.NAME + ", dealing",fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.4,mr="Physical Support")

  def target(self,types,location,locationS,al="",en=""):
    global bad
    bad = False
    wop = 0
    inviscount = 0
    for x in location:
      if x.invis > 0:
        inviscount = inviscount + 1
    if types == self.check:
      fw = input(fore.GREY_100 + "Check who's stats? " + style.RESET)
    elif types == self.mimic:
      fw = input(fore.GREY_100 + "Mimic who? ") 
    elif self in location or types == self.revive:
      fw = input(fore.GREY_100 + "Use on who? " + style.RESET) 
    else:
      fw = input(fore.GREY_100 + "Attack who? ") 
    if fw.isdigit() == True and fw != "0":
      if (len(location)-inviscount) >= int(fw):
        for x in location:
          if x.ID in locationS[(int(fw)-1)] and x.invis <=0:
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
      if fw.lower() == x.NAME.lower() and x.invis <=0:
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

  def counter(self,enemy):
    global CI
    CI = False
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
        CI = True

  def wildinstinct(self):
    if self.WI == False:
      time.sleep(1)
      print("\n"+self.NAME, "taps into his wild instincts, increasing his attack, speed, evasion, and critical chance, but reducing his magic attack, magic defense, and accuracy! His body starts to damage itself!")
      self.WI = True 
    elif self.WI == True:
      time.sleep(1)
      print("\n"+self.NAME, "reverts back to his normal state!")
      self.WI = False
  

  def smash(self,enemy,ally,targ):
    global sett
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 40
    a1 = ""
    a2 = ""
    a3 = ""
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
          self.cAPN = round(self.cAPN * (1.2+(0.1*self.sma)))
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
      diff = enemy.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n"+self.NAME, "tries to smash",enemy.NAME + ", but they dodge!")
        enemy.specialdodgecases(self,0,"Physical Melee")
      else:
        sett = enemy.cHP
        if random.randint(1,100) <= self.cCT:
          dmg = round(self.cAT*self.CTdmg)
          enemy.defense(self,"Physical",dmg)
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"critically smashes",enemy.NAME + ", but deals no damage!")
            else:
              print("\n"+self.NAME,"critically smashes",enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME,"critically smashes",enemy.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        else:
          dmg = round(self.cAT)
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
        if self.cAPN > enemy.cDF or enemy.cDF<=0:
          enemy.cHP = enemy.cHP - round(((self.cAT*enemy.dmgreduct)))
        else:
          enemy.cHP = enemy.cHP - round(((self.cAT*(1-(((enemy.cDF)-self.cAPN)/((enemy.cDF+100)-self.cAPN)))*enemy.dmgreduct)))
          
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
      print("\n"+self.NAME,"casts a barrier on himself, guarding him from physical damage for",ally.pbarrier,"hits!")
    else:
      print("\n"+self.NAME,"casts a barrier on",ally.NAME + ", guarding them from physical damage for",ally.pbarrier,"hits!")

  def fromtheshadows(self,ally,targ):
    global sett
    global seq
    global bad
    if self.invis == 0 and self.instant == False:
      self.invis = 4
      self.cMP = self.cMP - 75
      ally.teamS.remove(self.NAME)
      time.sleep(1)
      print("\n"+self.NAME, "goes invisible...")
    else:
      seq = 0
      while seq == 0:
        if self.instant == True:
          time.sleep(1)
          print("\n"+self.NAME, "appears from the shadows!")
          time.sleep(1) 
          bruh = []
          for x in targ.team:
            if x.invis <=0:
              bruh.append(x)
          response = "a"              
          c = "b"                          
          count = 0
          start = time.time()         
          elapsed = 0                 
          while elapsed < 2:           
            c = random.choice(string.ascii_lowercase + string.digits)
            print("\n",c)              
            response = input(fore.GREY_100 + "\nType the letter or number displayed: " + style.RESET) 
            elapsed = time.time() - start 
            count = count + 1
            if response == c and elapsed <2:       
              elapsed = 0
              start = time.time() 
              cut = random.choice(bruh)
              for x in targ.team:
                self.prehiteffects(x)
                if cut == x:
                  diff = x.cEV - self.cAC
                  if random.randint(1,100) <= diff:
                    print("\n"+self.NAME, "slashes",x.NAME + ", but they dodge!")
                    x.specialdodgecases(self,0,"Physical Melee")
                  else:
                    sett = x.cHP
                    if random.randint(1,100) <= self.cCT:
                      dmg = round((self.CTdmg*(0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT))
                      x.defense(self,"Physical",dmg)
                      if x.cHP > 0:
                        if (sett-x.cHP) == 0:
                          print("\n"+self.NAME,"critically slashes",x.NAME + ", but deals no damage!")
                        else:
                          print("\n"+self.NAME,"critically slashes",x.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
                      else:
                        print("\n"+self.NAME,"critically slashes",x.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
                      x.onhittimersdefense(self,0,dmg,"Physical Melee") 
                      if x.cHP <= 0:
                        x.purge("Death",targ,ally)
                        targ.team.remove(x)
                        targ.teamID.remove(x.ID)
                        targ.teamS.remove(x.NAME)
                        targ.deadteam.append(x)
                        targ.deadteamS.append(x.NAME)
                        bruh.remove(x)
                      else:
                        x.currentstats(targ,ally)
                    else:
                      dmg = round(((0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT))
                      x.defense(self,"Physical",dmg)
                      if x.cHP > 0:
                        if (sett-x.cHP) == 0:
                          print("\n"+self.NAME,"slashes",x.NAME + ", but deals no damage!")
                        else:
                          print("\n"+self.NAME,"slashes",x.NAME + ", dealing",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
                      else:
                        print("\n"+self.NAME,"slashes",x.NAME + ", dealing",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
                      x.onhittimersdefense(self,0,dmg,"Physical Melee")
                      if x.cHP <= 0:
                        x.purge("Death",targ,ally)
                        targ.team.remove(x)
                        targ.teamID.remove(x.ID)
                        targ.teamS.remove(x.NAME)
                        targ.deadteam.append(x)
                        targ.deadteamS.append(x.NAME)
                        bruh.remove(x)
                      else:
                        x.currentstats(targ,ally)
                    self.onhittimersoffense(x,0,"Physical Melee") 
            else:
              time.sleep(1)
              print("\n"+self.NAME, "fails to slash!")
              self.invis = 0
              ally.teamS.append(self.NAME)
              seq = 1
              break
            if count == 6:
              time.sleep(1)
              print("\n"+self.NAME, "successfully cuts through the enemies!")
              self.invis = 0
              ally.teamS.append(self.NAME)
              seq = 1
              break
            for x in targ.team:
              y = 0
              if x.cHP <=0:
                y = y + 1
            if y == len(targ.team):
              self.invis = 0
              ally.teamS.append(self.NAME)
              seq = 1
              break
          self.instant = False
        else:
          print(fore.BLACK + back.GREY_100 + "\nIt's",self.NAME+"'s turn." + style.RESET)
          fight = input(fore.GREY_100 + style.BOLD+"Flashcut, Items, Recover, or Check? " + style.RESET)
          if fight == "1" or fight.lower() == "flashcut":
            time.sleep(1)
            print("\n"+self.NAME,"appears from the shadows!")
            time.sleep(1) 
            bruh = []
            for x in targ.team:
              if x.invis <=0:
                bruh.append(x) 
            response = "a"              
            c = "b"                          
            count = 0
            start = time.time()         
            elapsed = 0                 
            while elapsed < 2:           
              c = random.choice(string.ascii_lowercase + string.digits)
              print("\n",c)              
              response = input(fore.GREY_100 + "\nType the letter or number displayed: " + style.RESET)
              elapsed = time.time() - start 
              count = count + 1
              if response == c and elapsed <2:       
                elapsed = 0
                start = time.time() 
                cut = random.choice(bruh)
                for x in targ.team:
                  if cut == x:
                    self.prehiteffects(x)
                    diff = x.cEV - self.cAC
                    if random.randint(1,100) <= diff:
                      print("\n"+self.NAME, "slashes",x.NAME +", but they dodge!")
                      x.specialdodgecases(self,0,"Physical Melee")
                    else:
                      sett = x.cHP
                      if random.randint(1,100) <= self.cCT:
                        dmg = round((self.CTdmg*(0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT))
                        x.defense(self,"Physical",dmg)
                        if x.cHP > 0:
                          if (sett-x.cHP) == 0:
                            print("\n"+self.NAME,"critically slashes",x.NAME + ", but deals no damage!")
                          else:
                            print("\n"+self.NAME,"critically slashes",x.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
                        else:
                          print("\n"+self.NAME,"critically slashes",x.NAME + ", dealing",fore.ORANGE_1 + style.BOLD + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
                        x.onhittimersdefense(self,0,dmg,"Physical Melee")
                        if x.cHP <= 0:
                          x.purge("Death",targ,ally)
                          targ.team.remove(x)
                          targ.teamID.remove(x.ID)
                          targ.teamS.remove(x.NAME)
                          targ.deadteam.append(x)
                          targ.deadteamS.append(x.NAME)
                          bruh.remove(x)
                        else:
                          x.currentstats(targ,ally)
                      else:
                        dmg = round(((0.6+(0.1*self.fromthes))*self.cAT)+((0.6+(0.1*self.fromthes))*self.cMAT))
                        x.defense(self,"Physical",dmg)
                        if x.cHP > 0:
                          if (sett-x.cHP) == 0:
                            print("\n"+self.NAME,"slashes",x.NAME + ", but deals no damage!")
                          else:
                            print("\n"+self.NAME,"slashes",x.NAME + ", dealing",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
                        else:
                          print("\n"+self.NAME,"slashes",x.NAME + ", dealing",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
                        x.onhittimersdefense(self,0,dmg,"Physical Melee")
                        if x.cHP <= 0:
                          x.purge("Death",targ,ally)
                          targ.team.remove(x)
                          targ.teamID.remove(x.ID)
                          targ.teamS.remove(x.NAME)
                          targ.deadteam.append(x)
                          targ.deadteamS.append(x.NAME)
                          bruh.remove(x)
                        else:
                          x.currentstats(targ,ally)
                      self.onhittimersoffense(x,0,"Physical Melee")
              else:
                time.sleep(1)
                print("\n"+self.NAME,"fails to slash!")
                self.invis = 0
                ally.teamS.append(self.NAME)
                seq = 1
                break
              if count == 6:
                time.sleep(1)
                print("\n"+self.NAME, "successfully cuts through the enemies!")
                self.invis = 0
                ally.teamS.append(self.NAME)
                seq = 1
                break
              for x in targ.team:
                y = 0
                if x.cHP <=0:
                  y = y + 1
              if len(targ.team) == 0:
                y = 0
              if y == len(targ.team):
                time.sleep(1)
                print("\n" + self.NAME, "successfully cuts through the enemies!")
                self.invis = 0
                ally.teamS.append(self.NAME)
                seq = 1
                break
          elif fight == "2" or fight.lower() == "items":
            bad = False
            self.inventorysystem(self,ally,targ)
            if bad == True:
              continue
            seq = 1
          elif fight == "3" or fight.lower() == "recover":
            buttsss = self.cMP
            time.sleep(1)
            self.cMP = self.cMP + (2*self.cMRG)
            if self.cMP > self.MP:
              self.cMP = self.MP 
            print("\n" + self.NAME, "relaxes to recover their inner strength, recovering",(self.cMP-buttsss),"mana!",self.NAME,"now has",self.cMP,"mana!")
            seq = 1
          elif fight == "4" or fight.lower() == "check":
            pepe = input("\nAllies or Enemies? ")
            if pepe == "1" or pepe.lower() == "allies":
              print("")
              print(ally.teamS)  
              self.target(self.check,ally.team,ally.teamID)
            elif pepe == "2" or pepe.lower() == "enemies":
              print("")
              print(targ.teamS)
              self.target(self.check,targ.team,targ.teamID)
            continue
          

  def enrage(self):
    time.sleep(1)
    self.enragev = 1 + (1-(self.cHP/self.HP))
    print("\n"+self.NAME, "enrages appropriately to his current injuries, changing his attack and speed!")


  def calligraphy(self,enemy):
    global sett
    self.cMP = self.cMP - 20
    self.isopoints = self.isopoints + 40
    self.prehiteffects(enemy)
    time.sleep(1)
    spac = round((2+(0.5*self.callig))*self.cAC)
    diff = enemy.cEV - spac
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "takes out her magic pen and summons the power of her calligraphy! It strides towards",enemy.NAME + ", but misses!")
      enemy.specialdodgecases(self,0.5,"Magical Ranged")
    else:
      sett = enemy.cHP
      if random.randint(1,100) <=self.cCT:
        dmg = round(self.CTdmg*self.cMAT*(1+(self.callig*0.25)))
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME, "takes out her magic pen and draws the power of her calligraphy! It strides towards",enemy.NAME +", but deals no damage!")
          else:
            print("\n"+self.NAME, "takes out her magic pen and draws the power of her calligraphy! It strides towards",enemy.NAME,"dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "takes out her magic pen and draws the power of her calligraphy! It strides towards",enemy.NAME,"dealing",style.BOLD + fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"critical damage!",enemy.NAME,"falls...")
      else:
        dmg = round(self.cMAT*(1+(self.callig*0.25)))
        enemy.defense(self,"Magical",dmg)
        if enemy.cHP > 0:
          if (sett-enemy.cHP) == 0:
            print("\n"+self.NAME, "takes out her magic pen and draws the power of her calligraphy! It strides towards",enemy.NAME +", but deals no damage!")
          else:
            print("\n"+self.NAME, "takes out her magic pen and draws the power of her calligraphy! It strides towards",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "takes out her magic pen and draws the power of her calligraphy! It strides towards",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
        
  def asmr(self,ally):   #a
    global sett 
    time.sleep(1)
    sett = self.cHP
    self.cHP = self.cHP - round(0.2*self.HP)
    self.cMP = self.cMP + (30+(5*self.asm))
    if self.cMP > self.MP:
      self.cMP = self.MP
    for x in ally.team:
      x.manaflow = [5,self]
    if len(ally.team) == 1:
      print("\n"+self.NAME,"performs ASMR, recovering",(30+(5*self.asm)),"mana at the cost of",(sett-self.cHP),"of her health! She reaches a state of flow, increasing her mana regeneration drastically!")
    else:
      print("\n"+self.NAME, "performs ASMR for everyone, recovering",(30+(5*self.asm)),"mana at the cost of",(sett-self.cHP),"of her health! Everyone reaches a state of flow, gaining drastically increased mana regeneration!")
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
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "pinpoints a vital target on the enemy and attempts to attack it, but misses!")
      enemy.specialdodgecases(self,0.5)
    else:
      if enemy.bleedt < 1:
        enemy.bleedt = 1
      enemy.bleedd = enemy.bleedd + ((1 + (0.2*self.pinp))*self.cAC)
      sett = enemy.cHP
      tdmg = round((0.6+(0.1*self.pinp))*self.cAT)
      enemy.cHP = enemy.cHP - tdmg
      if random.randint(1,100) <=self.cCT:
        dmg = round(self.CTdmg*self.cAT)
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          print("\n"+self.NAME, "pinpoints a vital target on the enemy and precisely attacks it, dealing",style.BOLD+str(sett-enemy.cHP)+style.RESET,"damage, and causing them to bleed heavily!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else:
          print("\n"+self.NAME, "pinpoints a vital target on the enemy and precisely attacks it, dealing",style.BOLD+str(sett-enemy.cHP)+style.RESET,"damage, and causing them to bleed heavily!",enemy.NAME,"falls...")
      else:
        dmg = round(self.cAT)
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
    ally.cHP = ally.cHP + round((0.1*ally.HP)+((2+(0.125*self.bake))*self.cMAT))
    if ally.cHP > ally.HP:
      ally.cHP = ally.HP
    time.sleep(0.5)
    if ally == self:
      print("\n"+self.NAME,"calls upon higher powers to heal herself for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett)+style.RESET,"health! She has",ally.cHP,"health now!")
    else:
      print("\n"+self.NAME,"calls upon higher powers to heal",ally.NAME,"for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett)+style.RESET,"health! He has",ally.cHP,"health now!")

  def omniheal(self,ally):
    global sett
    self.cMP = self.cMP - 50
    time.sleep(0.5)
    print("\n"+self.NAME,"opens the gates of heaven, healing everyone on the team!\n")
    time.sleep(0.2)
    for x in ally.team:
      sett = x.cHP
      x.cHP = x.cHP + round((0.1*x.HP)+((2+(0.125*self.bake))*self.cMAT))
      if x.cHP > x.HP:
        x.cHP = x.HP
      print(x.NAME,"heals for",fore.MEDIUM_SPRING_GREEN+ str(x.cHP-sett)+style.RESET,"health! They have",x.cHP," health now!")
      
  def perfectrequiem(self,enemy,al,targ):
    global sett
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 100
    time.sleep(1)
    print("\n"+self.NAME,"""takes out her violin and breathes, "Perfect Requiem..." """)
    time.sleep(1)
    response = "a"              
    c = "b"                     
    score = 0      
    count = 0
    start = time.time()         
    elapsed = 0                 
    while elapsed < 7:           
      c = random.choice(string.ascii_lowercase + string.digits)
      print("\n",c)              
      response = input(fore.GREY_100 + "\nType the letter or number displayed: " + style.RESET) 
      elapsed = time.time() - start 
      count = count + 1
      if response == c and elapsed <7:       
        score = score + 1
      if count == 6:
        break
      if score == 6:
        break
    dod = score
    for x in range(dod):
      diff = enemy.cEV - self.cAC
      if random.randint(1,100) <= diff:
        score = score - 1
    totat = score*(0.75+(0.05*self.perfectr))
    blow = 5+(0.4*self.perfectr)
    sett = enemy.cHP
    time.sleep(1)
    if dod == 0:
      print("\n"+self.NAME,"misses all her notes!")
    else:
      if random.randint(1,100) <= self.cCT:
        if score == 0:
          print("\n"+self.NAME, "violently plays through the battle, but",enemy.NAME,"dodges all the notes!")
          enemy.specialdodgecases(self,0.5,"Magical Ranged")
        else:
          dmg = round(self.CTdmg*totat*self.cMAT)
          enemy.defense(self,"Magical",dmg)
          if enemy.cHP>0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME, "violently plays through the battle, striking her notes to critically hit",enemy.NAME,score,"times, but deals no damage!")
            else:
              print("\n"+self.NAME, "violently plays through the battle, striking her notes to critically hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME, "violently plays through the battle, striking her notes to critically hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
          enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
      else: 
        if score == 0:
          print("\n"+self.NAME, "plays through the battle, but",enemy.NAME,"dodges all the notes!")
          enemy.specialdodgecases(self,0.5,"Magical Ranged")
        else:
          dmg = round(totat*self.cMAT)
          enemy.defense(self,"Magical",dmg)
          if enemy.cHP >0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME, "plays through the battle, striking her notes to hit",enemy.NAME,score,"times, but deals no damage!")  
            else:
              print("\n"+self.NAME, "plays through the battle, striking her notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!") 
          else:
            print("\n"+self.NAME, "plays through the battle, striking her notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
          enemy.onhittimersdefense(self,0.5,dmg,"Magical Ranged")
      if enemy.cHP >0 and dod == 6:
        enemy.currentstats(targ,al)
        diff = enemy.cEV - round(2*self.cAC)
        if random.randint(1,100) <= diff:
          print("\n"+self.NAME, "attempts to stun her opponent, but fails!")
          enemy.specialdodgecases(self,0.5,"Magical Melee")
        else:
          time.sleep(1)
          print("\n"+self.NAME, "achieves stunning her opponent.")
          time.sleep(1)
          print(""+self.NAME+": The finale...")
          time.sleep(1)
          sett = enemy.cHP
          self.cMPN = round(self.cMPN*2)
          dmg = round(blow*self.cMAT)
          enemy.defense(self,"Magical",dmg)
          if enemy.cHP > 0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME, "delivers the final blow, but deals no damage!")
            else:
              print("\n"+self.NAME, "delivers the final blow, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME, "has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME, "delivers the final blow, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"fades into specs of light...")   
          enemy.onhittimersdefense(self,0.5,dmg,"Magical Melee")            

  def revive(self,ally,a):
    self.cMP = self.cMP - 100
    if len(a.team) < 4:
      a.team.append(ally)
      a.teamS.append(ally.NAME)
    else:
      a.backteam.append(ally)
      a.backteamS.append(ally.NAME)
    a.teamID.append(ally.ID)
    a.deadteam.remove(ally)
    a.deadteamS.remove(ally.NAME)
    ally.deturn = 0
    ally.cHP = round(((0.3+(self.rev*0.05))*ally.HP))
    if ally.re == True:
      ally.resttimer = 21 - (ally.res)
    time.sleep(1)
    print(back.GREY_100 + fore.BLACK + style.BOLD+"\n"+self.NAME,"revives",ally.NAME+"!" + style.RESET)

  def runnershigh(self):
    self.cMP = self.cMP - 30
    self.runhigh = 21
    time.sleep(1)
    print("\n" + self.NAME, "enters the runner's high, removing and becoming immune to slows and increasing his attack and defense!")

  def shield(self):
    time.sleep(1)
    sett = self.cHP
    self.cHP = self.cHP + round((0.1+(0.01*self.shi))*self.HP)
    self.SHIE = True
    if self.cHP > self.HP:
      self.cHP = self.HP
    print("\n" + self.NAME,"shields himself, healing for",fore.MEDIUM_SPRING_GREEN+ str(self.cHP-sett) + style.RESET,"health, and gaining damage reduction! He has",self.cHP,"health now!")

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
    sett = ally.cHP
    ally.isopoints = ally.isopoints + (100+(50*self.isom))
    if ally.isopoints > (100*ally.isoLevel):
      ally.isopoints = (100*ally.isoLevel)
    time.sleep(1)
    if ally == self:
      print("\n"+self.NAME,"sings the isometric drawings song, boosting the level of all his skills by 1, and recovering his ISO-points to",str(ally.isopoints)+"!")
    else:
      print("\n"+self.NAME, "sings the isometric drawings song, boosting the level of all of",ally.NAME+ "'s skills by 1, and recovering their ISO-points to",str(ally.isopoints)+"!")

  def setskills(self):
    self.counte = self.counte - 1
    self.res = self.res - 1 
    self.fal = self.fal - 1
    self.hate = self.hate - 1
    self.wild = self.wild - 1
    self.ak = self.ak - 1
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
      print("\n"+self.NAME,"cannot do this with himself!")
      bad = True
    else:
      self.cMP = self.cMP - 100
      if ally == Ishraq or (self == Ishraq and ally == Julius):
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
            dmg = round((self.cAT + ally.cAT)*(2+(0.1*self.comb)))
            x.defense(self,"Magical",dmg)
            if x.cHP > 0:
              if (sett-x.cHP) == 0:
                print("\n"+x.NAME,"takes no damage!")
              else:
                print("\n"+x.NAME,"takes",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaning!")
            else:
              print("\n"+x.NAME,"takes",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")       
            x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")   
      elif ally == Kelly or (self == Kelly and ally == Julius):
        time.sleep(1)
        combMAT = (self.cMAT + ally.cMAT)*(2+(0.1*self.comb))
        for x in tea.team:
          x.cHP = x.cHP + round(combMAT)
          if x.cHP > x.HP:
            x.cHP = x.HP
        print("\n"+self.NAME+": Kelly! Sing with me!")
        time.sleep(0.5)
        print("\n"+self.NAME,"and Kelly sing the isometric drawings song, healing everyone for",fore.MEDIUM_SPRING_GREEN+ str(round(combMAT)) + style.RESET,"health!\n")
        for x in team:
          time.sleep(0.1)
          print(x.NAME,"has",x.cHP,"health now!")
      elif ally == Daniel or (self == Daniel and ally == Julius):
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
      elif ally == Arwyn or (self == Arwyn and ally == Julius):
        time.sleep(1)
        combSP = (self.cSP + ally.cSP)*(2+(0.1*self.comb))
        print("\n"+self.NAME+": Arwyn! Dance with me!")
        time.sleep(0.7)
        print("\n"+self.NAME,"and Arwyn, the Best Dancer, dance with each other, increasing everyone's armor and magic penetration by",str(round(combSP))+"!")
        for x in team:
          x.fAPN = x.fAPN + round(combSP)
          x.fMPN = x.fMPN + round(combSP)
      elif ally == Tim or (self == Tim and ally == Julius):
        print("")
        print(targ.teamS)
        self.target(self.timcomboattack,targ.team,targ.teamID,tea)
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
    diff = enemy.cEV - self.cAC
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n" + self.NAME, "tries to rub his greasy hands on",enemy.NAME + ", but they push him back!")
    else:
      if enemy.poisont < 3:
        enemy.poisont = 3
      enemy.greased = [3,self]
      enemy.poisond = enemy.poisond + ((0.4 + (0.1*self.grub))*self.cMAT) 
      print("\n" + self.NAME, "rubs his greasy hands on",enemy.NAME + ", poisoning them and lowering their evasion!")

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
        x.poisond = x.poisond + ((0.2 + (0.1*self.grub))*self.cMAT)
        dmg = round((1+(0.1*self.grub))*self.cMAT)
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
      print("\n",self.NAME,"cannot cast this skill on himself!")
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
      print("\n"+self.NAME,"bonds himself with",ally.NAME+", protecting them from damage and increasing their physical and magical attack!")
    
  def photosynthesis(self):
    if self.OB == False:
      time.sleep(1)
      print("\n"+self.NAME,"generates food in his body to keep on eating, causing him to regenerate health but lowering his attack drastically!")
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
    if self.cMP > self.MP:
      self.cMP = self.MP
    self.fAT = self.fAT * (1.125 + (0.125*self.jabb))
    self.cAT = round(self.fAT*self.pAT)
    time.sleep(1)
    print(back.YELLOW_1 + fore.BLACK + "\n!!!" + style.RESET,self.NAME,"starts rolling towards the enemies...",back.YELLOW_1 + fore.BLACK + "!!!" + style.RESET)
    for x in targ.team:
      self.prehiteffects(x)
      time.sleep(0.2)
      sett = x.cHP
      diff = x.cEV - self.cAC 
      if random.randint(1,100) <= diff:
        print("\n" + x.NAME,"moves out of the way!")
        x.specialdodgecases(self,0.1,"Physical Melee")
      else:
        if random.randint(1,100) <= self.cCT:
          dmg = round(self.CTdmg*self.cAT)
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
          dmg = round(self.cAT)
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
      print("\n"+self.NAME,"turns himself into an electron, increasing his accuracy, evasion, speed, and magic attack for 3 turns!")
    else:
      print("\n"+self.NAME,"turns,",ally.NAME,"into an electron, increasing their accuracy, evasion, speed, and magic attack for 3 turns!")

  def dab(self,enemy): 
    global sett  
    self.prehiteffects(enemy)
    self.cMP = self.cMP - 20
    time.sleep(1)
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n" + self.NAME,"dabs on",enemy.NAME+", but it's power doesn't reach them!")
      enemy.specialdodgecases(self,0.5)
    else:
      sett = enemy.cHP
      techm = 1.00
      if self.dabstack == 0:
        daba = 1.00
      else:
        daba = (1.1**self.dabstack)
        if enemy.ID != self.dabtarg:
          daba = 1.00
      speedm = 1.00 + ((0.01+(0.005*self.da))*self.cSP)
      if self.cAC > 100:
        techm = 1.00 + ((0.005+(0.0025*self.da))*(self.cAC - 100))
      dmg = round(((0.8+(0.1*self.da))*self.cAT)*techm*speedm*daba)
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
      print("\n"+self.NAME,"conjures a quen shield on himself, cleansing his debuffs and protecting him from damage for 1 hit!")
    else:
      print("\n"+self.NAME,"conjures a quen shield on",ally.NAME+", cleansing them of their debuffs and protecting them from damage for 1 hit!")

  def purge(self,types,ally,enemy,mid=False,op=False):
    if types == "Map Reset":
      self.rages = [0]
      self.mgh = [0]
      self.dark = 0
      self.glock = 0
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
      self.greased = [0]
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
    elif types == "Death": 
      self.ISOmode = False
      if self.NAME == "Shad":
        self.NAME == "Shah"
      if self.NAME == "Taco Lord":
        self.NAME == "Tim"
      self.skills = []
      if mid == False:
        for x in self.Sskills:
          self.skills.append(x)
      else:
        for x in self.Cskills:
          self.skills.append(x)
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
      self.chronot = 0
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
      self.chadwalked = 0
      self.chadlist = []
      self.hater = 0
      self.hatelis = []
      self.surge = 0
      if len(self.teth) > 0:
        for x in self.teth:
          x.tethered.remove(self)
      self.teth = []
      self.tethered = []
      self.ptelepath = 0
      self.telepath = 0
      self.mimicm = 0
      self.rehearsed = [0]
      self.prest = 0
      self.rested = 0
      self.ashamed = [0]
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
      self.greased = [0]
      self.stunned = False
      self.stunimmune = False
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
      #Quest-Specific Buffs
      self.Q1B = 0 #Richard fight Enraged Ishraq 2x attack boost
      self.cry = 0 #Nurse cry timer
      #Mob Essentials
      self.turncount = 0
      self.setHP = 0
      self.tw1 = 0
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
      #Dr.Graham
      self.scirc = 0
      self.inert = 0
      self.fricf = 0
      self.error = 0
      self.statr = False
      self.skillr = False
    
  def chronopower(self):
    self.cMP = self.cMP - 50
    time.sleep(0.7)
    print("\n" + self.NAME,"activates the power of time, igniting his weapon with its essence for 3 hits!")
    self.chronotime = 3

  def protobelt(self,targ):
    global sett
    self.cMP = self.cMP - 35
    time.sleep(1)
    print("\n" + self.NAME,"activates his protobelt, sending missles at every enemy and blowing him back, bringing him to safety for 1 hit!")
    for x in targ.team:
      self.prehiteffects(x)
      time.sleep(0.2)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n" + x.NAME,"dodges the missle!")
        x.specialdodgecases(self,0.1,"Magical Ranged")
      else:
        sett = x.cHP
        dmg = round((0.7+(0.15*self.proto))*self.cMAT)
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
    print("\n"+self.NAME,"throws his rubix cube onto the stage! It solves itself and explodes, causing all enemies to start dancing!")
    throw = round(self.cAC+(15*self.rub))
    for x in targ.team:
      diff = x.cEV - throw
      if random.randint(1,100) <= diff:
        time.sleep(0.3)
        print("\n" + x.NAME,"avoids the blast!")
      else:
        x.dance = 1

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
    print("\n" + self.NAME,"shuts himself up...")
    
  def silenceattack(self,enemy):
    global sett
    global lastat
    self.prehiteffects(enemy)
    sett = enemy.cHP
    diff = enemy.cEV - self.cAC 
    self.lastattack = "Silenced Auto"
    lastat = "Silenced Auto"
    self.cMP = self.cMP + self.cMRG
    if self.cMP > self.MP:
      self.cMP = self.MP 
    if random.randint(1,100) <= diff:
      time.sleep(1)
      print("\n" + self.NAME, "attacks, but", enemy.NAME, "dodges!")
      enemy.specialdodgecases(self,0.5,"True Melee")
    else:
      time.sleep(1)
      if random.randint(1,100) <= self.cCT:
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
    self.bleedd = self.bleedd + (0.067*self.HP)
    time.sleep(1)
    print("\n" + self.NAME,"starts cutting himself, lowering all enemy defense and magic defense!")

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
      pdmg = round((0.5+(0.1*self.gunb))*self.cAT)
      enemy.defense(self,"Physical",pdmg)
      mdmg = round((0.8+(0.1*self.gunb))*self.cMAT)
      enemy.defense(self,"Magical",mdmg)
      self.cHP = self.cHP + round((0.5+(0.1*self.gunb))*(sett-enemy.cHP))
      if self.cHP > self.HP:
        self.cHP = self.HP
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
      print("\nThe gunblade restores",self.NAME+"'s health with its stored energy, healing him for",fore.MEDIUM_SPRING_GREEN + str(round((0.5+(0.1*self.gunb))*(sett-enemy.cHP))) + style.RESET,"health!",self.NAME,"has",self.cHP,"health now!") 
      
  def sparknet(self,ally,eteam):
    global sett
    self.cMP = self.cMP - 50
    time.sleep(1)
    if len(eteam.team) == 1:
      for x in eteam.team:
        self.prehiteffects(x)
        diff = x.cEV - self.cAC 
        if random.randint(1,100) <= diff:
          print("\n" + self.NAME, "attempts to strike", x.NAME, "with a lightning bolt, but they dodge!")
          x.specialdodgecases(self,0.5,"Magical Ranged")
        else:
          x.sparkstun = x.sparkstun + 1
          sett = x.cHP
          dmg =  round((0.4+(0.05*self.spark))*self.cMAT)
          x.defense(self,"Magical",dmg)
          if x.cHP > 0:
            if (sett-x.cHP) == 0:
              print("\n" + self.NAME, "strikes", x.NAME, "with a lightning bolt, paralyzing them but dealing no damage!")
            else:
              print("\n" + self.NAME, "strikes", x.NAME, "with a lightning bolt, paralyzing them and dealing",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
          else:
            print("\n" + self.NAME, "strikes", x.NAME, "with a lightning bolt, paralyzing them and dealing",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
          x.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
    else:
      print("\n" + self.NAME, "sends out a sparknet that bounces between the enemies!")
      temp = None
      final = 0
      for boob in range(6):
        CTI = False
        time.sleep(0.3)
        if len(eteam.team) == 0 and temp != None:
          eteam.team.append(temp)
          temp = None
          final = 1
        if len(eteam.team) > 0:
          targ = random.choice(eteam.team)
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
          dmg = round((0.4+(0.05*self.spark))*self.cMAT)
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
              eteam.team.append(temp)
            if final == 1:
              break
            temp = targ
            eteam.team.remove(targ)
          else:
            if CTI == True:
              print("\nThe lightning bounces to", targ.NAME + ", paralyzing them and dealing", fore.PURPLE_1B + str(sett-targ.cHP) + style.RESET,"damage!",targ.NAME,"falls...")
            else:
              print("\nThe lightning bounces to", targ.NAME + ", dealing", fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",targ.NAME,"falls...")
            targ.onhittimersdefense(self,0.2,dmg,"Magical Ranged")
            if targ.cHP <= 0:
              targ.purge("Death",eteam,ally)
              eteam.team.remove(targ)
              eteam.teamID.remove(targ.ID)
              eteam.teamS.remove(targ.NAME)
              eteam.deadteam.append(targ)
              eteam.deadteamS.append(targ.NAME)
            else:
              targ.currentstats(eteam,ally)
      if temp != None:
        eteam.team.append(temp)  

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
      print("\n"+self.NAME,"tenses up, increasing his strength for his next physical attack!")
    elif self.tension == 2:
      print("\n"+self.NAME,"tenses up greatly, further increasing his strength for his next physical attack!")
    elif self.tension == 3:
      print("\n"+self.NAME,"tenses up immensely, extremely increasing his strength for his next physical attack!")

  def sickpump(self):
    time.sleep(1)
    if self.tension >= 3:
      self.tension = self.tension + 1
      if self.tension == 5:
        print(fore.ORANGE_RED_1+"\n"+self.NAME+": Protein...protein..."+style.BOLD+"MOM I NEED PROTEIN!!!"+style.RESET)
        time.sleep(1)
        print("\n"+self.NAME,"chugs gallons of proteins, and starts to beetle stride. His eyes dart forward and arms start flailing around. He becomes the epitome of CHAD, tension boosting to the limit of infinity!")
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
    self.tensionattack = True
    self.cMP = self.cMP - 30
    self.prehiteffects(enemy)
    diff = enemy.cEV - self.cAC
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "exerts the fiery inferno of working out onto",enemy.NAME + ", but misses!")
      enemy.specialdodgecases(self,0.5)
    else:
      sett = enemy.cHP
      pdmg = round((0.7+(0.1*self.infe))*self.cAT)
      enemy.defense(self,"Physical",pdmg)
      mdmg = round((1+(0.1*self.infe))*self.cMAT)
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
      enemy.onhittimersdefense(self,0.5,tot,"Mixed Ranged")
      self.onhittimersoffense(self,0.5) 

  def selfdestruct(self,enemy):
    global sett
    self.prehiteffects(enemy)
    time.sleep(1)
    selfsett = self.cHP
    self.cHP = self.cHP - round(0.75*self.HP)
    dmg = selfsett-self.cHP
    sett = enemy.cHP
    diff = enemy.cEV - self.cAC
    if random.randint(1,100) <= diff:
      print("\n"+self.NAME, "tries to grapple",enemy.NAME + ", but they break out!")
      enemy.specialdodgecases(self,0.5,"True Melee")
    else:
      print("\n"+self.NAME, "grapples",enemy.NAME + ", locking them down.")
      time.sleep(0.5)
      print("\n"+self.NAME+": Allahu Akbar")
      time.sleep(0.5)
      enemy.cHP = enemy.cHP - round((1.0+(0.1*self.selfd))*dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME,"self-destructs on",enemy.NAME+", but deals no damage!")
        else:
          print("\n"+self.NAME,"self-destructs on",enemy.NAME+", dealing",style.BOLD + fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"true damage!",enemy.NAME,"has",enemy.cHP,"health remaning!")
      else:
        print("\n"+self.NAME,"self-destructs on",enemy.NAME+", dealing",style.BOLD + fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"true damage!",enemy.NAME,"falls...")
      enemy.onhittimersdefense(self,0.5,dmg,"True Melee") 
      if self.cHP >0:
        print(self.NAME,"takes",dmg,"damage!",self.NAME,"has",self.cHP,"health now!")
      else:
        print(self.NAME,"takes",dmg,"damage!",self.NAME,"falls...")
      self.onhittimersdefense(self,0.5)
      
  def chadwalk(self,targ):
    self.cMP = self.cMP - 80
    time.sleep(1)
    print("\n"+self.NAME,"chad-walks across the battlefield to make up for his fragile masculinity, increasing allied critical chance and damage!")
    self.chadwalked = 5
    self.chadlist = []
    for x in targ.team:
      self.chadlist.append(x)
    self.chadlist.remove(self)
    self.chadlist.insert(0,self)
      
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
      selfsett = self.cHP
      self.cHP = self.cHP + round((self.HP-self.cHP)*(0.3+(0.05*self.suc)))
      if "Male" in enemy.GEN:
        dmg = round(self.CTdmg*self.cMAT*(1+(self.suc*0.5)))
        enemy.defense(self,"Magical",dmg)
        enemy.bleedt = 2
        enemy.bleedd = enemy.bleedd + ((0.5+(0.125*self.suc))*self.cMAT)
      else:
        dmg = round(self.cMAT*(1+(self.suc*0.5)))
        enemy.defense(self,"Magical",dmg)
      if enemy.cHP > 0:
        if (sett-enemy.cHP) == 0:
          print("\n"+self.NAME, "sucks off",enemy.NAME +", but deals no damage!")
        else:
          if "Male" in enemy.GEN:
            print("\n"+self.NAME, "sucks off and bites",enemy.NAME,"dealing",fore.PURPLE_1B+style.BOLD+str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
          else:
            print("\n"+self.NAME, "sucks off",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
      else:
        if "Male" in enemy.GEN:
          print("\n"+self.NAME, "sucks off and bites",enemy.NAME,"dealing",fore.PURPLE_1B+style.BOLD+str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        else:
          print("\n"+self.NAME, "sucks off",enemy.NAME,"dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      time.sleep(0.5)
      print("\n"+self.NAME,"heals for",fore.MEDIUM_SPRING_GREEN+str(self.cHP-selfsett)+style.RESET,"health!",self.NAME,"has",self.cHP,"health now!")
      enemy.onhittimersdefense(self,0.5,dmg,"Magical Melee")
  
  def powersurge(self,targ):
    self.cMP = self.cMP - 75
    time.sleep(1)
    print("\n"+self.NAME,"unleashes tethers from her body, clinging onto all enemies to drain their attack and magic attack!")
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
          self.target(self.attack,targ.team,targ.teamID)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and x.invis <=0:
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
          self.target(self.silenceattack,targ.team,targ.teamID)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and x.invis <=0:
              self.silenceattack(x)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      else:
        msett = self.cMP
        self.skillcatalog(enemy.lastattack,al,targ)
        if bad != True:
          mlost = (msett-self.cMP)
          if mlost < round(self.MP*(0.5-(0.05*self.mimi))):
            self.cMP = msett - round(self.MP*(0.5-(0.05*self.mimi)))
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
          self.target(self.attack,targ.team,targ.teamID)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and x.invis <=0:
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
          self.target(self.silenceattack,targ.team,targ.teamID)
        else:
          for x in targ.team:
            if x.ID in targ.teamID and x.invis <=0:
              self.silenceattack(x)
        if bad != True:
          self.dabtarg = ""
          self.dabstack = 0
      else:
        msett = self.cMP
        self.skillcatalog(lastat,al,targ)
        if bad != True:
          mlost = (msett-self.cMP)
          if mlost < round(self.MP*(0.5-(0.05*self.mimi))):
            self.cMP = msett - round(self.MP*(0.5-(0.05*self.mimi)))
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
    dmg = (self.cMAT*(((0.6+(0.1*self.desp))+((1+(0.25*self.desp))*(1-(self.cHP/self.HP))))*((1.2+(0.05*self.desp))**(4-len(ally.team)))))
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
    
  def AIdetector(self):
    if self.stunned == True and self.NAME != "Mr. Pudup":
      self.stunned = False
    else:
      if self.NAME == "Amira" and self.ID !="8":
        self.AmiraAI()
      elif self.NAME == "Mrs. Wells":
        self.MrsWellsAI()
      elif self.NAME == "Mr. Pudup":
        self.MrPudupAI()
      elif self.NAME == "Ryca":
        self.RycaAI()
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
      elif self.NAME == "The Librarian":
        self.LibrarianAI()
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
      self.enemyattacksys(self.AmiraPerfectrequiem,"Perfect Requiem",en=you)
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
    elif bruh == "Auto-Attack": 
      self.enemyattacksys(self.attack,"Auto")
    elif bruh == "Perfect Requiem":
      self.enemyattacksys(self.AmiraPerfectrequiem,"Perfect Requiem",en=you)

  def giant(self):
    time.sleep(1)
    print("\n"+self.NAME,"turns into a giant, increasing their physical damage drastically but reducing her evasion and magic attack tremendously!")
    self.giantess = 7

  def AmiraPerfectrequiem(self,enemy,targ):
    time.sleep(1)
    print("\n"+self.NAME,""" takes out her violin and breathes, "Perfect Requiem..." """)
    time.sleep(1)
    if self.giantess > 0:
      if random.randint(1,100) <= self.cCT:
        print("\n"+self.NAME,"violently plays through the battle, striking her notes to critically hit everyone!")
        for x in targ.team:
          score = 6
          for x in range(6):
            diff = x.cEV - self.cAC
            if random.randint(1,100) <= diff:
              score = score - 1
          time.sleep(0.2)
          if score == 0:
            print("\n"+x.NAME,"dodges all hits!")
            x.specialdodgecases(self,0.5,"Magical Ranged")
          else:
            sett = x.cHP
            dmg = round(self.CTdmg*score*self.cMAT)
            x.defense(self,"Magical",dmg)
            if x.cHP>0:
              if (sett-x.cHP) == 0:
                print("\n"+x.NAME,"gets hit",score,"times, but takes no damage!")
              else:
                print("\n"+x.NAME,"gets hit",score,"times, taking",fore.PURPLE_1B + style.BOLD + str(sett-x.cHP) + style.RESET,"critical damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n"+x.NAME,"gets hit",score,"times, taking",fore.PURPLE_1B + style.BOLD + str(sett-x.cHP)+ style.RESET,"critical damage!",x.NAME,"falls...")
            x.onhittimersdefense(self,0.2,dmg,"Magical Ranged") 
      else:
        print("\n"+self.NAME,"plays through the battle, striking her notes to hit everyone!")
        for x in targ.team:
          score = 6
          for x in range(6):
            diff = x.cEV - self.cAC
            if random.randint(1,100) <= diff:
              score = score - 1
          time.sleep(0.2)
          if score == 0:
            print("\n"+x.NAME,"dodges all hits!")
            x.specialdodgecases(self,0.5,"Magical Ranged")
          else:
            sett = x.cHP
            dmg = round(score*self.cMAT)
            x.defense(self,"Magical",dmg)
            if x.cHP>0:
              if (sett-x.cHP) == 0:
                print("\n"+x.NAME,"gets hit",score,"times, but takes no damage!")
              else:
                print("\n"+x.NAME,"gets hit",score,"times, taking",fore.PURPLE_1B + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n"+x.NAME,"gets hit",score,"times, taking",fore.PURPLE_1B + str(sett-x.cHP)+ style.RESET,"damage!",x.NAME,"falls...")
            x.onhittimersdefense(self,0.2,dmg,"Magical Ranged") 
    else:    
      sett = enemy.cHP
      if random.randint(1,100) <= self.cCT:
        score = 6
        for x in range(6):
          diff = enemy.cEV - self.cAC
          if random.randint(1,100) <= diff:
            score = score - 1
        if score == 0:
          print("\n"+self.NAME,"violently plays through the battle, but",enemy.NAME,"dodges all the notes!")
          enemy.specialdodgecases(self,0.5,"Magical Ranged")
        else:
          dmg = round(2*score*self.cMAT)
          enemy.defense(self,"Magical",dmg)
          if enemy.cHP>0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"violently plays through the battle, striking her notes to critically hit",enemy.NAME,score,"times, but deals no damage!")
            else:
              print("\n"+self.NAME,"violently plays through the battle, striking her notes to critically hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!") 
          else:
            print("\n"+self.NAME,"violently plays through the battle, striking her notes to critically hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
          enemy.onhittimersdefense(self,0.4,dmg,"Magical Ranged")
      else: 
        score = 6
        for x in range(6):
          diff = enemy.cEV - self.cAC
          if random.randint(1,100) <= diff:
            score = score - 1
        if score == 0:
          print("\n"+self.NAME,"plays through the battle, but",enemy.NAME,"dodges all the notes!")
          enemy.specialdodgecases(self,0.5,"Magical Ranged")
        else:
          dmg = round(score*self.cMAT)
          enemy.defense(self,"Magical",dmg)
          if enemy.cHP >0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"plays through the battle, striking her notes to hit",enemy.NAME,score,"times, but deals no damage!") 
            else:
              print("\n"+self.NAME,"plays through the battle, striking her notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!") 
          else:
            print("\n"+self.NAME,"plays through the battle, striking her notes to hit",enemy.NAME,score,"times, dealing",fore.PURPLE_1B + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
          enemy.onhittimersdefense(self,0.4,dmg,"Magical Ranged") 
      if enemy.cHP >0:
        enemy.currentstats()
        sett = enemy.cHP
        diff = enemy.cEV - round(2*self.cAC)
        time.sleep(2)
        if random.randint(1,100) <= diff:
          print("\n"+self.NAME, "attempts to stun her opponent, but fails!")
          enemy.specialdodgecases(self,0.5,"Magical Melee")
        else:
          print("\n"+self.NAME,"achieves stunning her opponent.")
          time.sleep(1)
          print("\n"+self.NAME+": The finale...")
          time.sleep(1)
          self.cMPN = round(2*self.cMPN)
          dmg2 = round(7*self.cMAT)
          enemy.defense(self,"Magical",dmg2)
          if enemy.cHP <= 0:
            if (sett-enemy.cHP) == 0:
              print("\n"+self.NAME,"delivers the final blow, but deals no damage!")
            else:
              print("\n"+self.NAME,"delivers the final blow, dealing",fore.PURPLE_1B + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"fades into specs of light...")
          else:
            print("\n"+self.NAME,"delivers the final blow, dealing",fore.PURPLE_1B + style.BOLD + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME, "has",enemy.cHP,"health remaining!")
          enemy.onhittimersdefense(self,0.4,dmg2,"Magical Melee") 

  def AmiraRevive(self,ally):
    bots.team.append(ally)
    bots.teamS.append(ally.NAME)
    bots.deadteam.remove(ally)
    bots.deadteamS.remove(ally.NAME)
    bots.teamID.append(ally.ID)
    ally.deturn = 0
    ally.cHP = round(0.5*ally.HP)
    if ally.re == True:
      ally.resttimer = 21 - (ally.res)
    time.sleep(1)
    print(back.GREY_100 + fore.BLACK + style.BOLD+"\n"+self.NAME,"revives",ally.NAME+"!" + style.RESET)
  
  def MrsWellsAI(self):
    global lastat
    attacks = []
    self.turncount = self.turncount + 1
    for x in you.team:
      if x.cHP < round(0.1*x.HP) and x.invis <=0:
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
        if x.cHP < round(0.1*x.HP) and x.invis <=0:
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
          x.cHP = x.cHP - round((0.15*self.missingnotes)*x.HP)
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
          x.cHP = x.cHP + round(0.2*x.HP)
          if x.cHP > x.HP:
            x.cHP = x.HP
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
        x.cHP = x.cHP - round(0.2*x.HP)
        time.sleep(0.2)
        if x.cHP <= 0:
          print(x.NAME,"takes",(sett-x.cHP),"damage!",x.NAME,"falls...")
        else:
          print(x.NAME,"takes",(sett-x.cHP),"damage!",x.NAME,"has",x.cHP,"health remaining!")
        
  def candy(self,enemy):
    time.sleep(1)
    sett = enemy.cHP
    enemy.cHP = enemy.cHP + round(0.5*enemy.HP)
    if enemy.cHP > enemy.HP:
      enemy.cHP = enemy.HP
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
        if x.burnt > 0 and x.invis <=0:
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
        time.sleep(0.2)
        print("Mr. Pudup: Hehe..I wish I was dumb enough to laugh at anything..*Inhales Loudly*")
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
        dmg = round(2*self.cMAT)
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
      dmg = round(self.cMAT*2.5)
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
    time.sleep(1)
    if random.randint(1,100) <= diff:
      print("\n" + self.NAME, "tries to cut through",enemy.NAME+", but they dodge!")
      enemy.specialdodgecases(self,0.5,"Physical Melee")
    else:
      if random.randint(1,100) <= self.cCT:
        dmg = round(4*self.CTdmg*self.cAT)
        enemy.defense(self,"Physical",dmg)
        if enemy.cHP >0:
          if (sett-enemy.cHP) == 0:
            print("\n" +self.NAME,"critically cuts through",enemy.NAME + ", but deals no damage!")
          else:
            print("\n" +self.NAME,"critically cuts through",enemy.NAME,"dealing",style.BOLD+ fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"has",enemy.cHP,"health remaining!")
        else: 
          print("\n" +self.NAME,"critically cuts through",enemy.NAME,"dealing",style.BOLD+ fore.ORANGE_1 + str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
      else:
        dmg = round(4*self.cAT)
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
        if deez <= 5:
          time.sleep(0.2)
          dmg = round(self.cAT)
          enemy.defense(self,"Physical",dmg)
        elif deez > 5:
          time.sleep(0.5)
          dmg = round((1.3**(3-(count-deez)))*self.cAT)
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
          print("\n" +self.NAME,"attacks",enemy.NAME,"dealing",style.BOLD+str(sett-enemy.cHP) + style.RESET,"damage!",enemy.NAME,"falls...")
        enemy.onhittimersdefense(self,0.1,dmg,"Physical Melee")
        self.onhittimersoffense(enemy,0.1)
        if enemy.cHP <=0:
          if len(targ.team) > 1:
            x.purge("Death",targ,ally)
            targ.team.remove(x)
            targ.teamID.remove(x.ID)
            targ.teamS.remove(x.NAME)
            targ.deadteam.append(x)
            targ.deadteamS.append(x.NAME)
            enemy = random.choice(targ.team)
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
      if self.rages[0] <= 0:
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
      if self.rages <=0 and self.cMP >=50:
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
      self.glacier(you.team)
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
    self.rages = [21,self]
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
      dmg = round(self.cMAT*5)
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
    for x in targ:
      time.sleep(0.2)
      self.prehiteffects(x)
      diff = x.cEV - self.cAC
      if random.randint(1,100) <= diff:
        print("\n" + x.NAME,"escapes the crash landing!")
        x.specialdodgecases(self,0.1,"Magical Ranged")
      else:
        x.frozen = 1
        sett = x.cHP
        dmg = round(2.5*self.cMAT)
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
      if x.invis <=0:
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
          dmg = round(self.cAT)
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
              enemy.purge("Death",targ,ally)
              targ.team.remove(x)
              targ.teamID.remove(x.ID)
              targ.teamS.remove(x.NAME)
              targ.deadteam.append(x)
              targ.deadteamS.append(x.NAME)
              bruh.remove(enemy)
            else:
              x.currentstats(targ,ally)
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
    for x in team:
      if (x.WI == True or x.valor > 0 or x.immortal > 0 or x.runhigh > 0 or x.SHIE > 0 or x.isoboost > 0 or x.OB > 0 or x.thehut > 0 or x.ionzied > 0 or x.knightb > 0 or x.safety > 0 or x.chronotime > 0 or x.quenshield == True or x.tension > 0 or x.chadwalked > 0 or x.manaflow > 0):
        attacks.append("Leech")
    yo = random.choice(attacks)
    if self.cHP <= round(0.3*self.HP) and self.nap == 1:
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
      for x in team:
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
      self.cHP = round(self.cHP + (0.05*self.HP))
      if self.cHP > self.HP:
        self.cHP = self.HP
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
      dmg = round(0.1*self.cSP*self.cAT)
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
        dmg = round(self.cMAT)
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
          dmg = round(50*self.cMAT)
          x.defense(self,"Magical",dmg)
        else:
          dmg = round(5*self.cMAT)
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

  def RycaAI(self):
    global lastat
    tar = []
    for x in bots.team:
      if x.cHP <= round(0.5*x.HP):
        tar.append(x)
    if len(tar) >0 and self.cMP >=5:
      targ = random.choice(tar)
      self.enemyHeal(targ,self.cMAT,5)
      self.lastattack = "Heal"
      lastat = "Heal"
    else:
      self.enemyattacksys(self.attack,"Auto")
     
  def enemyHeal(self,ally,amount,cost):
    self.cMP = self.cMP - cost
    time.sleep(1)
    sett = ally.cHP
    ally.cHP = ally.cHP + amount
    if ally.cHP > ally.HP:
      ally.cHP = ally.HP
    if ally == self:
      print("\n"+self.NAME,"heals themself for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett) + style.RESET,"health!",ally.NAME,"has",ally.cHP,"health now!")
    else:
      print("\n"+self.NAME,"heals",ally.NAME,"for",fore.MEDIUM_SPRING_GREEN+ str(ally.cHP-sett) + style.RESET,"health!",ally.NAME,"has",ally.cHP,"health now!")

  def JuliusAI(self):
    if self.cHP <= round(0.5*self.HP) and Kelly in you.team:
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
    if self.tw1 == 0 and self.cHP <= round(0.2*self.HP):
      self.enemyattacksys(self.curse,"Auto")
      self.tw1 = 1
    elif self.turncount % 3 == 0 and self.cMP >= 10:
      self.cMP = self.cMP - 10
      self.bookflurry(you)
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
            dmg = round(0.25*self.cMAT)
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
            dmg = round(0.5*self.cAT)
            x.defense(self,"Physical",dmg)
            if x.cHP >0:
              if (sett-x.cHP) == 0:
                print("\n" + x.NAME, "is smacked by a book, but takes no damage!")
              else:
                print("\n" + x.NAME, "is smacked by a book, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"has",x.cHP,"health remaining!")
            else:
              print("\n" + x.NAME, "is smacked by a book, taking",fore.ORANGE_1 + str(sett-x.cHP) + style.RESET,"damage!",x.NAME,"falls...")
            x.onhittimersdefense(self,0.2,dmg,"Physical Ranged")




class World:
  def __init__(self,ROOM,TYPE,RID,ENC): 
    self.ROOM = ROOM
    self.TYPE = TYPE
    self.RID = RID
    self.ENC = ENC
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
      self.paths = ["C-Wing Hall Ground Floor","Main Office","C-Wing Media Center","B-Wing Hallway 1st Floor","Main Lobby","D-Wing Hallway 1st Floor"]
    if self.ROOM == "D-Wing Hallway Ground Floor":
      self.paths = ["C-Wing Hall Ground Floor","H-Wing Complex Ground Floor","Cafe 2","D-Wing Hallway 1st Floor"]
    if self.ROOM == "DB-Wing Sector":
      self.paths = ["D-Wing Hallway Ground Floor"]
    if self.ROOM == "H-Wing Complex Ground Floor":
      self.paths = ["Automotive Building","H-Wing Complex 1st Floor","D-Wing Hallway Ground Floor"]
    if self.ROOM == "C-Wing Hall Ground Floor":
      self.paths = ["D-Wing Hallway Ground Floor","Cafe 1","C-Wing Nurse's Office","Cafe 2","C-Wing Hall 1st Floor","B-Wing Hallway Ground Floor"]
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
    Ishraq.Ishraqlevelup()
    Kelly.Kellylevelup()
    Julius.Juliuslevelup()
    Daniel.Daniellevelup()
    Tim.Timlevelup()
    Arwyn.Arwynlevelup()
    Shah.Shahlevelup()
    Amira.Amiralevelup()
    autosave()
    #ADD
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
          continue
        elif choice.lower() == "upgrades" or choice == "2":
          if len(you.isoinventory) == 0:
            print("\nYou have no Isometric Drawings.")
        elif choice.lower() == "party" or choice == "4":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1
        elif choice.lower() == "save" or choice == "5":
          print("\nSaving...")
          save("save")
          print("Save complete!")
        elif choice.lower() == "exit" or choice == "6":
          self.campexit()
          if sad == 1:
            continue
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
          continue
        elif choice.lower() == "party" or choice == "4":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1
        elif choice.lower() == "save" or choice == "5":
          print("\nSaving...")
          save("save")
          print("Save complete!")
        elif choice.lower() == "exit" or choice == "6":
          self.campexit()
          if sad == 1:
            continue
          boobs = 1
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
          for x in you.team:
            revival(x,o=True)
          for x in you.backteam:
            revival(x,o=True)
          for x in you.deadteam:
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
          continue
        elif choice.lower() == "party" or choice == "4":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1
        elif choice.lower() == "save" or choice == "5":
          print("\nSaving...")
          save("save")
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
          continue
        elif choice.lower() == "quests" or choice == "3":
          continue
        elif choice.lower() == "party" or choice == "4":
          teamswitch()
          if sad == 1:
            continue
          autosave()
          boobs = 1
        elif choice.lower() == "save" or choice == "5":
          print("\nSaving...")
          save("save")
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
            fi = input("\nWhich boss do you want to fight?\n(1) Amira  (2) Mrs. Wells\n(3) Mr. Pudup  (4) Aqua\n(5) Dr. Graham\nResponse: ")
            if fi != "1" and fi != "2" and fi !="3" and fi!="4" and fi !="5":
              continue
            dif = input("\nDifficulty Setting:\n(1) Easy  (2) Normal\n(3) Hard  (4) Insane\n(5) Nightmare\nResponse: ")
            if dif != "1" and dif !="2" and dif !="3" and dif!="4" and dif !="5":
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
    None
  
  def changeitem(self,pe):
    None

  def eqs(self,pe,inven):
    print("")
    print(inven)
    poo = input("What do you want to equip? ")
    if poo.isdigit() == True and poo != "0":
      if len(inven) >= int(poo):
        item = inven[(int(poo)-1)]
        if inven == you.weaponinventory:
          pe.equipcatalog(pe.weap,item,inven)
        elif inven == you.helminventory:
          pe.equipcatalog(pe.head,item,inven)
        elif inven == you.chestinventory:
          pe.equipcatalog(pe.body,item,inven)
        elif inven == you.bootsinventory:
          pe.equipcatalog(pe.lower,item,inven)
        elif inven == you.accessinventory:
          pe.equipcatalog(pe.access,item,inven)
    for x in inven:
      if poo.lower() == x.lower():
        item = x
        if inven == you.weaponinventory:
          pe.equipcatalog(pe.weap,item,inven)
        elif inven == you.helminventory:
          pe.equipcatalog(pe.head,item,inven)
        elif inven == you.chestinventory:
          pe.equipcatalog(pe.body,item,inven)
        elif inven == you.bootsinventory:
          pe.equipcatalog(pe.lower,item,inven)
        elif inven == you.accessinventory:
          pe.equipcatalog(pe.access,item,inven)
        break
  
  def changeequip(self,pe):
    nice = 0
    while nice == 0:
      print("\n"+pe.NAME+"'s Base Stats:\nHP:",str(pe.HP)+"\nMP:",str(pe.MP)+"\nMRG:",str(pe.MRG)+"\nAT:",str(pe.AT)+"\nDF:",str(pe.DF)+"\nMAT:",str(pe.MAT)+"\nMDF:",str(pe.MDF),"\nSP:",str(pe.SP)+"\nAC:",str(pe.AC)+"\nEV:",str(pe.EV)+"\nCT:",str(pe.CT)+"\nAPN:",str(pe.APN)+"\nMPN:",str(pe.MPN))
      if pe.isomode == True:
        print("ISO:",str(pe.isopoints))
      damn = input("\nWhat do you want to equip?\n(1) Headgear  (2) Bodygear  (3) Lowergear\n(4) Weapon  (5) Accessory  (6) Exit\nAction: ")
      if damn == "1" or damn.lower() == "headgear":
        if len(you.helminventory) == 0 and pe.head != "":
          pe.equipcatalog(pe.head,"",you.helminventory)
        elif len(you.helminventory) == 0:
          print("\nYou have no headgear!")
        else:
          self.eqs(pe,you.weaponinventory)
      if damn == "2" or damn.lower() == "bodygear":
        if len(you.chestinventory) == 0 and pe.body != "":
          pe.equipcatalog(pe.body,"",you.chestinventory)
        elif len(you.chestinventory) == 0:
          print("\nYou have no bodygear!")
        else:
          self.eqs(pe,you.chestinventory)
      if damn == "3" or damn.lower() == "lowergear":
        if len(you.bootsinventory) == 0 and pe.lower != "":
          pe.equipcatalog(pe.lower,"",you.bootsinventory)
        elif len(you.bootsinventory) == 0:
          print("\nYou have no lowergear!")
        else:
          self.eqs(pe,you.bootsinventory)
      if damn == "4" or damn.lower() == "weapon":
        if len(you.weaponinventory) == 0 and pe.weap != "":
          pe.equipcatalog(pe.weap,"",you.weaponinventory)
        elif len(you.weaponinventory) == 0:
          print("\nYou have no weapons!")
        else:
          self.eqs(pe,you.weaponinventory)
      if damn == "5" or damn.lower() == "accessory":
        if len(you.accessinventory) == 0 and pe.access != "":
          pe.equipcatalog(pe.access,"",you.accessinventory)
        elif len(you.accessinventory) == 0:
          print("\nYou have no accessories!")
        else:
          self.eqs(pe,you.accessinventory)
      if damn == "6" or damn.lower() == "exit":
        nice = 1
      
  def upgrades(self,pe):
    None

  def campexit(self):
    global sad
    global nextr
    sad = 0
    if self.RID == 6 or self.RID == 25:
      ro = rd(2)
      nextr = ro.ROOM
      nextro = ro
    if self.RID == 27:
      ro = rd(8)
      nextr = ro.ROOM
      nextro = ro
    if self.RID == 4:
      nah = 0
      while nah == 0:
        yi = input("\nExit where?\n(1) F-Wing Hallway 1st Floor  (2) F-Wing Hallway 2nd Floor\nAction: ")
        if yi == "1":
          ro = rd(1)
          nextr = ro.ROOM
          nextro = ro
          nah = 1
        if yi == "2":
          ro = rd(5)
          nextr = ro.ROOM
          nextro = ro
          nah = 1
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

    if self.RID == 6:
      if "All Hail..." in quests:
        if subject == "Julius":
          text("\n*Ishraq approaches Julius*","Ishraq, throwing a hand signal: Yo","Julius, looking up from his non-functional phone: So we gonna find that straight edge or what?","Ishraq, crossing his arms: Whenever you're ready.","Julius, looking back at his phone: I'll follow you out the door once you're good to go.")
          questssys("The Straight Edge","Start")
          you.team.append(Julius)
          you.teamS.append("Julius")
          self.people.remove(subject)
        if subject == "Edmond":
          text("\n*Ishraq approaches Edmond*","Ishraq, wrapping his arm around Edmond: How's Kelly?","Edmond: She's breathing, so she ain't dead.","Ishraq: Think she needs anything?","Brandon, examining: She has some bruises, and she's bleeding a little. Gotta get her something.","Ishraq, ready to help: I'll head to the F-Wing nurse and find something. You guys coming?","Edmond: I'm coming with you.")
          questssys("The FX-Wing Nurse","Start")
          supu("Edmond",11)
          for x in you.supportback:  
            you.supportteam.append(x)
            you.supportteamS.append(x.name)
            you.supportback.remove(x)
          self.people.remove("Edmond")
          self.people.remove("Brandon")
        if subject == "Brandon":
          text("\n*Ishraq approaches Brandon*","Ishraq, touching Brandon's shoulder: How's Kelly?","Brandon, biting his nails: She's breathing alright.","Ishraq, looking at Edmond: Think she needs anything?","Edmond, looking a little nervous: She has some bruises and cuts. They look kinda bad.","Ishraq, ready to help: I'll head to the F-Wing nurse and find something for her. You guys coming?","Brandon: I'll go with you.")
          supu("Brandon",21)
          for x in you.supportback:  
            you.supportteam.append(x)
            you.supportteamS.append(x.name)
            you.supportback.remove(x)
          questssys("The FX-Wing Nurse","Start")
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
            questssys("The FX-Wing Nurse","Finish")
            xpg(200)
            you.questinventory.remove("Ice Pack")
            if "Ruler" in you.questinventory:
              eventcheck()
          else:
            text("\nIshraq, staring at Kelly resting: Gotta go to the Nurse's office.")

      if subject == "David":
        if data[12] == 0:
          text("\n*Ishraq approaches David*","Ishraq, curious: What happened?","David, yelling in frustration: My birthday circuit! I was almost done! It's messed up now!","Ishraq, laughing: David, we're already working on arduino and you're still working on your birthday circuit? What the hell?","David, ordering his wires: Chill, I was almost done.","Ishraq, wanting to help: Yo, just give me your K-maps and I'll wire it for you.","David, determined: NO! I need to do this myself.","Ishraq, proud: Good. If you need help, I'm here.")
          data[12] = 1
        else:
          text("\n*Ishraq approaches David*","Ishraq, checking on David: You good?","David, working hard: Yeah.")

      if subject == "Metin":
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
          
      
      if subject == "Hassan":
        text("\n*Ishraq approaches Hassan*","Ishraq, pumped: You ready to get out there and trash these kids?","Hassan, also pumped: Yeeah, these wired ****** be pissin' me off. We fought some on our way down, and god DAMN they're strong!","Ishraq, shrugging: Hey, we've got to get power in numbers to save this school, and you can always help.","Hassan: Ight' bet. I'm about to cook these dudes.")
        supu("Hassan",21)

      if subject == "Noah":
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
          elif data[0] >=3:
            boop = input("\n(1) What are all these books?  (2) Sup.\nResponse: ")
          else:
            boop = "0"
            text("\nIshraq, looking at all the books Kelly gathered: What are all these books?","Kelly, looking back at Ishraq: I'm stealing books.","Ishraq, raising an eyebrow: For what?","Kelly, staring: To read them?","Ishraq, confused: Read?","Kelly, dumbfounded: Yeah, read. That's what you do with books.","Ishraq, shrugging: Who actually reads? I haven't read a single one of the class books for English. Sparknotes yo.","Kelly, also shrugging: Okay...good luck in English.","Ishraq, smirking: General. Screw Honors or Lang.")
          if boop == "1":
            text("\nIshraq, looking at all the books Kelly gathered: What are all these books?","Kelly, looking back at Ishraq: I'm stealing books.","Ishraq, raising an eyebrow: For what?","Kelly, staring: To read them?","Ishraq, confused: Read?","Kelly, dumbfounded: Yeah, read. That's what you do with books.","Ishraq, shrugging: Who actually reads? I haven't read a single one of the class books for English. Sparknotes yo.","Kelly, also shrugging: Okay...good luck in English.","Ishraq, smirking: General. Screw Honors or Lang.")
          elif boop == "2" and data[15] == 1 and data[0] >= 3 :
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
            text("\nIshraq, taking notice of a glowing book: Huh?","\n*Ishraq takes the book from the shelf and reads the title*\n","Ishraq: Isometric Drawings by Wycliffe A. Graham! What the hell? Graham wrote this? Or is it that...","\n*The book starts to rattle and flies out of Ishraq's hands, falling to the ground*\n","Ishraq, intrigued: Does Graham have something to do with the iso-stones?","\n*Ishraq tries to pick up the book, but it vibrates violently in his hands*\n","Ishraq, connecting the pieces: It's the same as when Kelly touched the stone in shop...")
            talk = "1"
            while talk == "1":
              boop = input("\n(1) Kelly!  (2) Julius!\nResponse: ")
              if boop == "1":
                text("\nIshraq, shouting across the room: Kelly!","Kelly, responding: Yeah?","Ishraq: Come take a look at this book.","\n*Kelly walks over to Ishraq*\n","Kelly, tapping Ishraq: What did you find?","Ishraq, pointing at the book at the floor: Look...it's inching towards you.","Kelly, curious: Wow, that's so cool!..It's also called Isometric Drawings by Wycliffe A. Graham...as in Dr. Graham?","\n*Kelly picks up the book*\n","Ishraq, thinking about it: Yeah, I find it very strange. Dr. Graham never metioned writing a book, and I doubt he would write it on isometric drawings.","Kelly: Then what do you think is going on?","Ishraq, concluding: No idea, but Graham is definitely connected to what's going on.","Kelly, agreeing: Definitely...now let's see what this book is so excited for.","\n*Kelly opens the book, and a magenta light radiates from it. The book drags Kelly into it, enveloping her! The book turns through all of its pages quickly and finally closes. A holographic light shines from the book, and Kelly's body reconstructs in the shape of magenta outlined geometric planes.*\n","Ishraq, not surprised: Well well well, look who's an Iso-wielder now.",fore.MAGENTA_1 + style.BOLD +"Kelly, feeling the power: Oh my god, I feel so alive right now!"+style.RESET,"\n*Julius runs over to see what's going on*\n","Julius, looking at the magenta aura around Kelly: YOU GOT AN ISO? SHEEESH!","\n*Kelly's calligraphy pen appears before her inside the book*\n",fore.MAGENTA_1 + style.BOLD + "Kelly, astonished: Hey! This was just in my bookbag!"+ style.RESET,"\n*Kelly touches the pen and feels its energy*\n",fore.MAGENTA_1 + style.BOLD + "Kelly, feeling comfort: It's filled with some type of power. I feel it."+style.RESET,style.BOLD + fore.MAGENTA_1 + back.GREY_100+"\n~Kelly has gained a new ability, Calligraphy! She utilizes the power within her magic calligraphy pen to attack enemies with high accuracy magic damage with written spells!\n" + style.RESET)
                talk = "2"
              elif boop == "2":
                text("\nIshraq, shouting across the room: Julius!","Julius, shouting back: What?!","Ishraq: Come check this out.","\n*Julius runs over to Ishraq*\n","Julius: Yeah?","Ishraq, looking at the book: Look at that book...****'s moving.","Julius, happy: Hey! It looks like it's comin' to me! Didn't Kelly say that the stone she found was going towards you?","Ishraq, nodding: Yeah, she did. Read the cover though.","Julius, crouching down: Isometric Drawings by Wycliffe A. Graham. As in GRAHAM?! HaHAA!","Ishraq, laughing: Heheh, yeah. I find it kind of weird too.","Julius, memeing: We all already knew Graham is god, so he's probably behind all this.")
                if data[15] == 1:
                  text("Ishraq, skeptical: Nah, I don't think he's causing all this...has to be the Fedora Man.")
                else:
                  text("Ishraq, taking it into consideration: Maybe, but I doubt it. Graham would never do this.")
                text("\n*Julius tries to pick up the book, but it starts shaking violently*\n","Julius, confused: What gives?","Ishraq, mentioning: Kelly also said when she picked up my Iso, it shook violently in her hands...","Julius, disappointed: Damn.","Ishraq, shouting across the room.: Kelly!","\n*Kelly walks over to Ishraq*\n","Kelly, responding: What?","Ishraq, pointing at the book at the floor: Look...it's inching towards you.","Kelly, curious: Wow, that's so cool!..It's also called Isometric Drawings by Wycliffe A. Graham...as in Dr. Graham?","\n*Kelly picks up the book*\n","Ishraq, confirming: Yeah, it's weird. Me and Julius think he's involved in some way","Kelly, agreeing: Definitely...now let's see what this book is so excited for.","\n*Kelly opens the book, and a magenta light radiates from it. The book drags Kelly into it, enveloping her! The book turns through all of its pages quickly and finally closes. A holographic light shines from the book, and Kelly's body reconstructs in the shape of magenta outlined geometric planes.*\n","Ishraq, not surprised: Well well well, look who's an Iso-wielder now.",fore.MAGENTA_1 + style.BOLD + "Kelly, feeling the power: Oh my god, I feel so alive right now!" + style.RESET,"\n*Kelly's calligraphy pen appears before her inside the book*\n",fore.MAGENTA_1 + style.BOLD + "Kelly, astonished: Hey! This was just in my bookbag!"+ style.RESET,"\n*Kelly touches the pen and feels its energy*\n",fore.MAGENTA_1 + style.BOLD + "Kelly, feeling comfort: It's filled with some type of power. I feel it."+style.RESET,style.BOLD + fore.MAGENTA_1 + back.GREY_100+"\n~Kelly has gained a new ability, Calligraphy! She utilizes the power within her magic calligraphy pen to attack enemies with high accuracy magic damage with written spells!\n" + style.RESET)
                talk = "2"
            Kelly.learnskill("Calligraphy")
            text("Ishraq:","Ishraq, suddenly suspecting: Too convenient though. Exactly where you said you think it was, you found your isometric drawing Kelly. Someone's listening to us.",fore.MAGENTA_1 + style.BOLD +"Kelly, shocked: Woah, you're right. This is kind of creepy."+style.RESET,"Julius, taking it different: Creepy? This means I should get mine in the Automotive Building! Let's go!","Ishraq: Yeah.")
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
          text("\nIshraq, opening the drawers of the front desk: Just some pencils...more weapons I guess.")
          additem("Pencil",2,you.weaponinventory)
          self.objects.remove("Front Desk")
          
    if self.RID == 25:

      if "The FX-Wing Nurse" in quests:
        if data[13] == 0:
          if subject == "Julius":
            text("\nIshraq, approaching Julius while still jittery: This is a mess.","Julius, calm: It is what it is...damn this is gonna stink.","Ishraq, planning for the future: We shouldn't leave the body in here. We could use this office.","Julius, not sure: I don't know...this office is kinda far. I think we should just loot this place and bring all the supplies to our shop room.","Ishraq, thinking even farther: How about when we get like a quarter of the school saved? That's like 1,000 kids. This office is a good place.","Julius, kinda getting it: Makes sense. Then where should we put the body?","Ishraq, thinking: Hmm...maybe just leave it outside. Just open the door to where the STEM building is being made.","Julius, laughing: HaHAA~! So were just gonn' throw her there?","Ishraq, smirking: You can do that. I still got **** to look for.","*Julius drags the body outta the room to finish the job*")
            self.people.remove("Julius")
          if subject == "File Cabinet":
            text("\nIshraq, to himself: Kelly got like what...a concussion? Head trauma? A, B, C...concussions.","*Ishraq reads the file*","Ishraq: This is just saying to get rest. **** it. I'ma just get Kelly an ice-pack.")
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
            input("\nJulius, to himself: Kelly has a concussion. Da **** am I looking here for, I need ice~!")
            self.objects.remove("File Cabinet")
            self.objects.append("Fridge")
          if subject == "Fridge":
            text("\n*Julius opens fridge and takes an ice pack. He wraps it in towel paper*","Julius, joking to himself: After I give this to Kelly, she'll accept me as her knight in shining armor, HaHAA~!")
            additem("Ice Pack",1,you.questinventory)
            self.objects.remove("Fridge")
          if subject == "Nurse" and self.TYPE == "Camp":
            text("\n*Julius slaps the nurse*","Julius, rubbing the nurse's face: Hello?","Julius, scratching himself: She's still unconscious.")
            if "Ice Pack" in you.questinventory:
              text("\n*Julius slaps Kelly's ice pack onto the Nurse's head*","*The Nurse awakens*","Julius, celebrating: YES~! HaHAA! I didn't expect that to work. I was just playing around.","The Nurse, drunk: Que diablos? Who are you? Shouldn't you be in class?","Julius, grinning: ~Keloke mamasita~.","The Nurse: Ai dios mio! What kind of dream is this?","Julius, still trying to keep a 'seductive' grin: The best kind.","The Nurse: Boy...I'll give you a chance. You can go back to class, and I will not report you.","Julius, laughing: HaHAA~! I didn't even do anything yet!","The Nurse, looking around: ...was there a fight in here?","Julius, still screwing around: Yer'. You and I played rough together...tsk tsk.","The Nurse, gagging: The hell did you drug me with!? There's no way I would **** with you!","Julius, done messing around: Okay, okay~! Relax! Haha...okay, so here's what really happened. You were going insane. Me and my friend laying over there had to fight you. Once we knocked you out, you got back to normal. Thing is, you injected this needle into him, and he started spazzing out. Now, he's almost like dead. I need you to help him.","The Nurse, giving Julius an unbelieving stare: You know what? I will check your friend out. But if you don't go back to class in 5 seconds, I'm calling the cops.","Julius, understanding: *Sigh*...alright, let me explain to you everything that's happening right now in this school.")
              input("\n*Julius explains the whole situation*")
              text("\nThe Nurse, serious: I don't know why you're still here or why I haven't done anything, but your stories are entertaining at best. If you're trying to cut class, I suggest you leave right now because I'm not giving you a pass.","Julius, also serious, picking up the syringe: Look at the stuff dripping out of this...its a glowing cyan-ish color. This don't look real right?","The Nurse, glaring at the needle Julius handed to her: Is this the **** you drugged me with?","Julius, grinning: COME ON! Just believe me already, HaHAA! My friend needs help!","*The nurse moves over to Ishraq, evaluating him*","The Nurse, shocked: He's in a state of paralysis! He's awake right now too! Ooh! I don't know how to help him! He needs to go to a doctor right now!","Julius, laughing: HaHAA~! Nurses...","The Nurse, still not chill with Julius: Shut up son. There is no cure for paralysis, but let's get him laying on the bed.","\n*The Nurse and Julius heave Ishraq onto a bed...time passes*","\nJulius, thinking out loud: He's down for good I guess...you said he was awake right?","The Nurse, still helping Ishraq in all ways she could: I've iced his muscles...massaged him for any stimulation...he can't even move his mouth.","*The nurse looks at the sample collected from the syringe*","The Nurse, talking to Julius: Do you know what this stuff is and where it came from?")
              if data[15] == 1:
                text("Julius, bringing up a past thought: Maybe...The Fedora Man, the guy who's trying to take revenge on our school must've dosed you. He probably knew all this was gonna happen.")
              else:
                text("Julius, thinking: Not sure...but something weird is definitely happening. The guy who tried kidnapping this girl I know has to have something to do with this.")
              text("*Heavy banging is heard from the door*","Julius, smirking: Wait here...I'll take care of these zombies.","The Nurse, worried: Wait! Make sure to be well rested before going out there!","\n~The FX-Wing Nurse has been unlocked. You can heal your health here at anytime.")
              self.TYPE = "Nurse"
          if subject == "Nurse" and self.TYPE == "Nurse":
            if data[14] == 0:
              text("\nThe Nurse, introducing herself: Oh, I forgot to mention, my name is Nurse Urquizo. Be careful out there, and make sure to use whatever you need.","Julius, ready: Thanks!","*Julius takes some medical supplies*")
              additem("Med-Kit",3,you.consumeinventory)
              additem("Bandages",10,you.consumeinventory)
              data[14] = 1
            elif data[14] == 1:
              text("\nNurse Urquizo, welcoming: Make sure to get some rest!")
    
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
        
      
          
  def randomencounter(self):
    global weight
    tis = random.randint(1,100)
    if tis <= self.ENC:
      ag = random.randint(1,100)
      print("!!!")
      dam = input("\nEnemies approach!\n(1) Fight  (2) Run\nAction: ")
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
        battle(you,bots,Cont=False)
      elif dam == "2" or dam.lower() == "run":
        time.sleep(0.5)
        print("\n*The team runs from the battle*")

class Support:
  def __init__(self,name,cd):
    self.name = name
    self.cd = cd   #cooldown
    self.ccd = 0   #current cooldown

  def use(self):
    self.ccd = self.cd

  def supporttimers(self):

    if self.ccd > 0:
      self.ccd = self.ccd - 1
      if self.ccd == 0:
        time.sleep(0.5)
        print("\n"+self.name,"is ready!")

def supu(name,cd):
  print("\n"+name,"has been unlocked as a support character!")
  you.supportback.append(Support(name,cd))

def teamskill():
  global Ishraq
  global Kelly
  global Julius
  global Tim
  global Daniel
  global Arwyn
  global Shah
  global Amira
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
    x.fal = Shah.fal
    x.progo = Shah.progo
    x.armw = Shah.armw
    x.infe = Shah.infe
    x.selfd = Shah.selfd
    x.chad = Shah.chad
    x.hate = Amira.hate
    x.suc = Amira.suc
    x.powers = Amira.powers
    x.telep = Amira.telep
    x.mimi = Amira.mimi
    x.desp = Amira.desp
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
    x.fal = Shah.fal
    x.progo = Shah.progo
    x.armw = Shah.armw
    x.infe = Shah.infe
    x.selfd = Shah.selfd
    x.chad = Shah.chad
    x.hate = Amira.hate
    x.suc = Amira.suc
    x.powers = Amira.powers
    x.telep = Amira.telep
    x.mimi = Amira.mimi
    x.desp = Amira.desp

def additem(item,amount,storage):
  for x in range(amount):
    storage.append(item)
  print("\n"+str(amount)+"x",item,"was added into your inventory.")

def wimple(ints,direct):
  global sad
  sad = 0
  if direct == "Team":
    for x in you.backteam:
      if x.NAME in you.backteamS[ints]:
        quickswitch(x,direct)
        break
  elif direct == "Backteam":
    for x in you.team:
      if x.NAME in you.teamS[ints]:
        quickswitch(x,direct)
        break

def teamswitch():
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
          wimple((int(come)-1),"Team")
          wop = 1
      for x in you.backteam:
        if come.lower() == x.NAME.lower() and x.NAME in you.backteamS:
          quickswitch(x,"Team")
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
          wimple((int(wow)-1),"Team")
          wop = 1
      for x in you.backteam:
        if wow.lower() == x.NAME.lower() and x.NAME in you.backteamS:
          quickswitch(x,"Team")
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
          wimple((int(wow)-1),"Backteam")
          wop = 1
      for x in you.team:
        if wow.lower() == x.NAME.lower() and x.NAME in you.teamS:
          quickswitch(x,"Backteam")
          wop = 1
      if wop != 1:
        continue
      else:
        nudes = 2
  elif len(you.team) < 4 and len(you.backteam) == 0:
    print("\nTeam:")
    print(you.teamS)
    print("\nYou do not have enough members to switch anyone out.")
    
def forceswitch(ally,bat=False):
  if ally in you.team:
    quickswitch(ally,"Force",bat)
    if len(you.backteam) > 0:
      teamswitch()
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


def revival(ally,MID=False,o=False):
  ally.cHP = ally.HP
  ally.cMP = ally.MP
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

def questssys(quest,soc):
  if soc == "Start":
    quests.append(quest)
    input("\nYou started the quest |"+quest+"|")
  elif soc == "Finish":
    quests.remove(quest)
    input("\n|"+quest+"| quest complete!")
    qcomp.append(quest)

def text(yes1,yes2="",yes3="",yes4="",yes5="",yes6="",yes7="",yes8="",yes9="",yes10="",yes11="",yes12="",yes13="",yes14="",yes15="",yes16="",yes17="",yes18="",yes19="",yes20="",yes21="",yes22=""):
  input(yes1)
  if yes2 != "":
    input(yes2)
  if yes3 != "":
    input(yes3)
  if yes4 != "":
    input(yes4)
  if yes5 != "":
    input(yes5)
  if yes6 != "":
    input(yes6)
  if yes7 != "":
    input(yes7)
  if yes8 != "":
    input(yes8)
  if yes9 != "":
    input(yes9)
  if yes10 != "":
    input(yes10)
  if yes11 != "":
    input(yes11)
  if yes12 != "":
    input(yes12)
  if yes13 != "":
    input(yes13)
  if yes14 != "":
    input(yes14)
  if yes15 !="":
    input(yes15)
  if yes16 !="":
    input(yes16)
  if yes17 !="":
    input(yes17)
  if yes18 !="":
    input(yes18)
  if yes19 !="":
    input(yes19)
  if yes20 !="":
    input(yes20)
  if yes21 !="":
    input(yes21)
  if yes22 !="":
    input(yes22)

def battle(p1,p2,Cont=None,Mid=None):
  global bots
  global sad
  global fightmod
  global victory
  global allfighters
  global lastat
  global player1
  global player2
  winc = False
  victory = 0
  if Mid == True:
    for x in p1.team: 
      x.midbattlesave()
    for x in p1.backteam:
      x.midbattlesave()
    p1.cteam = []
    p1.cbackteam = []
    p1.cdeadteam = []
    for x in p1.team:
      p1.cteam.append(x)
    for x in p1.backteam:
      p1.cbackteam.append(x)
    for x in p1.deadteam:
      p1.cdeadteam.append(x)
  for x in p2.team:
    p2.teamC.append(x)
  for x in p2.backteam:
    p2.backteamC.append(x)
  for x in p2.team:
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
      player1.teamID.append(x.ID)
    for x in player1.deadteam:
      allfighters.append(x)
      player1.teamID.append(x.ID)
      x.resttimer = 21 - x.res
    for x in player2.backteam:
      allfighters.append(x)
      player2.teamID.append(x.ID)
    for x in player2.deadteam:
      allfighters.append(x)
      player2.teamID.append(x.ID)
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
    for x in player1.supportteam:
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
            player1.teamID.remove(x.ID)
            if x.NAME in player1.teamS:
              player1.teamS.remove(x.NAME)
            player1.deadteam.append(x)
            player1.deadteamS.append(x.NAME)
      if len(player1.team) < 4 and len(player1.backteam) > 0:
        teamswitch()
      if len(player1.team) == 0 and len(player1.backteam) == 0:
        break
      for x in player1.deadteam:
        if x.re == True:
          x.resttimer = x.resttimer - 1
          if x.resttimer == 0:
            x.cHP = round((0.10+(0.05*x.res))*x.HP)
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
            player2.teamID.remove(x.ID)
            if x.NAME in player2.teamS:
              player2.teamS.remove(x.NAME)
            player2.deadteam.append(x)
            player2.deadteamS.append(x.NAME)
      if len(player2.team) == 0:
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
      for x in player1.supportteam:
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
            savereset()
            sad = 1
            winc = True
            poop = 1
            bots = Player()
        if redux == "1":
          continue
      if Cont == True:
        winc = True

def prebattleevent(p1,p2):
  for x in p2.team:
    if x.NAME == "Amira":
      forceswitch(Kelly,True)
      forceswitch(Amira,True)
    elif x.NAME == "Brandon" and x.HP == 60:
      Ishraq.learnskill("Wild Instinct")
      Ishraq.WI = True
      Ishraq.wild = 4
      forceswitch(Kelly,True)
      print("\nIshraq instantly taps into his wild instincts, increasing his attack, speed, evasion, and critical chance, but reducing his magic attack, magic defense, and accuracy! His body starts to damage itself!",fore.YELLOW_1 + style.BOLD+"(NO NEED TO ACTIVATE SKILL!!!)"+style.RESET)
    elif x.NAME == "Julius" and x.HP == 70:   
      Ishraq.WI = True
      Ishraq.wild = 4
    elif x.NAME == "Miguel":
      for x in range(4):
        Julius.battleinventory.append("Bandages")
        Ishraq.battleinventory.append("Bandages")
      Julius.learnskill("Runner's High")
      Julius.run = 0

def battleevent(p1,p2):
  if "Kelly" in p2.teamS and Kelly not in p2.team and "Amira" not in p2.teamS:
    p2.team.append(Kelly)
  if Ishraq.immortal > 0 and Ishraq.cHP <=0:
    time.sleep(1)
    print("\nIshraq gets back up!")
    Ishraq.cHP = 1
    if Ishraq not in p1.team:
      p1.team.append(Ishraq)
      p1.teamS.append(Ishraq.NAME)
      p1.deadteam.remove(Ishraq)
      p1.deadteamS.remove(Ishraq.NAME) 
  if Julius.ISOmode == True:
    if Julius.cHP <=0:
      Julius.ISOmode = False
      Julius.cHP = Julius.HP
      Julius.isoboost = 6
      Julius.isoboostL = 1
      Julius.runhigh = Julius.runhigh = 21
      time.sleep(1)
      print("\n"+Julius.NAME,"embraces his eternal will, standing back up to fight! He is fully powered-up by the runner's high and the isometric drawings!")
      Julius.Isopower(True)
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
    for x in p2.team:
      if x.NAME == "Richard":
        if Ishraq.cHP <= round(0.5*Ishraq.HP) and Kelly not in p1.team and fightmod == 1:
          p1.team.append(Kelly)
          p1.teamS.append("Kelly")
          p1.teamID.append(Kelly.ID)
          allfighters.append(Kelly)
          time.sleep(0.4)
          print("\nKelly: I'm here Ishraq!")
        elif fightmod == 3:
          Ishraq.Q1B = 1
  for x in p2.team:
    if x.NAME == "Mr. Pudup":
      x.stunimmune = True
  if "The FX-Wing Nurse" in quests:
    for x in p2.team:
      if x.NAME == "Miguel" and data[13] == 1 and Julius.cHP < Julius.HP and Ishraq not in p1.team:
        text("\n*Ishraq charges through the fight*","Ishraq, pumped up: YOU THOUGHT I WAS GONNA LET YOU ONLY FIGHT?!","Julius, grinning: Ayy~! Come on, we got this!")
        revival(Ishraq)
        p1.teamID.append(Ishraq.ID)
        allfighters.append(Ishraq)
  if "The Straight Edge" in quests:
    for x in p2.team:
      if x.NAME == "Hassan" or x.NAME == "Metin" or x.NAME == "Noah":
        x.confused = 99

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
  bots.teamS.append(ename)

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
  if questorbattle == "Battle":
    for x in bots.deadteam:
      if x.NAME == "Richard":
        xpg(50)
      if x.NAME == "Amira":
        xpg(5000)
      if x.NAME == "Ryca":
        xpg(50)
      if "Nurse" in x.NAME:
        xpg(50)
      if "Freshman" in x.NAME:
        xpg(3)
      if "Sophomore" in x.NAME:
        xpg(6)
      if "Junior" in x.NAME:
        xpg(10)
      if "Senior" in x.NAME:
        xpg(15)
  

def xpg(amount):
  for x in you.team:
    x.XP = x.XP + amount
  for x in you.backteam:
    x.XP = x.XP + round(amount/2)
  for x in you.deadteam:
    x.XP = x.XP + round(amount/4)

def save(load):
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
  global Shah
  global Amira
  global you
  if load == "save":
    os.remove('saves.txt')
    with open('saves.txt', 'wb') as f:
      pickle.dump([you,world,croom,Ishraq,Julius,Kelly,Daniel,Tim,Arwyn,Shah,Amira,croom,data,quests,qcomp], f, protocol=2)
  if load == "load":
    with open('saves.txt', 'rb') as f:
      you,world,croom,Ishraq,Julius,Kelly,Daniel,Tim,Arwyn,Shah,Amira,croom,data,quests,qcomp = pickle.load(f)
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
  Shah.savedstats()
  Amira.savedstats()
  you.teamC = []
  you.deadteamC = []
  you.backteamC = []
  for x in you.team:
    you.teamC.append(x)
  for x in you.deadteam:
    you.deadteamC.append(x)
  for x in you.backteam:
    you.backteamC.append(x)

def savereset(Con=""):
  if Con == "Mid":
    Ishraq.saverest(you,bots,"Mid")
    Kelly.saverest(you,bots,"Mid")
    Julius.saverest(you,bots,"Mid")
    Arwyn.saverest(you,bots,"Mid")
    Tim.saverest(you,bots,"Mid")
    Daniel.saverest(you,bots,"Mid")
    Shah.saverest(you,bots,"Mid")
    Amira.saverest(you,bots,"Mid")
  else:
    Ishraq.saverest(you,bots)
    Kelly.saverest(you,bots)
    Julius.saverest(you,bots)
    Arwyn.saverest(you,bots)
    Tim.saverest(you,bots)
    Daniel.saverest(you,bots)
    Shah.saverest(you,bots)
    Amira.saverest(you,bots)
  you.team = []
  you.teamS = []
  you.deadteam = []
  you.deadteamS = []
  you.backteam = []
  you.backteamS = []
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

def preeventcheck():
  global sad
  global enemy1
  global enemy2
  global enemy3
  global enemy4
  global enemy5
  global nextr
  global fightmod
  global team
  global teamS
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
        if "Brandon" in you.supportteamS:
          time.sleep(0.5)
          text("\nIshraq, opening the door: Let's head out.","Brandon, walking over: Followin'","Julius, having fun with stereotypes: How we gonna leave these two kids alone? They're gonna jank everything in here, haHAA!","Edmond, with a slight smile: I might honestly take Miller's hall passes.","Brandon, already outside: Let's go already.","Ishraq, looking at Julius: Alright, we should check my calc room for a ruler, bound to have one.","Julius, pointing up: It's upstairs right?","Ishraq, bringing up different objectives: Yeah, Mrs. Wells's classroom, or we could go to the nurse's office down the hall.")
        elif "Edmond" in you.supportteamS:
          text("\nIshraq: Let's head out.","Edmond, walking over: Followin'","Julius, making fun of Brandon's height and appearence: How we gonna leave Groot with David? He can't help David if he can't speak, haHAA!","Brandon, laughing: That's whack.","Julius: I am groot!","Edmond, already outside: Let's go already.","Ishraq, looking at Julius: Alright, we should check my calc room for a ruler, bound to have one.","Julius, pointing up: It's upstairs right?","Ishraq, bringing up different objectives: Yeah, Mrs. Wells's classroom, or we could go to the nurse's office down the hall.")
        xpg(100)
        questssys("All Hail...","Finish")
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
    questssys("Feeling Alone","Start")
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
      sad = 1




def eventcheck():
  global sad
  global enemy1
  global enemy2
  global enemy3
  global enemy4
  global enemy5
  global nextr
  global fightmod
  global team
  global teamS
  global victory
  global fi
  global dif
  victory = 0
  if croom[0].RID == -1:
    victory = 0
    if fi == "1":
      print("\n*Story excerpt for a future event in the game*")
      time.sleep(1)
      print("\n*The group enters the Auditorium*")
      time.sleep(1)
      text("\nAmira, theatrically: It's about time you all came...finally here to take away my gift? The only thing I have left?","Ishraq, done with Amira's stupidity: Don't you get it!? The fedora man is using your *** to take us out!","Kelly, trying to reason: He's not your friend just because he gave you these powers! And we're not your enemies for trying to stop you!","Amira, determined she figured it out: I get it...only you six get to be extraordinary and powerful...no one else can!","Daniel, mockingly: Guys, be careful, the power's getting to her head, aaghaha!!","Amira, flustered: The power has gotten to all of your heads!","Kelly, giving up on Amira: You're honestly beyond help.","Amira, psychotically: Funny you say that Kelly. I thank you for your cooperation in advance!","Kelly, choking: What do you me...!?","*Kelly is paralyzed and dragged towards Amira by her tethers*","Amira, smiling: Your powers are now mine Kelly...prepare for The End, haters.","Arwyn, ecstatic: Yes! Kelly is finally gone!","Daniel, bursting with masculinity: MY QUEEN!! I'M COMING FOR YOU!")
      if dif == "1":
        bots.team = [Entity("Amira",7000,0,400,100,400,100,60,100,100,1,1,1,0,"17","Female Boss"),Entity("Kelly",1000,0,0,0,0,0,0,0,0,0,0,0,0,"18","Female"),Entity("Jackie",2000,0,0,0,0,0,0,0,0,0,0,0,0,"19","Female"),Entity("Abby",2000,0,0,0,0,0,0,0,0,0,0,0,0,"20","Female"),Entity("Meryem",1000,0,0,0,0,0,0,0,0,0,0,0,0,"21","Female")]
        bots.teamS = ["Amira","Kelly","Jackie","Abby","Meryem"]
        bots.team[0].callig = 4
        battle(you,bots,Cont=False)
      if dif == "2":
        bots.team = [Entity("Amira",10000,0,500,100,500,100,65,100,100,1,1,1,0,"17","Female Boss"),Entity("Kelly",1500,0,0,0,0,0,0,0,0,0,0,0,0,"18","Female"),Entity("Jackie",2000,0,0,0,0,0,0,0,0,0,0,0,0,"19","Female"),Entity("Abby",2500,0,0,0,0,0,0,0,0,0,0,0,0,"20","Female"),Entity("Meryem",1000,0,0,0,0,0,0,0,0,0,0,0,0,"21","Female")]
        bots.teamS = ["Amira","Kelly","Jackie","Abby","Meryem"]
        bots.team[0].callig = 4
        battle(you,bots,Cont=False)
      if dif == "3": 
        bots.team = [Entity("Amira",12000,0,525,100,525,100,70,100,100,1,1,1,0,"17","Female Boss"),Entity("Kelly",2000,0,0,0,0,0,0,0,0,0,0,0,0,"18","Female"),Entity("Jackie",2500,0,0,0,0,0,0,0,0,0,0,0,0,"19","Female"),Entity("Abby",3000,0,0,0,0,0,0,0,0,0,0,0,0,"20","Female"),Entity("Meryem",1500,0,0,0,0,0,0,0,0,0,0,0,0,"21","Female")]
        bots.teamS = ["Amira","Kelly","Jackie","Abby","Meryem"]
        bots.team[0].callig = 4
        battle(you,bots,Cont=False)
      if dif == "4": 
        bots.team = [Entity("Amira",24000,0,525,100,525,100,70,100,100,1,1,1,0,"17","Female Boss"),Entity("Kelly",4000,0,0,50,0,75,0,0,0,0,0,0,0,"18","Female"),Entity("Jackie",5000,0,0,65,0,60,0,0,0,0,0,0,0,"19","Female"),Entity("Abby",6000,0,0,75,0,50,0,0,0,0,0,0,0,"20","Female"),Entity("Meryem",3000,0,0,55,0,70,0,0,0,0,0,0,0,"21","Female")]
        bots.teamS = ["Amira","Kelly","Jackie","Abby","Meryem"]
        bots.team[0].callig = 4
        battle(you,bots,Cont=False)
      if dif == "5":
        bots.team = [Entity("Amira",50000,0,525,100,525,100,100,100,100,1,1,1,0,"17","Female Boss"),Entity("Kelly",10000,0,0,50,0,75,0,0,0,0,0,0,0,"18","Female"),Entity("Jackie",12500,0,0,65,0,60,0,0,0,0,0,0,0,"19","Female"),Entity("Abby",15000,0,0,75,0,50,0,0,0,0,0,0,0,"20","Female"),Entity("Meryem",7500,0,0,55,0,70,0,0,0,0,0,0,0,"21","Female")]
        bots.teamS = ["Amira","Kelly","Jackie","Abby","Meryem"]
        bots.team[0].callig = 4
        battle(you,bots,Cont=False)
    if fi == "2":
      print("\n*Story excerpt for a future event in the game*")
      text("\nIshraq, bored: It's dark in here.","Tim, jokingly: Shh..You know Mrs. Wells..she can probably hear you from a mile away.","Ishraq, bluntly: Alpaca lookin-head***","Daniel, trying to hold his laugh in: HMPpghgh..HAHAHA!","Ishraq, overly-stating: Yo, I swear, anything I say makes this kid laugh.","Julius, agreeingly: Yooo~! For real, HaHAA!","Kelly, seriously: So we're just gonna keep yelling. Arwyn's going to die because of you guys.","Daniel, flippantly: Arwyn? Nah, he's good.","\n*Everyone pays attention to Arwyn, who is trying to sneak the Orange Key from Mrs. Wells*","\nArwyn, to himself: There's no way she can see me in this darkness...on top of that I'm invisible right now.","\n*The lights suddenely turn on, and the wired Mrs. Wells awakens from her shutdown*","\nKelly, extremely frustrated: Are you kidding...everything we do, everything we think of, why is it like somebody's one step ahead of us??","Ishraq, questioning the chain of recent events: I don't know...let's just see if Arwyn can pull this off, we'll jump in if he can't.","\n*Arwyn reaches for Mrs. Wells necklace, which has the Orange key attached*","*Mrs. Wells grabs Arwyn's arm*\n","Mrs. Wells, robotically: #That was cute honey, what are you doing?#","Julius, ready for action: Guys, run in!","\n*Julius kicks the door into the room open, and the team floods into the room*","*Mrs. Wells let's go of Arwyn's arm*\n","Mrs. Wells, demonically: #Now this isn't the way to enter your Calculus class, is it?#")
      if dif == "1":
        bots.team = [Entity("Mrs. Wells",9000,0,400,120,0,200,65,150,100,10,20,0,0,"17","Female Boss")]
        bots.teamS = ["Mrs. Wells"]
        battle(you,bots,Cont=False)
      if dif == "2":
        bots.team = [Entity("Mrs. Wells",12000,0,500,140,0,250,60,175,100,10,35,0,0,"17","Female Boss")]
        bots.teamS = ["Mrs. Wells"]
        battle(you,bots,Cont=False)
      if dif == "3":
        bots.team = [Entity("Mrs. Wells",15000,0,600,160,0,300,65,200,100,10,50,0,0,"17","Female Boss")]
        bots.teamS = ["Mrs. Wells"]
        battle(you,bots,Cont=False)
      if dif == "4":
        bots.team = [Entity("Mrs. Wells",30000,0,600,160,0,300,70,200,100,25,50,0,0,"17","Female Boss")]
        bots.teamS = ["Mrs. Wells"]
        battle(you,bots,Cont=False)
    if fi == "3":
      print("\n*Story excerpt for a future event in the game*")
      if dif == "1":
        bots.team = [Entity("Mr. Pudup",11000,0,450,130,450,100,60,100,110,10,0,20,0,"17","Male Boss")]
        bots.teamS = ["Mr. Pudup"]
        battle(you,bots,Cont=False)
      if dif == "2": 
        bots.team = [Entity("Mr. Pudup",14000,0,550,150,600,125,65,120,120,10,0,35,0,"17","Male Boss")]
        bots.teamS = ["Mr. Pudup"]
        battle(you,bots,Cont=False)
      if dif == "3": 
        bots.team = [Entity("Mr. Pudup",17000,0,650,170,750,150,70,140,130,10,0,50,0,"17","Male Boss")]
        bots.teamS = ["Mr. Pudup"]
        battle(you,bots,Cont=False)
      if dif == "4":
        bots.team = [Entity("Mr. Pudup",34000,0,650,170,750,170,75,140,130,10,50,50,0,"17","Male Boss")]
        bots.teamS = ["Mr. Pudup"]
        battle(you,bots,Cont=False)
    if fi == "4":
      print("\n*Story excerpt for a future event in the game*")
      if dif == "1":
        bots.team = [Entity("Terra",8750,100,230,125,120,75,40,120,100,10,40,0,30,"17","Male Boss"),Entity("Aqua",7000,100,190,75,240,125,50,100,100,10,0,40,30,"18","Female Boss")]
        bots.teamS = ["Terra","Aqua"]
        battle(you,bots,Cont=False)
      if dif == "2":
        bots.team = [Entity("Terra",10000,100,265,150,170,100,45,120,100,10,50,0,30,"17","Male Boss"),Entity("Aqua",8000,100,230,100,300,150,55,100,120,10,0,50,30,"18","Female Boss")]
        bots.teamS = ["Terra","Aqua"]
        battle(you,bots,Cont=False)
      if dif == "3":
        bots.team = [Entity("Terra",11250,100,300,175,200,125,50,120,100,10,60,0,30,"17","Male Boss"),Entity("Aqua",9000,100,260,150,350,200,60,100,120,10,0,60,30,"18","Female Boss")]
        bots.teamS = ["Terra","Aqua"]
        battle(you,bots,Cont=False)
      if dif == "4":
        bots.team = [Entity("Terra",22250,120,350,200,200,150,50,120,100,20,60,0,30,"17","Male Boss"),Entity("Aqua",18000,150,300,150,400,250,60,100,120,10,0,60,30,"18","Female Boss")]
        bots.teamS = ["Terra","Aqua"]
        battle(you,bots,Cont=False)
    if fi == "5":
      print("\n*Story except for a future event in the game*")
      text("\nShah: Hmm?","Ishraq, ready: Dr. Graham, we are ready to test our strength against you.","\n*Dr. Graham appears from Shah's body*","\nDr. Graham, smiling: Very well. Show me your power.")
      if dif == "1":
        bots.team = [Entity("Dr. Graham",20000,100,500,200,500,200,50,150,150,0,0,0,0,"17","Male Boss")]
        bots.teamS = ["Dr. Graham"]
        battle(you,bots,Cont=False)
      if dif == "2":
        bots.team = [Entity("Dr. Graham",35000,100,750,300,750,300,50,175,175,0,0,0,0,"17","Male Boss")]
        bots.teamS = ["Dr. Graham"]
        battle(you,bots,Cont=False)
      if dif == "3":
        bots.team = [Entity("Dr. Graham",50000,100,1000,400,1000,400,50,200,200,0,0,0,0,"17","Male Boss")]
        bots.teamS = ["Dr. Graham"]
        battle(you,bots,Cont=False)
      if dif == "4":
        bots.team = [Entity("Dr. Graham",75000,100,1300,500,1500,500,50,200,200,0,0,0,0,"17","Male Boss")]
        bots.teamS = ["Dr. Graham"]
        battle(you,bots,Cont=False)
      if dif == "5":
        bots.team = [Entity("Dr. Graham",100000,125,1500,500,2000,500,55,200,200,20,0,0,0,"17","Male Boss")]
        bots.teamS = ["Dr. Graham"]
        battle(you,bots,Cont=False)
    if victory == 1:
      time.sleep(2)
      print("\nCongratulations on beating a boss! All these bosses are in their most early stages, and may be changed in the future!")
      savereset()
  #------------------------------------------------------------------------------------
  if "Origins" in quests and croom[0].RID == 0:
    time.sleep(1)
    print("\n(Press enter to continue the dialogue)")
    time.sleep(1)
    text("\nDisclaimer: Some of the dialogues in this game are meant to be satirical and unnatural. These exaggerated dialogues do not represent any of the characters in real-life.","\n~It was a normal day at the school of PCTI, commonly referred to as Tech. Daniel was walking with his fellow engineering student, Kelly, through the hallways of Tech. On their way to their next class together, a man approached them, alarming Daniel.","\nDaniel is a Dominican Peruvian 10th grade engineering student at the highschool of PCTI. He is a VEX competitor, and one of the two students, the only in engineering, to get a 5 on the AP Physics 1 exam. He is infatuated with learning and helping others, but is anything but a saint. He loves to bully people for the sheer entertainment of it, but also finds it funny to get bullied. He has no shame whatsover, being able to do absolutely wild things.","\nKelly is a Korean 10th grade engineering student at the highschool of PCTI. She is 3rd in class ranking among 894 students in the 10th grade, a SkillsUSA officer, and placed 2nd in State for FBLA. She has obsessive oragnization tendencies that lead her to be good at managing things...and people. Under her hard outlook, she is quite the whimsical character who loves to experience new things. ","\nDaniel, bombastically: You dare stand in the way of none other than the great Kelly, and I, Daniel!?","???, irreverently: Oh, I'm sorry. You see...I can't proceed, as you're blocking the entire hallway with that frame of yours.","Daniel, trying to hold in a laugh: BHGFHHGH..!! You should watch your mouth...my calibur of expertise is far above anyone's inferior intellect.","???, cheering: Ah! A fellow man of culture I see! You have such a lovely mistress walking beside you! *Blows kisses*","Daniel, suddenly serious: Yes, but she is only mine to behold...so you better back off!","Kelly, confused and weirded out: What are you even saying?","???, aggressively: *Lunges to grope Kelly*, SHE SHALL BE MINE FOR THE TAKING!!","Kelly: *Shrieks*","Daniel, hero-like: *Pushes the man away from Kelly*, NO! I WILL STOP YOU RIGHT HERE! LET THIS BE A DUEL BETWEEN US MEN!","???, with the cool-guy tone: *Tips Fedora*, So be it then.")
    print("\nDaniel begins his duel the The Fedora Man!\n")
    bots.team = [Entity("The Fedora Man",1300,0,100,40,0,40,50,100,115,6,0,0,0,"17","Male")]
    bots.teamS = ["The Fedora Man"]
    battle(you,bots,Cont=True)
    time.sleep(2)
    if Daniel.cHP <=0:
      text("\nDaniel, defeated: Please...stay away from her","???, smirking: The better man deserves the woman...she's mine now.","Daniel, desperate: No...no..NO! I can't let you do that!","*Daniel lunges at the man, knocking his fedora off*","*The man turns around and looks at Daniel*","*Daniel gasps in shock*","Daniel, astonished: No..it can't be! There's no way!","???, revengeful: I'll be taking her with me, and the end will approach all of you...you and everyone you know at this god forsaken school!","*Daniel watches as the man opens up a teleportation rift, and walks away with Kelly in hand, fainting as he watched them go*")
    else:
      text("\nDaniel, victoriously: ...The better man deserves the woman...you lost, she's rightfully mine.","???, smirking whilst on the ground: ..You think you've won..cute.","Daniel, dominatingly: Ha! Pathetic. Learn your place worm!","???, anime: You're already dead.","Daniel, confused: What?","*Daniel falls to the ground*","Daniel, holding his chest: What...did you do..?","???, cool-guy tone: Never underestimate the power of grease.","Daniel, dramatically: No...it can't be! There's only one person who can wield the power of the grub!","???, revengeful: You lose. I'll be taking her with me, and the end will approach all of you...you and everyone you know at this god forsaken school!","*Daniel watches as the man opens up a teleportation rift, and walks away with Kelly in hand, fainting as he watched them go*")
    if Daniel in you.deadteam:
      you.deadteam.remove(Daniel)
      you.deadteamS.remove(Daniel.NAME)
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
        text("\nIshraq, genuinely trying to clarify: Who are you again?","Kelly, a little surprised: Ummm...Ishraq, it's me, Kelly? The noise must've hit you hard.")
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
            text("\nIshraq, using his normal loud greetings: Oh, HI KELLY!","Kelly, shocked at Ishraq's stupidity: SHHHH!! They're still around I think!","Ishraq, adrenaline rushing to him: ...!","*CRASH*","*Ishraq is ripped out of the closet*","Kelly, crying out loud: ISHRAQ!","Ishraq, a little unnerved: AAAGH SHIT!! YO! BOWERS GOT DUMB-STRENGTH RIGHT NOW!",)
            fightmod = 1
            print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
            talk = "3"
            break
      elif meet == "2":
        text("\nIshraq, with a little brain damage: I'M THE CONDUCTOR OF THE POOP TRAIN!!","Kelly, creeped out: ...Umm, okay. Don't you recognize me? Kelly? No? There's something wrong with you, and it was probably best to leave you out in the hallway.")
        talk = "1"
        while talk =="1":
          meet = input("\n(1) Chill, I'm good.   (2) GREEEEEEEN!\nResponse: ")
          if meet == "1":
            input("\nIshraq, back to his senses: Chill, I'm good.")
            time.sleep(1)
            text("Kelly, concerned with Ishraq's frivolous attitude: Oh, wow, seriously though, this isn't the time to be stupid.","Ishraq, bluntly: Honestly, I dont't...!","*CRASH*","*Ishraq is ripped out of the closet*","Kelly, crying out loud: ISHRAQ!","Ishraq, a little unnerved: Ishraq: AAAGH SHIT!! YO! BOWERS GOT DUMB-STRENGTH RIGHT NOW!")
            fightmod = 1
            print("\nIshraq begins his duel with the mind controlled Richard!\n")
            talk = "3"
            break
          elif meet == "2":
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
                text("\nIshraq, still calm: Relax.","???, more panic: Are you delusional Ishraq? How are we supposed to relax...WHEN WE'RE GONNA DIE?!","Ishraq, subtly realizing: Oh, it's you Kelly. Sorry, I was a bit drunk. Thanks for waking me up with your yelling.","Kelly, calming down: ...No, you're right. Yelling won't do us good, I should really...!","*CRASH*","*Kelly is ripped out of the closet*","Ishraq, dumbfounded: HOLY ****! KELLY!","*Ishraq leaps into the hallway, finding Kelly laying on the ground*","Ishraq, nervous: Hey, are you good?","Kelly: ...","Ishraq, enraged: Someone's boutta get their *** merked.","*Ishraq turns around*""Ishraq, ready to swing: Richard Bowers, eh? I'll assume you didn't do that by choice. I'm still gonna merk your ***.")
                fightmod = 3
                print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
                talk = "3"
                break
              elif meet == "2":
                text("\nIshraq, breaking the ice: Can I have my phone back?","???, calming down a little: ...Here I guess. Your lock screen is funny.","Ishraq, subtly realizing: Hehe...didn't realize it was you Kelly. I was still recovering from that noise.","Kelly, easing up: Glad you're back...!","*CRASH*","*Kelly is ripped out of the closet*","Ishraq, dumbfounded: HOLY ****! KELLY!","*Ishraq leaps into the hallway, finding Kelly laying on the ground*","Ishraq, nervous: Hey, are you good?","Kelly: ...","Ishraq, enraged: Someone's boutta get their *** merked.","*Ishraq turns around*","Ishraq, ready to swing: Richard Bowers, eh? I'll assume you didn't do that by choice. I'm still gonna merk your ***.")
                print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
                fightmod = 3
                talk = "3"
                break
          elif meet == "2":
            text("\nIshraq, genuinely trying to clarify : Who are you again?","Kelly, a little surprised: Ummm...Ishraq, it's me, Kelly? The noise must've hit you hard.","Ishraq, agreeingly: Yeah, it did...its wearing off though.","Kelly, trying to make sense of Ishraq's attitude: Makes sense why you were so careless about what's happening right now.","Ishraq, correcting Kelly: Nah, it wore off by then.","Kelly, shocked: Wow...!","*CRASH*","*Kelly is ripped out of the closet*","Ishraq, dumbfounded: HOLY ****! KELLY!","*Ishraq leaps into the hallway, finding Kelly laying on the ground*","Ishraq, nervous: Hey, are you good?","Kelly: ...","Ishraq, enraged: Someone's boutta get their *** merked.","*Ishraq turns around*","Ishraq, ready to swing: Richard, eh? I'll assume you didn't do that by choice. I'm still gonna merk your ***.")
            fightmod = 3
            print("\nIshraq begins his duel with the mind controlled Richard Bowers!\n")
            talk = "3"
            break
    if fightmod == 1 or fightmod == 3:
      bots.team = [Entity("Richard",100,0,7,50,0,0,45,85,100,0,0,0,0,"17","Male")]
      bots.teamS = ["Richard"]
      battle(you,bots,Cont=True)
    if fightmod == 2:
      bots.team = [Entity("Richard",75,0,7,50,0,0,40,60,100,0,0,0,0,"17","Male")]      
      bots.teamS = ["Richard"]
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
          boop = input("\n(1) **** you mean lil bruh?  (2) Yeah, I'm good.\nResponse: ")
          if boop == "1":
            data[0] = data[0] - 1
            text("\nIshraq: **** you mean lil bruh?","Kelly, disappointed: ...I'm gonna assume you got a bit more insensitive...","Ishraq, mockingly: Stay...sucking...me.","Kelly, putting her hand over her mouth: Ew, you're gross.","Ishraq: I already nutted...and you're still sucking.","Kelly, not taking it: I'm done with you. We can go our own ways.")
            talk = "2"
            while talk == "2":
              boop = input("\n(1) BEGONE THOT!  (2) Sorry, I wasn't thinking straight!\nResponse: ")
              if boop == "1":
                text("\nIshraq, with his extremely loud voice: BEGONE THOT!","\n*Kelly ignores and leaves Ishraq, trailing off down into the FX hallway. It was the last time they met. Ishraq soon was brought under control by an unknown force. His eyes turned pale, and he became just like Richard. Whatever happened at PCTI was never found out, and The Fedora Man had gotten what he wanted. That ends the story of PCTI Lockdown...")
                time.sleep(100000)
              if boop == "2":
                text("\nIshraq, realizing his rude behavior: Sorry, I wasn't thinking straight!","Kelly, petty: ...Still not forgiving you. I never thought you would ever say things like that.","Ishraq, confused: It wasn't me though.","Kelly, speaking her heart: But it was you. It's in you.","Ishraq, weirded out a little: Okay I guess...so what now?","Kelly: There's something wrong with Richard...I don't think this school is safe right now. Do you think everyone's being controlled like this?","Ishraq, thinking it over: Maybe, you said the noise shreaked all over school...maybe through the announcements.","Kelly, impressed: Yeah, that makes sense...wow! Wait! That must mean our shop-peoples are in danger! We have to go help them quick!","Ishraq, ready: Alright, let's go!")
                talk = "3"
          elif boop == "2":
            text("\nIshraq, calmly: Yeah, I'm good.","Kelly, glad: That's good. Now we can actually talk and figure things out.","Ishraq: So what now?","Kelly, thinking: Richard was able to rip you out of the closet...there's obviously something wrong with him.","Ishraq: Agreed.","Kelly, concluding: And there's probably more people just like Richard around, so we need to get out of here fast.","Ishraq, disagreeing: Nah, not yet. We need to help people.","Kelly, in a reluctant tone: I guess...do you think everyone's being controlled like this?","Ishraq, thinking it over: Maybe, you said the noise shreaked all over school...maybe through the announcements.","Kelly, impressed: Yeah, that makes sense...wow! Wait! That must mean our shop-peoples are in danger! We have to go help them quick!","Ishraq, ready: Alright, let's go!")
            time.sleep(1)
            talk = "3"
      else:
        if fightmod == 1:
          text("\nKelly, observing Richard's unconscious body: Oh my god, what's wrong with him?","Ishraq, shrugging: I don't know...seems like somethings controlling him, at the same time, making him way stronger.","Kelly, looking at Ishraq: This is getting too dangerous...we need to get out of here before we die!","Ishraq, with a questioning tone: What about Richard? Didn't you say you came through a portal?","Kelly, with self-interest: We can't be sure if Richard is still being controlled, and yeah, I did.")
        if fightmod == 3:
          text("\nIshraq, a little worried: Yo, Kelly. Kelly. Kelly. Come on, I know you're not dead...","Kelly, regaining consciousness: ...Ishraq? What happened?","Ishraq, trying to make sense: What seems to be a mind controlled Richard ripped you out of our hiding spot, and I just beat his ***.","Kelly, recovering: Damn...I feel bruised. How'd he rip me out through a door..? Ugh, we need to get out of here quick. This is dangeorus!","Ishraq, determined: Hold on...Richard stuck his hand through it, something's making everyone abnormal. We gotta get to the center of this...didn't you say you came through a portal?","Kelly: Yeah.")
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
                data[0] = data[0] - 1
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
      bots.team = [Entity("Alex",60,0,5,20,0,0,35,120,100,1,0,0,0,"17","Male"),Entity("Satya",45,0,8,10,0,0,40,100,120,2,0,0,0,"18","Male"),Entity("Ryca",40,10,4,20,15,0,30,100,100,50,0,0,0,"19","Female")]
      bots.teamS = ["Alex","Satya","Ryca"]
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
          text("\nKelly: YER!","Ishraq: YEERR!","???: YEEERRR!","Kelly, eyes widening: ...that sounded like Julius!","Ishraq, excited: Julius is fine then, let's meet him inside!","Kelly, grabbing Ishraq: Wait!..Fine.","*Ishraq and Kelly enter their shop room*","Ishraq, scanning the student tables: There's no one here.","Kelly, pointing: Ishraq! Your left! Their eyes are pale!","Ishraq, accepting death: Aaaand we're ****ed.","*Someone shuts the door*","Kelly: Ishraq, Julius just came in! HE JUST LOCKED US IN!","Ishraq, shouting: Kelly! Distract him as much as you can!","Kelly, panicking: Distract?! What do you mean distract?!")
          talk = "2"
        elif bruh == "2":
          text("\nKelly, scared: No way!","Ishraq, acting like the door opening wasn't creepy: Why not?","Kelly, giving Ishraq a You-Serious? face: You're joking, right? This is like those traps in those horror movies.","Ishraq, trying to use common-sense: Well, this isn't a horror movie.","Kelly, using more common-sense: Yeah, it's worse...this is real life.","Ishraq, yolo: Who cares, let's just go.","*Ishraq and Kelly enter their shop room*","Ishraq, scanning the student tables: There's no one here.","Kelly, pointing: Ishraq! Your left! Their eyes are pale!","Ishraq, accepting death: Aaaand we're ****ed.","*Someone shuts the door*","Kelly: Ishraq, Julius just came in! HE JUST LOCKED US IN!","Ishraq, shouting: Kelly! Distract him as much as you can!","Kelly, panicking: Distract?! What do you mean distract?!")
          talk = "2"
        while talk =="2":
          bruh = input("\n(1) Just do something!  (2) You know...girl things!\nResponse: ")
          if bruh == "1":
            text("\nIshraq, tensing up: Just do something!","Kelly, letting her body talk: Uuuh, Julius...*punches Julius as hard as she can*","Julius: ...","Kelly, surprised at herself: Haha..HA! I punched him! ...!","*Julius gets up from the ground, sweeping Kelly and smoothly grabbing her before she falls*","Julius, singing: Isometric...Isometric...ISOMETRIC DRAAAAWWWIIINGS!","*Julius starts to dance with her*","Ishraq, laughing a bit: That's good enough? Well, no going back now, save my friends or die trying.","David, flapping his arm against his chest like a sword as if he was playing Minecraft: TEAM! TEAM! TEAM!","Edmond, screaming at David: TEEAAAAM!","Brandon, announcing to the world: I...AM...GROOOOOOT!\n")
            talk == "3"
            break
          elif bruh == "2":
            text("\nIshraq, talking as if Kelly knew what he meant: You know...girl things!","Kelly, not knowing whether to be disgusted or not: Girl things? What does that even mean?","Ishraq, recalling: Remember when Daniel leaned over the table and moved his boobs up and down to get gummy bears from Julius? Try that!","Kelly, trying to stay serious: I can't do that!","Ishraq, being serious: Just do it!","Kelly, looking down: No, I literally can't do that!","Ishraq: Why?!","Kelly, raging: You're an asshole!","Ishraq, confused: What do you mean?!","*Julius sweeps Kelly and smoothly grabs her before she falls to the ground*","Julius, singing: Isometric...Isometric...ISOMETRIC DRAAAAWWWIIINGS!","*Julius starts to dance with her*","Ishraq, laughing a bit: That's good enough? Well, no going back now, save my friends or die trying.","David, flapping his arm against his chest like a sword as if he was playing Minecraft: TEAM! TEAM! TEAM!","Edmond, screaming at David: TEEAAAAM!","Brandon, announcing to the world: I...AM...GROOOOOOT!\n")
            talk == "3"
            break
      you.team = [Ishraq]
      you.teamS = ["Ishraq"]
      bots.team = [Entity("Brandon",120,0,20,40,0,0,50,100,100,0,0,0,0,"17","Male"),Entity("David",100,0,24,30,0,0,50,100,50,0,0,0,0,"18","Male"),Entity("Edmond",110,0,22,36,0,0,50,100,100,0,0,0,0,"19","Male")]
      bots.teamS = ["Brandon","David","Edmond"]
      battle(you,bots,Cont=True)
      time.sleep(1)
      if Ishraq.cHP > 0:
        text("\nDavid: Yo, this dude hacking!","Edmond: Word.","Brandon: Turn them shits off!","Ishraq: I'm sorry, the dude playing right now learned how to read this code!","David: Well...act like your getting your *** beat right now.","Ishraq: I'll try I guess.","*Ishraq falls...*")
      text("\nIshraq, losing consciousness: Kelly...fight..","Kelly, terrified: ISHRAQ!","*Something on Mr. Pudup's desk begins to glow red, Mr.Pudup being Ishraq's and Kelly's 9th grade engineering teacher, but only Ishraq's 10th grade teacher*","Kelly, puzzled: It's projecting an isometric drawing..?","*Julius tries grabbing Kelly to resume dancing, but she bolts for the drawing*","*The piece of metal began to vibrate intensely in her hands, hurting her*","Kelly, thinking to herself: Whooah, ow! What even is this? It's projecting a red holographic isometric drawing...","*Julius jerks Kelly back to him, and she drops the device*","Kelly, desperate: No no no!","*In a last attempt, Kelly kicks the device, and it lands near Ishraq*","\n*The object begins wrapping itself upon Ishraq, completely covering his body in an unknown metal. The metal compresses his body, briefly turning him into a shining red light. His body reconstructs from red outlined geometric planes. After the reconstruction, the object sends out a final pulse of energy, weakening everyone else in the room*\n",)
      input(style.BOLD + fore.RED_1 + back.GREY_100+"~Ishraq has gained a new ability, Wild Instinct! It increases his attack, speed, evasion, and critical strike chance! However, it reduces his accuracy, magic attack, magic defense, and damages his body!\n" + style.RESET)
      input(fore.RED_1 + style.BOLD + "Ishraq, looking at his hands: What is this feeling? This feels like pre-track season! OH YEAH, LET'S FIGHT!!" + style.RESET)
      revival(Ishraq)
      bots.team = [Entity("Brandon",60,0,10,20,0,0,25,100,50,0,0,0,0,"17","Male"),Entity("David",50,0,12,15,0,0,25,100,50,0,0,0,0,"18","Male"),Entity("Edmond",55,0,11,18,0,0,25,100,50,0,0,0,0,"19","Male")]
      bots.teamS = ["Brandon","David","Edmond"]
      battle(you,bots,Cont=False)
      if victory == 1:
        time.sleep(1)
        text("\n*Julius lets go of Kelly*","Kelly: Ishraq! Let's finish him!")
        revival(Kelly)
        bots.team = [Entity("Julius",70,10,10,20,0,0,50,100,50,0,0,0,0,"17","Male Boss")]
        bots.teamS = ["Julius"]
        battle(you,bots,Cont=False,Mid=True)
        if victory == 1:
          time.sleep(1)
          text("\nIshraq, cramping: *Huff*...Shit!","*Julius lunges at Ishraq*","*Ishraq dodges instinctively, causing Julius to plant into the ground*","*Kelly jumps onto Ishraq, attempting to take him down*","*Ishraq throws her off of him into the computers in the back*","Ishraq, realizing what he did: ****! I need to relax...relax.","*Ishraq cools down*","*Brandon, David, and Edmond slowly regain consciousness*","Ishraq, happy to see his friends: You guys good?","David, raising his arm: Uugh...te..teaam?","Ishraq, flapping his arm across his chest: Team. Team. Team.","Edmond, dizzy: What the hell... even happen Ishraq?","Brandon, joyfully laughing yet worried: Word, who broke those 2 computers? Ms. Miller gonna sue us.","Edmond: Facts.","David: Why is Kelly just laying near those computers though. Did someone throw her? Is she dead?","Edmond: She dead.")
          talk = "1"
          while talk == "1":
            butt = input("\n(1) *Explain what happened*  (2) Ms. Miller attacked me.\n(3) I threw her.  (4) Kelly's dead.\nResponse: ")
            if butt == "1":
              if data [15] == 1:
                text("\nIshraq, taking a long breath: Alright, where do I begin...Kelly was walking with Daniel not long ago. Some guy walks up to them, and starts fighting Daniel..","David, interrupting: He had his wood sword though, right?","Ishraq, grinning: I don't know, hopefully. Then, the guy showed Daniel up, and kidnapped Kelly. Here's where it gets funny. The guy opens up a portal, and takes her to some other dimension..","Brandon, not smiling: Ishraq, you're playin' too much. We're actually in serious trouble right now if someone sees this.","Ishraq, understanding why Brandon didn't believe anything he just said: I'll show you something that'll make you believe me..*Ishraq taps into his wild instincts, begining to emanate a red aura*, does this explain anything?","Edmond, in disbelief: WOAH?! What kinda roids is...?","Ishraq, explaining: Something I found in this dimension, cuz we're actually all in the portal with Kelly. I think everyone at tech is. Kelly fought the guy and got separated from him, but she ended up in the F-Wing after entering the portal. She saw everyone standing straight as hell, except me. She found me drunk, and we ended up coming here to see if anyone was alright. We found ya'll then, and you people attacked us.","David, goofing around: Damn, you beat us though...right?","Ishraq, excited to talk about it: You guys legit jumped my ***, but then I got that weird red aura somehow. It was weird. I felt like I disappeared for a moment. I was in some red space just floating. Then I came back and went ape ****.","Brandon, happy: Good thing you survived man. What should we do now though?","Ishraq, looking at Julius on the floor: We should really check on Kelly and Julius.","Edmond, running: I'll check on Kelly.","Brandon, walking: I will too.","Ishraq, nudging David: Let's go help Julius, David.","David, following: With you.","*Ishraq and David walk to Julius*","David, being serious: Yo, Julius. Wake up. Ms. Miller's not in the room, you can help me with my birthday circuit.","Ishraq, stating: Word, it's your chance David.","David, looks back at the table he sits at: Wait, where's my circuit, it's not on my table anym...NOO!","*David runs off*")
              else:
                text("\nIshraq, taking a long breath: Alright, where do I begin...Kelly said she was kidnapped by some guy who can make portals...","David, interrupting: Nether Portals?","Ishraq, grinning: Yes, like Minecraft...here's where it gets funny. The guy opens up a portal, and takes her to some other dimension..","Brandon, not smiling: Ishraq, you're playin' too much. We're actually in serious trouble right now if someone sees this.","Ishraq, understanding why Brandon didn't believe anything he just said: I'll show you something that'll make you believe me..*Ishraq taps into his wild instincts, begining to emanate a red aura*, does this explain anything?","Edmond, in disbelief: WOAH?! What kinda roids is...?","Ishraq, explaining: Something I found in this dimension, cuz we're actually all in the portal with Kelly. I think everyone at tech is. Kelly fought the guy and got separated from him, but she ended up in the F-Wing after entering the portal. She saw everyone standing straight as hell, except me. She found me drunk, and we ended up coming here to see if anyone was alright. We found ya'll then, and you people attacked us.","David, goofing around: Damn, you beat us though...right?","Ishraq, excited to talk about it: You guys legit jumped my ***, but then I got that weird red aura somehow. It was weird. I felt like I disappeared for a moment. I was in some red space just floating. Then I came back and went ape ****.","Brandon, happy: Good thing you survived man. What should we do now though?","Ishraq, looking at Julius on the floor: We should really check on Kelly and Julius.","Edmond, running: I'll check on Kelly.","Brandon, walking: I will too.","Ishraq, nudging David: Let's go help Julius, David.","David, following: With you.","*Ishraq and David walk to Julius*","David, being serious: Yo, Julius. Wake up. Ms. Miller's not in the room, you can help me with my birthday circuit.","Ishraq, stating: Word, it's your chance David.","David, looks back at the table he sits at: Wait, where's my circuit, it's not on my table anym...NOO!","*David runs off*")
              text("Ishraq, nudging Julius: Julius, come on. You're strong.","Julius, fidgeting: ...!","Ishraq: Hm..?","Julius, quietly whispering: Tupac is alive.","Ishraq, smiling: I know he is.","\n~Julius is a Uruguayan 10th grade engineering student at the highschool of PCTI. He is a varsity track distance runner prodigy. He is undeniably strong and has limitless stamina, boasting a vulgar and humerous attitude. He is quite popular around the school, and is not known to be truly hated by anyone.","\n*Ishraq helps Julius up*","Julius, looking around the room: My head is spinning...where is everyone?","Ishraq: No idea, but I'll fill you in.","*Ishraq fills Julius in on all the events up to now*","Julius, stroking his chin: I wanna know where to find some isometric drawings, cuz it sounds like we're gonna need them if we're up against an entire school.","Ishraq: Agreed.","Julius, looking at Ishraq in the eye: We could try drawing them, and see if they start glowing.","Ishraq, scanning the room again: You know where Miller put the straight edges?","Julius: No.","Ishraq, trying to grasp his ID lanyard: I got my 8th ID yesterday, I should have it with me...where's my ID..?","Julius, laughing: HaHAA! I got my ID, we chillin...wait, where's my ID?","Ishraq, shouting: YO DOES ANYONE HAVE THEIR ID?","Brandon, confused: I just had mine..","Edmond, creeped out: Same, but it's gone.","Ishraq, throwing his arms to the side with his hands open: What the hell? Where's the metersticks?")
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
      text("\nJulius, walking into the office slowly: The lights are off...power went out here.","*Lights flickering*","Ishraq, not moving: This ain't even a joke anymore. Why everything gotta be like a horror movie?","Julius, putting his arm across Ishraq's chest: Shhh...you hear that? I think some ***** is crying.","*Julius and Ishraq trying to listen more*","Ishraq, wide-eyed: Oh damn, someone is. Or something...","Julius, reminiscing: Aahh, this feels like finding the Witch in Left 4 Dead.","Ishraq, laughing in despair: Haha...we're dead.","Julius, serious: So, rock papers for whoever checks the cubicle?","Ishraq, picking his nose: Sure...ready?")
      talk = "1"
      jc = ["Rock","Paper","Scissors"]
      jm = random.choice(jc)
      while talk == "1":
        boop = input("\n(1) Rock  (2) Paper\n(3) Scissors\nResponse: ")
        if boop == "1":
          if jm == "Scissors":
            text("\nIshraq and Julius, whispering: Rock, papers, scissors, shoot...","Ishraq, smirking: I'm IshROCK!","Julius, facepalming: Yeah, I have no idea why I chose scissors. You always ****ing pick rock.")
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
      text("\n*Something shrieks from the cubicle*","Ishraq, crying on this inside: Yeah...screw the game, let's just leave.","Julius, ready to dip: Yeah, screw Kelly.","*The cubicle is knocked down, revealing a bloody nurse. The nurse charges at the students*","Ishraq, thoughts running through his mind: Fight...fight...if you can't run, fight...","Julius, already outside the office: What are ya doin'? MOVE!","Ishraq, adrenaline rushing through his veins: NO, WE HAVE TO FIGHT!","Julius, rushing back to help: ****ing hell!")
      bots.team = [Entity("The Nurse",250,10,10,0,20,0,70,80,130,20,0,0,0,"17","Female Boss")]
      bots.teamS = ["The Nurse"]
      battle(you,bots,Cont=False)
      if victory == 1:
        text("\n*The nurse grabs a scissor from a desk, charging Julius*","Julius, running: OOOOHHH ****!!","*Ishraq lunges at the nurse, slamming her away from Julius, dropping the scissors on the floor*","*The nurse picks up a syringe, and relentlessly charges at Ishraq*")
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
          text("\n*Ishraq picks up the scissors*","Ishraq, wildly charging at the Nurse: mpGH...aRUAAAAH!","*Ishraq stabs the nurse through the neck...The nurse falls to the ground, spewing blood*","Ishraq, vibrating: ****!","Julius, at a loss of words: Man...I don't know...","Ishraq, hands trembling: There's blood all over my hands. I just killed someone.","Julius, trying to keep himself and Ishraq calm: Don't worry, don't worry, bro, like...we were in danger. You had to.","Ishraq, enraged at himself: NO! I DIDN'T! I could've knocked her out! Easy!","Julius, making excuses for Ishraq: Bro, you saw that needle. Who knows what's in that injection.","Ishraq, praying: ...I'm not afraid of anything. But killing someone? It doesn't feel right, and I've always had this feeling that I would be afraid to do it.","Julius, poking the Nurse's butt: Stop thinking about it...let's just hide the body. Remove that freaking scissor too.","Ishraq, scared: Hell no.","Julius, dying on the inside: Aight, I'll take care of the body, you go look for stuff for Kelly.")
          data[13] = 0
          ro = rd(25)
          ro.people = ["Julius"]
          ro.objects = ["File Cabinet","Storage Closet","Nurse's Desk","Medical Cabinets"]
        if boop == "2":
          text("\n*Ishraq kicks the scissors away*","*The nurse injects the syringe into Ishraq*","Ishraq, vibrating as his left arm feels numb: ****!","*Julius tackles the nurse...Ishraq takes the syringe out of his arm*","Ishraq, heavily breathing: Juliuuus! Chokehold her!","*Julius pins the nurse into a chokehold...The nurse passes out*","*Ishraq sits on the ground and leans against a wall near the exit of the room.*","Julius, quickly coming to Ishraq's side: You okayy~?! That was ****in' wild.","Ishraq, shaking everywhere: Is this what a seizure feels like?","Julius, concerned: God damn...who knows what was in that needle.","Ishraq, voice giving out: Maybe...the nurse can..help.","Julius, worried: Yo Ishraq...you're spazzing out like crazy. Like you need some medical attention right now more than Kelly does.","Ishraq, eyes going up: Yeah...my body...can't move!","Julius, ready to run to shop: I'ma go get everyone! We need to figure something out!","Ishraq, with all his power: WAIT! It's...too dangerous! Just find something...in the room! Wake the...nurse up...","*Ishraq's body flails and suddenly fails. It's motionless now*")
          forceswitch(Ishraq)
          data[13] = 1
          ro = rd(25)
          ro.people = ["Ishraq","Nurse"]
          ro.objects = ["File Cabinet"]
    elif ro.TYPE == "Nurse":
      if data[13] == 0:
        text("\n*Ishraq looks down the hallway, seeing Julius running*","Ishraq, shouting: YO! WHAT'S HAPPENIN'?","Julius, approaching: GO! THESE PEOPLE HAVE BEEN CHASING ME ALL OVER THE SCHOOL!!","Ishraq, getting ready to run: HOW MANY?","Julius, reaching Ishraq: A LOT!","*Ishraq starts running alongside Julius*","Ishraq, casually: You know I can't run for long. Distance is terrible.","*A horde of students halt Julius and Ishraq's run*","Ishraq, already panting: Damn it...we're surrounded.","Julius, not backing down: If it's a fight, it's a fight.","Ishraq, back to back with Julius: Let's do this.")
      elif data[13] == 1:
        text("\n*Julius kicks the door open*","Julius, whippin' it: Oooh~! Ya'll not ready for my mixtape.","*Julius looks up, seeing 10 wired students surrounding him*","Julius, shocked: OH ****!...Well...peace!","*Julius dips, running through the crowd...the crowd chases him*","Julius, running smoothly: They can't run forever. I'll lap them through this entire school if I have to.","\n~Julius makes a full 2 miles around the entire school, out-manuevering hundreds of wired students","\nJulius, starting to break a sweat: Phew...that was a good run. I'm back at the nurse's office...","*Students start to surround Julius from all sides, some coming out of the ceiling*","Julius, desperately laughing: Damn...guess they can run forever...I have to fight...","*The students charge Julius*")
      revival(Julius,o=True)
      print("")
      input(style.BOLD + fore.GREEN_1 +"~Julius has gained a new ability, Runner's High! It increases his attack and defense, and makes him immune to slows for a period of time!" + style.RESET)
      bots.team = [Entity("Miguel",65,0,10,50,0,0,20,80,80,0,10,0,0,"17","Male"),Entity("Yairre",55,0,8,30,0,0,25,100,100,0,0,0,0,"18","Female"),Entity("Marlin",40,0,7,30,0,0,25,100,110,0,0,0,0,"19","Male"),Entity("Emily",35,0,7,35,0,0,20,110,100,0,0,0,0,"20","Female"),Entity("Ihsas",55,0,9,45,0,0,20,100,100,0,0,0,0,"21","Male")]
      bots.teamS = ["Miguel","Yairre","Marlin","Emily","Ihsas"]
      battle(you,bots,Cont=False)
      if victory == 1:
        time.sleep(0.5)
        print("\nThe next 5 students attack!")
        time.sleep(0.5)
        bots.team = [Entity("Isabella",30,0,8,0,0,0,35,120,160,30,0,0,0,"17","Female"),Entity("Micheal",25,0,6,30,0,0,25,100,90,0,0,0,0,"18","Male"),Entity("Melanie",40,0,6,40,0,0,20,100,80,0,0,0,0,"19","Female"),Entity("Josh",35,0,7,35,0,0,25,100,100,0,0,0,0,"20","Male"),Entity("Rachelle",45,0,6,45,0,0,20,100,80,0,0,0,0,"21","Female")]
        bots.teamS = ["Isabella","Micheal","Melanie","Josh","Rachelle"]
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
#-------------------------------------------------------------------------------------------------------
  if "The Straight Edge" in quests:
    if nextr == "Mrs. Wells's Classroom" and data[19] == 0:
      text("\nIshraq, kicking the door open: MRS. WELLS?","\n*Three students are fighting in the classroom*\n","Ishraq, surprised: HEY, Julius! That's Metin, Hassan, and Noah! ","Julius, indifferent: Who?","Ishraq, getting ready to fight: They're in our shop, we gotta stop them!","Julius, a little hesitant: We could just let them fight too...they're clearly wired.","Ishraq, taking interest: Wired?","Julius, looking for convenience: Mind-controlled. Just call em' wired.","Ishraq, agreeing: Sounds good.","Julius, ready to work with Ishraq: So what do you wanna do? Fight or let them fight?")
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
        bots.teamS = ["Metin","Hassan","Noah"]
        battle(you,bots,Cont=False)
        if victory == 1:
          text("\n*Hassan gets back up and charges Noah*","\nHassan, angry: #I HATE YOU, SO ANNOYING#","Noah, getting up in stance: #**** YOU ******#","\n*Hassan is about to make contact with Noah, when Metin explodes from below them*","Metin, about to end everyone: AAGGHHGH!","*Metin grabs Noah and Hassan's heads and bangs them together*","\nIshraq, amazed: God damn. They okay?","Metin, regaining clarity: I didn't go too hard I think. But then again, I don't even know my own strength.","Ishraq: You should be powering down soon. Whatever was screwing with your head is gone.","Metin, understandingly: You're right...but it felt good.","Ishraq, concerned: What do you mean?","Metin, trying to explain: I felt...like I lost my reason. My path. But I didn't care. Because the way it made me physically feel was so good.","Julius, trying to conclude: So this wired thing makes you feel so good that you don't care about your free will.","Noah, waking up: Somethin' like that...man my head hurts.","Hassan, also waking up: It's cuz yo' hard ass head! Bro, I'm hungry.","Ishraq, picking Hassan and Noah up: Alright, go to shop and we'll meet ya'll there once were done doing what we need to.")
          ro = rd(27)
          ro.objects = ["Ruler","Kit-Kat"]
          data[19] = 1
          ro = rd(6)
          ro.people.append("Metin")
          ro.people.append("Noah")
          ro.people.append("Hassan")
      elif boop == "2":
        text("\n*The three boys exchange many attacks. Hassan charges Noah*","\nHassan, angry: #I HATE YOU, SO ANNOYING#","Noah, in stance: #**** YOU ******#","\n*Hassan is about to make contact with Noah, when Metin explodes from below them*","Metin, about to end everyone: AAGGHHGH!","*Metin grabs Noah and Hassan's heads and smashes them together*","\nIshraq, itching to jump in: GOD DAMN! THEY'RE NOT OKAY!","Metin, regaining clarity: ...I didn't go too hard I think. But then again, I don't even know my own strength.","Ishraq, checking pulses: Bro...Hassan's dead.","Metin, shocked: WHAT?!","Ishraq, shocked: METIN! YOU KILLED HASSAN!","Metin, scared: WHAT?!","Ishraq, angry at himself: MAN! I KNEW I SHOULD'VE JUMPED IN!","Metin, confused: Bro, what's going on...is this a dream?")
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
        questssys("The Straight Edge","Finish")
        xpg(200)
        you.questinventory.remove("Ruler")
        you.weaponinventory.append("Ruler")
        text("\nIshraq, concluding: Hmm...maybe the isometric drawings are in random places around the school. Right Kelly?","Kelly, agreeing: Yeah, like I found that stone randomly on Pudup's table. It was there by sheer coincidence. I didn't expect it to do what it did to you...","Ishraq, trying to make a connection: Was there anything else about the stone?","Kelly, thinking back on it: Well, it was displaying a holographic red colored isometric drawing from it...and when I picked it up, it was shaking violently. It sort of hurt, and when I dropped it, I kind of saw like gravitate towards you. So I kicked it.","Ishraq, making a hypothesis: Okay, so it was naturally attracted to me. So, where do you guys feel natural in perhaps.","Julius, stumped: I feel natural everywhere.","Kelly, also a little skeptical: I feel the most natural here in shop.","Ishraq, quickly thinking of something else: Well, how about where the hell do you guys just think you would find an isometric drawing stone?","Kelly, without a doubt: The library.","Julius, a little unsure: Maybe the automotive building? Just seems like it would have one.","Ishraq, ready: It's settled then, we're going to those places.")
        questssys("No Talking in The Library","Start")
        questssys("More Than Meets The Eye","Start")
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
      bots.team = [Entity("The Librarian",750,30,25,40,40,100,70,150,100,10,0,10,0,"17","Female Boss")]
      bots.teamS = ["The Librarian"]
      battle(you,bots,Cont=False)
      if victory == 1:
        time.sleep(1)
        text("\nIshraq, panting: Toughest one yet.","Kelly, falling to the ground: Yeah...I mean that's the first wired that can levitate and throw books at you.","Julius, stretching: Alright, let's search for that stone.")
        ro = rd(14)
        ro.people = ["Kelly","Julius","The Librarian"]
        ro.objects = ["Bookcase A-D","Bookcase E-H","Bookcase I-L","Bookcase M-P","Bookcase Q-T","Bookcase W-Z","Computers","Front Desk"]
#---------------------------------------------------------------------------------------------
  if "More Than Meets The Eye" in quests:
    if nextr == "Automotive Building":
      None
#---------------------------------------------------------------------------------------------
  if "Feeling Alone" in quests:
    if nextr == "Cafe 2":
      None
#---------------------------------------------------------------------------------------------
  if nextr == "Auditorium" and "Final Showdown" in quests and croom[0].RID == 16:
    time.sleep(1)
    text("\nAmira: It's about time you all came...finally here to take away my gift? The only thing I have left?","Ishraq: Don't you get it!? The Fedora Man is using your *** to take us out!","Kelly: He's not your friend just because he gave you these powers! And we're not your enemies for trying to stop you!","Amira: I get it...only you six get to be extraordinary and powerful...no one else can!","Daniel: Guys, be careful, the power's getting to her head, aaghaha!!","Amira: The power has gotten to all of your heads!","Kelly: You're honestly beyond help.","Amira: Funny you say that Kelly. I thank you for your cooperation in advance!","Kelly: What do you me...!?","*Kelly is paralyzed and dragged towards Amira by her tethers*","Amira: Your powers are now mine...prepare for The End, haters.","Arwyn: Yes! Kelly is finally gone!","Daniel: MY QUEEN!! I'M COMING FOR YOU!")
    bots.team = [Entity("Amira",10000,0,500,100,500,100,60,100,100,1,1,1,0,"17","Female"),Entity("Kelly",1500,0,0,0,0,0,0,0,0,0,0,0,0,"18","Female"),Entity("Jackie",2000,0,0,0,0,0,0,0,0,0,0,0,0,"19","Female"),Entity("Abby",2500,0,0,0,0,0,0,0,0,0,0,0,0,"20","Female"),Entity("Meryem",1000,0,0,0,0,0,0,0,0,0,0,0,0,"21","Female")]
    bots.teamS = ["Amira","Kelly","Jackie","Abby","Meryem"]
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
data = [3,3,5,4,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nextr = 0
victory = 0
Colis = False
time.sleep(1)

rwe = input("Load?")
if rwe == "1":
  save("load")
  worldfunction()
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


for x in world:
  x.initroutes()
  
print("*Press enter to continue at all times*")
input("\nWelcome to the Demo version of PCTI Lockdown")
input("\nIn this Demo, you can either try the story mode or fight some bosses. You can catch a small glimpse of the story and travel the school of PCTI, or you can test your skill on bosses that will appear in the story in the future.")

boy = 1
while boy == 1:
  weee = input("\nWould you like to test the story mode or some boss battles?\n(1) Story  (2) Boss Battles\nResponse: ")
  if weee == "1":
    Ishraq = Entity("Ishraq",50,100,12,25,0,10,55,100,100,5,0,0,2,"1","Male")
    Kelly = Entity("Kelly",30,100,7,10,7,25,40,110,110,15,5,5,4,"2","Female")
    Julius = Entity("Julius",55,100,11,15,0,20,45,100,100,4,0,0,1,"3","Male")
    Daniel = Entity("Daniel",800,100,100,80,120,80,30,100,100,20,0,0,10,"4","Male")
    #Daniel = Entity("Daniel",45,100,8,15,15,5,4,100,100,6,0,0,3,"4","Male")
    Tim = Entity("Tim",40,100,9,12,10,25,50,100,100,7,0,0,2,"5","Male")
    Arwyn = Entity("Arwyn",35,100,10,5,5,15,35,100,100,10,0,0,4,"6","Male")
    Shah = Entity("Shah",45,100,10,20,5,10,50,100,100,4,0,0,3,"7","Male")
    Amira = Entity("Amira",50,100,10,10,10,10,45,100,100,10,10,10,5,"8","Female")
    Ishraq.learnskill("Counter")
    Daniel.learnskill("Grubby Hands")
    Daniel.addbattleitem("Chips")
    ro = rd(0)
    world.remove(ro)
    croom.append(ro)
    you.team = [Daniel]
    you.teamS = ["Daniel"]
    boy = 0
  elif weee == "2":
    Ishraq = Entity("Ishraq",150,100,12,27,0,10,56,100,100,5,0,0,4,"1","Male")
    Kelly = Entity("Kelly",60,105,7,10,17,25,41,110,115,15,5,5,5,"2","Female")
    Julius = Entity("Julius",95,105,56,15,0,20,61,100,100,4,0,0,2,"3","Male")
    Daniel = Entity("Daniel",45,100,13,20,15,5,30,105,100,6,0,0,4,"4","Male")
    Tim = Entity("Tim",90,105,12,12,13,25,51,100,100,7,0,0,3,"5","Male")
    Arwyn = Entity("Arwyn",135,105,10,5,10,15,36,100,100,11,0,0,4,"6","Male")
    Shah = Entity("Shah",145,100,10,20,6,10,51,100,100,4,0,0,4,"7","Male")
    Amira = Entity("Amira",100,110,15,15,15,15,46,100,100,11,12,12,6,"8","Female")
    #Auto = Entity("Autosentry",)
    Ishraq.XP = 100000
    Daniel.XP = 100000
    Kelly.XP = 100000
    Julius.XP = 100000
    Arwyn.XP = 100000
    Tim.XP = 100000
    Shah.XP = 100000
    Amira.XP = 100000
    Colis = True
    Ishraq.Ishraqlevelup()
    Daniel.Daniellevelup()
    Kelly.Kellylevelup()
    Julius.Juliuslevelup()
    Arwyn.Arwynlevelup()
    Tim.Timlevelup()
    Shah.Shahlevelup()
    Amira.Amiralevelup()
    Colis = False
    you.backteam = [Ishraq,Julius,Kelly,Daniel,Tim,Arwyn,Shah,Amira]
    you.backteamS = ["Ishraq","Julius","Kelly","Daniel","Tim","Arwyn","Shah","Amira"]
    you.supportteam = [Support("Brandon",21),Support("Edmond",11)]
    you.supportteamS = ["Brandon","Edmond"]
    for x in range(5):
      Ishraq.learnskill("Wild Instinct")  
      Ishraq.learnskill("Counter")   
      Ishraq.learnskill("Smash")     
      Ishraq.learnskill("Valorous Chant")
      Ishraq.learnskill("Immortality")     
      Ishraq.learnskill("Barrier")      
      Kelly.learnskill("Calligraphy")    
      Kelly.learnskill("ASMR")   
      Kelly.learnskill("Pinpoint")        
      Kelly.learnskill("Heal")        
      Kelly.learnskill("Perfect Requiem")   
      Kelly.learnskill("Revive")     
      Julius.learnskill("Rest")      
      Julius.learnskill("Runner's High")    
      Julius.learnskill("Shield")     
      Julius.learnskill("Tremors")    
      Julius.learnskill("Isometric Drawings")    
      Julius.learnskill("Combo")       
      Daniel.learnskill("Grubby Hands")    
      Daniel.learnskill("Taunt")          
      Daniel.learnskill("Knight's Vow")   
      Daniel.learnskill("Photosynthesis")       
      Daniel.learnskill("Enlargen")         
      Daniel.learnskill("Electron")      
      Arwyn.learnskill("Silence")       
      Arwyn.learnskill("Cut Myself")    
      Arwyn.learnskill("Gunblade")      
      Arwyn.learnskill("Spark Net")      
      Arwyn.learnskill("Darkness")      
      Arwyn.learnskill("From the Shadows")
      Tim.learnskill("Dab")             
      Tim.learnskill("Quen")              
      Tim.learnskill("Chronopower")   
      Tim.learnskill("Protobelt")      
      Tim.learnskill("Rubix Cube")
      Tim.learnskill("Autosentry")        
      Shah.learnskill("Fallen Symbol")  
      Shah.learnskill("Progressive Overload")
      Shah.learnskill("Arm Wrestling")
      Shah.learnskill("Inferno")
      Shah.learnskill("Self-Destruct")
      Shah.learnskill("Chad Walk")
      Amira.learnskill("Haters")
      Amira.learnskill("Suck")
      Amira.learnskill("Power Surge")
      Amira.learnskill("Telepathy")
      Amira.learnskill("Mimic")
      Amira.learnskill("Desperation")
    for x in you.backteam:
      x.isomode = True
    teamskill()
    print("\nIn this part of the Demo, you can face bosses with max level characters. You will have to choose your party members. Every character has their own strengths and weaknesses. To learn more about fighting and the characters, type the appropriate number.")
    boy = 2
    while boy == 2:
      print("\n(1) How to Fight  (2) "+fore.RED_1+"Red Iso-Wielder Ishraq"+style.RESET +"\n(3) "+fore.GREEN_1+"Green Iso-Wielder Julius"+style.RESET+"  (4) "+fore.MAGENTA_1+"Magenta Iso-Wielder Kelly"+style.RESET+"\n(5) "+fore.YELLOW_1+"Yellow Iso-Wielder Daniel"+style.RESET+"  (6) "+fore.CYAN_1+"Cyan-Iso Wielder Tim"+style.RESET+"\n(7) "+fore.DODGER_BLUE_1+"Blue-Iso Wielder Arwyn"+style.RESET+"  (8) "+fore.ORANGE_RED_1+"Graham's Disciple Shah"+style.RESET+"\n(9) "+fore.SKY_BLUE_1+"Amira"+style.RESET+"  (10) Continue")
      learn = input("Response: ") 
      if learn == "1":
        print("\nIn battle, you will see a command list that looks like this")
        print(fore.YELLOW_1 + "\nIt's Daniels's turn." + style.RESET,"\nAttack, Skills, Items, Recover, Check, Support, or Transform? ")
        input("\nTo interact with this command list, you can either type the commands or use corresponding numbers to what order they're in, such as 1 for attack, 2 for skills, etc.")
        tutorial = True
        while tutorial == True:
          s = input("\nWhat would you like to know about?\n(1) Attack (2) Skills (3) Items (4) Recover (5) Check (6) Support (7) Transform (8) I'm ready\nResponse: ")
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
            input("\nThe support command allows you to call assistance from the 4000 students in PCTI. You can assign up to three support fighters into your team that all have their individual skills, some having special skills with certain main allies. Their skills can be used without wasting a turn, and go on cooldown for a number of total turns in battle. In the Boss Battle Demo, you will by default have Brandon and Edmond support members.")
          if s.lower() == "transform" or s == "7":
            input("\nThe transform command lets a character surpass all their limits by borrowing power from their future-selves. Every character gains boosted stats and unique effects that are explained on their character pages.")
            continue
          if s.lower() == "i'm ready" or s == "8": 
            tutorial = False
      elif learn == "2":
        input("\nIshraq is a Bengali Peruvian 10th grade engineering student at the highschool of PCTI. He is a varsity track mid-distance sprinter, fencer, and VEX competitor. He is very adept at expressing his rage and care towards people, shouting loudly, procrastinating, and making new friends of all kinds. He believes everyone has the potential to do great things, looking beyond faults. His extroversion makes him a popular figure, but also puts off others. After becoming the Red Iso-Wielder, it began to take shape after his athleticism and ability to inspire.\n")
        input("He takes the role of a physical fighter with many defensive capabilites. With the highest attack and speed, he is the most fit among the Iso-wielders to fight a 1v1. However, he lacks magic capabilites. His skills are the following:")
        input("\nCounter - A passive ability of Ishraq's, where when he is attacked by an enemy's normal attack, he has a chance to counter them. The player must type whatever word is displayed with or without capilitization to successfully counter the enemy. Ishraq automatically counters attacks that he dodges.")
        input("\nWild Instict - Ishraq triggers his inner human insticts, boosting certain stats(Attack, Speed, Evasion, Critical Chance), but decreasing others(Magic Attack, Magic Defense, Accuracy), all at the cost of his health per turn.")
        input("\nSmash - Ishraq's Iso amplifes his next 3 attacks, allowing the player to do 3 attacks using the WASD keys. Each key does has a different effect that amplifies the next attack. Using W increases critical chance for the remaining attacks. Using A increases physical attack. Using S increases armor penetration. Using D increases accuracy. Doing certain sequences adds a special effect to the ability at the end, such as DDD or AAA ends with an AoE physical attack to all enemies.")
        input("\nValorous Chant - Ishraq shouts to rally his teammates, fearing enemies and increasing all allied attack, defense, and speed, each boost in order per ally alive(4 for all, 3 for AT&DF, 2 for AT, 1 for fear), none by himself.")
        input("\nImmortality - Ishraq refuses to die for 3 turns. He also gains passive lifesteal when activated.")
        input("\nBarrier - Ishraq puts up a barrier or an ally that nullfies physical damage for some hits.")
        input("\nTransforming with Ishraq causes him to become ENRAGED, instantly increasing his attack and speed according to his current health. The lower health he has, the more attack and speed he gains. Wild Instinct is replaced with the ability to Enrage, which does the same effect as stated above, in case you lose more health and want to gain more attack and speed. All stat boosts from Wild Instinct is made up through transformation base stat boosts. Ishraq also instantly activates his Immortality skill upon transformation, and the level of his Counter is increased by 3.")
      elif learn == "3":
        input("\nJulius is a Uruguayan 10th grade engineering student at the highschool of PCTI. He is a varsity track distance runner prodigy. He is undeniably strong and has limitless stamina, boasting a vulgar and humerous attitude. He is quite popular around the school, and is not known to be truly hated by anyone. After becoming the Green Iso-Wielder, it began to take shape after his fun vibe, enthusiastic singing talents, and his unlimited energy.\n")
        input("He takes the role of a physical tank with a variety of support and damage utilites. With the highest health, he is able to absorb a ton of damage and is on par with Ishraq with both base physical attack and defense. However, he has even lower magic capabilities. His skills are the following:")
        input("\nRest - When Julius dies, he is able to recover from death after some time. He can revive as much as he wants, as long as another member is still alive.")
        input("\nRunner's High - Julius experiences the runner's high, becoming immune to slows and increasing his attack and defense.")
        input("\nShield - Julius shields himself from incoming damage, reducing it and healing himself.")
        input("\nTremors - Julius sends tremors through the ground, dealing physical damage to all enemies based on his physical and magic attack. It has a chance to make enemies fall, stunning them. If they do not fall, they are slowed.")
        input("\nIsometric Drawings - Julius summons the power of isometric drawings by singing, buffing himself or an ally to increase the level of all their skills by 1, and recovering a great amount of their ISO-transformation points.")
        input("\nCombo - Julius combos with an ally, being able to do various things. With Ishraq, they can deal their combined physical damage as magic damage to all enemies. With Kelly, they can heal everyone in the party with their combined magic attack. With Daniel, they can cast Daniel's skill, Grubby Hands, on all enemies. With Tim, they can deal their combined physical and magical damage to one enemy as physical damage. With Arwyn, they can increase everyone's armor and magic penetration by their combined speed.")
        input("\nTo transform, Julius sings the isometric drawings song to instantly heals him for 20% of his maximum health, and removes his Runner's High skill. Transformation base stat boosts make up for the removal, and Julius's Shield skill is upgraded by 3 levels. Julius also puts the effect of Eternal Will on himself while he is transformed, which allows him to instantly revive at maximum health if he dies while transformed. Alongside that, he will have Runner's High and Isometric Drawings activated on himself upon revival.")
      elif learn == "4":
        input("\nKelly is a Korean 10th grade engineering student at the highschool of PCTI. She is 3rd in class ranking among 894 students in the 10th grade, a SkillsUSA officer, and placed 2nd in State for FBLA. She has obsessive organization tendencies that lead her to be good at managing things...and people. Under her hard outlook, she is quite the whimsical character who loves to experience new things. After becoming the Magenta Iso-Wielder, it began to take shape after her musical and artistic prowess, and her perfectionist outlook.")
        input("\nShe takes the role of a magical burst assassin healer hybrid. With the strongest single burst skill in the game, she can be essential to taking down high health targets. However, she lacks physical capabilities. Her skills are the following:")
        input("\nCalligraphy - Kelly uses her magic calligraphy pen to write a spell, dealing high accuracy magic damage. This skill generates triple iso-points.")
        input("\nASMR - Kelly performs ASMR, recovering a percentage of her mana and increasing everyone's mana regen at a cost of her health.")
        input("\nPinpoint - Kelly targets a vital on the enemy, striking it devastingly, dealing bonus true damage based on her physical attack, on top of her normal damage. This also causes the enemy to bleed based on Kelly's accuracy.")
        input("\nHeal - Kelly heals an ally based on her magic attack.")
        input("\nPerfect Requiem - Kelly performs the Perfect Requiem, taking out her violin to deal magic damage per successful note. Landing all her notes prepares the finale, which deals special effects based on her weapon, but by default massive penetrating magical damage.")
        input("\nRevive - Kelly revives a fallen ally for a percentage of their max health.")
        input("\nTo Transform, Kelly takes her initiative to be the 'leader', reminding everyone that she will be grading them on their efforts. In doing so, she recovers 40% of her mana, increases the level of her Perfect Requiem skill by 3, and replaces her Heal skill with Omniheal. Omniheal is the same thing as heal, but on all allies.")
      elif learn == "5":
        input("\nDaniel is a Dominican Peruvian 10th grade engineering student at the highschool of PCTI. He is a VEX competitor, and one of the two students, the only in engineering, to get a 5 on the AP Physics 1 exam. He is infatuated with learning and helping others, but is anything but a saint. He loves to bully people for the sheer entertainment of it, but also finds it funny to get bullied. He has no shame whatsover, being able to do absolutely wild things. After becoming the Yellow Iso-Wielder, it began to take shape after his greasiness, his bold and crude nature towards everyone, and his size?")
        input("He takes the role of a support tank with many supporting abilities. With the strongest defenses and lowest speed, he is able to absorb the most damage amongst the allies and significantly increase their damage outputs. He has many tools to protect allies as well. His skills are the following:")
        input("\nGrubby Hands - Daniels rubs an enemy with his greasy hands, poisoning them and reducing their evasion.")
        input("\nTaunt - Daniel taunts an enemy, forcing them to attack Daniel for 2 turns.")
        input("\nKnight's Vow - Daniel binds himself to an ally, taking a percentage of the damage they take for himself and increasing their attack and magic damage based on Daniel's max health.")
        input("\nPhotosynthesis - Daniel generates food in his body, regening his health but drastically lowering his physical attack until de-activated.")
        input("\nEnlargen - Daniel increases in size for 4 turns, gaining damage reduction but lowering his evasion. His next normal attack causes him to roll all over the enemies, dealing great physical damage.")
        input("\nElectron - Daniel turns himself or anyone into an electron, boosting his or their accuracy, evasion, speed, and magic damage for 3 turns.")
        input("\nWhen transforming, Daniel decides to *spoilers*. This fears all enemies and allows him to activate a 3-level upgraded Enlargen for however long he is transformed, and replaces his Grubby Hands skill with Grubby Tides. This is essentially the same skill, but to all enemies. Transforming removes his ability to cast Enlargen.")
      elif learn == "6":
        input("\nTim is a European 10th grade engineering student at the highschool of PCTI. He is a varsity fencer, VEX competitor, and the fastest builder when it comes to engineering a robot. He has a knack for making original puns constantly to the point where it pisses mostly everyone off. Similar to Daniel, he is not afraid to do unordinary things, but he has a limit. He is also at the rebel stage of his Christian boyhood. After becoming the Cyan Iso-Wielder, it began to take shape after his free spirit, and his ASL and mechanical mastery.")
        input("He takes the role of a magical fighter with many unique abilities. With the highest magic defense and the potential to deal the most damage, he is definitely a jack-of-all trades. His balanced stats make him a worthy frontline party member in all fights, but his skills surely secure him a spot, being:")
        input("\nDab - Tim dabs on the enemy dealing magic damage based on his physical attack, speed, and accuracy. Dabbing simultaneously on the same enemy causes every dab to deal increasing damage.")
        input("\nQuen - Tim shields himself or an ally and removes all negative effects from them. The shield lasts for 1 hit, and has a max threshold of shielding.")
        input("\nChronopower - Tim ignites his weapon with the essence of time, causing his normal attacks to deal bonus magic damage and stealing the enemy's speed for 3 turns for 3 attacks.")
        input("\nProtobelt - Tim uses his protobelt to shoot missles at all enemies, dealing magic damage. The belt pulls him to safety, making sure he dodges the next attack on him.")
        input("\nRubix Cube - Tim throws one of his rubix cubes at the enemies and it explodes, causing all enemies to start dancing for 2 turns. Dancing enemies have a chance to hit themselves or their allies, or just do nothing instead!")
        input("\nAutosentry - Tim sends out his assistant drone that acts as its own ally, with its own health and stats based on Tim's base stats. It automatically attacks whoever and charges up a Zap attack that deals magic damage and stuns an enemy for 1 turn.")
        input("\nTransforming with Tim turns him into The Taco Lord, gaining the ability to rain tacos at the enemies, and also supply allies with a perfectly delicious taco. These tacos are added into allied inventories and heal them for 25% of their max health and cleanse them of all debuffs. Enemies also become burned based on Tim's magic attack. Also, Tim instantly puts a quen shield on himself and increases the level of his dab by 3 levels.")
      elif learn == "7":
        input("\nArwyn is a Filipino 10th grade engineering student at the highschool of PCTI. A member alongside Ishraq in a VEX team in 9th grade and one of his childhood friends, he displays mechanical mastery with his long and slender fingers. However, he began to stop caring about everything and became obsessed with the game League of Legends. Despite that, he is extremely loyal to his individual friend groups with his multiple personas even though he may not show it. After becoming the Blue Iso-Wielder, it began to take shape after his depression, emo-nature, and League of Legends.")
        input("He takes the role of a hybrid mage assassin. He has many tools to work around enemy defenses, and has one of the highest consistent damage outputs. Every single one of his skills are deadly when used correctly. He is however stunted by his naturally low survivability. His skills are the following:")
        input("\nSilence - Arwyn stays shut like a lil' bruh, silencing himself for 3 turns(cannot cast skills), but converts his normal attacks to true damage plus some bonus true damage based on his magic attack.")
        input("\nCut Myself - Arwyn cuts himself, drastically reducing enemy defenses for some hits but causing himself to bleed for 3 turns.")
        input("\nGunblade - Arwyn shoots and slashes an enemy with his gunblade, dealing hybrid damage and healing a percentage of damage dealt.")
        input("\nSpark Net - Arwyn conjures a lightning chain that bounces between enemies, dealing magic damage. It stuns them if this ability crits. If there is one enemy, the chain does not bounce but stuns for sure.")
        input("\nDarkness - Arwyn shrouds the entire battlefield in darkness, reducing all enemy accuracy and increasing his critical chance and damage, and his armor and magic penetrations. ")
        input("\nFrom the Shadows - Arwyn disappears into the shadows, becoming invisible. He can then wait up to 3 turns or flashcut the enemies. He must react successively to keep continuing his attack. The shadows also deal magic damage to enemies each cut if the battle is shrouded in darkness.")
        input("\nTransforming with Arwyn turns him into a cold-blooded killer, instantly setting up a shroud of darkness on the field. While Arwyn is transformed, all enemies begin to decay some of their health, and his From the Shadows is upgraded by 3 levels.")
      elif learn == "8":
        input("\nShah is a Bengali 10th grade engineering student at the highschool of PCTI. He is known by the mass to be a plug if they need an essay written. Besides that, he works towards his own goals of becoming stronger. Despite being reserved to himself, he has a very loud mind that is either appealing or off-putting. After becoming Graham's Disciple, his granted iso-powers began to take shape after his gym obsession, constant need to prove his strength, and his goal to become a CHAD.")
        input("He takes the role of a physical berserker. He is able to charge up tons of power to deal extreme damage in one blow. He is also able to keep control of the battle with his duel mechanic. His skills are the following:")
        input("\nFallen Symbol - While Shah is dead, all allies receive physical and magical attack and damage reduction.")
        input("\nProgressive Overload - Shah tenses up, increasing his physical attack. This can be done up to 3 times. Upon using any type of physical damage, all charges are expended.")
        input("\nArm Wrestling - Shah begins an arm-wrestling match with an enemy, locking them into a duel. Shah can only deal damage to that enemy, and that enemy can only deal damage to Shah(enemy becomes taunted to Shah). Shah also gains physical and magical attack and damage reduction while arm wrestling, and the person he is arm wrestling has their defenses and evasion reduced.")
        input("\nInferno - Shah exerts the inferno of the gym onto an enemy, dealing hybrid damage that burns the enemy based on how much damage was dealt for 2 turns.")
        input("\nSelf-Destruct - Shah self-destructs onto the enemy, taking 75% of his max health to deal true damage based on his health lost.")
        input("\nChad Walk - Shah does the chad walk, increasing all allied critical chance and crit damage.")
        input("\nTransforming with Shah allows him to work out instantly, maximum tension boosting to 3 boosts or going to 4 boosts if already at 3 boosts. Progressive Overload is replaced by Sick Pump, which instantly takes you to 3 boosts, or let you go beyond up to 5 boosts(Instantly to 3 if below 3, +1 boost when 3 or above). Shah's Arm Wrestling ability is upgraded by 3 levels.")
      elif learn == "9":
        input("\nAmira is an Egyptian 10th grade medical student at the highschool of PCTI. She is a HOSA member, soccer player and fencer, serves as the president of the Class of 2020, and plans on becoming an EMT. She is infamously known around the school for her artificial behavior. As charming as the devil, she gets what she wants from anyone and is quick to get rid of her 'fake' friends once she has reaped their benefits. In a constant battle of making and losing friends, she coldly looks forward with a constant smile. Bestowed upon with power from The Fedora Man, she has cultivated it over the years to become a force to be reckoned with.")
        input("She takes the role of a magical jack-of-all trades. She mainly has magic damage tools, but is indefinitely flexible to any fight. Her vampiric strength only grows the more defeated the team becomes and how powerful the enemy is. Her skills are the following:")
        input("\nHaters - Any enemy that attacks Amira becomes her 'Hater' for 2 turns. For every hater Amira has, she gains evasion and critical chance. She also gains bonus penetrations when attacking haters.")
        input("\nSuck - Amira sucks off the enemy, dealing magic damage and healing for her missing health. This deals critical damage to males.")
        input("\nPower Surge - Amira goes on a power trip and tethers the enemies with the organic tentacles on her back. She steals a percentage of damages divided amongst all enemies(For example, if 1 enemy is being drained, take 30% from that enemy; if 2 enemies are being drained, take 15% from each).")
        input("\nTelepathy - Amira whispers into the ear of an enemy, using her mind games to fear the enemy and cause her next 3 basic attacks to deal bonus magic damage. Passively, every 3 hits Amira deals bonus magic damage, which can stack with the activation of this skill.")
        input("\nMimic - Amira mimics the last attack done in battle.")
        input("\nDesperation - Amira cries out of her broken state, releasing a malefic aura across the battlefield that deals magic damage based on her missing health and how many allies are dead.")
        input("\nTransforming with Amira makes her declare everyone as her 'Haters', marking all enemies with the Haters passive. Her mimic ability is changed to become a choice skill, where she can mimic the last attack of a chosen enemy or ally. Power Surge is increased by 3 levels.")
      elif learn == "10":
        ro = rd(-1)
        world.remove(ro)
        croom.append(ro)
        boy = 0

worldfunction()