import vk_api
import argparse

from modules.commenter import PostComments
from modules.poster import PublishPosts

def LoadConfig():
    import config
    return config.LOGIN, config.PASSWORD, config.LINKSFILE, config.MESSAGES

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
    parser = argparse.ArgumentParser(description="VK commenter script")
    parser.add_argument("mode", choices=["comment", "post"], help="Attack mode")
    parser.add_argument("--config", help="Python config file")
    parser.add_argument("--login", help="User login")
    parser.add_argument("--password", help="User password")
    parser.add_argument("--message", help="Message to post")
    parser.add_argument("--links", help="Target links file")
    args = parser.parse_args()

    print("VK Commenter\n")

    if args.config: LOGIN, PASSWORD, LINKSFILE, MESSAGES = LoadConfig()
    else:
        if args.login: LOGIN = args.login
        else: LOGIN = input("Login: ")

        if args.password: PASSWORD = args.password
        else: PASSWORD = input("Password: ")

        if args.message: MESSAGES = [args.message]
        else: MESSAGES = [input("Message: ")]

        if args.links: LINKSFILE = args.links
        else: LINKSFILE = input("Links file: ")

    vk_session = vk_api.VkApi(login=LOGIN, password=PASSWORD, app_id=6121396, captcha_handler=SolveCaptcha)
    vk_session.auth()

    vk = vk_session.get_api()

    print("[?] Login successful")

    if args.mode == "comment":
        PostComments(vk, MESSAGES, GetLinks(LINKSFILE))
    elif args.mode == "post":
        PublishPosts(vk, MESSAGES, GetLinks(LINKSFILE))
if __name__ == "__main__": main()
