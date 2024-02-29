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
    return link.replace("https://vk.com/", '').replace("http://vk.com/", '').replace("wall", '')

def Post(vk, comment, id):
    vk.wall.post(owner_id=id, message=comment)

def PublishPosts(vk, messages, links, forceQuit=False):
    for link in links:
        id = LinkToID(link)
        try:
            Post(vk, GetMessage(messages), id)
        except Exception as e:
            if "parent deleted" in str(e).lower():
                print(f"[-] {e} ({link})")
            else:
                print(f"[-] {e} ({link})")
                if forceQuit: exit()
        else:
            print("[+] Posted on", link)