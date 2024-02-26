import vk_api
import random

MESSAGES = [] # Messages to post
FORCEQUIT = False # Quit if unknown error has occurred
LINKSFILE = "links.txt"
LOGIN = ""
PASSWORD = ""

def LoadConfig():
    global LOGIN, PASSWORD, LINKSFILE, MESSAGES
    try:
        import config
        LOGIN = config.LOGIN
        PASSWORD = config.PASSWORD
        LINKSFILE = config.LINKSFILE
        MESSAGES = config.MESSAGES
    except:
        return False
    return True

# Randomly change cyrillic characters to latin to avoid detection in VK
def Obfuscate(msg):
    if random.getrandbits(1):
        msg = msg.replace('о', 'o')
    if random.getrandbits(1):
        msg = msg.replace('е', 'e')
    
    return msg

# Get random message
def GetMessage():
    global MESSAGES
    return Obfuscate(random.choice(MESSAGES))

# Get list of target links to post on
def GetLinks(file):
    with open(file) as links:
        return links.read().split()

# Convert link to post to ID
def LinkToID(link):
    return link.split("wall")[-1].split('_')

# Captcha solver
def SolveCaptcha(c):
    print("[!] Captcha needed:", c.get_url())
    key = input("[>] Please enter the code: ")
    return c.try_again(key)

def main():
    global MESSAGES
    global FORCEQUIT
    global LOGIN
    global PASSWORD
    print("VK Commenter\n")

    if not LoadConfig():
        LOGIN = input("Login: ")
        PASSWORD = input("Password: ")
        MESSAGES += [input("Comment: ")]
    
    links = GetLinks(LINKSFILE)

    vk_session = vk_api.VkApi(login=LOGIN, password=PASSWORD, app_id=6121396, captcha_handler=SolveCaptcha)
    vk_session.auth()

    vk = vk_session.get_api()

    print("[?] Login successful")

    for link in links:
        ids = LinkToID(link)
        try:
            status = vk.wall.createComment(owner_id=ids[0], post_id=ids[1], message=GetMessage())
        except Exception as e:
            if "parent deleted" in str(e).lower():
                print(f"[-] {e} ({link})")
            else:
                print(f"[-] {e} ({link})")
                if FORCEQUIT: exit()
        else:
            print("[+] Posted on", link)

if __name__ == "__main__": main()
