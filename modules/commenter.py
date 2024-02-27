import vk_api
import random

# Randomly change cyrillic characters to latin to avoid detection by repetition
def Obfuscate(msg):
    if random.getrandbits(1):
        msg = msg.replace('о', 'o')
    if random.getrandbits(1):
        msg = msg.replace('е', 'e')
    
    return msg

# Get random message
def GetMessage(messages):
    return Obfuscate(random.choice(messages))

# Convert link to post to ID
def LinkToID(link):
    return link.split("wall")[-1].split('_')

def PostComment(vk, comment, IDs):
    vk.wall.createComment(owner_id=IDs[0], post_id=IDs[1], message=comment)

def PostComments(vk, messages, links, forceQuit=False):
    for link in links:
        ids = LinkToID(link)
        try:
            PostComment(vk, GetMessage(messages), ids)
        except Exception as e:
            if "parent deleted" in str(e).lower():
                print(f"[-] {e} ({link})")
            else:
                print(f"[-] {e} ({link})")
                if forceQuit: exit()
        else:
            print("[+] Posted on", link)