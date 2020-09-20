import requests
from bs4 import BeautifulSoup


class AternosAPI():
    def __init__(self, headers, cookie, SEC):
        self.headers = {}
        self.cookies = {}
        self.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
        self.headers['Cookie'] = headers
        self.cookies['ATERNOS_SESSION'] = cookie
        self.SEC = SEC
        self.JavaSoftwares = ['Vanilla', 'Spigot', 'Forge', 'Magma', 'Snapshot', 'Bukkit', 'Paper', 'Modpacks', 'Glowstone']
        self.BedrockSoftwares = ['Bedrock', 'Pocketmine-MP']
        self.CheckVaildInput()

    def CheckVaildInput(self):
        """Determine if cookies are valid."""
        webserver = requests.get(url='https://aternos.org/server/',cookies=self.cookies,headers=self.headers)
        if ("logout" in webserver):
            pass
        else:
            return "Invalid Cookie"

    def GetStatus(self):
        """Get server status as a str."""
        webserver = requests.get(url='https://aternos.org/server/',cookies=self.cookies,headers=self.headers)
        webdata = BeautifulSoup(webserver.content, 'html.parser')
        status = webdata.find('span', class_='statuslabel-label').get_text()
        status = status.strip()
        return status
    
    def GetPlayerCount(self):
        """Get count of players/slots from homepage."""
        webserver = requests.get(url='https://aternos.org/server/',cookies=self.cookies,headers=self.headers)
        webdata = BeautifulSoup(webserver.content, 'html.parser')
        status = webdata.find('span', id='players').get_text()
        status = status.strip()
        return status

    def GetPlayers(self):
        """Get list of player names."""
        webserver = requests.get(url='https://aternos.org/players/',cookies=self.cookies,headers=self.headers)
        webdata = BeautifulSoup(webserver.content, 'html.parser')
        result = []
        players = webdata.find('div', class_='playerlist')
        players = players.findChildren("div", class_="player")
        for p in players:
            player = p.findChildren("div", class_="playerinfo")[0]
            player = player.findChildren("div", class_="playername")[0].get_text()
            player = player.strip()
            result.append(player)
        return result

    def StartServer(self):
        """Skip queue and start server."""
        serverstatus = self.GetStatus()
        if serverstatus == "Online":
            return "Server Already Running"
        else:
            startserver = requests.get(url=f"https://aternos.org/panel/ajax/start.php?headstart=0&SEC={self.SEC}", cookies=self.cookies, headers=self.headers)
            self.skip_queue()
    
    def StopServer(self):
        """Stop server."""
        serverstatus = self.GetStatus()
        if serverstatus == "Offline":
            return "Server Already Offline"
        else:
            stopserver = requests.get(url=f"https://aternos.org/panel/ajax/stop.php?SEC={self.SEC}",cookies=self.cookies,headers=self.headers)
            return "Server Stopped"

    def GetServerInfo(self):
        """Get server IP, port, and software."""
        ServerInfo = requests.get(url='https://aternos.org/server/',cookies=self.cookies,headers=self.headers)
        ServerInfo = BeautifulSoup(ServerInfo.content, 'html.parser')

        Software = ServerInfo.find('span', id='software').get_text()
        Software = Software.strip()
        print(Software)

        if(Software in self.JavaSoftwares):
            IP = ServerInfo.find('div', class_='server-ip mobile-full-width').get_text()
            IP = IP.strip()

            IP = IP.split(" ")
            IP = IP[0].strip()

            Port = "25565(Optional)"

            return f"{IP},{Port},{Software}"

        elif(Software in self.BedrockSoftwares):
            IP = ServerInfo.find('span', id='ip').get_text()
            IP = IP.strip()

            Port = ServerInfo.find('span', id='port').get_text()
            Port = Port.strip()

            return f"{IP},{Port},{Software}"

    def queue_confirm(self):
        """Confirm Aternos server start."""
        confirm = requests.get(url=f'https://aternos.org/panel/ajax/confirm.php?SEC={self.SEC}',cookies=self.cookies,headers=self.headers)
        return confirm.status_code

    def queue_number(self):
        """Position in start queue."""
        webserver = requests.get(url='https://aternos.org/server/',cookies=self.cookies,headers=self.headers)
        webdata = BeautifulSoup(webserver.content, 'html.parser')
        status = webdata.find('span', class_='server-status-label-right').get_text()
        return status.strip()

    def skip_queue(self):
        """Skip start queue."""
        i = 0
        while i < 1:
            serverstatus = self.GetStatus()
            queue_number = self.queue_number()
            confirm = self.queue_confirm()
            print(serverstatus+" : "+queue_number+" : "+str(confirm)+"\r", end="")
            if serverstatus == "Online":
                i = 1
                return "Server Started"
