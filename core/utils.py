import os
import paramiko

from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

address = os.getenv('SSH_HOST')
port = int(os.getenv('SSH_PORT'))
usr = os.getenv('SSH_USER')
pwd = os.getenv('SSH_PASSWORD')


# def launch_on_host(cmd, ignore_stderr=False, host=None):
#     """Launch a command on host using launcher system.

#     Launcher system runs the command with a root privillage.
#     But it could excute only a few limited programs which
#     are in LAUNCHER_BINS_DIR. Also launcher is not a sudoer.
#     So it is safe from attacks atempting to run other
#     dangerous commands.

#     The ip of the host should be given by command line argument --jf-ip
#     or passed by param host.
#     """
#     if host is None:
#         host = None
#         if host is None:
#             raise KeyError('CLI argument --jf-ip not given.')
#     result_stdout, result_stderr = execute_command_ssh(host, 'launcher', 'qwerty', cmd)
#     if result_stdout is None:
#         return None
#     else:
#         result_stdout = result_stdout.decode('utf-8')
#     if result_stderr is not None:
#         result_stderr = result_stderr.decode('utf-8')
#     if not ignore_stderr and result_stderr is not None and len(result_stderr) > 0:
#         raise RemoteError(result_stderr)
#     return result_stdout, result_stderr


def execute_command_ssh(cmd):
    """ Throws IOError when host down or something.
    """
    # address = 1
    # usr = 2
    # pwd = 3 
    # address = address.split(':')
    # if len(address) == 1:
    #     hostname = address[0]
    #     port = 22
    # elif len(address) == 2:
    #     hostname = address[0]
    #     port = address[1]
    # else: #IPv6 case or typo or something
    #     raise ValueError('Unsuppoted address {}'.format(':'.join(address)))


    client = paramiko.SSHClient()
    # client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print(address, port, usr, pwd)
        client.connect(address, port=port, username=usr, password=pwd)
    except paramiko.ssh_exception.SSHException: # tcp timeout
        traceback.print_exc()
        return None, None
    except Exception as e:
        print('eee: ', e)

    _, stdout, stderr = client.exec_command(cmd)
    result_stdout, result_stderr = stdout.read(), stderr.read()
    client.close()

    return result_stdout, result_stderr
