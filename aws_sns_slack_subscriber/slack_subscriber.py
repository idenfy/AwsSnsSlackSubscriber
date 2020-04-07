from aws_cdk import aws_lambda
from aws_cdk.aws_sns import ITopic
from aws_cdk.aws_sns_subscriptions import LambdaSubscription
from aws_cdk.core import Stack
from aws_sns_slack_subscriber import root_path


class SlackSubscriber(aws_lambda.Function):
    def __init__(self, scope: Stack, id: str, slack_webhook_url_path: str, sns_topic: ITopic) -> None:
        super().__init__(
            scope,
            id,
            code=aws_lambda.Code.from_asset(f'{root_path}/src'),
            handler='lambda.handler',
            runtime=aws_lambda.Runtime.NODEJS_12_X,
            environment={
                'SLACK_WEBHOOK_URL_PATH': slack_webhook_url_path
            }
        )

        sns_topic.add_subscription(LambdaSubscription(self))
