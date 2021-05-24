from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

class OrganisorAndLoginRequiredMixin(AccessMixin):

    def dispatch(self,request,*args,**kwargs):
        if not request.user.isauthenticated or not request.user.is_organisor:
            return redirect("login")            
        return super().dispatch(request,*args,**kwargs)