import os
import logging
import requests
import argh
import time


class Parser(object):
    def __init__(self, base_dir, oddjob_api):
        super(Parser, self).__init__()
        self.base_dir = base_dir
        self.oddjob_api = oddjob_api
        self.logger = logging.getLogger(self.__class__.__name__)

    def parse(self):
        self.parse_documentation_directory()
        self.remove_deleted_items()

    def parse_documentation_directory(self):
        products = os.listdir(self.base_dir)
        for product in products:
            product_path = os.path.join(self.base_dir, product)
            if os.path.isdir(product_path):
                self.logger.debug('Found {}/ product.'.format(product_path))
                product_id = self.get_or_create_product(name=product)
                self.parse_product_directory(directory=product_path, product_id=product_id)
            else:
                self.logger.error('Found file {} in product directory, it should not be here.'
                             .format(product_path))

    def parse_product_directory(self, directory, product_id):
        releases = os.listdir(directory)
        for release in releases:
            release_path = os.path.join(directory, release)
            if os.path.isdir(release_path):
                self.logger.debug('Found {}/ release.'.format(release_path))
                release_id = self.get_or_create_release(name=release, product_id=product_id)
                self.parse_release_directory(directory=release_path, release_id=release_id)
            else:
                self.logger.error('Found file {} in release directory, it should not be here.'
                             .format(release_path))

    def parse_release_directory(self, directory, release_id):
        artifacts = os.listdir(directory)
        for artifact in artifacts:
            artifact_path = os.path.join(directory, artifact)
            if os.path.isdir(artifact_path):
                self.logger.debug('Found {}/ artifact.'.format(artifact_path))
                self.get_or_create_artifact(name=artifact, release_id=release_id)
            else:
                self.logger.error('Found file {} in artifact directory, it should not be here.'
                                      .format(artifact_path))

    def get_or_create_product(self, name):
        product_id = self.get_product_id(name)
        if product_id is None:
            self.logger.debug('Product {} does not exist.'.format(name))
            return self.create_product(name=name)
        else:
            self.logger.debug('Product {} already exists.'.format(name))
            return product_id

    def create_product(self, name):
        new = {}
        new['product'] = {}
        new['product']['name'] = name
        response = requests.post('{}/products'.format(self.oddjob_api), json=new)
        if response.status_code == 201:
            self.logger.debug('Product {} created.'.format(name))
            return response.json().get('product').get('id')

    def get_or_create_release(self, name, product_id):
        release_id = self.get_release_id(name, product_id)
        if release_id is None:
            self.logger.debug('Release {} does not exist.'.format(name))
            return self.create_release(name=name, product_id=product_id)
        else:
            self.logger.debug('Release {} already exists.'.format(name))
            return release_id

    def create_release(self, name, product_id):
        new = {}
        new['release'] = {}
        new['release']['name'] = name
        new['release']['product'] = product_id
        response = requests.post('{}/releases'.format(self.oddjob_api), json=new)
        if response.status_code == 201:
            self.logger.debug('Release {} created.'.format(name))
            return response.json().get('release').get('id')

    def get_or_create_artifact(self, name, release_id):
        artifact_id = self.get_artifact_id(name, release_id)
        if artifact_id is None:
            self.logger.debug('Artifact {} does not exist.'.format(name))
            return self.create_artifact(name=name, release_id=release_id)
        else:
            self.logger.debug('Artifact {} already exists.'.format(name))
            return artifact_id

    def create_artifact(self, name, release_id):
        new = {}
        new['artifact'] = {}
        new['artifact']['name'] = name
        new['artifact']['release'] = release_id
        response = requests.post('{}/artifacts'.format(self.oddjob_api), json=new)
        if response.status_code == 201:
            self.logger.debug('Artifact {} created.'.format(name))
            return response.json().get('artifact').get('id')

    def remove_deleted_items(self):
        local_paths = set(self.get_local_paths())
        remote_paths = set(self.get_remote_paths())
        remove_paths = list(remote_paths.difference(local_paths))
        sorted_remote_paths = sorted(remove_paths, key=lambda x: -len(x.split('/')))
        self.remove_paths(paths=sorted_remote_paths)

    def get_local_paths(self):
        local_paths = []
        products = os.listdir(self.base_dir)
        for product in products:
            product_path = os.path.join(self.base_dir, product)
            if os.path.isdir(product_path):
                local_paths.append(product)
                releases = os.listdir(product_path)
                for release in releases:
                    release_path = os.path.join(product_path, release)
                    if os.path.isdir(release_path):
                        local_paths.append(u'{}/{}'.format(product, release))
                        artifacts = os.listdir(release_path)
                        for artifact in artifacts:
                            artifact_path = os.path.join(release_path, artifact)
                            if os.path.isdir(artifact_path):
                                local_paths.append(u'{}/{}/{}'.format(product, release, artifact))
        return local_paths

    def get_remote_paths(self):
        response = requests.get('{}/path-tree'.format(self.oddjob_api))
        if response.status_code == 200:
            return response.json()
        else:
            return []

    def remove_paths(self, paths):
        for path in paths:
            parts = path.split('/')
            if len(parts) == 3:
                self.logger.debug('Going to remove artifact {}/{}/{}'.format(*parts))
                self.delete_artifact(product=parts[0], release=parts[1], artifact=parts[2])
            if len(parts) == 2:
                self.logger.debug('Going to remove release {}/{}'.format(*parts))
                self.delete_release(product=parts[0], release=parts[1])
            if len(parts) == 1:
                self.logger.debug('Going to remove product {}'.format(*parts))
                self.delete_product(product=parts[0])

    def delete_product(self, product):
        product_id = self.get_product_id(product)
        if product_id:
            response = requests.delete('{}/products/{}'.format(self.oddjob_api, product_id))
            if response.status_code == 204:
                self.logger.info('Deleted product {}'.format(product))

    def delete_release(self, product, release):
        product_id = self.get_product_id(product)
        if product_id:
            release_id = self.get_release_id(release, product_id)
            if release_id:
                response = requests.delete('{}/releases/{}'.format(self.oddjob_api, release_id))
                if response.status_code == 204:
                    self.logger.info('Deleted release {}'.format(release))

    def delete_artifact(self, product, release, artifact):
        product_id = self.get_product_id(product)
        if product_id:
            release_id = self.get_release_id(release, product_id)
            if release_id:
                artifact_id = self.get_artifact_id(artifact, release_id)
                if artifact_id:
                    response = requests.delete('{}/artifacts/{}'
                                               .format(self.oddjob_api, artifact_id))
                    if response.status_code == 204:
                        self.logger.info('Deleted artifact {}'.format(artifact))

    def get_product_id(self, product_name):
        product_id = None
        response = requests.get('{}/products?name={}'.format(self.oddjob_api, product_name))
        if response.status_code == 200:
            if len(response.json().get('product')) == 1:
                product_id = response.json().get('product')[0].get('id')
        return product_id

    def get_release_id(self, release_name, product_id):
        release_id = None
        response = requests.get('{}/releases?name={}&product={}'
                                .format(self.oddjob_api, release_name, product_id))
        if response.status_code == 200:
            if len(response.json().get('release')) == 1:
                release_id = response.json().get('release')[0].get('id')
        return release_id

    def get_artifact_id(self, artifact_name, release_id):
        artifact_id = None
        response = requests.get('{}/artifacts?name={}&release={}'
                                .format(self.oddjob_api, artifact_name, release_id))
        if response.status_code == 200:
            if len(response.json().get('artifact')) == 1:
                artifact_id = response.json().get('artifact')[0].get('id')
        return artifact_id


def main(base_dir='/data/docs/', oddjob_api='http://webapp:8000/api/v1', interval=10):
    logging.basicConfig(level=logging.DEBUG)
    parser = Parser(base_dir=base_dir, oddjob_api=oddjob_api)
    while True:
        try:
            parser.parse()
        except Exception:
            pass
        time.sleep(interval)

argh.dispatch_command(main)
