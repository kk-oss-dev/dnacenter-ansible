from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DNACSDK,
    dnac_argument_spec,
)

# Get common arguements specification
argument_spec = dnac_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    tags=dict(type="list"),
    author=dict(type="str"),
    composite=dict(type="bool"),
    containingTemplates=dict(type="list"),
    createTime=dict(type="int"),
    customParamsOrder=dict(type="bool"),
    description=dict(type="str"),
    deviceTypes=dict(type="list"),
    failurePolicy=dict(type="str"),
    id=dict(type="str"),
    language=dict(type="str"),
    lastUpdateTime=dict(type="int"),
    latestVersionTime=dict(type="int"),
    name=dict(type="str"),
    parentTemplateId=dict(type="str"),
    projectId=dict(type="str"),
    projectName=dict(type="str"),
    rollbackTemplateContent=dict(type="str"),
    rollbackTemplateParams=dict(type="list"),
    softwareType=dict(type="str"),
    softwareVariant=dict(type="str"),
    softwareVersion=dict(type="str"),
    templateContent=dict(type="str"),
    templateParams=dict(type="list"),
    validationErrors=dict(type="dict"),
    version=dict(type="str"),
))

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def get_object(self, params):
        new_object = dict(
            tags=params.get("tags"),
            author=params.get("author"),
            composite=params.get("composite"),
            containingTemplates=params.get("containingTemplates"),
            createTime=params.get("createTime"),
            customParamsOrder=params.get("customParamsOrder"),
            description=params.get("description"),
            deviceTypes=params.get("deviceTypes"),
            failurePolicy=params.get("failurePolicy"),
            id=params.get("id"),
            language=params.get("language"),
            lastUpdateTime=params.get("lastUpdateTime"),
            latestVersionTime=params.get("latestVersionTime"),
            name=params.get("name"),
            parentTemplateId=params.get("parentTemplateId"),
            projectId=params.get("projectId"),
            projectName=params.get("projectName"),
            rollbackTemplateContent=params.get("rollbackTemplateContent"),
            rollbackTemplateParams=params.get("rollbackTemplateParams"),
            softwareType=params.get("softwareType"),
            softwareVariant=params.get("softwareVariant"),
            softwareVersion=params.get("softwareVersion"),
            templateContent=params.get("templateContent"),
            templateParams=params.get("templateParams"),
            validationErrors=params.get("validationErrors"),
            version=params.get("version"),
            project_id=params.get("projectId"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        dnac = DNACSDK(params=self._task.args)

        response = dnac.exec(
            family="configuration_templates",
            function='create_template',
            op_modifies=True,
            params=self.get_object(self._task.args),
        )
        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
