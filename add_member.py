import asyncio
import json
from itertools import dropwhile
from helper.helpfun import add_mem

async def main():
        #loads member
        user_id = (json.load(open("data/user.json")))
        #loads users and channel info
        config = (json.load(open("config.json")))
        
        
          
        #list to chcek active member
        activelist = ['UserStatus.LONG_AGO', 'UserStatus.LAST_MONTH', 'UserStatus.LAST_WEEK', 'UserStatus.OFFLINE', 'UserStatus.RECENTLY', 'UserStatus.ONLINE' ]
        #count retrive old state             
        last_active = config["from_date_active"]
        added = 0
        active = []
        for x in dropwhile(lambda y: y != last_active, activelist):
           active.append(x)
        await add_mem(user_id, config, active)

asyncio.run(main())