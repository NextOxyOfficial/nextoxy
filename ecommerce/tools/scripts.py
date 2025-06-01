from ecommerce.models import Plugin, ShopPlugin

# these code will be added before footer 
def generateCode(shop):
    code = ''
    fb_chat = ShopPlugin.objects.filter(shop=shop, activated=True, plugin__code='fbchat').first()
    if fb_chat:
        code += fb_chat.data['fields']['Code']['value']
    return code
# these code will be added before footer 
def generateNavCode(shop):
    code = ''
    pl = ShopPlugin.objects.filter(shop=shop, activated=True, plugin__code='gverigy').first()
    if pl:
        code += pl.data['fields']['Code']['value']
    return code

