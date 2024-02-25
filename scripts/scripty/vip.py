import os
import subprocess
import re
import xbmcgui
import xbmcvfs

path = xbmcvfs.translatePath("special://profile/addon_data/plugin.video.stream-cinema-2-release/settings.xml")

vip_check = subprocess.check_output(["grep", "last_vip_check", path])
vip_check = re.search(r'>\s*(\d+)\.', vip_check.decode("utf-8"))
if vip_check:
    vip_check = vip_check.group(1)
    subprocess.call(["kodi-send", "-a", f"SetProperty(vip_check,{vip_check},10000)"])
    
vip_duration = subprocess.check_output(["grep", "provider.vip_duration", path])
vip_duration = re.search(r'>\s*(.*?)\s*<', vip_duration.decode("utf-8"))
if vip_duration:
    xbmcgui.Dialog().notification('VIP Days Webshare', 'Kontrola zbývajícich dní předplatného', xbmcgui.NOTIFICATION_INFO, 2000, sound=True)
    vip_duration = vip_duration.group(1)
    vip_days = re.search(r'\(Dny: (\d+)\)', vip_duration).group(1)
    color = ""
    if int(vip_days) > 14:
        color = "blue"
    elif int(vip_days) > 7:
        color = "yellow"
    else:
        color = "red"
    subprocess.call(["kodi-send", "-a", f"SetProperty(vip_days,[COLOR {color}]{vip_days}[/COLOR],10000)"])

