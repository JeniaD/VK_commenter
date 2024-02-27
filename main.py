import vk_api
from modules.commenter import PostComments

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

# Get list of target links to post on
def GetLinks(file):
    with open(file) as links:
        return links.read().split()

# Captcha solver
def SolveCaptcha(c):
    print("[!] Captcha needed:", c.get_url())
    key = input("[>] Please enter the code: ")
    return c.try_again(key)

def main():
    global MESSAGES
    global LOGIN
    global PASSWORD
    print("VK Commenter\n")

    if not LoadConfig():
        LOGIN = input("Login: ")
        PASSWORD = input("Password: ")
        MESSAGES += [input("Comment: ")]

    vk_session = vk_api.VkApi(login=LOGIN, password=PASSWORD, app_id=6121396, captcha_handler=SolveCaptcha)
    vk_session.auth()

    vk = vk_session.get_api()

    print("[?] Login successful")

    PostComments(vk, MESSAGES, GetLinks(LINKSFILE))
if __name__ == "__main__": main()
