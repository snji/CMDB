from django.shortcuts import render
from finalcmdb.settings import commands
from .utils import get_acctive_host, is_ssh_up, login_ssh_password
from .models import Server


# Create your views here.

def scanhost(request):
    if request.method == 'POST':
        scanhosts = request.POST.get('scanhosts')
        scanhosts = scanhosts.split(',')
        servers = []
        for net_host in scanhosts:
            active_host = get_acctive_host(net_host)
            for host in active_host:
                if is_ssh_up(host):
                    # server = Server.objects.get(IP=host)
                    # if not server:
                    try:
                        server = Server.objects.get(IP=host)
                    except:
                        server = Server(IP=host)
                    finally:
                        for attr, cmd in commands.items():
                            result = login_ssh_password(host=host, username='westos', password='westos', command=cmd)
                            setattr(server, attr, result)
                        server.save()
                        servers.append(server)
                else:
                    pass
    else:
        return render(request, 'scan.html')

    return render(request, 'scan.html', {'servers': servers})
