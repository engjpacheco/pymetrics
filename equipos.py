# Lista de equipos

equipos = [
    "IMM",
    "ROBOT",
    "THERMO",
    "MAGUIRE",
    "SOFT-TRIM",
    "BOOTH",
    "T1XX",
    "CX483",
    "U725",
    "KXX/KM",
    "BT1CG/PERFCAR/P708",
    "Otros",
    "Gap Hidder",
    "JL",
]

# id de equipos:
moldeo = 12
softrim = 4
booth = 10
vinil = 2
t1xx = 6
cx483 = 18
u725 = 1
kxx = 6
bt1cg = 5 
gap_hidder = 2

# IMM
imm_key = [imm for imm in range(1,moldeo + 1)]
imm_value = [id + 1000 for id in imm_key]
imm_id = {k:v for (k,v) in zip(imm_key, imm_value)}
print(imm_id)

# ROBOT
robot_key = [robot for robot in range(1,moldeo + 1)]
robot_value = [id + 2000 for id in robot_key]
robot_id = {k:v for (k,v) in zip(robot_key, robot_value)}
print(robot_id)

# THERMO
thermo_key = [thermo for thermo in range(1,moldeo + 1)]
thermo_value = [id + 3000 for id in thermo_key]
thermo_id = {k:v for (k,v) in zip(thermo_value, thermo_key)}
print(thermo_id)

# MAGUIRE
maguire_key = [maguire for maguire in range(1,moldeo + 1)]
maguire_value = [id + 4000 for id in maguire_key]
maguire_id = {k:v for (k,v) in zip(maguire_value, maguire_key)}
print(maguire_id)

# SOFT-TRIM
softrim_key = [softrim for softrim in range(1,softrim + 1)]
softrim_value = [id + 6000 for id in softrim_key]
softrim_id = {k:v for (k,v) in zip(softrim_value, softrim_key)}
print(softrim_id)

# BOOTH
booth_key = [booth for booth in range(1,booth + 1)]
booth_value = [id + 8000 for id in booth_key]
booth_id = {k:v for (k,v) in zip(booth_value, booth_key)}
print(booth_id)
