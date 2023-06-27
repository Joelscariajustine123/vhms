import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings
import logging

logger = logging.getLogger(__name__)




class Command(BaseCommand):
    help = 'Starts the Ethereum node'

    def handle(self, *args, **options):
        # Get the configuration values from Django settings
        datadir = settings.ETHEREUM_DATADIR
        network_id = settings.ETHEREUM_NETWORK_ID
        rpc_port = settings.ETHEREUM_RPC_PORT
        rpc_address = settings.ETHEREUM_RPC_ADDRESS
        allowed_cors_domains = settings.ETHEREUM_ALLOWED_CORS_DOMAINS
        p2p_port = settings.ETHEREUM_P2P_PORT
        num_threads = settings.ETHEREUM_MINER_THREADS

        # Set the command with appropriate parameters
        command = [
            'geth',
            '--datadir', datadir,
            '--networkid', network_id,
            '--rpc', '--rpcapi', 'personal,eth,net,web3',
            '--rpcport', str(rpc_port),
            '--rpcaddr', rpc_address,
            '--rpccorsdomain', allowed_cors_domains,
            '--port', str(p2p_port),
            '--ipcdisable',
            '--mine',
            '--minerthreads', str(num_threads)
        ]

        try:
            # Run the command
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Wait for the process to complete (optional)
            process.wait()

            # Log the output
            output, error = process.communicate()
            output = output.decode()
            error = error.decode()
            logger.info(output)
            logger.error(error)

        except Exception as e:
            logger.exception('Error starting Ethereum node: {}'.format(str(e)))
import subprocess
from django.core.management.base import BaseCommand
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Starts the Ethereum node'

    def handle(self, *args, **options):
        # Get the configuration values from Django settings
        datadir = settings.ETHEREUM_DATADIR
        network_id = settings.ETHEREUM_NETWORK_ID
        rpc_port = settings.ETHEREUM_RPC_PORT
        rpc_address = settings.ETHEREUM_RPC_ADDRESS
        allowed_cors_domains = settings.ETHEREUM_ALLOWED_CORS_DOMAINS
        p2p_port = settings.ETHEREUM_P2P_PORT
        num_threads = settings.ETHEREUM_MINER_THREADS

        # Set the command with appropriate parameters
        command = [
            'geth',
            '--datadir', datadir,
            '--networkid', network_id,
            '--rpc', '--rpcapi', 'personal,eth,net,web3',
            '--rpcport', str(rpc_port),
            '--rpcaddr', rpc_address,
            '--rpccorsdomain', allowed_cors_domains,
            '--port', str(p2p_port),
            '--ipcdisable',
            '--mine',
            '--minerthreads', str(num_threads)
        ]

        try:
            # Run the command
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Wait for the process to complete (optional)
            process.wait()

            # Log the output
            output, error = process.communicate()
            output = output.decode()
            error = error.decode()
            logger.info(output)
            logger.error(error)

        except Exception as e:
            logger.exception('Error starting Ethereum node: {}'.format(str(e)))
