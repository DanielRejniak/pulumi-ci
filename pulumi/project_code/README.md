# mai-aia-poc-deploy

This repo contains the Pulumi project code and is attached as a git submodule to `mai-aia-poc-deploy-config`.

The directory at `pulumi/projects/..` contains a set of Pulumi projects where each project everything that is required to deploy a Pulumi stack. This included the Pulumi program `(e.g. __main__.py )` and any addional files associated with stack definition. 

Additionally the code at `pulumi/projects/..` is referanced in `mai-aia-poc-deploy-config` and acts as shared content.