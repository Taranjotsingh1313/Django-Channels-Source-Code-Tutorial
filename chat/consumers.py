from channels.generic.websocket import AsyncJsonWebsocketConsumer

class ChatConsumer(AsyncJsonWebsocketConsumer):
    '''Called when user wants to connect using websockets'''
    async def connect(self):
        await self.accept()
    
    '''When user wants to send us the data'''
    async def receive_json(self, content):
        data = content
        if data['command'] == 'join':
            await self.channel_layer.group_add(
                data['groupname'],
                self.channel_name
            )
            print("user added")
        elif data['command'] == 'send':
            if self.scope['user'].is_authenticated:
                await self.channel_layer.group_send(
                    'publicchat',
                    {
                        'type':'chat.message', # this should be a function and . means _
                        'message':data['message'],
                        'user':str(self.scope['user'])
                    }
                )
            else:
                await self.send_json({
                    'warning':True
                })
          
        '''When user disconnect '''
    async def disconnect(self,msg):
        pass
    async def chat_message(self,event):
        await self.send_json({
            'message':event['message'],
            'user':event['user']
        })
