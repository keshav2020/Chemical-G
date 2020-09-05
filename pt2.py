# ther are only 18 chemicals here i an working to make it
# more intrestin. Enjoy this game.
from pygame import mixer
import random
turn = 17
no_of_chance = 0
corret_answers = 0
n = 0

"""Music"""
mixer.init()
mixer.music.load("music.mp3")
mixer.music.play()
mixer.music.set_pos(20 )
print("\f\f\f\f\f\f\f\f You Can Lern Chemican Names 100% by "
      "Playing This "
      "Game for atleast 25 times \f\f\f\f\f\f\f\f\n")
print("Enter The chemical Name of Given Chemicals \n ")
while n <= 17:
       n = n + 1
       all = ["Hydrogen","Helium","lithium","Beryllium","Boron",
       "Carbon","Nitrogen","Oxygen","Florine","Neon",
       "Sodium","Magnesium","Aluminium","Silicon",
       "Phosphorus","Sulphur","Chlorine","Argon"]
       reward = ["Nice\n", "Good\n", "Execelent\n",
               "correct\n"]
       inps = ["H","He","Li","Be","B","C","N","O","F",
               "Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
       wrong = "Wrong Answer\n"
       rand1 = random.choice(reward)
       rand = random.choice(all)
       print(rand)
       inp1 = input()
       if rand==all[0] and inp1 == inps[0]:
              corret_answers = corret_answers + 1
              print(str(corret_answers)+"/18 is Your "
                                        "score ")
              print(rand1)
              continue

       if rand==all[1] and inp1 == inps[1]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[2] and inp1 == inps[2]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand==all[3] and inp1 == inps[3]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[4] and inp1 == inps[4]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[5] and inp1 == inps[5]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand==all[6] and inp1 == inps[6]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand==all[7] and inp1 == inps[7]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand==all[8] and inp1 == inps[8]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[9] and inp1 == inps[9]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[10] and inp1 == inps[10]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[11] and inp1 == inps[11]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[12] and inp1 == inps[12]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[13] and inp1 == inps[13]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[14] and inp1 == inps[14]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[15] and inp1 == inps[15]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[16] and inp1 == inps[16]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + "/18 is Your "
                                          "score ")
              continue
       if rand == all[17] and inp1 == inps[17]:
              print(rand1)
              corret_answers = corret_answers + 1
              print(str(corret_answers) + \
                     "/18 is Your "
                                          "score ")
              continue
       else:
              rand == all[0:20] and inp1 != inps[0:20]
              print(wrong)

       # n = n + 1
compli = "\t\t\t\t\t\t\t\t\t\t\t\t\t\tCorrect Answers Were "+str(
       corret_answers)
print(compli)
if corret_answers == 18:
       print("\f\f\f\fWell Done!!!!!!!")
else:
       print("\f\f\f\fYou need More Practice!!!!!!!")