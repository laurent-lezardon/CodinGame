import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# vaults_time liste des temps de décodage des coffres
print("Debug messages...", file=sys.stderr, flush=True)
vaults_time = []
robbers_activity = []
# robbers quantity nombre de voleurs
robbers_quantity = int(input())
# vault_quantity nombre de coffres
vault_quantity = int(input())
#--------- élaboration de la liste des temps de décodage  ----------
# entrées : characters_quantity (nombre de charactères du code), numbers_quantity (nombre de chiffres dans le code)
for i in range(vault_quantity):
    characters_quantity, numbers_quantity = [int(j) for j in input().split()]
    print("index coffre :",i)
    print("characters_quantity",characters_quantity)
    print("numbers_quantity",numbers_quantity)
    print("vaults_time",vaults_time)
    time = 10**numbers_quantity*5**(characters_quantity-numbers_quantity)
    print("time", time)
    vaults_time.append(time)
    print("vaults_time :",vaults_time)
# ---------- coffres en cours -----------
# attribution d'un coffre par voleur si au moins autant de coffres que de voleurs)
for i in range(min(robbers_quantity,vault_quantity)):
    # un coffre attribué est enlevé de la liste vault_time
    robbers_activity.append((i,vaults_time.pop(0)))
    print(robbers_activity)


print("final",robbers_activity)
