from . import AWSAttribute, AWSProperty, validate_pausetime
from .validators import boolean, integer, positive_integer


class AutoScalingRollingUpdate(AWSProperty):
    props = {
        "MaxBatchSize": (positive_integer, False),
        "MinInstancesInService": (integer, False),
        "MinSuccessfulInstancesPercent": (integer, False),
        "PauseTime": (validate_pausetime, False),
        "SuspendProcesses": ([str], False),
        "WaitOnResourceSignals": (boolean, False),
    }


class AutoScalingScheduledAction(AWSProperty):
    props = {
        "IgnoreUnmodifiedGroupSizeProperties": (boolean, False),
    }


class AutoScalingReplacingUpdate(AWSProperty):
    props = {
        "WillReplace": (boolean, False),
    }


class CodeDeployLambdaAliasUpdate(AWSProperty):
    props = {
        "AfterAllowTrafficHook": (str, False),
        "ApplicationName": (boolean, True),
        "BeforeAllowTrafficHook": (str, False),
        "DeploymentGroupName": (boolean, True),
    }


class UpdatePolicy(AWSAttribute):
    props = {
        "AutoScalingRollingUpdate": (AutoScalingRollingUpdate, False),
        "AutoScalingScheduledAction": (AutoScalingScheduledAction, False),
        "AutoScalingReplacingUpdate": (AutoScalingReplacingUpdate, False),
        "CodeDeployLambdaAliasUpdate": (CodeDeployLambdaAliasUpdate, False),
        "UseOnlineResharding": (boolean, False),
        "EnableVersionUpgrade": (boolean, False),
    }


class ResourceSignal(AWSProperty):
    props = {
        "Count": (positive_integer, False),
        "Timeout": (validate_pausetime, False),
    }


class AutoScalingCreationPolicy(AWSProperty):
    props = {
        "MinSuccessfulInstancesPercent": (integer, False),
    }


class CreationPolicy(AWSAttribute):
    props = {
        "AutoScalingCreationPolicy": (AutoScalingCreationPolicy, False),
        "ResourceSignal": (ResourceSignal, True),
    }
