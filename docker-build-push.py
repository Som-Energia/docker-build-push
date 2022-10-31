import sys
import docker


def build_push_docker_image(moll, dockerfile_path, registry_tag):
    '''
    moll: e.g. http://moll.somenergia.lan:2375/
    registry_tag: registry.somenergia.coop:5000/somenergia-something:latest

    assumes that you've logged in at least once so that you have the login credentials
    under ~/.docker/config.json
    '''

    client = docker.DockerClient(base_url=moll)

    # TODO push :latest and date, sha or something to pin the requirements version and detect image registry changes

    r = client.images.build(path=dockerfile_path, tag=registry_tag)
    print(r)

    print("push image to registry")
    r = client.api.push(registry_tag)
    print(r)
    return r


if __name__ == '__main__':

    if len(sys.argv)-1 < 3:
        print("usage: python docker-build-push moll dockerfile_path registry_tag")
        sys.exit(0)

    moll = sys.argv[1]
    dockerfile_path = sys.argv[2]
    registry_tag = sys.argv[3]

    print(f'Running build push with {moll} {dockerfile_path} {registry_tag}')
    build_push_docker_image(moll, dockerfile_path, registry_tag)

