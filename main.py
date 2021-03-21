from os import environ
# import logging
from pyrogram import Client, idle

api_id = 3883605
api_hash = 6569ffa07e587b87e91d108b21e41c18
session_name = BQBT44Ki_Ado1f5r1tRpz-y2-eGo_89vu7pkcuL2cMOAnA9hzylFigUsQ6OchZsziAdW-hVPEwQC3OWj6da97IFsB04wzZICaPk-RW_20RLUD_ciby5Fc7XOIbNxTssJi-sUeXWZBSBTpgakMQ3V-d7qRmP4UXrJ1IReH_RYsmR8qdhGsR8M_BbWxx1y_ZA_5IhjMI1UAxkcVexaOsc6Dg1g8wKWttFK0HViENPjdjD2IXoLmgdb4pzafbJrPTA_VzGWbkSkHygcPGVG1YzUcAEQMpY2uBpYsZ8GtZuC9v_Yqf08Yv1TmP2TNevF1n7ynMGo7YKvbR52hydx8sKhNBguTS80WwA

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client(session_name, api_id, api_hash, plugins=plugins)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
