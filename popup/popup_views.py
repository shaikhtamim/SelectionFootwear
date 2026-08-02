from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from user_agents import parse
import traceback

from .models import VisitorLead


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


@require_POST
def save_visitor(request):
    try:

        name = request.POST.get("name")
        shop_name = request.POST.get("shop_name")
        mobile = request.POST.get("mobile")

        ip = get_client_ip(request)

        user_agent_string = request.META.get("HTTP_USER_AGENT", "")
        user_agent = parse(user_agent_string)

        browser = user_agent.browser.family
        operating_system = user_agent.os.family

        if user_agent.is_mobile:
            device = "Mobile"
        elif user_agent.is_tablet:
            device = "Tablet"
        else:
            device = "Desktop"

        visitor, created = VisitorLead.objects.get_or_create(
        mobile=mobile,
        shop_name=shop_name,
        defaults={
        "name": name,
        "ip_address": ip,
        "browser": browser,
        "device": device,
        "operating_system": operating_system,
        "user_agent": user_agent_string,
        "visit_count": 1,
        "last_visit": timezone.now(),
    },
)

        if not created:
            visitor.name = name
            visitor.shop_name = shop_name
            visitor.ip_address = ip
            visitor.browser = browser
            visitor.device = device
            visitor.operating_system = operating_system
            visitor.user_agent = user_agent_string
            visitor.visit_count += 1
            visitor.last_visit = timezone.now()
            visitor.save()

        return JsonResponse({
            "status": "success"
        })

    except Exception:
        traceback.print_exc()

        return JsonResponse({
            "status": "error"
        }, status=500)