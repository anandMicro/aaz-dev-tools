# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from azure.cli.core.aaz import *


@register_command(
    "databricks workspace create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create a new workspace.

    :example: Create a workspace
        az databricks workspace create --resource-group MyResourceGroup --name MyWorkspace --location westus --sku standard

    :example: Create a workspace with managed identity for storage account
        az databricks workspace create --resource-group MyResourceGroup --name MyWorkspace --location eastus2euap --sku premium --prepare-encryption
    """

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations(), result_callback=self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrType(
            options=['--workspace-name', '--name', '-n'],
            help='The name of the workspace.',
            required=True,
            id_part='name',
        )
        _args_schema.tags = AAZDictArg(
            options=['--tags'],
            help='Resource tags.',
        )
        _args_schema.location = AAZResourceLocationArg(
            help='The geo-location where the resource lives',
            required=True,
        )
        _args_schema.managed_resource_group_id = AAZStrType(
            options=['--managed-resource-group-id'],
            help='The managed resource group Id.',
            required=True,
        )
        _args_schema.parameters = AAZObjectArg(
            options=['--parameters'],
            help='The workspace\'s custom parameters.',
        )
        _args_schema.ui_definition_uri = AAZStrType(
            options=['--ui-definition-uri'],
            help='The blob URI where the UI definition file is located.',
        )
        _args_schema.authorizations = AAZListArg(
            options=['--authorizations'],
            singular_options=['--authorization'],
            help='The workspace provider authorizations.',
        )
        _args_schema.sku = AAZObjectArg(
            options=['--sku'],
            help='The SKU of the resource.',
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrType(
        )

        parameters = cls._args_schema.parameters
        parameters.aml_workspace_id = AAZObjectArg(
            options=['aml-workspace-id'],
            help='The ID of a Azure Machine Learning workspace to link with Databricks workspace',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.aml_workspace_id)
        parameters.custom_virtual_network_id = AAZObjectArg(
            options=['custom-virtual-network-id'],
            help='The ID of a Virtual Network where this Databricks Cluster should be created',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.custom_virtual_network_id)
        parameters.custom_public_subnet_name = AAZObjectArg(
            options=['custom-public-subnet-name'],
            help='The name of a Public Subnet within the Virtual Network',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.custom_public_subnet_name)
        parameters.custom_private_subnet_name = AAZObjectArg(
            options=['custom-private-subnet-name'],
            help='The name of the Private Subnet within the Virtual Network',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.custom_private_subnet_name)
        parameters.enable_no_public_ip = AAZObjectArg(
            options=['enable-no-public-ip'],
            help='Should the Public IP be Disabled?',
        )
        cls._build_args_workspace_custom_boolean_parameter_create(parameters.enable_no_public_ip)
        parameters.load_balancer_backend_pool_name = AAZObjectArg(
            options=['load-balancer-backend-pool-name'],
            help='Name of the outbound Load Balancer Backend Pool for Secure Cluster Connectivity (No Public IP).',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.load_balancer_backend_pool_name)
        parameters.load_balancer_id = AAZObjectArg(
            options=['load-balancer-id'],
            help='Resource URI of Outbound Load balancer for Secure Cluster Connectivity (No Public IP) workspace.',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.load_balancer_id)
        parameters.nat_gateway_name = AAZObjectArg(
            options=['nat-gateway-name'],
            help='Name of the NAT gateway for Secure Cluster Connectivity (No Public IP) workspace subnets.',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.nat_gateway_name)
        parameters.public_ip_name = AAZObjectArg(
            options=['public-ip-name'],
            help='Name of the Public IP for No Public IP workspace with managed vNet.',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.public_ip_name)
        parameters.prepare_encryption = AAZObjectArg(
            options=['prepare-encryption'],
            help='Prepare the workspace for encryption. Enables the Managed Identity for managed storage account.',
        )
        cls._build_args_workspace_custom_boolean_parameter_create(parameters.prepare_encryption)
        parameters.encryption = AAZObjectArg(
            options=['encryption'],
            help='Contains the encryption details for Customer-Managed Key (CMK) enabled workspace.',
        )
        parameters.require_infrastructure_encryption = AAZObjectArg(
            options=['require-infrastructure-encryption'],
            help='A boolean indicating whether or not the DBFS root file system will be enabled with secondary layer of encryption with platform managed keys for data at rest.',
        )
        cls._build_args_workspace_custom_boolean_parameter_create(parameters.require_infrastructure_encryption)
        parameters.storage_account_name = AAZObjectArg(
            options=['storage-account-name'],
            help='Default DBFS storage account name.',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.storage_account_name)
        parameters.storage_account_sku_name = AAZObjectArg(
            options=['storage-account-sku-name'],
            help='Storage account SKU name, ex: Standard_GRS, Standard_LRS. Refer https://aka.ms/storageskus for valid inputs.',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.storage_account_sku_name)
        parameters.vnet_address_prefix = AAZObjectArg(
            options=['vnet-address-prefix'],
            help='Address prefix for Managed virtual network. Default value for this input is 10.139.',
        )
        cls._build_args_workspace_custom_string_parameter_create(parameters.vnet_address_prefix)

        encryption = cls._args_schema.parameters.encryption
        encryption.value = AAZObjectArg(
            options=['value'],
            help='The value which should be used for this field.',
        )

        value = cls._args_schema.parameters.encryption.value
        value.key_source = AAZStrType(
            options=['key-source'],
            help='The encryption keySource (provider). Possible values (case-insensitive):  Default, Microsoft.Keyvault',
            default='Default',
            enum={'Default': 'Default', 'Microsoft.Keyvault': 'Microsoft.Keyvault'},
        )
        value.key_name = AAZStrType(
            options=['key-name'],
            help='The name of KeyVault key.',
        )
        value.keyversion = AAZStrType(
            options=['keyversion'],
            help='The version of KeyVault key.',
        )
        value.keyvaulturi = AAZStrType(
            options=['keyvaulturi'],
            help='The Uri of KeyVault.',
        )

        authorizations = cls._args_schema.authorizations
        authorizations.Element = AAZObjectArg(
        )

        Element = cls._args_schema.authorizations.Element
        Element.principal_id = AAZStrType(
            options=['principal-id'],
            help='The provider\'s principal identifier. This is the identity that the provider will use to call ARM to manage the workspace resources.',
            required=True,
        )
        Element.role_definition_id = AAZStrType(
            options=['role-definition-id'],
            help='The provider\'s role definition identifier. This role will define all the permissions that the provider must have on the workspace\'s container resource group. This role definition cannot have permission to delete the resource group.',
            required=True,
        )

        sku = cls._args_schema.sku
        sku.name = AAZStrType(
            options=['name'],
            help='The SKU name.',
            required=True,
        )
        sku.tier = AAZStrType(
            options=['tier'],
            help='The SKU tier.',
        )
        return _args_schema

    _args_workspace_custom_boolean_parameter_create = None

    @classmethod
    def _build_args_workspace_custom_boolean_parameter_create(cls, schema):
        if cls._args_workspace_custom_boolean_parameter_create is not None:
            schema.value = cls._args_workspace_custom_boolean_parameter_create.value
            return

        cls._args_workspace_custom_boolean_parameter_create = AAZObjectArg(
        )

        workspace_custom_boolean_parameter_create = cls._args_workspace_custom_boolean_parameter_create
        workspace_custom_boolean_parameter_create.value = AAZBoolArg(
            options=['value'],
            help='The value which should be used for this field.',
            required=True,
        )

        schema.value = cls._args_workspace_custom_boolean_parameter_create.value

    _args_workspace_custom_string_parameter_create = None

    @classmethod
    def _build_args_workspace_custom_string_parameter_create(cls, schema):
        if cls._args_workspace_custom_string_parameter_create is not None:
            schema.value = cls._args_workspace_custom_string_parameter_create.value
            return

        cls._args_workspace_custom_string_parameter_create = AAZObjectArg(
        )

        workspace_custom_string_parameter_create = cls._args_workspace_custom_string_parameter_create
        workspace_custom_string_parameter_create.value = AAZStrType(
            options=['value'],
            help='The value which should be used for this field.',
            required=True,
        )

        schema.value = cls._args_workspace_custom_string_parameter_create.value

    def _execute_operations(self):
        yield self.WorkspacesCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class WorkspacesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"
        ERROR_FORMAT = "ODataV4Format"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    deserialization_callback=self.on_200_201,
                    lro_options={'final-state-via': 'azure-async-operation'},
                    path_format_arguments=self.url_parameters,
                )
            return self.on_error(session)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def url_parameters(self):
            parameters = {
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
            }
            return parameters


__all__ = ["Create"]
