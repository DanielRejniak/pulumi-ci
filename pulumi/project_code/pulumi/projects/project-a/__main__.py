"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources

# Config
config = pulumi.Config()
RESOURCE_GROUP_NAME = config.require("resource_group_name")
STORAGE_ACCOUNT_NAME = config.require("storage_account_name")

# Fetch Resource Group
resource_group = resources.get_resource_group(RESOURCE_GROUP_NAME)

# Create an Azure resource (Storage Account)
account = storage.StorageAccount('sa',
    account_name=STORAGE_ACCOUNT_NAME,
    resource_group_name=resource_group.name,
    sku=storage.SkuArgs(
        name=storage.SkuName.STANDARD_LRS,
    ),
    kind=storage.Kind.STORAGE_V2)
