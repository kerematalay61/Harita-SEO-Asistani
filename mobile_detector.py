"""
Kullanıcının mobil cihaz mı masaüstü mü kullandığını tespit eder.
"""
from user_agents import parse

def is_mobile(user_agent_string):
    user_agent = parse(user_agent_string)
    return user_agent.is_mobile or user_agent.is_tablet
is_mobile(request.headers.get("User-Agent"))
