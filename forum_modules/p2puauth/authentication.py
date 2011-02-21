from forum.authentication.base import AuthenticationConsumer, ConsumerTemplateContext, InvalidAuthentication
from forms import ClassicLoginForm

class P2PUAuthConsumer(AuthenticationConsumer):
    def process_authentication_request(self, request):
        form_auth = ClassicLoginForm(request.POST)

        if form_auth.is_valid():
            return form_auth.get_user()
        else:
            raise InvalidAuthentication(" ".join(form_auth.errors.values()[0]))

class P2PUAuthContext(ConsumerTemplateContext):
    mode = 'TOP_STACK_ITEM'
    weight = 10
    human_name = 'P2PU authentication'
    stack_item_template = 'modules/p2puauth/loginform.html'
    show_to_logged_in_user = False

