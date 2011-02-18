from forum_modules.localauth.authentication import LocalAuthConsumer, LocalAuthContext

class P2PUAuthConsumer(LocalAuthConsumer):
    pass

class P2PUAuthContext(LocalAuthContext):
    mode = 'TOP_STACK_ITEM'
    weight = 10
    human_name = 'P2PU authentication'
    stack_item_template = 'modules/p2puauth/loginform.html'
