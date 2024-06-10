import os
import subprocess
import logging
import click

def setup_logging():
    debug_mode = os.environ.get('RXD_DEBUG', 'False') == 'True'
    logging_level = logging.DEBUG if debug_mode else logging.INFO
    logging.basicConfig(level=logging_level, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info(f"Debug mode: {debug_mode}")

class GPGManager:
    @staticmethod
    def kill_gpg_agent():
        try:
            subprocess.run(['gpgconf', '--kill', 'gpg-agent'], check=True)
            logging.info("GPG agent cache cleared successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to clear GPG agent cache: {e}")

    @staticmethod
    def encrypt_file(input_file, output_file):
        try:
            cmd = [
                'gpg',
                '--symmetric',
                '--cipher-algo', 'AES256',
                '--batch', '--yes',
                '--output', output_file,
                input_file
            ]
            subprocess.run(cmd, check=True)
            logging.info(f"File encrypted successfully to {output_file}.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to encrypt file: {e}")

    @staticmethod
    def decrypt_file(input_file, output_file):
        try:
            cmd = [
                'gpg',
                '--decrypt',
                '--batch', '--yes',
                '--output', output_file,
                input_file
            ]
            subprocess.run(cmd, check=True)
            logging.info(f"File decrypted successfully to {output_file}.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to decrypt file: {e}")

class EnvManager:
    def __init__(self, project_path, organization, generate_file=False):
        self.project_path = project_path
        self.organization = organization
        self.generate_file = generate_file
        try:
            self.base_path = os.environ['RXD_LOCAL_ENV_PATH']
            logging.debug(f"RXD_LOCAL_ENV_PATH={self.base_path}")
        except KeyError:
            logging.error("The environment variable 'RXD_LOCAL_ENV_PATH' is not set")
            raise
        
        self.base_path = os.path.expanduser(self.base_path)
        self.org_dir = os.path.join(self.base_path, self.organization)
        self.env_dir = os.path.join(self.org_dir, '.envs')
        self.template_file = os.path.join(self.project_path, '.envs', '.env.template')
        logging.debug(f"Initialized EnvManager with base_path: {self.base_path}, org_dir: {self.org_dir}, env_dir: {self.env_dir}, template_file: {self.template_file}")

    def load_template_vars(self):
        vars_to_extract = {}
        with open(self.template_file, 'r') as file:
            for line in file:
                if '=' in line:
                    var_name, var_value = line.strip().split('=')
                    vars_to_extract[var_name] = var_value
                    logging.debug(f"Found variable in template: {var_name}")
        return vars_to_extract

    def extract_and_export_vars(self, env_file, vars_to_extract):
        exported_vars = {}
        with open(env_file, 'r') as file:
            for line in file:
                if '=' in line:
                    var_name, var_value = line.strip().split('=', 1)
                    if var_name in vars_to_extract:
                        os.environ[var_name] = var_value
                        exported_vars[var_name] = var_value
                        logging.info(f"Exported {var_name}")
        return exported_vars

    def write_exported_vars(self, export_file, exported_vars):
        with open(export_file, 'w') as file:
            for var_name, var_value in exported_vars.items():
                file.write(f'{var_name}={var_value}\n')
                logging.debug(f"Written to export file: {var_name}")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            logging.info(f"Deleted file {file_path}.")
        except OSError as e:
            logging.error(f"Error deleting file {file_path}: {e}")

    def process(self):
        # Load template variables
        template_vars = self.load_template_vars()

        # Check if environment variable is in template file
        if 'ENVIRONMENT' not in template_vars:
            logging.error("The 'ENVIRONMENT' variable is not defined in the .env.template file")
            return {}
        
        environment = os.getenv('ENVIRONMENT', template_vars['ENVIRONMENT'])
        logging.debug(f"Environment set to: {environment}")
        
        # Validate the environment and set the corresponding file name
        if environment == 'development':
            env_file_name = '.env.dev.gpg'
        elif environment == 'production':
            env_file_name = '.env.prd.gpg'
        elif environment == 'staging':
            env_file_name = '.env.stg.gpg'
        else:
            logging.error("Invalid environment. Choose from 'development', 'production', or 'staging'.")
            return {}

        encrypted_file = os.path.join(self.env_dir, env_file_name)
        decrypted_file = os.path.join(self.env_dir, 'local.env')

        # Clear GPG agent cache
        GPGManager.kill_gpg_agent()

        # Decrypt the file
        GPGManager.decrypt_file(encrypted_file, decrypted_file)

        # Extract and export variables
        exported_vars = self.extract_and_export_vars(decrypted_file, template_vars)

        # Add environment variable
        exported_vars['ENVIRONMENT'] = environment

        # Write the exported variables to a temporary file if generate_file is True
        if self.generate_file:
            export_file = os.path.join(self.project_path, '.envs', '.env.exported')
            self.write_exported_vars(export_file, exported_vars)

        # Delete the decrypted file
        self.delete_file(decrypted_file)

        return exported_vars

    def encrypt_env_file(self, env_file):
        output_file = os.path.join(self.env_dir, os.path.basename(env_file) + '.gpg')
        GPGManager.encrypt_file(env_file, output_file)

    def decrypt_env_file(self, project_path, filename):
        # Crear la carpeta .envs en el directorio actual si no existe
        output_dir = os.path.join(project_path, '.envs')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        output_file = os.path.join(output_dir, '.env.exported_' + filename)
        
        env_files = {
            'development': '.env.dev.gpg',
            'production': '.env.prd.gpg',
            'staging': '.env.stg.gpg'
        }

        if filename in env_files:
            input_file = os.path.join(self.env_dir, env_files[filename])
        else:
            input_file = os.path.join(self.env_dir, filename)
        
        GPGManager.decrypt_file(input_file, output_file)
        
        exported_vars = {}
        with open(output_file, 'r') as file:
            for line in file:
                if '=' in line:
                    var_name, var_value = line.strip().split('=', 1)
                    exported_vars[var_name] = var_value
                    logging.debug(f"Extracted variable: {var_name}")
        
        logging.info(f"File decrypted successfully to {output_file}.")
        return exported_vars

@click.group()
def cli():
    """CLI to manage environment variables using GPG."""
    setup_logging()

@cli.command()
@click.argument('env_file', type=click.Path(exists=True))
@click.option('--organization', default='default_org', help='Name of the organization')
def encrypt(env_file, organization):
    """Encrypt a .env file."""
    project_path = os.getcwd()
    manager = EnvManager(project_path, organization)
    manager.encrypt_env_file(env_file)

@cli.command()
@click.argument('project_path', type=click.Path(exists=True))
@click.argument('filename', type=str)
@click.option('--organization', default='default_org', help='Name of the organization')
def decrypt(project_path, filename, organization):
    """Decrypt a specified file."""
    manager = EnvManager(project_path, organization)
    exported_vars = manager.decrypt_env_file(project_path, filename)
    for var_name, var_value in exported_vars.items():
        print(f'{var_name}={var_value}')

@cli.command()
@click.argument('project_path', type=click.Path(exists=True))
@click.argument('organization', type=str)
@click.option('--generate-file', is_flag=True, help='Generate an exported.env file')
def process(project_path, organization, generate_file):
    """Process environment files."""
    manager = EnvManager(project_path, organization, generate_file)
    exported_vars = manager.process()
    for var_name, var_value in exported_vars.items():
        print(f'{var_name}={var_value}')

@cli.command()
@click.argument('organization', type=str)
def init(organization):
    """Initialize the directory structure for a new organization."""
    base_path = os.environ.get('RXD_LOCAL_ENV_PATH', None)
    if not base_path:
        print("The environment variable 'RXD_LOCAL_ENV_PATH' is not set.")
        return

    org_dir = os.path.join(os.path.expanduser(base_path), organization)
    env_dir = os.path.join(org_dir, '.envs')

    try:
        os.makedirs(env_dir, exist_ok=True)
        print(f"Created directory structure for {organization} at {env_dir}")
    except OSError as e:
        print(f"Error creating directory structure: {e}")


@cli.command()
def hello():
    """Print a friendly hello message."""
    message = """
    ######################################
    #                                    #
    #  Hello from 'Central Var RXD' CLI! #
    #                                    #
    ######################################
    """
    print(message)

if __name__ == '__main__':
    cli()