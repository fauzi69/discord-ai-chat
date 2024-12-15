import requests, random, sys, yaml, time, openai

class Discord:

    def __init__(self, t):
        self.base = "https://discord.com/api/v9"
        self.auth = { 'authorization': t }
        
    def getMe(self):
        u = requests.get(self.base + "/users/@me", headers=self.auth).json()
        return u
        
    def getMessage(self, cid, l):
        u = requests.get(self.base + "/channels/" + str(cid) + "/messages?limit=" + str(l), headers=self.auth).json()
        return u
        
    def sendMessage(self, cid, txt):    
        u = requests.post(self.base + "/channels/" + str(cid) + "/messages", headers=self.auth, json={ 'content': txt }).json()
        return u

    def replyMessage(self, cid, mid, txt):    
        u = requests.post(self.base + "/channels/" + str(cid) + "/messages", headers=self.auth, json={ 'content': txt, 'message_reference': { 'message_id': str(mid) } }).json()
        return u

    def deleteMessage(self, cid, mid):
        u = requests.delete(self.base + "/channels/" + str(cid) + "/messages/" + str(mid), headers=self.auth)
        return u

def quote():
    u = requests.get("https://raw.githubusercontent.com/lakuapik/quotes-indonesia/master/raw/quotes.min.json").json()
    return random.choice(list(u))['quote']

def gpt_reply(prompt, model="gpt-3.5-turbo"):
    try:
        # Customize prompt to encourage casual and adaptive responses
        custom_prompt = f"You're a fun, chill AI buddy. Reply casually and adapt to this style: {prompt}"
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": custom_prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[ERROR] AI response failed: {e}"

def main():
    with open('config.yaml') as cfg:
        conf = yaml.load(cfg, Loader=yaml.FullLoader)

    if not conf['BOT_TOKEN']:
        print("[!] Please provide discord token at config.yaml!")
        sys.exit()

    if not conf['CHANNEL_ID']:
        print("[!] Please provide channel id at config.yaml!")
        sys.exit()

    openai.api_key = conf.get('OPENAI_API_KEY')
    if not openai.api_key:
        print("[!] Please provide OpenAI API key at config.yaml!")
        sys.exit()

    mode = conf['MODE']
    delay = conf['DELAY']
    del_after = conf['DEL_AFTER']

    if not mode: 
        mode = "quote"
        
    while True:
        for token in conf['BOT_TOKEN']:
            try:
                for chan in conf['CHANNEL_ID']:

                    Bot = Discord(token)
                    me = Bot.getMe()['username'] + "#" + Bot.getMe()['discriminator']
                    
                    if mode == "quote":
                        q = quote()
                        send = Bot.sendMessage(chan, q)
                        print("[{}][{}][QUOTE] {}".format(me, chan, q))                
                        if del_after:
                            Bot.deleteMessage(chan, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))

                    elif mode == "ai_chat":
                        res = Bot.getMessage(chan, "1")
                        getlast = list(reversed(res))[0]                
                        user_message = getlast['content']
                        ai_reply = gpt_reply(user_message)

                        if conf['REPLY']:
                            send = Bot.replyMessage(chan, getlast['id'], ai_reply)
                            print("[{}][{}][AI_REPLY] {}".format(me, chan, ai_reply))
                        else:
                            send = Bot.sendMessage(chan, ai_reply)
                            print("[{}][{}][AI_REPLY] {}".format(me, chan, ai_reply))

                        if del_after:
                            Bot.deleteMessage(chan, send['id'])
                            print("[{}][DELETE] {}".format(me, send['id']))

            except Exception as e:
                print(f"[Error] {token} : {e}")
        
        print("-------[ Delay for {} seconds ]-------".format(delay))
        time.sleep(delay)

if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")
