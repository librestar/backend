import json
import typing as t
import ansible_runner
from uuid import uuid4

from app.db.session import SessionLocal
from app.db.models.port import Port
from app.db.models.user import User
from app.db.models.server import Server
from app.db.models.port_forward import PortForwardRule
from app.db.crud.server import get_server
from app.db.crud.port import get_port

from tasks import celery_app
from tasks.utils.runner import run_async
from tasks.utils.handlers import iptables_finished_handler, status_handler


@celery_app.task()
def brook_runner(
    port_id: int,
    server_id: int,
    port_num: int,
    command: str = None,
    args: str = None,
    remote_ip: str = None,
    update_status: bool = False,
):
    server = get_server(SessionLocal(), server_id)

    extravars = {
        "host": server.ansible_name,
        "local_port": port_num,
        "remote_ip": remote_ip,
        "brook_args": f"{command} {args}",
        "update_status": update_status,
        "update_brook": update_status and not server.config.get('brook'),
    }
    r = run_async(
        server=server,
        playbook="brook.yml",
        extravars=extravars,
        status_handler=lambda s, **k: status_handler(port_id, s, update_status),
        finished_callback=iptables_finished_handler(server, port_id, True)
        if update_status
        else lambda r: None,
    )
    return r[1].config.artifact_dir