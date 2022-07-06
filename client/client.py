from subsystems import configuration, renderer, resource, state



def main():
    # we load the subsystems in the order required, the subsystems assume that the ones before have loaded OK.
    # if they haven't, runtime errors should be generated.
    configuration.Configuration.instance().on_active()
    resource.Resource.instance().on_active()
    state.State.instance.on_active()
    renderer.Renderer.instance.on_active()
