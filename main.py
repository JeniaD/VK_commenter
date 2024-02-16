import vk_api
import random
import time

MESSAGES = [] # Messages to post
FORCEQUIT = False # Quit if unknown error has occurred

# Change cyrillic characters to latin to avoid detection in VK
def Obfuscate(msg):
    if random.getrandbits(1):
        msg = msg.replace('о', 'o')
    if random.getrandbits(1):
        msg = msg.replace('е', 'e')
    
    return msg

# Get random message
def GetMessage():
    return Obfuscate(random.choice(MESSAGES))

# Get list of target links to post on
def GetLinks(file):
    with open(file) as links:
        return links.read().split()

# Convert link to post to ID
def LinkToID(link):
    return link.split("wall")[-1].split('_')

# Deprecated (used to get token by login/password)
def GetToken(login, password):
    vk = vk_api.VkApi(login, password)
    vk.auth()
    time.sleep(3)
    vk = vk.get_api()
    
    user = vk.users.get()
    
    import json
    with open('vk_config.v2.json', 'r') as data_file:
        data = json.load(data_file)

    for xxx in data[login]['token'].keys():
        for yyy in data[login]['token'][xxx].keys():
            accessToken = data[login]['token'][xxx][yyy]['access_token']
    
    return accessToken

# Captcha solver
def SolveCaptcha(c):
    print("[!] Captcha needed:", c.get_url())
    key = input("[>] Please enter the code: ")
    return c.try_again(key)

def main():
    global MESSAGES
    global FORCEQUIT
    print("VK Commenter\n")
    
    links = GetLinks("links.txt")
    login = input("Login: ")
    password = input("Password: ")
    MESSAGES += [input("Comment: ")]

    # session = vk_api.VkApi(token=GetToken(login, password))
    # vk = session.get_api()

    vk_session = vk_api.VkApi(login=login, password=password, app_id=6121396, captcha_handler=SolveCaptcha)
    vk_session.auth()

    vk = vk_session.get_api()

    print("[?] Login successful")

    for link in links:
        ids = LinkToID(link)
        try:
            status = vk.wall.createComment(owner_id=ids[0], post_id=ids[1], message=GetMessage())
        except Exception as e:
            if "parent deleted" in str(e).lower(): print(f"[-] {e} ({link})")
            elif "captcha" in str(e).lower():
                print("[!] Captcha needed")
                exit()
            else:
                print(f"[!] Unknown error: {e} ({link})")
                # print(ids)
                if FORCEQUIT: exit()
        else:
            print("[+] Posted on", link)

if __name__ == "__main__": main()
