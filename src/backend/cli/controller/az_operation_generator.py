from cli.model.atomic import CLIAtomicCommand
from command.model.configuration import CMDCommand, CMDHttpOperation, CMDCondition, CMDConditionAndOperator, \
    CMDConditionOrOperator, CMDHttpRequestJsonBody, CMDConditionHasValueOperator, CMDInstanceUpdateOperation, \
    CMDJsonInstanceUpdateAction, CMDGenericInstanceUpdateAction, CMDHttpResponseJsonBody, CMDClsSchemaBase
from utils.case import to_camel_case, to_snack_case
from utils import exceptions
from utils.plane import PlaneEnum
from utils.error_format import AAZErrorFormatEnum


class AzOperationGenerator:

    def __init__(self, name, cmd_ctx, operation):
        self.name = name
        self._cmd_ctx = cmd_ctx
        self._operation = operation
        self.is_long_running = False

    @property
    def when(self):
        return self._operation.when


class AzHttpResponseGenerator:

    def __init__(self, cmd_ctx, response):
        self._cmd_ctx = cmd_ctx
        self._response = response
        self.status_codes = response.status_codes
        self.callback_name = "on_" + "_".join(str(code) for code in response.status_codes)
        self.variant_name = None
        self.callback_schema_name = None
        if response.body is not None and isinstance(response.body, CMDHttpResponseJsonBody) and \
                response.body.json is not None and response.body.json.var is not None:
            variant = response.body.json.var
            self.variant_name = self._cmd_ctx.get_variant(variant)
            self.schema_builder = f"_build_schema_{self.callback_name}"
            self.schema = response.body.json.schema


class AzHttpRequestContentGenerator:

    def __init__(self, cmd_ctx, body):
        self._cmd_ctx = cmd_ctx
        self._body = body


class AzHttpOperationGenerator(AzOperationGenerator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assert isinstance(self._operation, CMDHttpOperation)

        if self._operation.long_running is not None:
            self.is_long_running = True
            self.lro_options = {
                'final-state-via': self._operation.long_running.final_state_via
            }

        self.success_responses = []

        error_format = None
        for response in self._operation.http.responses:
            if not response.is_error:
                self.success_responses.append(AzHttpResponseGenerator(self._cmd_ctx, response))
            else:
                if not isinstance(response.body, CMDHttpResponseJsonBody):
                    raise NotImplementedError()
                schema = response.body.json.schema
                if not isinstance(schema, CMDClsSchemaBase):
                    raise NotImplementedError()
                name = schema.type[1:]
                if not error_format:
                    error_format = name
                if error_format != name:
                    raise exceptions.InvalidAPIUsage(f"Multiple error formats in one operation: {name}, {error_format}")
        if not AAZErrorFormatEnum.validate(error_format):
            raise exceptions.InvalidAPIUsage(f"Invalid error format: {error_format}")
        self.error_format = error_format

        # specify content
        self.content = None
        self.form_content = None
        self.stream_content = None
        if self._operation.http.request.body:
            body = self._operation.http.request.body
            if isinstance(body, CMDHttpRequestJsonBody):
                self.content = AzHttpRequestContentGenerator(self._cmd_ctx, body)
            else:
                raise NotImplementedError()

    @property
    def url(self):
        return self._operation.http.path

    @property
    def method(self):
        return self._operation.http.request.method.upper()

    @property
    def url_parameters(self):
        path = self._operation.http.request.path
        if not path:
            return None
        parameters = []
        if path.params:
            for param in path.params:
                parameters.append([
                    param.name,
                    self._cmd_ctx.get_argument(param.arg),
                    False,
                ])
        if path.consts:
            for param in path.consts:
                assert param.const
                parameters.append([
                    param.name,
                    param.default.value,
                    True
                ])
        return parameters

    @property
    def query_parameters(self):
        query = self._operation.http.request.query
        if not query:
            return None
        parameters = []
        if query.params:
            for param in query.params:
                parameters.append([
                    param.name,
                    self._cmd_ctx.get_argument(param.arg),
                    False,
                ])
        if query.consts:
            for param in query.consts:
                assert param.const
                parameters.append([
                    param.name,
                    param.default.value,
                    True
                ])
        return parameters

    @property
    def header_parameters(self):
        header = self._operation.http.request.header
        if not header:
            return None
        parameters = []
        if header.params:
            for param in header.params:
                parameters.append([
                    param.name,
                    self._cmd_ctx.get_argument(param.arg),
                    False,
                ])
        if header.consts:
            for param in header.consts:
                assert param.const
                parameters.append([
                    param.name,
                    param.default.value,
                    True
                ])
        return parameters


class AzJsonUpdateOperationGenerator(AzOperationGenerator):
    pass


class AzGenericUpdateOperationGenerator(AzOperationGenerator):
    pass
