from yaml import load
from jinja2 import Environment, FileSystemLoader


class ClientBuilder():

    def __init__(self, configuration):
        """Initializes the Builder

        :param configuration: A yaml string containing all information needed for the client
        """
        self.config = load(configuration)

    def build(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('client.stub')
        out = template.render(config=self.config)
        client_file = open('../client.py', 'w')
        client_file.write(out)
        client_file.close()


if __name__ == "__main__":
    file = open('api.yaml', 'r')
    config = file.read()
    file.close()
    cb = ClientBuilder(config)
    cb.build()
