from charms.reactive import when, when_not, set_state


@when_not('${metadata.package}.installed')
def install_${metadata.package.replace('-', '_')}():
    #raw
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    #end raw
    set_state('${metadata.package}.installed')
