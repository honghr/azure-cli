# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "netappfiles update-network-sibling-set",
)
class UpdateNetworkSiblingSet(AAZCommand):
    """Update the network features of a network sibling set

    Update the network features of the specified network sibling set

    :example: Update Network sibling set
        az -l westus2 --network-sibling-set-id {SIBLIING_SET_ID} --subnet-id {SUBNET_ID} --network-sibling-set-state-id {SIBLING_SET_STATE_ID} --network-features Standard
    """

    _aaz_info = {
        "version": "2024-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.netapp/locations/{}/updatenetworksiblingset", "2024-03-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            required=True,
            id_part="name",
        )

        # define Arg Group "Body"

        _args_schema = cls._args_schema
        _args_schema.network_features = AAZStrArg(
            options=["--network-features"],
            arg_group="Body",
            help="Network features available to the volume",
            required=True,
            default="Basic",
            enum={"Basic": "Basic", "Basic_Standard": "Basic_Standard", "Standard": "Standard", "Standard_Basic": "Standard_Basic"},
        )
        _args_schema.network_sibling_set_id = AAZStrArg(
            options=["--network-sibling-set-id"],
            arg_group="Body",
            help="Network Sibling Set ID for a group of volumes sharing networking resources in a subnet.",
            required=True,
            fmt=AAZStrArgFormat(
                pattern="^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$",
                max_length=36,
                min_length=36,
            ),
        )
        _args_schema.network_sibling_set_state_id = AAZStrArg(
            options=["--state-id", "--network-sibling-set-state-id"],
            arg_group="Body",
            help="Network sibling set state Id identifying the current state of the sibling set.",
            required=True,
        )
        _args_schema.subnet_id = AAZResourceIdArg(
            options=["--subnet-id"],
            arg_group="Body",
            help="The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes. Example /subscriptions/subscriptionId/resourceGroups/resourceGroup/providers/Microsoft.Network/virtualNetworks/testVnet/subnets/{mySubnet}",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.NetAppResourceUpdateNetworkSiblingSet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class NetAppResourceUpdateNetworkSiblingSet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.NetApp/locations/{location}/updateNetworkSiblingSet",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "location", self.ctx.args.location,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("networkFeatures", AAZStrType, ".network_features", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("networkSiblingSetId", AAZStrType, ".network_sibling_set_id", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("networkSiblingSetStateId", AAZStrType, ".network_sibling_set_state_id", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("subnetId", AAZStrType, ".subnet_id", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.network_features = AAZStrType(
                serialized_name="networkFeatures",
            )
            _schema_on_200.network_sibling_set_id = AAZStrType(
                serialized_name="networkSiblingSetId",
            )
            _schema_on_200.network_sibling_set_state_id = AAZStrType(
                serialized_name="networkSiblingSetStateId",
            )
            _schema_on_200.nic_info_list = AAZListType(
                serialized_name="nicInfoList",
            )
            _schema_on_200.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            _schema_on_200.subnet_id = AAZStrType(
                serialized_name="subnetId",
            )

            nic_info_list = cls._schema_on_200.nic_info_list
            nic_info_list.Element = AAZObjectType()

            _element = cls._schema_on_200.nic_info_list.Element
            _element.ip_address = AAZStrType(
                serialized_name="ipAddress",
                flags={"read_only": True},
            )
            _element.volume_resource_ids = AAZListType(
                serialized_name="volumeResourceIds",
            )

            volume_resource_ids = cls._schema_on_200.nic_info_list.Element.volume_resource_ids
            volume_resource_ids.Element = AAZStrType()

            return cls._schema_on_200


class _UpdateNetworkSiblingSetHelper:
    """Helper class for UpdateNetworkSiblingSet"""


__all__ = ["UpdateNetworkSiblingSet"]
